---
tags:
  - type/reference
  - topics/ai
  - topics/development
type: reference
created: 2026-01-10
modified: 2026-01-10
status: active
---

# Agent SDK Patterns

Reference documentation for Claude Agent SDK patterns extracted from the official `anthropics/claude-agent-sdk-demos/research-agent` example.

## Core Architecture

### Client Initialization

```python
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, AgentDefinition, HookMatcher

options = ClaudeAgentOptions(
    permission_mode="bypassPermissions",
    setting_sources=["project"],      # Load skills from .claude directory
    system_prompt=lead_agent_prompt,  # Lead agent's instructions
    allowed_tools=["Task"],           # Lead only delegates
    agents=agents,                    # Dict of subagent definitions
    hooks=hooks,                      # Pre/post tool hooks
    model="haiku"                     # Default model
)

async with ClaudeSDKClient(options=options) as client:
    await client.query(prompt=user_input)
    async for msg in client.receive_response():
        process_message(msg)
```

### AgentDefinition Structure

```python
agents = {
    "researcher": AgentDefinition(
        description=(
            "Use this agent when you need to gather research information. "
            "Detailed description that guides Task tool routing..."
        ),
        tools=["WebSearch", "Write"],   # Available tools for this agent
        prompt=researcher_prompt,        # Loaded from .txt file
        model="haiku"                    # Model for this agent
    ),
    "report-writer": AgentDefinition(
        description="Use this agent when creating formal reports...",
        tools=["Skill", "Write", "Glob", "Read", "Bash"],
        prompt=report_writer_prompt,
        model="haiku"
    )
}
```

**Key Patterns:**
- `description` field is CRITICAL - it guides Task tool routing
- Use detailed descriptions that explain WHEN to use the agent
- Different agents get different `tools` based on their role
- Use cheaper models (haiku) for parallel workers, stronger models for synthesis

## Hooks System

### HookMatcher Setup

```python
hooks = {
    'PreToolUse': [
        HookMatcher(
            matcher=None,  # Match ALL tools (or specify tool names)
            hooks=[tracker.pre_tool_use_hook]
        )
    ],
    'PostToolUse': [
        HookMatcher(
            matcher=None,
            hooks=[tracker.post_tool_use_hook]
        )
    ]
}
```

### Hook Function Signatures

```python
async def pre_tool_use_hook(self, hook_input, tool_use_id, context):
    """
    Called before every tool invocation.

    Args:
        hook_input: Dict with 'tool_name' and 'tool_input'
        tool_use_id: Unique ID for this tool call
        context: Execution context

    Returns:
        {'continue_': True} to proceed with tool execution
    """
    tool_name = hook_input['tool_name']
    tool_input = hook_input['tool_input']

    # Log, track, validate...

    return {'continue_': True}

async def post_tool_use_hook(self, hook_input, tool_use_id, context):
    """
    Called after every tool invocation.

    Args:
        hook_input: Dict with 'tool_response'
        tool_use_id: Same ID from pre_tool_use
        context: Execution context
    """
    tool_response = hook_input.get('tool_response')

    # Log completion, capture results...

    return {'continue_': True}
```

## SubagentTracker Pattern

The official demo uses `SubagentTracker` to track parent-child relationships:

```python
@dataclass
class ToolCallRecord:
    timestamp: str
    tool_name: str
    tool_input: Dict[str, Any]
    tool_use_id: str
    subagent_type: str
    parent_tool_use_id: Optional[str] = None
    tool_output: Optional[Any] = None
    error: Optional[str] = None

@dataclass
class SubagentSession:
    subagent_type: str
    parent_tool_use_id: str
    spawned_at: str
    description: str
    prompt_preview: str
    subagent_id: str  # e.g., "RESEARCHER-1"
    tool_calls: List[ToolCallRecord] = field(default_factory=list)

class SubagentTracker:
    def __init__(self, transcript_writer=None, session_dir=None):
        self.sessions: Dict[str, SubagentSession] = {}
        self.tool_call_records: Dict[str, ToolCallRecord] = {}
        self._current_parent_id: Optional[str] = None
        self.subagent_counters: Dict[str, int] = defaultdict(int)

    def register_subagent_spawn(self, tool_use_id, subagent_type, description, prompt):
        """Register when Task tool spawns a new subagent."""
        self.subagent_counters[subagent_type] += 1
        subagent_id = f"{subagent_type.upper()}-{self.subagent_counters[subagent_type]}"
        # Track session...
        return subagent_id

    def set_current_context(self, parent_tool_use_id):
        """Update context from message stream (parent_tool_use_id)."""
        self._current_parent_id = parent_tool_use_id
```

**Key Insight:** The `parent_tool_use_id` from messages links child agent tool calls to their parent Task spawn.

## Message Processing

```python
def process_assistant_message(msg, tracker, transcript):
    """Process AssistantMessage from response stream."""

    # Update tracker with parent context
    parent_id = getattr(msg, 'parent_tool_use_id', None)
    tracker.set_current_context(parent_id)

    for block in msg.content:
        block_type = type(block).__name__

        if block_type == 'TextBlock':
            transcript.write(block.text)

        elif block_type == 'ToolUseBlock':
            if block.name == 'Task':
                # Register subagent spawn
                subagent_id = tracker.register_subagent_spawn(
                    tool_use_id=block.id,
                    subagent_type=block.input.get('subagent_type'),
                    description=block.input.get('description'),
                    prompt=block.input.get('prompt', '')
                )
```

## Session & Transcript Management

### Session Setup

```python
def setup_session() -> tuple[Path, Path]:
    """Create timestamped session directory."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    session_dir = Path("logs") / f"session_{timestamp}"
    session_dir.mkdir(parents=True, exist_ok=True)

    transcript_file = session_dir / "transcript.txt"
    return transcript_file, session_dir
```

### TranscriptWriter

```python
class TranscriptWriter:
    def __init__(self, transcript_file: Path):
        self.file = open(transcript_file, "w", encoding="utf-8")

    def write(self, text: str, end: str = "", flush: bool = True):
        """Write to both console and file."""
        print(text, end=end, flush=flush)
        self.file.write(text + end)

    def write_to_file(self, text: str, flush: bool = True):
        """Write to file only (not console)."""
        self.file.write(text)
```

### JSONL Tool Logging

```python
def _log_to_jsonl(self, log_entry: Dict[str, Any]):
    """Write structured log entry."""
    if self.tool_log_file:
        self.tool_log_file.write(json.dumps(log_entry) + "\n")
        self.tool_log_file.flush()

# Log entry structure:
{
    "event": "tool_call_start",
    "timestamp": "2025-01-10T14:30:00.000Z",
    "tool_use_id": "toolu_abc123",
    "agent_id": "RESEARCHER-1",
    "agent_type": "researcher",
    "tool_name": "WebSearch",
    "tool_input": {"query": "..."},
    "parent_tool_use_id": "toolu_lead_xyz"
}
```

## Lead Agent Prompt Patterns

The lead agent prompt should include:

1. **Role Definition** - Clear statement that this is an orchestrator
2. **Delegation Rules** - NEVER do research/writing, ONLY delegate
3. **Workflow Steps** - Explicit numbered steps for the workflow
4. **Parallel Spawning** - Instructions to spawn multiple agents at once
5. **Tool Usage** - How to format Task tool calls
6. **Response Style** - Keep responses short, action-oriented
7. **Examples** - Good and bad response examples

```markdown
**CRITICAL RULES:**
1. You MUST delegate ALL research to specialized subagents
2. Keep ALL responses SHORT - maximum 2-3 sentences
3. Get straight to work immediately

<workflow>
STEP 1: ANALYZE - Break into 2-4 subtopics
STEP 2: SPAWN RESEARCHERS (IN PARALLEL)
STEP 3: WAIT FOR COMPLETION
STEP 4: SPAWN REPORT WRITER
STEP 5: CONFIRM COMPLETION
</workflow>

<delegation_rules>
1. You NEVER research yourself - ALWAYS delegate
2. ALWAYS spawn 2-4 researchers in parallel
3. ALWAYS wait for ALL to finish before next step
</delegation_rules>
```

## Subagent Prompt Patterns

Subagent prompts should include:

1. **Available Tools** - List what tools they have
2. **Output Locations** - Where to save files
3. **Quality Standards** - What makes good output
4. **File Naming** - Consistent naming conventions
5. **Format Templates** - Markdown/output structure

```markdown
<available_tools>
WebSearch: Search the internet
Write: Save to files/research_notes/
</available_tools>

<file_workflow>
STEP 1: Use WebSearch 5-10 times
STEP 2: Extract all data
STEP 3: Write to files/research_notes/{topic}.md
</file_workflow>

<output_format>
# [Topic] Research Notes
## Key Statistics
- [Statistic 1] (Source)
...
</output_format>
```

## File-Based Coordination

The official demo uses the filesystem for agent coordination:

```
files/
├── research_notes/     # Researchers write here
├── data/               # Data analyst summaries
├── charts/             # Generated visualizations
└── reports/            # Final PDF outputs
```

**Pattern:** Agents write to specific directories, later agents read from those directories. No explicit message passing - the filesystem IS the coordination layer.

## Key Takeaways

1. **Lead agent = Task tool only** - Pure orchestrator
2. **Descriptions drive routing** - Detailed descriptions for AgentDefinition
3. **Hooks for observability** - Pre/post hooks capture all tool calls
4. **parent_tool_use_id = lineage** - Links child calls to parent spawn
5. **File system = coordination** - Agents communicate via files
6. **Prompts in separate files** - Easier iteration
7. **Models by role** - haiku for workers, sonnet/opus for synthesis
8. **Parallel spawning** - Multiple Task calls in one response

## Related Notes

- [[Research Agent SDK Implementation]]
- [[MCP Server Design Patterns]]

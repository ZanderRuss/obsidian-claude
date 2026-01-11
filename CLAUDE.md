# CLAUDE.md - Obsidian Vault Integration Guide

This file provides guidance to Claude Code when working with this Obsidian vault and knowledge management system.

## Philosophy: AI as Thinking Partner

> "AI amplifies thinking, not just writing."

This vault uses Claude as a **thinking partner** - an AI that helps explore ideas through dialogue rather than just generating content. The emphasis is on:

- **Questions before answers** - Clarify understanding through inquiry
- **Exploration before production** - Think deeply before creating
- **Connections over content** - Link ideas, find patterns
- **Iteration over perfection** - Build understanding incrementally

When working in this vault, prioritize helping the user *think* rather than just *produce*.

## Project Overview

This is an Obsidian vault with AI-powered knowledge management using the PARA method. The vault serves as a personal knowledge base and second brain with full Claude integration via MCP.

## Vault Structure (PARA Method)

```text
Obsidian-Template-Vault/
├── 0. Inbox/                  # Temporary capture point
├── 1. Projects/               # Active initiatives with deadlines
├── 2. Areas (Ongoing)/        # Ongoing responsibilities
├── 3. Resources (Dynamic)/    # Reference materials
├── 4. Archive (Supportive)/   # Completed/inactive items
├── Images/                    # Attachments
├── Home.md                    # Dashboard with Dataview queries
├── 6. Metadata/               # System documentation
│   ├── Templates/             # Note templates
│   ├── Workflows/             # Automation documentation
│   └── Reference/             # System reference
└── .obsidian/                 # Obsidian configuration (17 plugins)
```

### PARA Categorization Guide

| Destination | Criteria | Examples |
|-------------|----------|----------|
| `1. Projects` | Has deadline, specific outcome | Client deliverables, launches |
| `2. Areas (Ongoing)` | No end date, ongoing responsibility | Health, finances, learning |
| `3. Resources (Dynamic)` | Reference material, no action required | Research, how-tos, collections |
| `4. Archive (Supportive)` | Completed or no longer active | Done projects, old resources |

## Available Commands

### Knowledge Workflows

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/thinking-partner` | Explore ideas through questioning | Complex problems, brainstorming |
| `/daily-review` | End-of-day reflection and capture | Every evening (5-10 min) |
| `/weekly-synthesis` | Identify patterns across the week | Sunday or Monday (30-60 min) |
| `/research-assistant` | Deep topical investigation | Learning new topics |
| `/inbox-processor` | Organize captured notes via PARA | Weekly or when backlog builds |

### Advanced Analysis

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/smart-link` | AI-powered connection suggestions | After creating notes, finding orphans |
| `/graph-analysis` | Analyze knowledge graph health | Monthly vault maintenance |
| `/extract-todos` | Find and consolidate scattered tasks | Weekly task review |
| `/summarize-project` | Create project executive summary | Project check-ins, handoffs |

### Content Transformation

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/flashcards` | Generate spaced repetition cards | Learning/studying topics |
| `/note-to-blog` | Transform notes into publishable content | Content creation |
| `/voice-process` | Structure voice transcriptions | After voice capture |
| `/web-clip` | Save web articles as markdown | Research, bookmarking |

### Git & Documentation

| Command | Purpose |
|---------|---------|
| `/commit` | Create git commits |
| `/create-pr` | Create pull requests |
| `/pr-review` | Review pull requests |
| `/update-docs` | Update documentation |
| `/create-architecture-documentation` | Generate architecture docs with diagrams |

### Academic Research Workflow

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/quick-research` | Rapid 5-10 source investigation | Casual exploration, time-constrained |
| `/research-project-init` | Create phased research folder | Starting Complete Research Track |
| `/research-progress` | Check research phase completion | Monitor progress, find gaps |
| `/research-ideate` | Socratic exploration of research ideas | Starting new research, brainstorming |
| `/lit-search` | Literature search across Zotero + web | Finding relevant papers |
| `/deep-research` | Comprehensive multi-source investigation | Background research, surveys |
| `/evidence-qa` | Evidence-grounded Q&A over your PDFs | Answering specific research questions |
| `/lit-review` | Generate structured literature review | Writing related work sections |
| `/paper-outline` | Create paper structure for venue | Starting paper writing |
| `/paper-draft` | Draft specific paper sections | Writing methodology, experiments |
| `/paper-review` | Simulate peer review feedback | Before submission |
| `/paper-polish` | Grammar, style, consistency | Final editing pass |
| `/export-paper` | Export to LaTeX/PDF/Word | Submission preparation |

## Available Agents

### Obsidian Operations Team

- **vault-optimizer**: Performance optimization, file size analysis, attachment management
- **moc-agent**: Map of Content creation and maintenance
- **tag-agent**: Tag taxonomy standardization and hierarchy
- **content-curator**: Content organization and curation
- **metadata-agent**: Frontmatter and metadata management
- **connection-agent**: Link and relationship management
- **review-agent**: Content quality review

### Research Team

- **literature-reviewer**: Literature analysis, synthesis, and critical evaluation
- **research-methodologist**: Experimental design and methodology review
- **paper-editor**: Academic writing polish and style improvement
- **citation-manager**: Citation verification and BibTeX management
- **experiment-designer**: ML experiment design and ablation planning
- **research-orchestrator**: Multi-phase research coordination with quality gates
- **research-progress-tracker**: Progress monitoring and gap analysis
- **academic-researcher**: Academic database searching
- **research-synthesizer**: Cross-source synthesis
- **fact-checker**: Claim verification
- **data-analyst**: Quantitative analysis
- **report-generator**: Structured report creation
- **query-clarifier**: Query refinement
- **research-coordinator**: Task coordination
- **research-brief-generator**: Research brief creation
- **technical-researcher**: Technical implementation research

### Workflow Support

- **prompt-engineer**: Prompt optimization
- **task-decomposition-expert**: Complex task breakdown
- **search-specialist**: Search optimization

## MCP Integration

This vault has MCP (Model Context Protocol) configured for direct vault access using [mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian):

- **Obsidian MCP**: mcp-obsidian for vault operations (requires Local REST API plugin)
- **Zotero MCP**: zotero-mcp for reference library integration

### Configuration Files

| File | Purpose | Used By | Committed? |
|------|---------|---------|------------|
| `.mcp.json` | MCP config (project root) | Claude Code CLI | No (gitignored) |
| `.mcp.json.example` | Template to copy | — | Yes |
| `claude_desktop_config.json` | MCP config in AppData | Claude Desktop App | No |
| `.claude/settings.json` | Shared project settings | Both | Yes |
| `.claude/settings.local.json` | Your local overrides | Both | No (gitignored) |

### Two Environments

This project supports **two different Claude environments**:

| Environment | Config Location | When to Use |
|-------------|-----------------|-------------|
| **Claude Desktop App** | `%APPDATA%\Claude\claude_desktop_config.json` (Win) | Main desktop chat |
| **Claude Code CLI** | `.mcp.json` in project root | Terminal-based sessions |

### Setup (for users who need help)

When helping users connect Claude to their Obsidian vault:

1. **Install the plugin**: Settings > Community plugins > Browse > "Local REST API" > Install > Enable
2. **Copy API key**: Settings > Community plugins > Local REST API > copy the key shown
3. **Configure MCP** based on which environment they use:

**For Claude Code CLI** (`.mcp.json` in project root):
```json
{
  "mcpServers": {
    "obsidian": {
      "command": "uvx",
      "args": ["mcp-obsidian"],
      "env": {
        "OBSIDIAN_API_KEY": "key-from-plugin-settings"
      }
    }
  }
}
```

**For Claude Desktop App** (add to `claude_desktop_config.json`):
Same JSON structure, but add to the existing `mcpServers` object in the Desktop config file.

**Common issues:**
- Obsidian must be running for the API to work
- Zotero must be running for Zotero MCP to work
- API key must match exactly (no extra spaces)
- Restart Claude Code/Desktop after config changes
- Claude Code CLI uses `.mcp.json` at project root (NOT `.claude/mcp.json`)

See: `6. Metadata/Reference/Local REST API Setup.md` for detailed guide

### Obsidian MCP Capabilities

- Direct file read/write operations
- Semantic search across vault
- Programmatic note creation
- Template execution

### Zotero MCP Capabilities

- `zotero_semantic_search` - AI-powered similarity search
- `zotero_search_items` - Keyword search in library
- `zotero_get_item_metadata` - Get citation details + BibTeX
- `zotero_get_annotations` - Extract PDF highlights
- `zotero_get_fulltext` - Access document text

### Citation Tools Integration

| Tool                         | Use For                                              |
|------------------------------|------------------------------------------------------|
| **Zotero MCP**               | Searching existing library, getting PDF annotations  |
| **citation-management skill** | Google Scholar/PubMed search, DOI→BibTeX, validation |

## Automation Pipelines

### Voice Memo Processing

```
Record → Transcribe → Sync to Inbox → /voice-process → Structured Note
```

See: `6. Metadata/Workflows/Workflow - Voice Memo Automation.md`

### GitHub CI/CD

```
Create Issue (mobile) → GitHub Action → Claude processes → Commits result
```

See: `6. Metadata/Workflows/Workflow - GitHub Automation.md`

### Research Pipeline

```
Query → Web Search → Source Gathering → /web-clip → Synthesis
```

See: `6. Metadata/Workflows/Workflow - Research Automation.md`

### Academic Paper Pipeline

```
Ideate → Literature → Evidence → Outline → Draft → Review → Export
```

**Full Pipeline**:
1. `/research-ideate` → Research questions & hypotheses
2. `/lit-search` → Find relevant papers in Zotero + web
3. `/evidence-qa` → Ground claims in your PDF corpus
4. `/lit-review` → Synthesize into literature review
5. `/paper-outline` → Structure for target venue
6. `/paper-draft` → Write sections with citations
7. `/paper-review` → Simulate peer review
8. `/paper-polish` → Final editing pass
9. `/export-paper` → LaTeX/PDF for submission

See: `6. Metadata/Workflows/Workflow - Academic Research Pipeline.md`

## Working Modes

### Thinking Mode

Use when exploring, learning, or problem-solving:

- Ask clarifying questions before suggesting solutions
- Search vault for existing related content
- Document insights as they emerge
- Create thinking logs in `0. Inbox/`
- Focus on connections and patterns

### Writing Mode

Use when producing content or documentation:

- Use appropriate templates from `6. Metadata/Templates/`
- Add proper frontmatter
- Create bidirectional links
- Update related MOCs
- Follow naming conventions

### Automation Mode

Use when batch processing or maintaining vault:

- Run `/graph-analysis` for health checks
- Use `/extract-todos` for task consolidation
- Process inbox with `/inbox-processor`
- Generate summaries with `/summarize-project`

## Note Standards

### Frontmatter Template

```yaml
---
tags:
  - category/subcategory
type: note|project|moc|daily-note|research|voice-memo|web-clip
created: YYYY-MM-DD
modified: YYYY-MM-DD
status: draft|active|completed|archived
---
```

### Link Conventions

- Wiki link: `[[Note Name]]`
- Aliased: `[[Note Name|Display Text]]`
- Embedded: `![[Note Name]]`
- To heading: `[[Note Name#Heading]]`

### Naming Conventions

| Type | Format | Example |
|------|--------|---------|
| Regular notes | Title Case | `Meeting with Client.md` |
| Daily notes | Date | `2025-01-10.md` |
| MOCs | Prefixed | `MOC - Topic Name.md` |
| Templates | Prefixed | `Template - Type.md` |
| Voice memos | Prefixed | `Voice-2025-01-10-1430.md` |
| Web clips | Prefixed | `Clip - Article Title.md` |
| Research | Prefixed | `Research - Topic.md` |

## Obsidian Flavored Markdown

**IMPORTANT**: When creating or editing notes in this vault, use **Obsidian Flavored Markdown** syntax.

For full syntax reference, see: `.claude/skills/obsidian-markdown/SKILL.md`

### Key Differences from Standard Markdown

| Feature | Standard Markdown | Obsidian Markdown |
|---------|-------------------|-------------------|
| Internal links | `[Note](Note.md)` | `[[Note]]` |
| Aliased links | `[Display](Note.md)` | `[[Note\|Display]]` |
| Embeds | N/A | `![[Note]]` or `![[image.png]]` |
| Callouts | N/A | `> [!note]` |
| Highlights | N/A | `==highlighted==` |
| Block references | N/A | `[[Note#^block-id]]` |

### Quick Reference

```markdown
[[Note Name]]                    Internal link
[[Note Name|Display Text]]       Aliased link
[[Note Name#Heading]]            Link to heading
![[Note Name]]                   Embed note
![[image.png]]                   Embed image
![[image.png|300]]               Embed with width

> [!note] Title                  Callout (note, tip, warning, etc.)
> Content here

==highlighted text==             Highlight
%%hidden comment%%               Comment (not rendered)
```

### Frontmatter (Properties)

All notes should include YAML frontmatter:

```yaml
---
tags:
  - topic/subtopic
type: note
created: 2025-01-10
status: draft
---
```

## Tag Hierarchy

```text
content/
├── notes/
├── projects/
├── research/
├── voice-memo/
├── web-clip/
└── daily/

topics/
├── technology/
├── business/
└── personal/

status/
├── active/
├── review/
├── unprocessed/
└── archived/

type/
├── moc/
├── meeting/
├── thinking-log/
├── flashcards/
└── reference/
```

## Daily Workflow

### Morning (5 min)

1. Review yesterday's note
2. Set top 3 intentions
3. Quick inbox scan

### During Day

1. Capture quick notes to `0. Inbox/`
2. Record voice memos for longer thoughts
3. Use `/thinking-partner` for complex problems
4. Clip interesting articles with `/web-clip`

### Evening (5-10 min)

1. Run `/daily-review`
2. Process voice memos with `/voice-process`
3. Quick inbox triage
4. Set tomorrow's focus

### Weekly

1. Run `/weekly-synthesis`
2. Full `/inbox-processor` pass
3. Run `/graph-analysis` for vault health
4. Run `/extract-todos` for task consolidation
5. Archive completed work

## Integration Points

### Smart Connections

AI-powered note linking and discovery. Use for finding related content.

### Dataview

Query vault content with SQL-like syntax:

```dataview
TABLE status, created
FROM "1. Projects"
WHERE status = "active"
SORT created DESC
```

### Local REST API

Enabled on port 27124 (HTTPS) for external programmatic access. This is required for mcp-obsidian to connect.

## Performance Guidelines

- Keep markdown files under 1MB
- Compress images (85% JPEG quality)
- Archive content older than 2 years
- Remove orphaned attachments periodically
- Use MOCs instead of deeply nested folders
- Run `/graph-analysis` monthly for health checks

## Security Considerations

- Never commit sensitive data to notes
- Use environment variables for API keys
- MCP API key stored securely
- Review plugin permissions
- Keep plugins updated
- Backup vault regularly

## Before Completing Any Task

- [ ] Explored existing vault content for context
- [ ] Asked clarifying questions if needed
- [ ] Links are working and bidirectional where appropriate
- [ ] Tags follow the established hierarchy
- [ ] Frontmatter is complete and accurate
- [ ] Content is in the appropriate PARA location
- [ ] Related MOCs updated if needed
- [ ] User understands next steps

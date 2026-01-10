# Obsidian + Claude Integration

A comprehensive, **portable** integration between [Obsidian](https://obsidian.md) and [Claude Code](https://claude.ai/code) for AI-powered knowledge management using the PARA method.

**29 commands • 16 agents • 18 AI skills • 17 curated plugins • Full research workflow • MCP integration**

---

## Philosophy

> "AI amplifies thinking, not just writing."

This vault uses Claude as a **thinking partner** — an AI that helps explore ideas through dialogue rather than just generating content:

- **Questions before answers** — Clarify understanding through inquiry
- **Exploration before production** — Think deeply before creating
- **Connections over content** — Link ideas, find patterns
- **Iteration over perfection** — Build understanding incrementally

## What Can You Do With This?

| You Want To... | Just Say... |
|----------------|-------------|
| Find research papers | "Find papers about climate change" |
| Write academic documents | "Help me write an introduction for my paper" |
| Analyze data | "Run a statistical analysis on this data" |
| Create charts | "Make a bar chart showing these results" |
| Manage citations | "Create a citation for this paper" |
| Search the web | "Search for the latest news on AI" |
| Work with documents | "Create a Word document with this content" |

Claude becomes your research assistant, writing partner, and data analyst - all in one.

---

## How It Works

You'll use **two apps together**:

```
+-------------------+          +-------------------+
|  Claude Code      |  <---->  |     Obsidian      |
|  Desktop          |          |                   |
|                   |          |                   |
|  Your AI partner  |          |  Your notes vault |
|  that helps you   |          |  where everything |
|  think & work     |          |  is stored        |
+-------------------+          +-------------------+
         |                              |
         +----------- Both open to -----+
                  the same folder
```

---

## Quick Start (No Coding Required)

### Step 1: Download This Project

Click the green **Code** button above, then **Download ZIP**.

```
+------------------------------------------+
|  [<> Code v]                             |
|  +------------------------------------+  |
|  | Clone                              |  |
|  | Open with GitHub Desktop           |  |
|  | Download ZIP  <-- Click this       |  |
|  +------------------------------------+  |
+------------------------------------------+
```

**Extract the ZIP file** to a location you'll remember (like `Documents/obsidian-claude/`).

### Step 2: Open the Folder in Claude Code Desktop

1. **Open Claude Code Desktop** (download from [claude.ai/download](https://claude.ai/download))
2. **Select the folder** you just extracted (File > Open Folder)
3. Navigate to the folder containing `SETUP.bat` and `README.md`

> **Why this matters:** Claude Code Desktop can only work with files in the folder you select.

### Step 3: Run Setup

In Claude Code Desktop, ask Claude: "Please run the setup script"

Or type: `run SETUP.bat` (Windows) or `run SETUP.command` (Mac)

### Step 4: Open the Vault in Obsidian

1. **Open Obsidian** (download from [obsidian.md](https://obsidian.md))
2. Click **"Open folder as vault"**
3. Navigate to: `your-folder/Obsidian-Template-Vault/`

**That's it!** You now have Claude Code Desktop and Obsidian working together.

> For more detailed instructions, see [INSTALLATION.md](INSTALLATION.md)

---

## Quick Start (For Developers)

### Apply to Your Existing Vault

Run the setup script to apply this configuration to your existing Obsidian vault:

**Windows (PowerShell):**
```powershell
git clone https://github.com/ZanderRuss/obsidian-claude.git
cd obsidian-claude
.\scripts\setup.ps1 -VaultPath "C:\path\to\your\vault"
```

**Linux/macOS:**
```bash
git clone https://github.com/ZanderRuss/obsidian-claude.git
cd obsidian-claude
chmod +x scripts/setup.sh
./scripts/setup.sh -v ~/path/to/your/vault
```

The setup script will:
- Copy all 29 commands and 16 agents to your vault
- Create PARA folder structure (if missing)
- Copy templates and CLAUDE.md
- Install research tools (Zotero MCP, PaperQA2)
- Provide setup instructions for Obsidian plugins

### Start Fresh with Sample Vault

1. Clone this repository
2. Open `Obsidian-Template-Vault` folder as a vault in Obsidian
3. Enable the Local REST API plugin
4. Copy your API key to `.claude/mcp.json`
5. Run Claude Code: `claude`

### Prerequisites

- [Obsidian](https://obsidian.md) with Local REST API plugin enabled
- [Claude Code CLI](https://claude.ai/code) installed
- Node.js 18+
- Python 3.10+ (for research tools)

### Research Tools Installation

```bash
# Install uv (recommended package manager)
pip install uv

# Zotero MCP - Reference library integration
uv tool install "git+https://github.com/54yyyu/zotero-mcp.git"
zotero-mcp setup --skip-semantic-search
zotero-mcp update-db --fulltext  # Build search index

# PaperQA2 - Evidence-based Q&A over PDFs
pip install "paper-qa>=5"
```

## Project Structure

```
.
├── .claude/                          # Claude Code configuration
│   ├── agents/                       # 16 specialized AI agents
│   ├── commands/                     # 29 slash commands
│   ├── skills/                       # 18 AI skills
│   ├── hooks/                        # Automation hooks
│   ├── mcp.json                      # MCP server configuration
│   └── settings.local.json           # Local settings
├── Obsidian-Template-Vault/          # Obsidian vault (PARA structure)
│   ├── 0. Inbox/                     # Capture point
│   ├── 1. Projects/                  # Active initiatives
│   ├── 2. Areas (Ongoing)/           # Ongoing responsibilities
│   ├── 3. Resources (Dynamic)/       # Reference materials
│   ├── 4. Archive (Supportive)/      # Completed items
│   ├── 6. Metadata/                  # System docs & templates
│   └── .obsidian/                    # Obsidian config
├── CLAUDE.md                         # Master Claude configuration
├── INSTALLATION.md                   # Non-technical setup guide
└── README.md                         # This file
```

## Included Plugins (17)

The template vault comes pre-configured with curated plugins for research workflows:

### Essential

| Plugin | Purpose |
|--------|---------|
| [Local REST API](https://github.com/coddingtonbear/obsidian-local-rest-api) | Claude Code MCP integration |
| [MCP Tools](https://github.com/jacksteamdev/obsidian-mcp-tools) | Claude Desktop integration |
| [Dataview](https://github.com/blacksmithgu/obsidian-dataview) | Queries, dashboards |
| [Templater](https://github.com/SilentVoid13/Templater) | Advanced templates |

### Organization

| Plugin | Purpose |
|--------|---------|
| [Omnisearch](https://github.com/scambier/obsidian-omnisearch) | Full-text search |
| [Tag Wrangler](https://github.com/pjeby/tag-wrangler) | Tag management |
| [Auto Note Mover](https://github.com/farux/obsidian-auto-note-mover) | PARA automation |
| [Homepage](https://github.com/mirnovov/obsidian-homepage) | Auto-open dashboard |
| [Calendar](https://github.com/liamcain/obsidian-calendar-plugin) | Daily notes calendar |

### Research & Writing

| Plugin | Purpose |
|--------|---------|
| [Longform](https://github.com/kevboh/longform) | Thesis/paper organization |
| [Kanban](https://github.com/mgmeyers/obsidian-kanban) | Project management |
| [Excalidraw](https://github.com/zsviczian/obsidian-excalidraw-plugin) | Diagrams, flowcharts |
| [Zotero Integration](https://github.com/mgmeyers/obsidian-zotero-desktop-connector) | Import annotations |

### Formatting

| Plugin | Purpose |
|--------|---------|
| [Linter](https://github.com/platers/obsidian-linter) | Markdown formatting |
| [Table Editor](https://github.com/ganesshkumar/obsidian-table-editor) | Spreadsheet-like tables |
| [Banners](https://github.com/noatpad/obsidian-banners) | Visual note headers |
| [Icon Folder](https://github.com/FlorianWoworetz/obsidian-iconize) | Folder icons |

> **Note**: Plugins marked for installation (Longform, Kanban, Excalidraw, Zotero Integration) need to be installed via Obsidian's Community Plugins on first launch.

## Commands

### Knowledge Workflows

| Command | Purpose | Usage |
|---------|---------|-------|
| `/thinking-partner` | Explore ideas through Socratic questioning | Complex problems, brainstorming |
| `/daily-review` | End-of-day reflection and capture | Every evening (5-10 min) |
| `/weekly-synthesis` | Identify patterns across the week | Sunday/Monday (30-60 min) |
| `/research-assistant` | Deep topical investigation with web search | Learning new topics |
| `/inbox-processor` | Organize captured notes via PARA | Weekly or when backlog builds |

### Advanced Analysis

| Command | Purpose | Usage |
|---------|---------|-------|
| `/smart-link` | AI-powered connection suggestions | After creating notes |
| `/graph-analysis` | Analyze knowledge graph health | Monthly maintenance |
| `/extract-todos` | Find and consolidate scattered tasks | Weekly task review |
| `/summarize-project` | Create project executive summary | Project check-ins |

### Content Transformation

| Command | Purpose | Usage |
|---------|---------|-------|
| `/flashcards` | Generate spaced repetition cards | Learning/studying |
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
| `/create-architecture-documentation` | Generate architecture docs |

### Academic Research Workflow

| Command | Purpose | Usage |
|---------|---------|-------|
| `/research-ideate` | Socratic exploration of research ideas | Starting new research |
| `/lit-search` | Literature search (Zotero + web) | Finding relevant papers |
| `/deep-research` | Comprehensive multi-source investigation | Background research |
| `/evidence-qa` | Evidence-grounded Q&A over PDFs | Research questions |
| `/lit-review` | Generate structured literature review | Related work sections |
| `/paper-outline` | Create paper structure for venue | Starting paper writing |
| `/paper-draft` | Draft specific paper sections | Writing methodology |
| `/paper-review` | Simulate peer review feedback | Before submission |
| `/paper-polish` | Grammar, style, consistency | Final editing |
| `/export-paper` | Export to LaTeX/PDF/Word | Submission prep |

## AI Skills (18)

Skills provide specialized AI capabilities accessible via natural language or commands:

| Skill | Purpose |
|-------|---------|
| `ai-search` | AI-powered web search |
| `scientific-writing` | Academic paper writing |
| `literature-review` | Research paper synthesis |
| `citation-management` | Citation creation and validation |
| `statistical-analysis` | Statistics and hypothesis testing |
| `plotly` | Interactive data visualizations |
| `seaborn` | Statistical plots |
| `docx` | Word document creation/editing |
| `xlsx` | Excel spreadsheet operations |
| `pdf-processing-pro` | PDF text extraction and analysis |
| `exploratory-data-analysis` | Data file analysis |
| `scientific-slides` | Presentation creation |
| `venue-templates` | Journal/conference templates |
| `perplexity-search` | Perplexity AI search |
| `obsidian-markdown` | Obsidian-flavored markdown |
| `scientific-brainstorming` | Research ideation |
| `scientific-critical-thinking` | Research evaluation |

## Agents

### Obsidian Operations Team

| Agent | Purpose |
|-------|---------|
| `vault-optimizer` | Performance optimization, file size analysis |
| `moc-agent` | Map of Content creation and maintenance |
| `tag-agent` | Tag taxonomy standardization |
| `content-curator` | Content organization and curation |
| `metadata-agent` | Frontmatter and metadata management |
| `connection-agent` | Link and relationship management |
| `review-agent` | Content quality review |

### Development & Documentation

| Agent | Purpose |
|-------|---------|
| `code-reviewer` | Code review for plugin development |
| `debugger` | Debug issues in scripts and plugins |
| `technical-writer` | Documentation generation |
| `security-auditor` | Security analysis |

### Research Team

| Agent | Purpose |
|-------|---------|
| `literature-reviewer` | Literature analysis and synthesis |
| `research-methodologist` | Experimental design and methodology |
| `paper-editor` | Academic writing polish and style |
| `citation-manager` | Citation verification and BibTeX |
| `experiment-designer` | ML experiment design and ablations |

## MCP Integration

The vault connects to Obsidian via the [Model Context Protocol](https://modelcontextprotocol.io/) for direct vault access.

### Configuration

Located in `.claude/mcp.json`:

```json
{
  "mcpServers": {
    "obsidian": {
      "command": "npx",
      "args": ["-y", "mcp-obsidian"],
      "env": {
        "OBSIDIAN_API_KEY": "your-api-key",
        "OBSIDIAN_HOST": "https://127.0.0.1:27124",
        "OBSIDIAN_VERIFY_SSL": "false"
      }
    },
    "zotero": {
      "command": "zotero-mcp",
      "env": {
        "ZOTERO_LOCAL": "true"
      }
    }
  }
}
```

### Obsidian MCP Capabilities

- Direct file read/write operations
- Semantic search across vault
- Programmatic note creation
- Template execution

### Zotero MCP Capabilities

- Semantic search across your library
- Citation retrieval with BibTeX export
- PDF annotation extraction
- Full-text document access

### PaperQA2 Capabilities

- RAG-based Q&A over your PDF corpus
- Evidence-grounded answers with citations
- Multi-document synthesis
- Source verification and scoring

### Setup

**Obsidian MCP:**
1. Install the [Local REST API](https://github.com/coddingtonbear/obsidian-local-rest-api) plugin
2. Enable HTTPS (port 27124)
3. Copy your API key to `.claude/mcp.json`

**Zotero MCP:**
1. Install Zotero 7+ with Local API enabled
2. Run: `pip install git+https://github.com/54yyyu/zotero-mcp.git`
3. Run: `zotero-mcp setup`
4. Build search index: `zotero-mcp update-db --fulltext`

**PaperQA2:**
1. Run: `pip install paper-qa>=5`
2. Set API key: `export ANTHROPIC_API_KEY=your-key` (or `OPENAI_API_KEY`)
3. Usage: `pqa ask "Your question" --paper-directory /path/to/pdfs`

See: [Research Tools Setup.md](Obsidian-Template-Vault/6.%20Metadata/Reference/Research%20Tools%20Setup.md)

## Automation Pipelines

### Voice Memo Processing

```
Record → Transcribe (Whisper) → Sync to Inbox → /voice-process → Structured Note
```

**Setup Options:**
- Apple Shortcuts (iOS)
- PowerShell + Whisper (Windows)
- Tasker (Android)

See: [Workflow - Voice Memo Automation.md](Obsidian-Template-Vault/6.%20Metadata/Workflows/Workflow%20-%20Voice%20Memo%20Automation.md)

### GitHub CI/CD

```
Create Issue (mobile) → GitHub Action → Claude processes → Commits result
```

Trigger vault tasks from anywhere via GitHub Issues with the `claude-task` label.

See: [Workflow - GitHub Automation.md](Obsidian-Template-Vault/6.%20Metadata/Workflows/Workflow%20-%20GitHub%20Automation.md)

### Research Pipeline

```
Query → /research-assistant → Web Search → /web-clip → Synthesis → Structured Notes
```

Automated research with source evaluation (CRAAP test) and structured output.

See: [Workflow - Research Automation.md](Obsidian-Template-Vault/6.%20Metadata/Workflows/Workflow%20-%20Research%20Automation.md)

### Academic Paper Pipeline

```
Ideate → Literature → Evidence → Outline → Draft → Review → Export
```

End-to-end academic paper writing workflow:

1. `/research-ideate` → Research questions & hypotheses
2. `/lit-search` → Find papers in Zotero + web
3. `/evidence-qa` → Ground claims in your PDF corpus
4. `/lit-review` → Synthesize into literature review
5. `/paper-outline` → Structure for target venue
6. `/paper-draft` → Write sections with citations
7. `/paper-review` → Simulate peer review
8. `/export-paper` → LaTeX/PDF for submission

See: [Workflow - Academic Research Pipeline.md](Obsidian-Template-Vault/6.%20Metadata/Workflows/Workflow%20-%20Academic%20Research%20Pipeline.md)

## Hooks

### Conventional Commits

Located in `.claude/hooks/conventional-commits.py`

Validates commit messages follow conventional commit format:
- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation
- `refactor:` - Code refactoring
- `test:` - Tests
- `chore:` - Maintenance

## Templates

Located in `Obsidian-Template-Vault/6. Metadata/Templates/`:

### General Templates

| Template | Purpose |
|----------|---------|
| `Template - Project.md` | Project documentation |
| `Template - Daily Note.md` | Daily journal/review |
| `Template - Meeting Notes.md` | Meeting documentation |
| `Template - Research Note.md` | Research compilation |
| `Template - MOC.md` | Map of Content |

### Academic Research Templates

| Template | Purpose |
|----------|---------|
| `Template - Paper Project.md` | Full paper project tracking |
| `Template - Literature Note.md` | Individual paper notes |
| `Template - Research Ideation.md` | Research idea exploration |
| `Template - Experiment Log.md` | ML experiment tracking |

## Daily Workflow

### Morning (5 min)
1. Review yesterday's note
2. Set top 3 intentions
3. Quick inbox scan

### During Day
1. Capture to `0. Inbox/`
2. Record voice memos for longer thoughts
3. Use `/thinking-partner` for complex problems
4. Clip articles with `/web-clip`

### Evening (5-10 min)
1. Run `/daily-review`
2. Process voice memos with `/voice-process`
3. Quick inbox triage

### Weekly
1. Run `/weekly-synthesis`
2. Full `/inbox-processor` pass
3. Run `/graph-analysis` for vault health
4. Run `/extract-todos` for task consolidation

## Note Standards

### Frontmatter

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

### Naming Conventions

| Type | Format | Example |
|------|--------|---------|
| Regular notes | Title Case | `Meeting with Client.md` |
| Daily notes | Date | `2025-01-10.md` |
| MOCs | Prefixed | `MOC - Topic Name.md` |
| Templates | Prefixed | `Template - Type.md` |
| Voice memos | Prefixed | `Voice-2025-01-10-1430.md` |
| Web clips | Prefixed | `Clip - Article Title.md` |

### Tag Hierarchy

```
content/       → notes, projects, research, voice-memo, web-clip
topics/        → technology, business, personal
status/        → active, review, unprocessed, archived
type/          → moc, meeting, thinking-log, flashcards
```

## PARA Method

| Folder | Criteria | Examples |
|--------|----------|----------|
| `1. Projects` | Has deadline, specific outcome | Client work, launches |
| `2. Areas (Ongoing)` | No end date, ongoing responsibility | Health, finances |
| `3. Resources (Dynamic)` | Reference material | Research, how-tos |
| `4. Archive (Supportive)` | Completed or inactive | Done projects |

## Security

- Vault repository should be **private**
- API keys stored in environment variables or `.claude/mcp.json` (gitignored)
- Review GitHub Action logs for sensitive data
- Use `.gitignore` for personal/sensitive notes
- Keep plugins updated

## Troubleshooting

### MCP Connection Issues

1. Ensure Obsidian is running with Local REST API enabled
2. Verify HTTPS is enabled on port 27124
3. Check API key matches in `.claude/mcp.json`
4. Restart Claude Code after config changes

### Command Not Found

Commands must be run from within Claude Code CLI:
```bash
claude
> /thinking-partner
```

### Voice Processing Issues

1. Ensure transcription is complete before processing
2. Check file is in `0. Inbox/` with correct naming
3. Verify `voice-memo` tag is present

## Credits

Built with:

**Core Integration:**
- [Claude Code Templates](https://github.com/davila7/claude-code-templates) - CLI tool for templates
- [Claudesidian](https://github.com/heyitsnoah/claudesidian) - Thinking partner philosophy
- [mcp-obsidian](https://github.com/smithery-ai/mcp-obsidian) - MCP server for Obsidian
- [Obsidian Local REST API](https://github.com/coddingtonbear/obsidian-local-rest-api) - REST API plugin

**Research Tools:**
- [Zotero MCP](https://github.com/54yyyu/zotero-mcp) - Reference library integration
- [PaperQA2](https://github.com/Future-House/paper-qa) - Evidence-based Q&A over PDFs
- [OpenDraft](https://github.com/federicodeponte/opendraft) - Multi-agent paper generation
- [GPT Researcher](https://github.com/assafelovic/gpt-researcher) - Deep research agent
- [Claude Scientific Writer](https://github.com/K-Dense-AI/claude-scientific-writer) - Academic writing toolkit

## License

MIT

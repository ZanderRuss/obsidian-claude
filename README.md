# Obsidian + Claude Integration

A comprehensive, **portable** integration between [Obsidian](https://obsidian.md) and [Claude Code](https://claude.ai/code) for AI-powered knowledge management and research using the PARA method.

**31 commands • 26 agents • 18 AI skills • 3 hooks • 17 curated plugins • Full research workflow • MCP integration**

---

## The Problem

> Your ideas are scattered across note apps, documents, AI chat histories, and your head. Great conversations vanish. Insights never connect. There's a gap between capturing a thought and actually developing it into something deeper. 

---

## Philosophy

> Capture it. Store it. Connect it. Your thoughts, research, chats, documents, and projects all organised and woven into an interconnected web, surfacing insights across domains. From scattered ideas to structured knowledge, AI that thinks *with* you, not *for* you."

---

### Amplify Your Thinking

Claude becomes your research partner, thought partner, and writing partner—helping you dig deeper into ideas, challenge your assumptions, and discover angles you hadn't considered. Your vault accumulates context over time, so every conversation builds on the last. The more you use it, the smarter the system gets.

<p align="center">
<img src="images/Amplify-Thinking.png" alt="Amplify - Research partner, thought partner, writing partner" width="100%">
</p>

---

### Explore Before You Create

Before writing that paper or making that decision—map the territory. Claude helps you explore the problem space, ask better questions, and surface hidden assumptions. Understand what you're really trying to achieve before jumping to solutions. Deep thought before creation leads to work that's actually worth creating.

<p align="center">
<img src="images/Explore-Before-Creation.png" alt="Explore - Deep thought before creation" width="100%">
</p>

---

### Connect Ideas, Find Patterns

The real breakthroughs happen when ideas connect across domains. Claude helps you weave threads between notes, surface forgotten insights, and notice patterns you'd otherwise miss. Transform scattered thoughts into structured understanding—where every idea finds its place in a growing web of knowledge.


<p align="center">
<img src="images/Connect-Discover.png" alt="Connect - Link ideas, find patterns" width="100%">
</p>

---

### Iterate Toward Understanding

Understanding builds through cycles of exploration, creation, and refinement. Each conversation with Claude, each note you capture, each connection you make adds another layer. Don't aim for perfect first drafts—aim for progressive clarity. Your vault grows not just in size, but in depth and interconnectedness.

<p align="center">
<img src="images/Iterate-Incrementally.png" alt="Iterate - Build understanding incrementally" width="100%">
</p>

---

## Why Obsidian?

### Your Data, Your Control

- **Local-first** — Your notes are plain markdown files on your computer, not locked in someone's cloud
- **No subscription required** — Free for personal use, forever
- **Future-proof** — Even if Obsidian disappears, your files remain readable
- **Privacy** — Your thoughts never leave your machine unless you choose to sync them

### Powerful by Design

- **Bidirectional links** — Connect ideas with `[[wikilinks]]` and see what links back
- **Graph view** — Visualize your knowledge as an interconnected web
- **Search everything** — Full-text search across thousands of notes in milliseconds
- **Extensible** — 1,500+ community plugins to customize your workflow

### Why It Pairs Perfectly with Claude

| Obsidian Provides | Claude Provides |
|-------------------|-----------------|
| Permanent storage | Intelligent conversation |
| Structure (folders, tags, links) | Pattern recognition |
| Your accumulated context | Fresh thinking and connections |
| Plain text you own | AI that reads and writes it |

---

## The PARA Method

PARA organises your knowledge by **actionability**, not by topic. Everything goes in one of four folders:

| Folder | What Goes Here | Key Question |
|--------|----------------|--------------|
| **P**rojects | Active work with a deadline | "What am I working on right now?" |
| **A**reas | Ongoing responsibilities (no end date) | "What do I need to maintain?" |
| **R**esources | Reference material, interests | "What might be useful someday?" |
| **A**rchive | Completed or inactive items | "What's done or on hold?" |

### Why This Works

**Traditional approach:** Organise by topic (like a library)
- Problem: Where does "AI for climate research" go? AI folder? Climate folder? Research folder?

**PARA approach:** Organize by what you're *doing* with it
- If it's an active project → Projects
- If it's ongoing responsibility → Areas  
- If it's just reference → Resources
- If it's done → Archive

**The result:** Active work stays visible. Everything else gets out of the way. When a project finishes, move it to Archive. When you start something new, it goes in Projects. Simple.

### PARA + Claude

Claude helps you *use* PARA without thinking about it:
- `/inbox-processor` — Automatically sorts captured notes into the right folder
- `/daily-review` — Surfaces what needs attention today
- `/weekly-synthesis` — Finds patterns across your week's notes

---

### In Practice

| Instead of... | Try... |
|---------------|--------|
| "Write my introduction" | "Help me figure out what my paper is really arguing" |
| "Summarize this article" | "What are the key ideas here and how do they connect to my research?" |
| "Give me a literature review" | "What questions should I be asking about this topic?" |

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

**Two-Track System:**
- **Quick Research**: 5-10 sources, single file, ~15-30 min, no quality gates
- **Complete Research**: 20+ sources (12 peer-reviewed), 6-phase pipeline, PhD-grade with enforced quality gates

| Command | Purpose | Track | Usage |
|---------|---------|-------|-------|
| `/research-ideate` | Socratic exploration of research ideas | Both | Starting new research |
| `/quick-research` | Rapid 5-10 source investigation | Quick | Exploration, background research |
| `/research-project-init` | Create phased research folder structure | Complete | Starting PhD-level projects |
| `/research-progress` | Check research phase completion & gaps | Complete | Progress tracking, source analysis |
| `/lit-search` | Literature search (Zotero + web) | Both | Finding relevant papers |
| `/deep-research` | Comprehensive multi-source investigation | Complete | Background research, surveys |
| `/evidence-qa` | Evidence-grounded Q&A over PDFs | Complete | Research questions with citations |
| `/lit-review` | Generate structured literature review | Complete | Related work sections |
| `/paper-outline` | Create paper structure for venue | Complete | Starting paper writing |
| `/paper-draft` | Draft specific paper sections | Complete | Writing methodology, experiments |
| `/paper-review` | Simulate peer review feedback | Complete | Before submission |
| `/paper-polish` | Grammar, style, consistency | Complete | Final editing pass |
| `/export-paper` | Export to LaTeX/PDF/Word | Complete | Submission preparation |

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

## Agents (26)

### Obsidian Operations Team (7)

| Agent | Purpose |
|-------|---------|
| `vault-optimizer` | Performance optimization, file size analysis |
| `moc-agent` | Map of Content creation and maintenance |
| `tag-agent` | Tag taxonomy standardization |
| `content-curator` | Content organization and curation |
| `metadata-agent` | Frontmatter and metadata management |
| `connection-agent` | Link and relationship management |
| `review-agent` | Content quality review |

### Workflow Support (3)

| Agent | Purpose |
|-------|---------|
| `prompt-engineer` | Prompt optimization |
| `search-specialist` | Deep web research and fact-checking |
| `task-decomposition-expert` | Break complex projects into steps |

### Research Team (16)

<p align="center">
<img src="images/Research-Team.png" alt="Research - Literature review, research methodologist, paper editor, citation manager, experiment designer" width="100%">
</p>

| Category | Agents |
|----------|--------|
| **Orchestration** (5) | `research-orchestrator`, `research-coordinator`, `research-progress-tracker`, `research-brief-generator`, `query-clarifier` |
| **Gathering** (4) | `academic-researcher`, `technical-researcher`, `data-analyst`, `fact-checker` |
| **Analysis** (4) | `research-synthesizer`, `literature-reviewer`, `citation-manager`, `research-methodologist` |
| **Writing** (3) | `report-generator`, `paper-editor`, `experiment-designer` |

## Hooks (3)

Hooks are Python scripts that run automatically to transform and validate Claude's output:

| Hook | Trigger | Purpose |
| ------ | --------- | --------- |
| `obsidian-markdown.py` | Write to vault files | Converts standard markdown to Obsidian format (wikilinks, callouts, frontmatter) |
| `conventional-commits.py` | Git commits | Validates commit messages follow conventional format (`feat:`, `fix:`, etc.) |
| `research-quality-gate.py` | Write to research files | Enforces citation requirements for Complete Research Track (blocks `[citation needed]`, requires References section) |

**How hooks work:**

- Run silently in the background before tool execution
- Can **pass**, **block**, or **modify** Claude's actions
- Configured in `.claude/settings.json`

See: [.claude/hooks/README.md](.claude/hooks/README.md) for details

## Included Plugins (16)

The template vault comes pre-configured with curated plugins for research workflows:

### Essential

| Plugin | Purpose |
|--------|---------|
| [Local REST API](https://github.com/coddingtonbear/obsidian-local-rest-api) | **Required for MCP** - Enables Claude to read/write your vault |
| [Dataview](https://github.com/blacksmithgu/obsidian-dataview) | Queries, dashboards |
| [Templater](https://github.com/SilentVoid13/Templater) | Advanced templates |

> **Note:** We use [mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) (external Python tool) for MCP connectivity, which connects via the Local REST API plugin.

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

This vault supports **two research tracks**:

**Quick Research Track** (exploration, background research):

```
/quick-research → WebSearch (5-10 sources) → Single Output File
```

- No quality gates
- ~15-30 minutes
- Output: `3. Resources (Dynamic)/Research/Quick Research - [Topic].md`

**Complete Research Track** (PhD-grade, publications, thesis):

```
/research-project-init → 6-Phase Pipeline:
  Phase 0: Brief (00-brief.md)
  Phase 1: Sources (10-sources.md)
  Phase 2: Notes (20-notes.md)
  Phase 3: Synthesis (30-synthesis.md) ← Quality Gate (citations required)
  Phase 4: Draft (40-draft.md) ← Quality Gate (no unsupported claims)
  Phase 5: Bibliography (99-bibliography.md)

/research-progress → Check phase completion and gaps
```

**Full Academic Pipeline**:

1. `/research-ideate` → Research questions & hypotheses
2. `/lit-search` → Find papers in Zotero + web
3. `/evidence-qa` → Ground claims in your PDF corpus
4. `/lit-review` → Synthesize into literature review
5. `/paper-outline` → Structure for target venue
6. `/paper-draft` → Write sections with citations
7. `/paper-review` → Simulate peer review
8. `/paper-polish` → Final editing pass
9. `/export-paper` → LaTeX/PDF for submission

See: [Workflow - Academic Research Pipeline.md](Obsidian-Template-Vault/6.%20Metadata/Workflows/Workflow%20-%20Academic%20Research%20Pipeline.md)

## MCP Integration (Connecting Claude to Your Vault)

MCP (Model Context Protocol) lets Claude directly read and write to your Obsidian vault and Zotero library. This is **optional** but powerful.

---

### Quick Setup (5 minutes)

#### Step 1: Install the Obsidian Plugin

1. Open **Obsidian** with your vault
2. Go to **Settings** (gear icon) → **Community plugins**
3. Click **Browse**, search for "**Local REST API**"
4. Click **Install**, then **Enable**
5. Go back to **Community plugins** → click **Local REST API**
6. **Copy the API key** shown at the top (you'll need this!)

#### Step 2: Install Required Tools

Open a terminal (PowerShell on Windows, Terminal on Mac) and run:

```bash
# Install uv (Python package manager) if you don't have it
pip install uv

# Install the Obsidian MCP connector
# (This happens automatically when Claude starts, but you can pre-install)
uvx mcp-obsidian --help
```

**For Zotero users** (optional):
```bash
pip install zotero-mcp
```

#### Step 3: Configure Claude

You need to tell Claude where to find Obsidian. There are **two places** to configure this, depending on how you use Claude:

| How You Use Claude | Config File Location |
|--------------------|---------------------|
| **Claude Desktop App** (chat interface) | See "Claude Desktop Setup" below |
| **Claude Code** (terminal/CLI) | See "Claude Code Setup" below |

> **Tip:** Configure both if you want MCP everywhere!

---

### Claude Desktop Setup

1. **Find the config file:**
   - **Windows:** Press `Win+R`, type `%APPDATA%\Claude`, press Enter. Open `claude_desktop_config.json`
   - **Mac:** Open Finder, press `Cmd+Shift+G`, type `~/Library/Application Support/Claude/`

2. **Add this to the file** (inside the `"mcpServers": {` section):

```json
    "obsidian": {
      "command": "uvx",
      "args": ["mcp-obsidian"],
      "env": {
        "OBSIDIAN_API_KEY": "PASTE-YOUR-API-KEY-HERE"
      }
    },
    "zotero": {
      "command": "zotero-mcp",
      "args": ["serve"],
      "env": {
        "ZOTERO_LOCAL": "true"
      }
    }
```

3. **Replace** `PASTE-YOUR-API-KEY-HERE` with the key you copied from Obsidian
4. **Restart Claude Desktop** (File → Quit, then reopen)

---

### Claude Code Setup

1. **Copy the example config:**
   ```bash
   cp .mcp.json.example .mcp.json
   ```

2. **Edit `.mcp.json`** and replace `YOUR_OBSIDIAN_API_KEY_HERE` with your API key

```json
{
  "mcpServers": {
    "obsidian": {
      "command": "uvx",
      "args": ["mcp-obsidian"],
      "env": {
        "OBSIDIAN_API_KEY": "your-api-key-from-plugin"
      }
    },
    "zotero": {
      "command": "zotero-mcp",
      "args": ["serve"],
      "env": {
        "ZOTERO_LOCAL": "true"
      }
    }
  }
}
```

3. **Start Claude Code from the project directory:**
   ```bash
   cd /path/to/obsidian-claude
   claude
   ```

> **Note:** MCP servers only load when Claude Code starts. After changing `.mcp.json`, open a new terminal and run `claude` again.

---

### Troubleshooting MCP

**"MCP not connecting"**
- Is Obsidian running? (It must be open!)
- Is Zotero running? (Required for Zotero MCP)
- Did you restart Claude after editing the config?
- Does your API key match exactly? (No extra spaces)

**"Command not found: uvx"**
- Run `pip install uv` first

**Still stuck?**
- Check the [mcp-obsidian docs](https://github.com/MarkusPfundstein/mcp-obsidian)
- See `6. Metadata/Reference/Local REST API Setup.md` in the vault

---

### What MCP Enables

Once connected, Claude can:

| Obsidian | Zotero |
|----------|--------|
| Read/write notes directly | Search your library |
| Search across your vault | Get citations + BibTeX |
| Create notes from templates | Extract PDF annotations |
| Navigate between linked notes | Full-text document access |

### PaperQA2 Capabilities

- RAG-based Q&A over your PDF corpus
- Evidence-grounded answers with citations
- Multi-document synthesis
- Source verification and scoring

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

## Hooks (3)

### Obsidian Markdown Converter

Located in `.claude/hooks/obsidian-markdown.py`

Automatically converts standard markdown to Obsidian Flavored Markdown when writing to vault files:

- `[text](file.md)` → `[[file|text]]` (wikilinks)
- `![alt](image.png)` → `![[image.png]]` (embeds)
- `> Note:` → `> [!note]` (callouts)
- Adds frontmatter if missing (tags, type, created, status)

**Path coverage**: Processes all vault files including `0. Inbox`, `1. Projects`, `2. Areas`, `3. Resources`, `4. Archive`, and `6. Metadata`.

This runs silently in the background—paste research in any format and it auto-converts.

### Conventional Commits

Located in `.claude/hooks/conventional-commits.py`

Validates commit messages follow conventional commit format:

- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation
- `refactor:` - Code refactoring
- `test:` - Tests
- `chore:` - Maintenance

### Research Quality Gate

Located in `.claude/hooks/research-quality-gate.py`

Enforces citation requirements for Complete Research Track files:

- **Phase 3 (Synthesis)**: Requires citations, blocks `[citation needed]` markers
- **Phase 4 (Draft)**: Requires References section, blocks `[unsupported]` markers

Quality gates only apply to standard phase file names (`30-synthesis`, `40-draft`). Save as WIP to bypass temporarily.

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
- Copy all 31 commands and 26 agents to your vault
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

### MCP Setup

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

## Project Structure

```
.
├── .claude/                          # Claude Code configuration
│   ├── agents/                       # 26 specialized AI agents
│   │   ├── obsidian-operations/      # 7 vault maintenance agents
│   │   ├── workflow-support/         # 3 planning/research agents
│   │   └── research-team/            # 16 research & writing agents
│   ├── commands/                     # 31 slash commands
│   ├── skills/                       # 18 AI skills
│   ├── hooks/                        # 3 automation hooks
│   │   ├── obsidian-markdown.py      # Markdown format conversion
│   │   ├── conventional-commits.py   # Commit message validation
│   │   └── research-quality-gate.py  # Research citation enforcement
│   ├── mcp.json                      # MCP server configuration
│   └── settings.json                 # Project settings & hook registration
├── Obsidian-Template-Vault/          # Obsidian vault (PARA structure)
│   ├── 0. Inbox/                     # Capture point
│   ├── 1. Projects/                  # Active initiatives
│   ├── 2. Areas (Ongoing)/           # Ongoing responsibilities
│   ├── 3. Resources (Dynamic)/       # Reference materials
│   ├── 4. Archive (Supportive)/      # Completed items
│   ├── 6. Metadata/                  # System docs & templates
│   │   ├── Templates/                # Note templates (including Research/)
│   │   ├── Workflows/                # Automation documentation
│   │   └── Reference/                # System reference & guides
│   └── .obsidian/                    # Obsidian config (17 plugins)
├── CLAUDE.md                         # Master Claude configuration
├── INSTALLATION.md                   # Non-technical setup guide
└── README.md                         # This file
```

## Security

- Vault repository should be **private**
- API keys stored in environment variables or `.claude/mcp.json` (gitignored)
- Review GitHub Action logs for sensitive data
- Use `.gitignore` for personal/sensitive notes
- Keep plugins updated

## Troubleshooting

### MCP Connection Issues (Local REST API)

**Quick checklist:**

1. Is Obsidian running? (The API only works when Obsidian is open)
2. Is the Local REST API plugin enabled in Obsidian?
3. Does the API key in your config match the one in plugin settings?
4. Did you restart Claude Code after changing the config?

**Step-by-step diagnosis:**

1. **Check Obsidian plugin settings:**
   - Settings > Community plugins > Local REST API
   - Verify "Enable Encrypted (HTTPS) Server" is ON
   - Note the port (default: 27124 for HTTPS, 27123 for HTTP)

2. **Verify your configuration:**
   ```json
   {
     "OBSIDIAN_API_KEY": "must-match-plugin-settings",
     "OBSIDIAN_HOST": "https://127.0.0.1:27124",
     "OBSIDIAN_VERIFY_SSL": "false"
   }
   ```

3. **Test the API manually:**
   - Open browser: `http://127.0.0.1:27123/` (if HTTP enabled)
   - You should see a response (even an auth error means it's working)

**If HTTPS isn't working, try HTTP:**

1. In plugin settings, enable "Enable Non-encrypted (HTTP) Server"
2. Update config: `"OBSIDIAN_HOST": "http://127.0.0.1:27123"`
3. Remove `OBSIDIAN_VERIFY_SSL` line
4. Restart Claude Code

**Certificate issues:**

The plugin uses a self-signed SSL certificate. If you see certificate errors:
- Use `"OBSIDIAN_VERIFY_SSL": "false"` in your config
- Or switch to HTTP mode (port 27123)
- Or click "Re-generate Certificates" in plugin settings

See [Local REST API documentation](https://coddingtonbear.github.io/obsidian-local-rest-api/) for more details.

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
- [mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) - MCP server for Obsidian
- [Obsidian Local REST API](https://github.com/coddingtonbear/obsidian-local-rest-api) - REST API plugin

**Research Tools:**
- [Zotero MCP](https://github.com/54yyyu/zotero-mcp) - Reference library integration
- [PaperQA2](https://github.com/Future-House/paper-qa) - Evidence-based Q&A over PDFs
- [OpenDraft](https://github.com/federicodeponte/opendraft) - Multi-agent paper generation
- [GPT Researcher](https://github.com/assafelovic/gpt-researcher) - Deep research agent
- [Claude Scientific Writer](https://github.com/K-Dense-AI/claude-scientific-writer) - Academic writing toolkit

## License

MIT

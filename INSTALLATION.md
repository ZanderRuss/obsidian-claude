# Obsidian + Claude: Your AI-Powered Second Brain

Turn your Obsidian vault into an intelligent knowledge management system with Claude as your thinking partner.

**No coding required.** Setup takes about 10 minutes.

---

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

## Get Started in 4 Steps

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

**Extract the ZIP file** to a location you'll remember:
- Good location: `Documents/obsidian-claude/`
- The extracted folder should contain `SETUP.bat`, `README.md`, etc.

### Step 2: Open the Folder in Claude Code Desktop

This is the crucial step that connects Claude to your project.

1. **Open Claude Code Desktop** (the app, not the website)
2. **Select the folder** you just extracted
   - Click "Open Folder" or use File > Open Folder
   - Navigate to the folder containing `SETUP.bat` and `README.md`
   - Select it and click "Open"

```
+------------------------------------------+
|  Claude Code Desktop                     |
|  +------------------------------------+  |
|  |                                    |  |
|  |  [Open Folder]  <-- Click this     |  |
|  |                                    |  |
|  |  Then select your obsidian-claude  |  |
|  |  folder                            |  |
|  +------------------------------------+  |
+------------------------------------------+
```

> **Why this matters:** Claude Code Desktop can only work with files in the folder you select. This step gives Claude access to the project files.

### Step 3: Run Setup (Inside Claude Code Desktop)

Now that Claude can see your files, run the setup script:

**Windows:** Type in the chat: `run SETUP.bat`

**Mac/Linux:** Type in the chat: `run SETUP.command`

Or just ask Claude: "Please run the setup script"

The setup will:
- Check for Python (and help you install it if needed)
- Install the tools that power the AI skills
- Create the Obsidian vault template

### Step 4: Open the Vault in Obsidian

1. **Open Obsidian** (download from [obsidian.md](https://obsidian.md) if needed)
2. Click **"Open folder as vault"**
3. Navigate to: `your-folder/Obsidian-Template-Vault/`
4. Click "Open"

```
+------------------------------------------+
|  Obsidian                                |
|  +------------------------------------+  |
|  |                                    |  |
|  |  Open folder as vault              |  |
|  |  [Obsidian-Template-Vault]         |  |
|  |                                    |  |
|  +------------------------------------+  |
+------------------------------------------+
```

**That's it!** You now have:
- Claude Code Desktop open to your project folder
- Obsidian open to your new vault
- Both working together!

---

## After Setup: Connect Claude to Your Vault

This lets Claude read and write notes directly in your vault.

Ask Claude in Claude Code Desktop:
> "Help me connect you to my Obsidian vault"

Claude will walk you through:
1. Installing the Local REST API plugin in Obsidian
2. Copying the API key
3. Adding it to your configuration

---

## Alternative: Use With an Existing Vault

If you already have an Obsidian vault you want to use:

1. Download and extract this project
2. Copy the `.claude/` folder from this project into your vault's folder
3. Open your vault folder in Claude Code Desktop
4. Run the setup script

> ⚠️ **Note:** For testing, we recommend using the included template vault first. Once you're comfortable, you can apply it to your main vault.

---

## What You Get

### 18 AI Skills

Type commands like `/ai-search` or `/scientific-writing` to access specialized AI capabilities:

**Research & Writing**
- Literature reviews and paper searches
- Citation management
- Academic writing assistance
- Templates for major journals (Nature, IEEE, NeurIPS, etc.)

**Data & Analysis**
- Statistical analysis
- Interactive charts and visualizations
- Data exploration

**Documents**
- Word documents (.docx)
- Excel spreadsheets (.xlsx)
- PDF text extraction

**Web Search**
- AI-powered web search (works out of the box!)

### Obsidian Vault Template

A ready-to-use vault organized with the PARA method:
- **Projects** - Active work with deadlines
- **Areas** - Ongoing responsibilities
- **Resources** - Reference materials
- **Archive** - Completed items

Includes 17 curated plugins for research workflows.

### (Optional) Direct Vault Connection

Connect Claude directly to your Obsidian vault so it can read and write notes for you. Claude will help you set this up.

---

## Requirements

| What | Where to Get It |
|------|-----------------|
| Claude Desktop | [claude.ai/download](https://claude.ai/download) |
| Obsidian | [obsidian.md](https://obsidian.md) |
| Python (free) | Setup script will help you install it |

**Operating Systems:** Windows 10+, macOS 12+, Linux

---

## Frequently Asked Questions

### Do I need to know how to code?
**No.** The setup scripts handle everything automatically. You just click and follow instructions.

### Is Python required?
Python is needed for some advanced features (like searching academic databases directly). The setup script will help you install it - it's free and takes about 2 minutes. Most features work fine without Python too.

### Do I need to pay for anything?
You need a Claude subscription (Pro or Team) for Claude Desktop. Everything else is free.

### What if I already have an Obsidian vault?
You can use the skills with any vault! The included template is just a starting point. Claude can help you integrate the tools with your existing vault.

### How do I get help?
- Ask Claude! Just describe your problem.
- Check the [GitHub Issues](https://github.com/ZanderRuss/obsidian-claude/issues)
- Read the troubleshooting section in Claude-Instructions.md

---

## Quick Reference Card

```
MOST USEFUL COMMANDS

/ai-search           Search the web for current info
/scientific-writing  Help writing academic papers
/literature-review   Find and organize research
/citation-management Create and format citations
/statistical-analysis Statistics and data analysis
/plotly              Create interactive charts
/docx                Work with Word documents
/xlsx                Work with Excel files

TIP: You can also just ask naturally:
"Find papers about machine learning"
"Help me analyze this data"
"Create a citation for this article"
```

---

---

## For Developers

<details>
<summary>Click to expand technical details</summary>

### Philosophy

> "AI amplifies thinking, not just writing."

This vault uses Claude as a **thinking partner** - an AI that helps explore ideas through dialogue:

- **Questions before answers** - Clarify understanding through inquiry
- **Exploration before production** - Think deeply before creating
- **Connections over content** - Link ideas, find patterns
- **Iteration over perfection** - Build understanding incrementally

### Project Structure

```
.
├── .claude/                          # Claude Code configuration
│   ├── agents/                       # 16 specialized AI agents
│   ├── commands/                     # 29 slash commands
│   ├── skills/                       # 18 AI skills
│   ├── hooks/                        # Automation hooks
│   └── settings.json                 # Settings
├── Obsidian-Template-Vault/          # Obsidian vault (PARA structure)
│   ├── 0. Inbox/                     # Capture point
│   ├── 1. Projects/                  # Active initiatives
│   ├── 2. Areas (Ongoing)/           # Ongoing responsibilities
│   ├── 3. Resources (Dynamic)/       # Reference materials
│   ├── 4. Archive (Supportive)/      # Completed items
│   ├── 6. Metadata/                  # System docs & templates
│   └── .obsidian/                    # Obsidian config
├── CLAUDE.md                         # Master Claude configuration
├── SETUP.bat                         # Windows setup script
├── SETUP.command                     # Mac/Linux setup script
└── README.md                         # This file
```

### Manual Setup (Alternative to Scripts)

```bash
# Clone the repository
git clone https://github.com/ZanderRuss/obsidian-claude.git
cd obsidian-claude

# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate
# Activate (Mac/Linux)
source .venv/bin/activate

# Install dependencies
pip install -r .claude/skills/requirements.txt
```

### Apply to Existing Vault

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

### Configuration Files

| File | Purpose | Used By | Committed? |
|------|---------|---------|------------|
| `.mcp.json` | MCP config (project root) | Claude Code CLI | No (gitignored) |
| `.mcp.json.example` | Template to copy | — | Yes |
| `claude_desktop_config.json` | MCP config in AppData | Claude Desktop App | No |
| `.claude/settings.json` | Shared project settings | Both | Yes |
| `.claude/settings.local.json` | Your local overrides | Both | No (gitignored) |

### MCP Configuration

This project supports **two different Claude environments**:

| Environment | What It Is | Config Location |
|-------------|------------|-----------------|
| **Claude Desktop App** | The standalone desktop application | `%APPDATA%\Claude\claude_desktop_config.json` (Windows) or `~/Library/Application Support/Claude/` (Mac) |
| **Claude Code CLI** | Terminal-based Claude Code | `.mcp.json` in project root |

> **Important:** These are separate configurations. Configure both if you want MCP everywhere.

The vault connects to Obsidian via [Model Context Protocol](https://modelcontextprotocol.io/) using [mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian):

```json
{
  "mcpServers": {
    "obsidian": {
      "command": "uvx",
      "args": ["mcp-obsidian"],
      "env": {
        "OBSIDIAN_API_KEY": "your-api-key"
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

**For Claude Code CLI:**
1. Copy `.mcp.json.example` to `.mcp.json` (at project root)
2. Replace `YOUR_OBSIDIAN_API_KEY_HERE` with your Obsidian Local REST API key
3. Start Claude Code from the project directory: `claude`

**For Claude Desktop App:**
1. Open `%APPDATA%\Claude\claude_desktop_config.json` (Windows) or `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac)
2. Add the obsidian and zotero servers to the `mcpServers` object
3. Fully quit and reopen Claude Desktop

### Research Tools (Advanced)

For researchers needing direct database access:

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

See: [Research Tools Setup.md](Obsidian-Template-Vault/6.%20Metadata/Reference/Research%20Tools%20Setup.md)

### Included Plugins (16)

**Essential:** Local REST API (for MCP), Dataview, Templater

**Organization:** Omnisearch, Tag Wrangler, Auto Note Mover, Homepage, Calendar

**Research:** Longform, Kanban, Excalidraw, Zotero Integration

**Formatting:** Linter, Table Editor, Banners, Icon Folder

### All Commands (29)

| Command | Purpose |
|---------|---------|
| `/thinking-partner` | Explore ideas through questioning |
| `/daily-review` | End-of-day reflection |
| `/weekly-synthesis` | Weekly pattern identification |
| `/research-assistant` | Deep topical investigation |
| `/inbox-processor` | Organize notes via PARA |
| `/smart-link` | AI-powered link suggestions |
| `/graph-analysis` | Knowledge graph health |
| `/extract-todos` | Find scattered tasks |
| `/summarize-project` | Project summaries |
| `/flashcards` | Spaced repetition cards |
| `/note-to-blog` | Transform notes to posts |
| `/voice-process` | Structure transcriptions |
| `/web-clip` | Save web articles |
| `/commit` | Git commits |
| `/create-pr` | Pull requests |
| `/pr-review` | Review PRs |
| `/update-docs` | Update documentation |
| `/create-architecture-documentation` | Architecture docs |
| `/research-ideate` | Research brainstorming |
| `/lit-search` | Literature search |
| `/deep-research` | Comprehensive investigation |
| `/evidence-qa` | Evidence-grounded Q&A |
| `/lit-review` | Literature reviews |
| `/paper-outline` | Paper structure |
| `/paper-draft` | Draft sections |
| `/paper-review` | Peer review simulation |
| `/paper-polish` | Final editing |
| `/export-paper` | Export to LaTeX/PDF |
| `/paper-to-code` | Extract implementations |

### All Agents (16)

**Obsidian Operations:**
vault-optimizer, moc-agent, tag-agent, content-curator, metadata-agent, connection-agent, review-agent

**Development:**
code-reviewer, debugger, technical-writer, security-auditor

**Research:**
literature-reviewer, research-methodologist, paper-editor, citation-manager, experiment-designer

### Automation Pipelines

**Voice Memo Processing:**
```
Record → Transcribe (Whisper) → Sync to Inbox → /voice-process → Structured Note
```

**GitHub CI/CD:**
```
Create Issue (mobile) → GitHub Action → Claude processes → Commits result
```

**Academic Paper Pipeline:**
```
Ideate → Literature → Evidence → Outline → Draft → Review → Export → Code
```

### Note Standards

**Frontmatter:**
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

**Naming Conventions:**
| Type | Format | Example |
|------|--------|---------|
| Regular notes | Title Case | `Meeting with Client.md` |
| Daily notes | Date | `2025-01-10.md` |
| MOCs | Prefixed | `MOC - Topic Name.md` |
| Templates | Prefixed | `Template - Type.md` |

**Tag Hierarchy:**
```
content/  → notes, projects, research, voice-memo, web-clip
topics/   → technology, business, personal
status/   → active, review, unprocessed, archived
type/     → moc, meeting, thinking-log, flashcards
```

### PARA Method

| Folder | Criteria | Examples |
|--------|----------|----------|
| `1. Projects` | Has deadline, specific outcome | Client work, launches |
| `2. Areas (Ongoing)` | No end date, ongoing responsibility | Health, finances |
| `3. Resources (Dynamic)` | Reference material | Research, how-tos |
| `4. Archive (Supportive)` | Completed or inactive | Done projects |

### Security

- Vault repository should be **private**
- API keys stored in environment variables or `.claude/mcp.json` (gitignored)
- Review GitHub Action logs for sensitive data
- Use `.gitignore` for personal/sensitive notes
- Keep plugins updated

### Troubleshooting

**MCP Connection Issues:**
1. Ensure Obsidian is running with Local REST API enabled
2. Verify HTTPS is enabled on port 27124
3. Check API key matches in `.claude/mcp.json`
4. Restart Claude Code after config changes

**Command Not Found:**
Commands must be run from within Claude Code CLI:
```bash
claude
> /thinking-partner
```

</details>

---

## Credits

Built with [mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian), [Zotero MCP](https://github.com/54yyyu/zotero-mcp), [PaperQA2](https://github.com/Future-House/paper-qa), and many other open source projects.

Inspired by [Claudesidian](https://github.com/heyitsnoah/claudesidian) and the "AI as thinking partner" philosophy.

## License

MIT

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
Obsidian-Vault-Live/
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

### Vault Maintenance

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/vault-optimize` | Analyze performance, file sizes, attachments | Monthly or when vault feels slow |
| `/moc-generate` | Identify and create missing Maps of Content | After adding many notes, monthly |
| `/tag-normalize` | Standardize tag taxonomy, merge duplicates | Quarterly or when tags feel messy |
| `/content-curate` | Find outdated/redundant content, suggest improvements | Monthly content review |
| `/metadata-fix` | Standardize frontmatter across all notes | After bulk imports, quarterly |
| `/find-connections` | Discover missing links between related notes | After creating notes, weekly |
| `/vault-review` | Comprehensive quality audit of entire vault | Monthly or before major work |

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
| `/paper-prep` | Setup tracking systems before writing | Starting new paper/thesis |

### Pre-Writing Quality Setup

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/paper-prep` | Create tracking systems (citations, metrics, abbreviations, scope) | Before drafting ANY academic document |

**What `/paper-prep` creates:**
- **Citation Tracker** - ensure every claim sourced
- **Abbreviation Tracker** - define on first use
- **Key Metrics Table** - single source of truth for numbers
- **Study Boundaries** - prevent over-generalization
- **README** - usage instructions

**Integration with `/paper-write` and `/thesis-write`:**
- Orchestrators check for tracking systems on startup
- Quality gates validate against tracking systems during writing
- Prevents issues like numeric inconsistencies, missing citations, undefined abbreviations

**Time investment:** 30-60 minutes setup saves 4+ hours of rework

### Thesis & Paper Writing (Multi-Agent Pipeline)

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/thesis-init` | Initialize thesis project structure | Starting PhD thesis or large document |
| `/thesis-write` | Write complete thesis with multi-agent pipeline | Full thesis production (90k+ words) |
| `/chapter-write` | Write single chapter | Individual chapter drafting |
| `/paper-write` | Write conference/journal paper | Conference submissions, journal articles |
| `/quality-check` | Run all quality control agents | Before submission, after major revisions |
| `/paper-revise` | Handle reviewer feedback | Post-review revision process |

## Available Agents

### Obsidian Operations Team

These agents can be invoked via slash commands (see Vault Maintenance section above):

| Agent | Command | Purpose |
|-------|---------|---------|
| **vault-optimizer** | `/vault-optimize` | Performance optimization, file size analysis, attachment management |
| **moc-agent** | `/moc-generate` | Map of Content creation and maintenance |
| **tag-agent** | `/tag-normalize` | Tag taxonomy standardization and hierarchy |
| **content-curator** | `/content-curate` | Content organization and curation |
| **metadata-agent** | `/metadata-fix` | Frontmatter and metadata management |
| **connection-agent** | `/find-connections` | Link and relationship management |
| **review-agent** | `/vault-review` | Content quality review |

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

### Paper-Writing Team

Multi-agent system for PhD-level academic writing (22 agents across 5 layers):

**Orchestration Layer:**
- **thesis-orchestrator**: Coordinates entire thesis writing process
- **chapter-coordinator**: Manages single chapter production
- **paper-orchestrator**: Coordinates conference/journal paper writing

**Section Writers:**
- **introduction-writer**: Introduction with research questions, contributions
- **lit-review-writer**: Literature review with synthesis and gap identification
- **methodology-writer**: Methods section with domain-appropriate terminology
- **results-writer**: Results with figures, tables, and analysis
- **discussion-writer**: Interpretation, limitations, implications
- **conclusion-writer**: Summary and future work
- **abstract-writer**: Structured abstracts
- **figure-designer**: Figure captions and table descriptions

**Quality Control:**
- **document-validator**: Consistency, cross-references, numeric consistency, abbreviations, structural changes
- **argument-validator**: Logic, evidence, claim support, hedging, evidence hierarchy
- **citation-validator**: Citation accuracy, 6 format patterns, pre/post-conversion verification
- **small-sample-validator**: Enforces hedging for n<30 studies
- **plagiarism-checker**: Paraphrase quality, attribution verification
- **humanization-agent**: Remove AI-generated patterns, ensure natural writing

**Revision Agents:**
- **reviewer-response**: Generate response letters to peer reviewers
- **change-manager**: Track revisions, generate diffs
- **change-integrator**: Merge revisions, resolve conflicts

**Export Pipeline:**
- **latex-specialist**: Convert Markdown to LaTeX
- **formatting-validator**: Venue compliance checking

### Workflow Support

- **prompt-engineer**: Prompt optimization
- **task-decomposition-expert**: Complex task breakdown
- **search-specialist**: Search optimization

## Quality Control System

The vault uses a **3-layer quality system** for academic writing:

### Layer 1: Prevention (Pre-Writing)

- **Tracking systems** (via `/paper-prep`): Citations, metrics, abbreviations, scope boundaries
- **Evidence hierarchy guidance**: Match claim strength to evidence level
- **Methodology templates**: Ensure traceable calculations

### Layer 2: Detection (During Writing)

- **Quality gates at phase transitions**: Validate after section writing, before assembly, before export
- **Fail-fast behavior**: Pipeline halts on critical issues (score < 0.6)
- **Incremental validation**: 5 checkpoints throughout the pipeline

### Layer 3: Validation (Pre-Export)

- **Multi-agent quality control**: 6+ specialized validators
- **Pre-submission checklists**: Venue-specific (conference, journal, thesis, report)
- **Export readiness verification**: Citation format, structural integrity, compliance

### Quality Agents

| Agent | Purpose | Key Checks |
|-------|---------|------------|
| `argument-validator` | Claims and evidence | Evidence hierarchy, hedging, claim support |
| `document-validator` | Document consistency | Numeric consistency, abbreviations, structural changes |
| `citation-validator` | Citation completeness | 6+ format patterns, pre/post-conversion matching |
| `small-sample-validator` | Small sample hedging | Enforces hedging for n<30 studies |
| `plagiarism-checker` | Paraphrase quality | Attribution, originality |
| `humanization-agent` | AI pattern removal | Natural writing style |

### Quality Gate Thresholds

| Score | Status | Action |
|-------|--------|--------|
| >= 0.8 | **Pass** | Proceed to next phase |
| 0.6 - 0.8 | **Warning** | Auto-fix attempt, then proceed |
| 0.4 - 0.6 | **Major** | HALT, require manual fixes |
| < 0.4 | **Critical** | HALT, full diagnostic report |

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

## Home Dashboard

The vault includes a professional dashboard at [Home.md](Obsidian-Vault-Live/Home.md) with:

### Dashboard Features

**Live Metrics:**

- Total notes count
- Active projects count with status warnings
- Inbox items with overflow alerts
- Open tasks tracker
- Areas count

**Today's Focus** (Tasks Plugin):

- 🔥 Overdue & Due Today
- 📌 High Priority Tasks
- ⏰ This Week's tasks
- ✨ Recently Completed

**Organized Sections:**

- Active Projects table
- Areas of Focus (collapsible for quick access)
- Prompt Library preview
- Inbox status
- Recent Activity log
- Knowledge Graph analytics (Hub notes, Orphan notes, Vault growth)
- Recent Notes browser
- Tasks by Project

**Claude Workflows Reference:**

- All commands organized by category (Daily, Research, Writing, Maintenance, Knowledge)
- Quick access to command documentation

### Dashboard Philosophy

The dashboard follows these principles:
- **Simple, reliable queries** over complex calculations
- **Fast loading** (< 2 seconds)
- **Progressive disclosure** (collapsible sections)
- **Working navigation** beats fancy metrics
- **Clarity over complexity**

All Dataview queries use basic syntax for reliability. Task management is handled by the Tasks plugin for robustness.

### Visual Navigation

**[[Vault Overview]]** - Mind Map Integration:

- Open the note, then `Ctrl+P` (Windows) or `Cmd+P` (Mac) → type "mind map" for visual vault structure
- Shows all Projects, Areas, Resources organized hierarchically
- Interactive navigation tool

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

**Dashboard Best Practices:**
- Keep queries simple (avoid nested choice(), date() functions)
- Use TABLE queries for structured data
- Prefer static date formats over dynamic labels
- Let Tasks plugin handle task filtering
- Collapse long sections by default

### Local REST API

Enabled on port 27124 (HTTPS) for external programmatic access. This is required for mcp-obsidian to connect.

## Performance Guidelines

- Keep markdown files under 1MB
- Compress images (85% JPEG quality)
- Archive content older than 2 years
- Remove orphaned attachments periodically
- Use MOCs instead of deeply nested folders
- Run `/graph-analysis` monthly for health checks

## AI Provider Routing

This vault uses multiple AI providers for different tasks. Provider routing is configured via environment variables in `.env`.

### Current Routing Configuration

| Task | Provider | Why |
|------|----------|-----|
| **Web Search** | Claude WebSearch | Built-in, free, no API key needed |
| **Web Search Fallback** | Perplexity | Real-time citations when Claude is rate-limited |
| **Image Generation** | Gemini (Nano Banana Pro) | Best quality for slides and figures |
| **Literature Search** | Perplexity | Real-time academic paper discovery |
| **Text Embeddings** | OpenAI | Industry standard, Zotero MCP uses this |

### Environment Variables for Routing

```bash
# Primary web search provider
AI_SEARCH_PROVIDER=claude

# Fallback when primary is unavailable
AI_SEARCH_FALLBACK=perplexity

# Image generation (slides, figures)
IMAGE_GENERATION_PROVIDER=gemini
IMAGE_GENERATION_MODEL=google/gemini-3-pro-image-preview

# Literature/academic search
LITERATURE_SEARCH_PROVIDER=perplexity
```

### How Skills Use Routing

| Skill | Reads From | Default Behavior |
|-------|------------|------------------|
| `ai-search` | `AI_SEARCH_PROVIDER` | Uses Claude WebSearch unless `--provider` flag specified |
| `perplexity-search` | Always Perplexity | Dedicated Perplexity wrapper |
| `scientific-slides` | `IMAGE_GENERATION_MODEL` | Uses Gemini via OpenRouter for Nano Banana Pro |
| `literature-review` | `LITERATURE_SEARCH_PROVIDER` | Uses Perplexity for real-time paper search |

### Required API Keys by Task

| Task | Required Key | Optional Fallback |
|------|--------------|-------------------|
| Web Search | None (Claude built-in) | `PERPLEXITY_API_KEY` or `OPENROUTER_API_KEY` |
| Image Generation | `OPENROUTER_API_KEY` | `GEMINI_API_KEY` (direct) |
| Literature Search | `PERPLEXITY_API_KEY` | `OPENROUTER_API_KEY` |
| Embeddings | `OPENAI_API_KEY` | — |

### Notes

- **Claude WebSearch** is always the default for web queries—it's free and requires no API key
- **Nano Banana Pro** (Gemini image generation) requires OpenRouter API key
- **Perplexity** can be accessed via direct API key OR via OpenRouter
- Skills auto-load from `.env` file—no manual `export` needed

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

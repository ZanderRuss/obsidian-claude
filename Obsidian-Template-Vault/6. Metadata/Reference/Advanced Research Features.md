---
tags:
  - type/reference
  - topics/research
  - topics/advanced
type: reference
created: 2026-01-11
status: active
---

# Advanced Research Features

This guide covers advanced features for power users and PhD-level research workflows.

## Quick Reference

| Feature | Purpose | Setup Required |
|---------|---------|----------------|
| Complete Research Track | PhD-grade phased research | None (built-in) |
| Quality Gate Hooks | Enforce citation requirements | Enabled by default |
| arXiv MCP | Local paper storage & analysis | Optional install |
| GitHub Actions | Remote/mobile triggering | Repository setup |
| Zotero Integration | Citation management | Zotero MCP required |

---

## Two-Track Research System

This vault supports two distinct research workflows:

### Quick Research (`/quick-research`)

**When to use:**

- Exploring a new topic casually
- Background research for a meeting
- Understanding before committing to deep work
- Time-constrained investigations

**What you get:**

- Single output file
- 5-10 sources
- No quality gates
- ~15-30 minutes

**Output location:** `3. Resources (Dynamic)/Research/Quick Research - [Topic].md`

### Complete Research (`/deep-research` + `/research-project-init`)

**When to use:**

- Thesis/dissertation work
- Academic publications
- Systematic literature reviews
- Any work requiring citations

**What you get:**

- 6-phase folder structure
- 20+ sources (12+ peer-reviewed)
- Enforced quality gates
- Publication-ready outputs

**Output location:** `3. Resources (Dynamic)/Research/[Project Name]/`

### Comparison

| Aspect | Quick Research | Complete Research |
|--------|---------------|-------------------|
| Sources | 5-10 | 20+ (min 12 peer-reviewed) |
| Phases | 1 | 6 |
| Quality gates | None | Mandatory |
| Output | Single file | Phased folder |
| Time investment | 15-30 min | Days to weeks |
| Use case | Exploration | Publication |

---

## Complete Research Phases

### Phase 0: Brief (`00-brief.md`)

Define your research scope, questions, and requirements.

**Key sections:**

- Research questions (primary + sub-questions)
- Scope (inclusions/exclusions)
- Source requirements
- Success criteria

**Template:** [[Template - Research Brief (00)]]

### Phase 1: Sources (`10-sources.md`)

Collect and evaluate sources using CRAAP criteria.

**Target distribution:**

| Type | Minimum |
|------|---------|
| Peer-reviewed | 12 |
| Technical | 5 |
| Web/industry | 5 |
| Books | 2 (optional) |

**Template:** [[Template - Research Sources (10)]]

### Phase 2: Notes (`20-notes.md`)

Extract findings, identify themes, note contradictions.

**Key activities:**

- Note-taking by source
- Thematic organization
- Pattern identification
- Gap analysis

**Template:** [[Template - Research Notes (20)]]

### Phase 3: Synthesis (`30-synthesis.md`) — Quality Gate

Synthesize findings into coherent analysis.

> [!warning] Quality Gate
> This file is blocked from saving if:
> - No citations present
> - `[citation needed]` markers remain

**Template:** [[Template - Research Synthesis (30)]]

### Phase 4: Draft (`40-draft.md`) — Quality Gate

Write the paper/report with proper academic structure.

> [!warning] Quality Gate
> This file is blocked from saving if:
> - No References section
> - `[unsupported]` markers remain

**Template:** [[Template - Research Draft (40)]]

### Phase 5: Bibliography (`99-bibliography.md`)

Compile all citations in BibTeX format.

**Template:** [[Template - Research Bibliography (99)]]

---

## Quality Gates

Quality gates are **automatically enforced via hooks** for Complete Research track.

### What Gets Checked

| Phase File | Checks Applied |
|------------|----------------|
| `30-synthesis` | Has citations, no `[citation needed]` |
| `40-draft` | Has references section, no `[unsupported]` |

### Citation Patterns Recognized

The quality gate accepts these citation formats:

- `[@citekey]` — BibTeX style
- `(Author, 2024)` — APA-like
- `[1]` — Numbered references
- `[[Paper - ...]]` — Obsidian literature links
- `et al.` — Academic citation indicator

### Bypassing Quality Gates

If you need to save work-in-progress that fails gates:

1. **Rename the file** — Save as `30-synthesis-WIP.md` instead
2. Quality gates only apply to standard phase file names
3. Rename back when ready for final version

### Manual Quality Check

Run the fact-checker agent manually:

```
Check this research synthesis for unsupported claims:
[paste content]
```

Or use `/research-progress` to preview gate readiness.

---

## Research Commands

### Quick Track

| Command | Purpose |
|---------|---------|
| `/quick-research [topic]` | Rapid 5-10 source investigation |

### Complete Track

| Command | Purpose |
|---------|---------|
| `/research-project-init [name]` | Create phased folder structure |
| `/research-progress [folder]` | Check phase completion status |
| `/deep-research [topic]` | Comprehensive investigation |

### Academic Pipeline

| Command | Purpose |
|---------|---------|
| `/research-ideate` | Socratic exploration |
| `/lit-search` | Literature search |
| `/evidence-qa` | Evidence-grounded Q&A |
| `/lit-review` | Generate literature review |
| `/paper-outline` | Create paper structure |
| `/paper-draft` | Draft sections |
| `/paper-review` | Simulate peer review |
| `/paper-polish` | Final editing |
| `/export-paper` | Export to LaTeX/PDF |

---

## arXiv MCP Integration (Optional)

### When to Install

Install if you:

- Need **local paper storage** across sessions
- Want **category-based filtering** (cs.AI, stat.ML, etc.)
- Require **systematic analysis** of many papers
- Work primarily with preprints

### When Claude WebSearch Suffices

Skip if you:

- Do occasional research
- Need current information (WebSearch is real-time)
- Don't need persistent local copies
- Prefer simplicity over features

### Installation

```bash
# Via uvx (recommended)
uv tool install arxiv-mcp-server

# Add to .claude/mcp.json
{
  "mcpServers": {
    "arxiv": {
      "command": "arxiv-mcp-server",
      "env": {}
    }
  }
}
```

### Available Tools

| Tool | Purpose |
|------|---------|
| `arxiv_search` | Search papers with category/date filters |
| `arxiv_download` | Download paper to local storage |
| `arxiv_list` | List downloaded papers |
| `arxiv_read` | Access downloaded paper content |

### Repository

- GitHub: https://github.com/blazickjp/arxiv-mcp-server
- License: Apache-2.0

---

## Zotero Integration

### Required Setup

See [[Local REST API Setup]] for Zotero MCP configuration.

### Key Commands

```
# Search your library
Use Zotero MCP to find papers on "attention mechanisms"

# Get annotations
Get my highlights from [paper citekey]

# Export bibliography
Export BibTeX for papers tagged "transformer-project"
```

### Available Tools

| Tool | Purpose |
|------|---------|
| `zotero_semantic_search` | AI-powered similarity search |
| `zotero_search_items` | Keyword search in library |
| `zotero_get_item_metadata` | Get citation details + BibTeX |
| `zotero_get_annotations` | Extract PDF highlights |
| `zotero_get_fulltext` | Access document text |

---

## GitHub Actions (Advanced)

> [!warning] Cost Note
> GitHub Actions are **free for public repositories**. Private repositories have usage limits:
> - Free tier: 2,000 minutes/month
> - Pro: 3,000 minutes/month
> - Plus Anthropic API costs for Claude

### Use Cases

- Trigger research from mobile via GitHub app
- Queue research tasks for async processing
- Automated literature monitoring

### Setup Requirements

1. Repository on GitHub (public recommended)
2. `ANTHROPIC_API_KEY` in repository secrets
3. Workflow files in `.github/workflows/`

### Setup Guide

1. **Add API key to secrets:**
   - Repository → Settings → Secrets → Actions
   - New secret: `ANTHROPIC_API_KEY`

2. **Create workflow file** (see `.github/workflows/` for templates)

3. **Test with manual dispatch:**
   - Actions tab → Select workflow → Run workflow

---

## Troubleshooting

### Quality Gate Blocking Valid Content

**Symptom:** Hook blocks file that has citations

**Check:**

1. Citation format matches recognized patterns:
   - `[@citekey]` (BibTeX)
   - `(Author, 2024)` (APA-like)
   - `[1]` (numbered)
   - `[[Paper - ...]]` (Obsidian links)

2. No leftover `[citation needed]` text

3. File name matches phase pattern (e.g., contains `30-synthesis`)

### Hook Not Processing Files

**Symptom:** Files not getting Obsidian markdown conversion

**Check:**

1. File path includes one of:
   - `Obsidian-Template-Vault`
   - `3. Resources`
   - `1. Projects`
   - `0. Inbox`
   - `2. Areas`
   - `4. Archive`
   - `6. Metadata`

2. File ends with `.md`

3. Restart Claude Code after config changes

### Research Progress Not Finding Files

**Symptom:** `/research-progress` reports missing phases

**Check:**

1. File names contain phase identifiers:
   - `00-brief` or `Brief`
   - `10-sources` or `Sources`
   - etc.

2. Files are in the correct research folder

---

## Related Documentation

- [[Workflow - Academic Research Pipeline]] — Full pipeline overview
- [[Workflow - Research Automation]] — Automation patterns
- [[Local REST API Setup]] — MCP configuration guide
- [[CLAUDE.md]] — Project-wide instructions

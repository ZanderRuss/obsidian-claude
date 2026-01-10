---
tags:
  - type/reference
  - topics/research
  - topics/setup
type: reference
created: 2025-01-10
modified: 2025-01-10
status: active
---

# Research Tools Setup Guide

Complete setup guide for the Claude + Obsidian research workflow.

## Overview

This guide covers installation and configuration of:
1. **Zotero MCP** - Reference library integration
2. **PaperQA2** - Evidence-based Q&A over PDFs
3. **Claude Scientific Writer** (optional) - Structured paper generation
4. **GPT Researcher** (optional) - Deep web research

## Quick Start

### Minimum Setup (Recommended)

1. **Zotero + Zotero MCP** - Essential for citation management
2. **PaperQA2** - Essential for evidence-grounded research

```bash
# Install Zotero MCP
pip install git+https://github.com/54yyyu/zotero-mcp.git
zotero-mcp setup

# Install PaperQA2
pip install paper-qa>=5
```

---

## 1. Zotero MCP Setup

### Prerequisites

- Zotero 7+ installed
- Local REST API enabled in Zotero

### Installation

**Option A: Using pip (Recommended)**
```bash
pip install git+https://github.com/54yyyu/zotero-mcp.git
zotero-mcp setup
```

**Option B: Using uv**
```bash
uv tool install "git+https://github.com/54yyyu/zotero-mcp.git"
zotero-mcp setup
```

### Enable Zotero Local API

1. Open Zotero
2. Go to Edit → Settings → Advanced → General
3. Enable "Allow other applications on this computer to communicate with Zotero"

### Configure MCP

The MCP configuration is already added to `.claude/mcp.json`:

```json
{
  "mcpServers": {
    "zotero": {
      "command": "zotero-mcp",
      "env": {
        "ZOTERO_LOCAL": "true"
      }
    }
  }
}
```

### Initialize Semantic Search Database

```bash
# Basic index (metadata only)
zotero-mcp update-db

# Full index (with PDF text) - Recommended
zotero-mcp update-db --fulltext

# Check status
zotero-mcp db-status
```

### Available Zotero MCP Tools

| Tool | Description |
|------|-------------|
| `zotero_semantic_search` | AI-powered similarity search |
| `zotero_search_items` | Keyword search |
| `zotero_advanced_search` | Multi-criteria filtering |
| `zotero_search_by_tag` | Tag-filtered retrieval |
| `zotero_get_item_metadata` | Get citation details + BibTeX |
| `zotero_get_item_fulltext` | Access document text |
| `zotero_get_annotations` | Extract PDF highlights |
| `zotero_get_collections` | List collections |
| `zotero_get_tags` | List all tags |

### Usage Examples

```
# In Claude Code:

# Search your library
"Search my Zotero for papers about transformer attention mechanisms"

# Get citation
"Get the BibTeX citation for the Vaswani et al. attention paper"

# Extract annotations
"Show me my highlights from the BERT paper"
```

---

## 2. PaperQA2 Setup

### Installation

```bash
pip install paper-qa>=5
```

### Configuration

Set your API keys:

```bash
# OpenAI (default)
export OPENAI_API_KEY=your-key-here

# Or use Claude
export ANTHROPIC_API_KEY=your-key-here
```

### Usage

**CLI Usage**
```bash
# Ask questions about papers in current directory
pqa ask "What methods achieve state-of-the-art performance?"

# Specify paper directory
pqa ask "Question" --paper-directory /path/to/pdfs
```

**Python API**
```python
from paperqa import Settings, ask

answer = ask(
    "What are the main limitations of attention mechanisms?",
    settings=Settings(
        paper_directory="path/to/your/pdfs",
        answer_max_sources=8
    )
)

print(answer.answer)
print(answer.references)
```

### Integration with Workflow

1. Export PDFs from Zotero to a local folder
2. Run PaperQA over that folder
3. Use `/evidence-qa` command which integrates with this

---

## 3. Claude Scientific Writer (Optional)

For structured academic paper generation.

### Installation

```bash
pip install scientific-writer
```

### Usage

```bash
# Initialize in project
scientific-writer init

# Generate paper structure
scientific-writer create --type imrad --topic "Your Topic"
```

### As Claude Code Plugin

If using Claude Code in IDE:
1. Install the scientific-writer plugin from marketplace
2. Use `/scientific-writer:init` to initialize
3. Use commands like `/scientific-writer:paper`, `/scientific-writer:review`

---

## 4. GPT Researcher (Optional)

For deep web research with citations.

### Installation

```bash
pip install gpt-researcher
```

### Configuration

```bash
export OPENAI_API_KEY=your-key
export TAVILY_API_KEY=your-tavily-key  # For web search
```

### Usage

```python
from gpt_researcher import GPTResearcher

async def research():
    researcher = GPTResearcher(query="Your topic", report_type="research_report")
    report = await researcher.conduct_research()
    return report
```

---

## Environment Setup

### Recommended Environment Variables

Add to your shell profile (`.bashrc`, `.zshrc`, or PowerShell profile):

```bash
# API Keys
export OPENAI_API_KEY=sk-...
export ANTHROPIC_API_KEY=sk-ant-...
export TAVILY_API_KEY=tvly-...  # For web research

# Zotero
export ZOTERO_LOCAL=true

# PaperQA
export PAPERQA_LLM=claude-3-5-sonnet  # Use Claude instead of OpenAI
```

### Windows PowerShell

```powershell
# Add to $PROFILE
$env:OPENAI_API_KEY = "sk-..."
$env:ANTHROPIC_API_KEY = "sk-ant-..."
$env:ZOTERO_LOCAL = "true"
```

---

## Verification

### Test Zotero MCP

```bash
# Check installation
zotero-mcp version

# Test connection (Zotero must be running)
zotero-mcp test
```

### Test PaperQA

```bash
# Quick test with a paper
pqa ask "What is this paper about?" --paper-directory ./test-papers
```

### Test in Claude Code

```
# Start Claude Code
claude

# Test Zotero
> Search my Zotero library for machine learning papers

# Test literature search
> /lit-search transformer efficiency
```

---

## Troubleshooting

### Zotero MCP Issues

**"Connection refused"**
- Ensure Zotero is running
- Verify Local API is enabled in Zotero settings
- Check firewall settings

**"Database not found"**
- Run `zotero-mcp update-db` to create search database
- Try `zotero-mcp update-db --force-rebuild` for fresh build

**Slow semantic search**
- First search builds index, subsequent searches faster
- Use `--fulltext` flag during setup for better results

### PaperQA Issues

**"API key not found"**
- Set `OPENAI_API_KEY` or `ANTHROPIC_API_KEY`
- Check key is valid

**"No papers found"**
- Verify PDF files exist in specified directory
- Check file permissions
- Try with `--verbose` flag

---

## Tool Comparison

| Feature | Zotero MCP | PaperQA2 | GPT Researcher |
|---------|------------|----------|----------------|
| Search your library | ✅ | ❌ | ❌ |
| Q&A over PDFs | Limited | ✅ | ❌ |
| Web research | ❌ | ❌ | ✅ |
| Citation export | ✅ | ❌ | ❌ |
| Annotations | ✅ | ❌ | ❌ |
| Report generation | ❌ | Limited | ✅ |

### Recommended Stack

1. **Zotero MCP** - Citation management, library search
2. **PaperQA2** - Evidence-based Q&A
3. **GPT Researcher** - Background research (when needed)

---

## Integration Architecture

```
                    ┌─────────────────┐
                    │  Claude Code    │
                    │  /lit-search    │
                    │  /evidence-qa   │
                    └────────┬────────┘
                             │
         ┌───────────────────┼───────────────────┐
         ▼                   ▼                   ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│   Zotero MCP    │ │    PaperQA2     │ │  GPT Researcher │
│   (Citations)   │ │  (Evidence QA)  │ │  (Web Research) │
└────────┬────────┘ └────────┬────────┘ └────────┬────────┘
         │                   │                   │
         ▼                   ▼                   ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│  Zotero Library │ │   PDF Corpus    │ │    Web/arXiv    │
└─────────────────┘ └─────────────────┘ └─────────────────┘
```

---

## Next Steps

After setup:
1. [ ] Test Zotero connection with `zotero-mcp test`
2. [ ] Run `zotero-mcp update-db --fulltext` to build search index
3. [ ] Export some PDFs for PaperQA testing
4. [ ] Try `/lit-search` command
5. [ ] Try `/evidence-qa` command
6. [ ] Set up research project using [[Template - Paper Project]]

---

## Related

- [[Workflow - Academic Research Pipeline]]
- [[Template - Paper Project]]
- [[Template - Literature Note]]

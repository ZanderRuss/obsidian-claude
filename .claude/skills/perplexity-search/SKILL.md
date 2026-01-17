---
name: perplexity-search
description: Perform AI-powered web searches with real-time information using Perplexity models. Supports academic mode for scholarly sources, Pro Search for multi-step reasoning, date/domain filtering, file attachments for PDF analysis, and presets for common use cases. Access via direct Perplexity API (preferred) or OpenRouter fallback.
---

# Perplexity Search

## Overview

Perform AI-powered web searches using Perplexity models with full support for:

- **Academic mode** - Prioritize peer-reviewed scholarly sources
- **Pro Search** - Multi-step reasoning for complex analysis
- **Date filtering** - Publication date ranges and recency filters
- **Domain filtering** - Allowlist/denylist with TLD support (`.edu`, `.gov`)
- **File attachments** - Analyze PDFs and documents directly
- **Presets** - Quick configurations for common use cases

This skill provides access to all Perplexity models through either:
1. **Direct Perplexity API** (preferred) - Full feature support
2. **OpenRouter fallback** - Basic features via single API key

> **Best Practices Reference**: See `.claude/docs/perplexity-best-practices.md` for comprehensive API documentation and agent integration guidance.

## When to Use This Skill

Use this skill when:
- Searching for current information or recent developments (2024 and beyond)
- Finding latest scientific publications and research (**use `--academic`**)
- Getting real-time answers grounded in web sources
- Verifying facts with source citations
- Conducting literature searches across multiple domains
- Accessing information beyond the model's knowledge cutoff
- Performing domain-specific research (biomedical, technical, clinical)
- Analyzing PDFs or documents with questions (**use `--files`**)
- Comparing current approaches or technologies (**use `--pro`**)

**Do not use** for:
- Simple calculations or logic problems (use directly)
- Tasks requiring code execution (use standard tools)
- Questions well within the model's training data (unless verification needed)

## Quick Start

### Setup (One-time)

**Option 1: Direct Perplexity API (Recommended - Full Features)**

1. Get API key from https://www.perplexity.ai/settings/api
2. Add to `.env` file:
   ```bash
   PERPLEXITY_API_KEY=pplx-your-key-here
   ```

**Option 2: OpenRouter Fallback (Basic Features)**

1. Get API key from https://openrouter.ai/keys
2. Add to `.env` file:
   ```bash
   OPENROUTER_API_KEY=sk-or-v1-your-key-here
   ```

> **Note**: Direct API supports all features (academic mode, domain filtering, etc.). OpenRouter has limited feature support.

3. **Install dependencies**:
   ```bash
   uv pip install requests python-dotenv
   ```

4. **Verify setup**:
   ```bash
   python scripts/perplexity_search.py --check-setup
   ```

## Basic Usage

```bash
# Simple search
python scripts/perplexity_search.py "What are the latest developments in CRISPR?"

# Academic mode (prioritizes scholarly sources)
python scripts/perplexity_search.py "CRISPR clinical trials" --academic

# Use preset (combines mode + domains)
python scripts/perplexity_search.py "gene therapy" --preset academic

# Save results
python scripts/perplexity_search.py "CAR-T therapy" --output results.json
```

## New Features

### Academic Mode

Prioritizes peer-reviewed papers, journal articles, and scholarly databases.

```bash
# Simple academic search
python scripts/perplexity_search.py "transformer efficiency" --academic

# Academic preset (mode + curated journal domains + high context)
python scripts/perplexity_search.py "transformer efficiency" --preset academic
```

**When to use**: Literature reviews, systematic reviews, citing research, any academic writing.

### Pro Search (Multi-Step Reasoning)

Enables automated multi-step research with tool orchestration. The model autonomously:
- Conducts targeted web searches
- Fetches detailed content from specific URLs
- Chains tools together for comprehensive answers

```bash
# Enable Pro Search (auto-enables streaming)
python scripts/perplexity_search.py "Compare PyTorch vs TensorFlow benchmarks" --pro

# Combine with academic mode
python scripts/perplexity_search.py "Compare BERT vs GPT architectures" --pro --academic
```

**When to use**: Complex comparative analysis, multi-faceted research, deep investigations.

### Date Filtering

Control the time range of search results.

```bash
# Publication date range (MM/DD/YYYY or YYYY-MM-DD format)
python scripts/perplexity_search.py "COVID variants" --date-after 01/01/2024
python scripts/perplexity_search.py "COVID variants" --date-after 2024-01-01 --date-before 2024-06-30

# Recency filter (quick relative time)
python scripts/perplexity_search.py "AI news" --recency week
python scripts/perplexity_search.py "climate research" --recency month
```

**Recency options**: `day`, `week`, `month`, `year`

> **Note**: Cannot combine `--recency` with specific date filters.

### Domain Filtering

Control which websites appear in results. Maximum 20 domains.

```bash
# Allowlist mode (only these domains)
python scripts/perplexity_search.py "machine learning" --domains "arxiv.org,nature.com,science.org"

# Denylist mode (exclude these domains, prefix with -)
python scripts/perplexity_search.py "climate change" --domains "-reddit.com,-quora.com,-medium.com"

# TLD filtering (all .edu and .gov sites)
python scripts/perplexity_search.py "policy research" --domains ".gov,.edu"
```

**Academic domain shorthand** (via preset):
```bash
python scripts/perplexity_search.py "gene editing" --preset academic
# Applies: nature.com, science.org, cell.com, nih.gov, arxiv.org, etc.
```

### Presets

Quick configurations for common use cases:

| Preset | Mode | Domains | Other |
|--------|------|---------|-------|
| `academic` | academic | nature.com, science.org, arxiv.org, .edu, .gov | high context |
| `technical` | - | github.com, stackoverflow.com, docs sites | Pro Search |
| `news` | - | excludes social media | recency: week |
| `medical` | academic | nih.gov, pubmed.gov, nejm.org, lancet.com | high context |
| `legal` | - | .gov, .edu, law.cornell.edu | - |

```bash
# List all presets
python scripts/perplexity_search.py --list-presets

# Use a preset
python scripts/perplexity_search.py "diabetes treatment" --preset medical
python scripts/perplexity_search.py "webpack configuration" --preset technical
```

### File Attachments (PDF Analysis)

Analyze documents directly with Perplexity. **Transformative for evidence-based Q&A.**

```bash
# Analyze a PDF
python scripts/perplexity_search.py "What are the key findings?" --files paper.pdf

# Multiple files
python scripts/perplexity_search.py "Compare methodologies" --files "paper1.pdf,paper2.pdf"

# Combine with web search for verification
python scripts/perplexity_search.py "Verify these claims against current research" --files paper.pdf --academic
```

**Supported formats**: PDF, DOC, DOCX, TXT, RTF
**Limits**: 50MB per file, 30 files total, 60-second processing timeout

**When to use**: Answering questions about specific papers, verifying claims, extracting methodology details.

## Available Models

| Model | Best For | Cost |
|-------|----------|------|
| `sonar-pro` (default) | General search, good balance | $$ |
| `sonar-pro-search` | Advanced agentic search | $$$ |
| `sonar` | Simple fact lookups | $ |
| `sonar-reasoning-pro` | Step-by-step analysis | $$ |
| `sonar-reasoning` | Basic reasoning | $ |
| `sonar-deep-research` | Comprehensive deep research | $$$$ |

```bash
# Select model
python scripts/perplexity_search.py "quantum computing" --model sonar-reasoning-pro
```

## All CLI Options

```
Usage: perplexity_search.py <query> [options]

Positional:
  query                    The search query

Basic Options:
  --model MODEL           Model to use (default: sonar-pro)
  --backend BACKEND       API backend: auto, direct, openrouter
  --max-tokens N          Maximum tokens (default: 4000)
  --temperature T         Response temperature 0.0-1.0 (default: 0.2)
  --output FILE           Save results to JSON file
  --verbose               Print detailed information

Search Mode:
  --academic              Enable academic mode (scholarly sources)
  --pro                   Enable Pro Search (multi-step reasoning)
  --preset NAME           Use preset: academic, technical, news, medical, legal

Date Filtering:
  --date-after DATE       Only after this date (MM/DD/YYYY or YYYY-MM-DD)
  --date-before DATE      Only before this date
  --recency PERIOD        Quick filter: day, week, month, year

Domain Filtering:
  --domains DOMAINS       Comma-separated domains (prefix - to exclude)

File Attachments:
  --files FILES           Comma-separated file paths (PDF, DOC, TXT)

Other:
  --stream                Enable streaming (auto-enabled for Pro Search)
  --check-setup           Verify API key and dependencies
  --list-presets          Show available presets
```

## Programmatic Usage

```python
from scripts.perplexity_search import search_with_perplexity

# Basic search
result = search_with_perplexity("What are the latest CRISPR developments?")

# Academic search with date filtering
result = search_with_perplexity(
    query="Transformer efficiency improvements",
    academic=True,  # Enable academic mode
    search_after_date="01/01/2023",  # Papers from 2023+
    search_domain_filter=["arxiv.org", "nature.com"],
    verbose=True
)

# Pro Search for complex analysis
result = search_with_perplexity(
    query="Compare mRNA vs viral vector vaccine platforms",
    pro=True,  # Multi-step reasoning
    preset="medical"  # Use medical preset
)

# PDF analysis
result = search_with_perplexity(
    query="What methodology does this paper use?",
    files=["paper.pdf"]
)

if result["success"]:
    print(result["answer"])
    if result.get("citations"):
        print("Citations:", result["citations"])
else:
    print(f"Error: {result['error']}")
```

## Common Use Cases

### Academic Literature Search

```bash
# Find recent peer-reviewed research
python scripts/perplexity_search.py \
  "What are the latest findings on gut microbiome and Parkinson's disease?" \
  --preset academic \
  --date-after 2023-01-01
```

### Technical Documentation

```bash
# Search code and docs
python scripts/perplexity_search.py \
  "How to implement WebSocket reconnection in Python with exponential backoff?" \
  --preset technical
```

### Evidence-Based Analysis

```bash
# Analyze a paper and verify against web
python scripts/perplexity_search.py \
  "What claims does this paper make and are they supported by current research?" \
  --files "research_paper.pdf" \
  --academic
```

### Systematic Review Support

```bash
# Find papers in date range with academic filter
python scripts/perplexity_search.py \
  "Randomized controlled trials on intermittent fasting for type 2 diabetes" \
  --preset medical \
  --date-after 2020-01-01 \
  --date-before 2024-12-31
```

### News and Current Events

```bash
# Recent news excluding social media
python scripts/perplexity_search.py \
  "What are the latest AI regulation developments?" \
  --preset news
```

## Integration with Agents

This skill is used by multiple research agents. Configure them in their agent definitions:

| Agent | Recommended Settings |
|-------|---------------------|
| `academic-researcher` | `--preset academic` or `--academic --context-size high` |
| `literature-reviewer` | `--preset academic --pro` (multi-step synthesis) |
| `fact-checker` | `--domains "-reddit.com,-quora.com"` (exclude social) |
| `evidence-qa` | `--files <pdfs>` (primary use case) |
| `research-synthesizer` | `--pro --academic` (comprehensive synthesis) |
| `technical-researcher` | `--preset technical` |

See `.claude/docs/perplexity-best-practices.md` for detailed agent configuration guidance.

## Cost Management

**Approximate costs per query:**

| Model | Fast Search | Pro Search |
|-------|-------------|------------|
| sonar | $0.001-0.002 | N/A |
| sonar-pro | $0.002-0.005 | $0.020-0.050 |
| sonar-reasoning-pro | $0.005-0.010 | N/A |
| sonar-deep-research | $0.050+ | N/A |

**Cost factors:**
- Context size: low ($), medium ($$), high ($$$)
- File attachments: Charged by input tokens (document size)
- Pro Search: Significantly higher due to multi-step reasoning

**Optimization tips:**
1. Use `sonar` for simple fact lookups
2. Default to `sonar-pro` with `fast` search type
3. Reserve `--pro` for complex multi-step analysis
4. Set `--max-tokens` to limit response length
5. Use `--context-size low` for simple queries

## Troubleshooting

### Advanced Features Not Working

**Issue**: Academic mode or domain filtering not applied

**Cause**: Using OpenRouter backend (limited feature support)

**Solution**: Configure direct Perplexity API:
```bash
# Add to .env
PERPLEXITY_API_KEY=pplx-your-key-here

# Verify
python scripts/perplexity_search.py --check-setup
```

### Pro Search Not Working

**Issue**: Pro Search results look like regular search

**Cause**: Pro Search requires streaming

**Solution**: Streaming is auto-enabled with `--pro`, but ensure you're using direct API.

### File Attachment Errors

**Issue**: "File too large" or "Unsupported file type"

**Limits**:
- Max 50MB per file
- Max 30 files per request
- Supported: PDF, DOC, DOCX, TXT, RTF
- PDFs must be text-based (not scanned images)

### Date Filter Errors

**Issue**: "Invalid date format"

**Solution**: Use `MM/DD/YYYY` (e.g., `01/15/2024`) or `YYYY-MM-DD` (e.g., `2024-01-15`)

**Note**: Cannot combine `--recency` with `--date-after`/`--date-before`

## Resources

### Bundled Resources

**Scripts:**
- `scripts/perplexity_search.py`: Main search script with all features

**References:**
- `.claude/docs/perplexity-best-practices.md`: Comprehensive API guide and agent integration

**Assets:**
- `assets/.env.example`: Example environment file template

### External Resources

**Perplexity:**
- API Docs: https://docs.perplexity.ai/
- API Keys: https://www.perplexity.ai/settings/api

**OpenRouter (Fallback):**
- Dashboard: https://openrouter.ai/account
- API Keys: https://openrouter.ai/keys

## Dependencies

### Required
```bash
uv pip install requests
```

### Recommended
```bash
uv pip install python-dotenv  # For .env file support
uv pip install litellm        # For OpenRouter fallback
```

### Environment Variables

**Required (one of):**
- `PERPLEXITY_API_KEY`: Direct API key (full features)
- `OPENROUTER_API_KEY`: OpenRouter key (basic features)

**Optional:**
- `DEFAULT_MODEL`: Default model (default: sonar-pro)
- `DEFAULT_MAX_TOKENS`: Default max tokens (default: 4000)

## Summary

This skill provides:

1. **Academic Mode** - Prioritize peer-reviewed scholarly sources
2. **Pro Search** - Multi-step reasoning for complex analysis
3. **Date Filtering** - Publication date ranges and recency filters
4. **Domain Filtering** - Allowlist/denylist with TLD support
5. **File Attachments** - Analyze PDFs and documents directly
6. **Presets** - Quick configurations (academic, technical, news, medical, legal)
7. **Dual Backend** - Direct API (full features) or OpenRouter (fallback)

For comprehensive API documentation and agent integration guidance, see `.claude/docs/perplexity-best-practices.md`.

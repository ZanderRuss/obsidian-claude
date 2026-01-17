---
name: perplexity-academic
description: Academic-focused web search optimized for scholarly research. Pre-configured with academic mode, peer-reviewed source prioritization, and curated academic domains. Use for literature searches, citation verification, and research discovery.
---

# Perplexity Academic Search

## Overview

A specialized academic search skill built on Perplexity's Academic Mode. This skill comes pre-configured with optimal settings for scholarly research:

- **Academic mode enabled by default** - Prioritizes peer-reviewed sources
- **Curated academic domains** - Nature, Science, Cell, NEJM, PubMed, arXiv, etc.
- **High context size** - Maximum detail for comprehensive literature searches
- **Date filtering** - Focus on recent research (configurable)

> **For general web search**, use `perplexity-search` instead.
> **For full Perplexity features**, see `.claude/docs/perplexity-best-practices.md`.

## When to Use This Skill

**Use this skill when:**
- Searching for peer-reviewed academic papers
- Finding recent scientific publications
- Conducting literature reviews
- Verifying claims against scholarly sources
- Discovering research in specific academic domains
- Supporting systematic reviews

**Do not use for:**
- General web searches (use `perplexity-search`)
- Technical documentation (use `--preset technical`)
- News and current events (use `--preset news`)
- Non-academic fact-checking

## Quick Start

### Setup

Uses the same API keys as `perplexity-search`:

```bash
# In .env file - Direct API (preferred)
PERPLEXITY_API_KEY=pplx-your-key-here

# OR OpenRouter fallback
OPENROUTER_API_KEY=sk-or-v1-your-key-here
```

> **Note**: Academic mode requires Direct Perplexity API. OpenRouter has limited feature support.

### Basic Usage

```bash
# Simple academic search (academic mode auto-enabled)
python scripts/perplexity_academic.py "CRISPR gene editing clinical trials"

# With date filter for recent research
python scripts/perplexity_academic.py "transformer architecture improvements" --recent 2023

# Medical/clinical research
python scripts/perplexity_academic.py "mRNA vaccine mechanisms" --domain medical

# With Pro Search for complex analysis
python scripts/perplexity_academic.py "Compare BERT vs GPT architectures" --pro

# Save results with citations
python scripts/perplexity_academic.py "gut microbiome Parkinson's" --output results.json
```

## Pre-Configured Settings

This skill automatically applies:

| Setting | Value | Purpose |
|---------|-------|---------|
| `search_mode` | `academic` | Prioritize peer-reviewed sources |
| `context_size` | `high` | Maximum detail for research |
| `model` | `sonar-pro` | Best balance of quality/cost |
| `max_tokens` | `4000` | Comprehensive responses |

### Default Academic Domains

When no `--domain` specified, searches across:

```
arxiv.org, nature.com, science.org, cell.com,
nih.gov, pubmed.gov, ncbi.nlm.nih.gov,
pnas.org, sciencedirect.com, springer.com,
wiley.com, .edu
```

## CLI Options

```
Usage: perplexity_academic.py <query> [options]

Positional:
  query                    Academic search query

Domain Presets:
  --domain DOMAIN         Domain preset: general, medical, biomedical,
                          cs, physics, chemistry, social (default: general)

Date Filtering:
  --recent YEAR           Only papers from this year onwards
  --date-after DATE       Specific start date (YYYY-MM-DD)
  --date-before DATE      Specific end date (YYYY-MM-DD)

Search Mode:
  --pro                   Enable Pro Search (multi-step reasoning)

Output:
  --output FILE           Save results to JSON file
  --verbose               Show detailed information
  --citations-only        Output only citations (for BibTeX generation)
```

## Domain Presets

| Preset | Domains | Best For |
|--------|---------|----------|
| `general` | All academic domains | Broad literature search |
| `medical` | nih.gov, pubmed.gov, nejm.org, lancet.com, bmj.com | Clinical research |
| `biomedical` | nature.com, cell.com, pnas.org, ncbi.nlm.nih.gov | Life sciences |
| `cs` | arxiv.org, acm.org, ieee.org | Computer science |
| `physics` | arxiv.org, aps.org, iop.org | Physics |
| `chemistry` | acs.org, rsc.org, nature.com/nchem | Chemistry |
| `social` | .edu, jstor.org, ssrn.com | Social sciences |

```bash
# Medical/clinical research
python scripts/perplexity_academic.py "diabetes treatment RCT" --domain medical

# Computer science papers
python scripts/perplexity_academic.py "transformer attention mechanisms" --domain cs

# Broad academic search
python scripts/perplexity_academic.py "climate change impacts" --domain general
```

## Programmatic Usage

```python
from scripts.perplexity_academic import academic_search

# Simple search
result = academic_search("What are recent advances in CRISPR?")

# With domain preset and date filter
result = academic_search(
    query="CAR-T therapy clinical outcomes",
    domain_preset="medical",
    recent_year=2023,
    verbose=True
)

# Pro Search for synthesis
result = academic_search(
    query="Compare mRNA vs viral vector vaccines",
    pro=True
)

if result["success"]:
    print(result["answer"])
    print("\nCitations:")
    for citation in result.get("citations", []):
        print(f"  - {citation}")
else:
    print(f"Error: {result['error']}")
```

## Integration with Research Agents

This skill is the **primary search tool** for research agents:

| Agent | Recommended Usage |
|-------|-------------------|
| `academic-researcher` | Default search tool |
| `literature-reviewer` | With `--pro` for synthesis |
| `fact-checker` | Verify claims against scholarly sources |
| `research-synthesizer` | Multiple queries, cross-reference |

### Agent Configuration Example

In agent definitions, reference this skill:

```yaml
skills: perplexity-academic
```

Or invoke programmatically:

```python
from scripts.perplexity_academic import academic_search

# In literature-reviewer agent
findings = academic_search(
    query="systematic review methodology guidelines",
    domain_preset="medical",
    recent_year=2020
)
```

## Common Use Cases

### Literature Search

```bash
# Find recent papers on a topic
python scripts/perplexity_academic.py \
  "machine learning for drug discovery" \
  --recent 2023 \
  --domain biomedical
```

### Citation Discovery

```bash
# Find papers to cite
python scripts/perplexity_academic.py \
  "transformer architecture attention mechanisms" \
  --domain cs \
  --citations-only
```

### Research Verification

```bash
# Verify a claim against literature
python scripts/perplexity_academic.py \
  "Is intermittent fasting effective for type 2 diabetes?" \
  --domain medical \
  --recent 2020
```

### Systematic Review Support

```bash
# Find RCTs in date range
python scripts/perplexity_academic.py \
  "randomized controlled trials SGLT2 inhibitors" \
  --domain medical \
  --date-after 2020-01-01 \
  --date-before 2024-12-31 \
  --pro
```

## Output Format

Results include:

```json
{
  "success": true,
  "query": "Original query",
  "answer": "Synthesized response with inline citations",
  "citations": [
    {
      "number": 1,
      "url": "https://nature.com/...",
      "title": "Paper title if available"
    }
  ],
  "model": "sonar-pro",
  "search_mode": "academic",
  "domain_preset": "general",
  "usage": {
    "input_tokens": 150,
    "output_tokens": 1200
  }
}
```

## Cost Considerations

Academic searches use higher context which increases cost:

| Query Type | Approximate Cost |
|------------|------------------|
| Simple academic query | $0.003-0.005 |
| Pro Search academic | $0.025-0.050 |
| Deep research query | $0.050+ |

**Tips to manage costs:**
1. Use specific, focused queries
2. Reserve `--pro` for complex synthesis needs
3. Use `--recent` to limit search scope
4. Batch related queries together

## Troubleshooting

### Academic Mode Not Working

**Issue**: Results don't prioritize scholarly sources

**Cause**: Using OpenRouter backend

**Solution**: Configure direct Perplexity API:
```bash
PERPLEXITY_API_KEY=pplx-your-key-here
```

### No Recent Papers Found

**Issue**: Results are older than expected

**Solution**:
1. Check `--recent` year is reasonable (not future)
2. Topic may have limited recent publications
3. Try broader query terms

### Missing Citations

**Issue**: Response lacks source citations

**Solution**:
1. Ensure using direct Perplexity API
2. Academic mode should always return citations
3. Check API key is valid

## Dependencies

Same as `perplexity-search`:

```bash
uv pip install requests python-dotenv
```

## Related Resources

- **General search**: `.claude/skills/perplexity-search/SKILL.md`
- **Best practices**: `.claude/docs/perplexity-best-practices.md`
- **Perplexity API docs**: https://docs.perplexity.ai/

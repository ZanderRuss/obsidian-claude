---
name: ai-search
description: Model-agnostic AI-powered web search. Use Claude's built-in WebSearch by default, or plug in your own API from OpenAI, Anthropic, Google Gemini, or Perplexity. This skill provides real-time web search with source citations for research, fact-checking, and accessing current information beyond model knowledge cutoffs.
---

# AI Search (Model-Agnostic)

## Overview

Perform AI-powered web searches using your preferred provider. This skill is **model-agnostic** - use Claude's built-in WebSearch by default (no API key needed), or plug in your own API from:

- **Claude WebSearch** (default) - Built-in, no setup required
- **OpenAI** (GPT-4o with web browsing)
- **Anthropic** (Claude API with tool use)
- **Google Gemini** (with Search grounding)
- **Perplexity** (via OpenRouter)

## When to Use This Skill

Use this skill when:
- Searching for current information or recent developments
- Finding latest scientific publications and research
- Verifying facts with source citations
- Accessing information beyond the model's knowledge cutoff
- Conducting domain-specific research (biomedical, technical, clinical)
- Comparing current approaches or technologies

**Do not use** for:
- Simple calculations or logic problems (use directly)
- Tasks requiring code execution (use standard tools)
- Questions well within the model's training data (unless verification needed)

## Quick Start

### Default: Claude WebSearch (Recommended)

No setup required. Simply ask Claude to search:

```
Search the web for the latest developments in CRISPR gene editing in 2024-2025.
```

Claude will use its built-in WebSearch tool and provide results with source citations.

**Advantages:**
- No API key needed
- No cost to you
- Automatic source citations
- Integrated with Claude's reasoning

### External Providers

For users who want to use their own API keys or specific providers.

#### Option 1: OpenAI

```bash
# Set API key
export OPENAI_API_KEY='sk-...'

# Search
python scripts/ai_search.py "CRISPR developments 2024" --provider openai
```

#### Option 2: Anthropic

```bash
# Set API key
export ANTHROPIC_API_KEY='sk-ant-...'

# Search
python scripts/ai_search.py "CRISPR developments 2024" --provider anthropic
```

#### Option 3: Google Gemini

```bash
# Set API key
export GEMINI_API_KEY='...'

# Search
python scripts/ai_search.py "CRISPR developments 2024" --provider gemini
```

#### Option 4: Perplexity (via OpenRouter)

```bash
# Set API key
export OPENROUTER_API_KEY='sk-or-v1-...'

# Search
python scripts/ai_search.py "CRISPR developments 2024" --provider perplexity
```

## Provider Comparison

| Provider | Setup | Cost | Strengths | Best For |
|----------|-------|------|-----------|----------|
| **Claude WebSearch** | None | Free* | Integrated reasoning, citations | Default use, research |
| **OpenAI** | API key | $$ | GPT-4o web browsing | General queries |
| **Anthropic** | API key | $$ | Claude with tools | Complex reasoning |
| **Gemini** | API key | $ | Google Search grounding | Broad web coverage |
| **Perplexity** | OpenRouter key | $$ | Real-time citations | Scientific literature |

*Free with Claude Code subscription

## Usage Examples

### Basic Search (Claude WebSearch)

Just ask naturally:
```
What are the latest clinical trial results for CAR-T cell therapy in 2024-2025?
```

### External Provider Search

```bash
# OpenAI
python scripts/ai_search.py \
  "Compare PyTorch vs TensorFlow for transformers in 2024" \
  --provider openai \
  --output results.json

# Gemini with grounding
python scripts/ai_search.py \
  "Latest AlphaFold 3 accuracy improvements" \
  --provider gemini \
  --verbose

# Perplexity for scientific literature
python scripts/ai_search.py \
  "Gut microbiome Parkinson's disease research 2024" \
  --provider perplexity \
  --model sonar-pro
```

## Crafting Effective Queries

### Be Specific and Detailed

**Good examples:**
- "What are the latest clinical trial results for CAR-T cell therapy in treating B-cell lymphoma published in 2024?"
- "Compare the efficacy and safety profiles of mRNA vaccines versus viral vector vaccines for COVID-19"
- "Explain AlphaFold3 improvements over AlphaFold2 with specific accuracy metrics"

**Bad examples:**
- "Tell me about cancer treatment" (too broad)
- "CRISPR" (too vague)
- "vaccines" (lacks specificity)

### Include Time Constraints

Web search excels at finding current information:
- "What papers were published in Nature Medicine in 2024 about long COVID?"
- "What are the latest developments (past 6 months) in large language model efficiency?"
- "What was announced at NeurIPS 2024 regarding AI safety?"

### Specify Domain and Sources

For high-quality results, mention source preferences:
- "According to peer-reviewed publications in high-impact journals..."
- "Based on FDA-approved treatments..."
- "From clinical trial registries like clinicaltrials.gov..."

## Configuration

### Environment Variables

The easiest way to configure API keys is using a `.env` file at your project root:

**Option 1: Use .env file (Recommended)**

1. Copy the template: `cp .env.template .env`
2. Edit `.env` and uncomment/fill in the keys you need
3. Scripts auto-load from `.env` - no manual export needed!

```bash
# In your .env file:
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GEMINI_API_KEY=AIza...
OPENROUTER_API_KEY=sk-or-v1-...
```

> **Security Note**: The `.env` file is gitignored. Never commit API keys!

**Option 2: Export in shell**

```bash
# Claude WebSearch - no configuration needed

# OpenAI
export OPENAI_API_KEY='sk-...'

# Anthropic
export ANTHROPIC_API_KEY='sk-ant-...'

# Google Gemini (supports both names)
export GEMINI_API_KEY='...'
# or: export GOOGLE_API_KEY='...'

# Perplexity (via OpenRouter)
export OPENROUTER_API_KEY='sk-or-v1-...'
```

**Optional dependency for .env support:**
```bash
pip install python-dotenv
```

### Configuration File

Create `~/.ai-search.json` for persistent configuration:

```json
{
  "default_provider": "claude",
  "providers": {
    "openai": {
      "model": "gpt-4o",
      "max_tokens": 4000
    },
    "anthropic": {
      "model": "claude-sonnet-4-20250514",
      "max_tokens": 4000
    },
    "gemini": {
      "model": "gemini-2.0-flash",
      "max_tokens": 4000
    },
    "perplexity": {
      "model": "sonar-pro",
      "max_tokens": 4000
    }
  }
}
```

## Integration with Other Skills

### Literature Review

Use with `literature-review` skill:
1. Use AI search to find recent papers and preprints
2. Supplement PubMed searches with real-time web results
3. Verify citations and find related work

### Scientific Writing

Use with `scientific-writing` skill:
1. Find recent references for introduction/discussion
2. Verify current state of the art
3. Check latest terminology and conventions

### Citation Management

Use with `citation-management` skill:
1. Find DOIs for recent papers
2. Get publication details for citations
3. Verify author and venue information

## Best Practices

### Provider Selection

1. **Start with Claude WebSearch**: Free, integrated, works for most queries
2. **Use external providers when**: You need specific model capabilities, want to compare results, or have rate limits on Claude

### Query Design

1. **Be specific**: Include domain, time frame, and constraints
2. **Use terminology**: Domain-appropriate keywords and phrases
3. **Specify sources**: Mention preferred publication types or journals
4. **Structure questions**: Clear components with explicit context

### Cost Optimization

When using external providers:
1. **Use Claude WebSearch for exploration**: Free initial research
2. **Reserve external APIs for specific needs**: Targeted queries
3. **Set token limits**: Use `--max-tokens` to control costs
4. **Monitor usage**: Track API spending

## Troubleshooting

### Claude WebSearch Not Working

Claude WebSearch is built-in and should always work. If issues occur:
- Ensure you're asking a web search-appropriate question
- Try rephrasing more specifically
- Check Claude Code is up to date

### API Key Errors

```
Error: API key not configured for provider: openai
```

**Solution**: Set the appropriate environment variable:
```bash
export OPENAI_API_KEY='sk-...'
```

### Rate Limiting

**Solution**: Wait and retry, or switch to a different provider temporarily.

### Invalid Model

**Solution**: Check available models for your provider in the configuration section.

## Resources

### Bundled Resources

**Scripts:**
- `scripts/ai_search.py`: Main search script with provider abstraction
- `scripts/providers/`: Provider implementations

**References:**
- `references/provider_setup.md`: Detailed setup for each provider
- `references/query_strategies.md`: Query design best practices

**Assets:**
- `assets/.env.example`: Environment variable template
- `assets/config.example.json`: Configuration file template

### External Resources

**Provider Documentation:**
- OpenAI: https://platform.openai.com/docs
- Anthropic: https://docs.anthropic.com
- Google AI: https://ai.google.dev/docs
- OpenRouter: https://openrouter.ai/docs

## Dependencies

### For External Providers

```bash
# Install via pip
pip install openai anthropic google-generativeai litellm

# Or via requirements
pip install -r requirements.txt
```

### Required Environment Variables

| Provider | Variable | Get Key From |
|----------|----------|--------------|
| OpenAI | `OPENAI_API_KEY` | https://platform.openai.com/api-keys |
| Anthropic | `ANTHROPIC_API_KEY` | https://console.anthropic.com |
| Gemini | `GEMINI_API_KEY` | https://aistudio.google.com/apikey |
| Perplexity | `OPENROUTER_API_KEY` | https://openrouter.ai/keys |

## Summary

This skill provides:

1. **Model-agnostic search**: Use any provider you prefer
2. **Zero-config default**: Claude WebSearch works out of the box
3. **External API support**: Plug in OpenAI, Anthropic, Gemini, or Perplexity
4. **Scientific focus**: Optimized for research and literature search
5. **Easy integration**: Works with other scientific skills

Use AI-powered web search to find current information, recent research, and grounded answers with source citations.

# Perplexity API Best Practices Guide

> Comprehensive guidance for building best-in-class search tools using the Perplexity API. This document informs skill development, agent design, and integration patterns.

---

## Table of Contents

1. [API Capabilities Overview](#api-capabilities-overview)
2. [Academic Research Mode](#academic-research-mode)
3. [Pro Search (Multi-Step Reasoning)](#pro-search-multi-step-reasoning)
4. [Date and Time Filtering](#date-and-time-filtering)
5. [Domain Filtering](#domain-filtering)
6. [File Attachments (PDF Analysis)](#file-attachments-pdf-analysis)
7. [Image Capabilities](#image-capabilities)
8. [Search Control Options](#search-control-options)
9. [Prompt Engineering](#prompt-engineering)
10. [Model Selection Guide](#model-selection-guide)
11. [Cost Optimization](#cost-optimization)
12. [Integration Recommendations](#integration-recommendations)
13. [Agent-Specific Guidance](#agent-specific-guidance)

---

## API Capabilities Overview

Perplexity's Sonar API provides powerful real-time search capabilities with several advanced features that our skills and agents can leverage:

| Capability | Parameter | Use Case | Available In |
|------------|-----------|----------|--------------|
| **Academic Mode** | `search_mode: "academic"` | Peer-reviewed papers, journals | All Sonar models |
| **Pro Search** | `search_type: "pro"` | Multi-step reasoning, complex queries | Sonar Pro (streaming only) |
| **Date Filtering** | `search_after_date_filter`, etc. | Time-bounded research | All models |
| **Domain Filtering** | `search_domain_filter` | Source curation, TLD targeting | All models |
| **File Attachments** | Message content array | PDF/document analysis | All models |
| **Image Input** | `image_url` type | Visual analysis, OCR | All except sonar-deep-research |
| **Image Returns** | `return_images: true` | Visual search results | All models |
| **Video Returns** | `media_response.overrides.return_videos` | Video search results | Sonar Pro |
| **Search Classifier** | `enable_search_classifier: true` | Smart search triggering | All models |

---

## Academic Research Mode

### Overview

The **academic filter** prioritizes scholarly sources and is **critical** for our research agents.

```python
completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[{"role": "user", "content": "Query here"}],
    search_mode="academic",  # <-- Enable academic mode
    web_search_options={"search_context_size": "high"}
)
```

### What Academic Mode Does

- **Prioritizes**: Peer-reviewed research papers, journal articles, scholarly databases
- **Deprioritizes**: General web content, blogs, forums, social media
- **Focus**: Academically rigorous foundations for answers

### Best Practices

1. **Use for all research agents**: `academic-researcher`, `literature-reviewer`, `research-synthesizer`
2. **Combine with date filtering**: Get recent peer-reviewed work
3. **Pair with high context**: `search_context_size: "high"` for comprehensive coverage
4. **Acknowledge limitations**:
   - Very recent publications (within months) may be unavailable
   - Availability varies by field/topic
   - Some paywalled content remains inaccessible

### Recommended Agent Integration

| Agent | Use Academic Mode? | Reasoning |
|-------|-------------------|-----------|
| `academic-researcher` | **Always** | Primary purpose is scholarly search |
| `literature-reviewer` | **Always** | Literature reviews require peer-reviewed sources |
| `fact-checker` | **Often** | Verification against authoritative sources |
| `research-synthesizer` | **Often** | Synthesis benefits from quality sources |
| `technical-researcher` | **Sometimes** | Only for technical papers, not code/docs |

---

## Pro Search (Multi-Step Reasoning)

### Overview

Pro Search enables automated multi-step research with tool orchestration. The model autonomously:
1. Conducts targeted web searches
2. Fetches detailed content from specific URLs
3. Chains tools together for comprehensive answers

### Critical Requirement

> ⚠️ **Pro Search ONLY works with streaming enabled**. Non-streaming requests fall back to standard Sonar Pro.

```python
# Pro Search requires streaming
response = client.chat.completions.create(
    model="sonar-pro",
    messages=[{"role": "user", "content": query}],
    stream=True,  # <-- REQUIRED for Pro Search
    web_search_options={"search_type": "pro"}  # <-- Enable Pro Search
)
```

### Search Types

| Type | When to Use | Cost |
|------|-------------|------|
| `"fast"` | Simple fact lookups, basic queries | Lower |
| `"pro"` | Complex analysis, comparative research, multi-step reasoning | Higher |
| `"auto"` | Let classifier decide based on query complexity | Variable |

### Built-in Tools

Pro Search automatically uses two tools:

1. **`web_search`**: Targeted queries with custom filters
2. **`fetch_url_content`**: Retrieves detailed information from specific URLs

Tool executions appear in the `reasoning_steps` array of streaming responses.

### Best Practices

1. **Use for complex queries**: Comparative analysis, multi-faceted research
2. **Always stream**: Implement proper streaming handlers
3. **Monitor reasoning**: Access `reasoning_steps` for transparency
4. **Budget appropriately**: Pro Search costs significantly more

### Recommended Agent Integration

| Agent | Recommended Search Type | Reasoning |
|-------|------------------------|-----------|
| `research-orchestrator` | `"pro"` | Complex multi-phase coordination |
| `research-synthesizer` | `"pro"` | Cross-source synthesis benefits from multi-step |
| `academic-researcher` | `"auto"` | Let classifier decide based on query |
| `fact-checker` | `"fast"` | Simple verification queries |
| `technical-researcher` | `"pro"` | Deep technical investigations |

---

## Date and Time Filtering

### Available Filters

#### 1. Publication Date Filters (Original Creation)
```python
search_after_date_filter="3/1/2025"    # After this date
search_before_date_filter="3/5/2025"   # Before this date
```

#### 2. Last Updated Filters (Content Modification)
```python
last_updated_after_filter="3/1/2025"   # Updated after this date
last_updated_before_filter="3/5/2025"  # Updated before this date
```

#### 3. Recency Filter (Quick Relative Time)
```python
search_recency_filter="week"  # Options: "day", "week", "month", "year"
```

### Date Format

**Required format**: `"%m/%d/%Y"` (e.g., `"3/1/2025"` or `"03/01/2025"`)

### Validation Pattern
```python
import re
date_pattern = r'^(0?[1-9]|1[0-2])/(0?[1-9]|[12][0-9]|3[01])/[0-9]{4}$'
if not re.match(date_pattern, date_string):
    raise ValueError("Invalid date format")
```

### Key Constraints

- ❌ `search_recency_filter` **cannot** be combined with specific date filters
- ✅ Publication and last-updated filters can be combined
- ✅ Date filters work with domain filters

### Best Practices

1. **Use recency for convenience**: `"month"` for recent developments
2. **Use specific dates for precision**: Academic research with known timeframes
3. **Combine both date types**: Publication + last-updated for comprehensive coverage
4. **Avoid overly narrow ranges**: May limit useful results

### Agent Use Cases

| Agent | Recommended Filter | Example |
|-------|-------------------|---------|
| `academic-researcher` | Publication date range | Papers from 2023-2024 |
| `technical-researcher` | Recency + last-updated | Recently maintained docs |
| `fact-checker` | Recency filter | Current information |
| `literature-reviewer` | Publication date range | Systematic review timeframe |

---

## Domain Filtering

### Overview

The `search_domain_filter` parameter controls which websites appear in results.

**Maximum**: 20 domains per request

### Two Operating Modes

#### Allowlist Mode (Include Only)
```python
search_domain_filter=["nature.com", "science.org", "cell.com"]
```

#### Denylist Mode (Exclude)
```python
search_domain_filter=["-reddit.com", "-pinterest.com", "-quora.com"]
```

> ⚠️ **Use either allowlist OR denylist, never both simultaneously**

### Filtering Levels

| Level | Format | Example | Behavior |
|-------|--------|---------|----------|
| Root domain | `"nature.com"` | Matches `nature.com/*` and all subdomains |
| Subdomain | `"blog.nature.com"` | Matches only that subdomain |
| TLD | `".gov"` | Matches all `.gov` sites |
| Specific URL | `"https://..."` | Matches only that page |

### Academic-Focused Domain Lists

#### High-Quality Academic Sources
```python
ACADEMIC_DOMAINS = [
    "nature.com", "science.org", "cell.com",
    "nih.gov", "ncbi.nlm.nih.gov",
    "arxiv.org", "biorxiv.org", "medrxiv.org",
    "pubmed.gov", "sciencedirect.com",
    "springer.com", "wiley.com", "plos.org"
]
```

#### TLD-Based Academic Filtering
```python
# Government and educational sources only
search_domain_filter=[".gov", ".edu"]
```

#### Exclude Low-Quality Sources
```python
EXCLUDE_DOMAINS = [
    "-reddit.com", "-quora.com", "-pinterest.com",
    "-medium.com", "-linkedin.com", "-facebook.com",
    "-twitter.com", "-youtube.com"
]
```

### Best Practices

1. **Quality over quantity**: Fewer, highly relevant domains produce better results
2. **TLD for categories**: `.gov`, `.edu` for authoritative sources
3. **Root domains for coverage**: Include all subdomains automatically
4. **Test narrowly**: Very restrictive filtering may yield no results

### Agent Integration

| Agent | Recommended Domains | Mode |
|-------|---------------------|------|
| `academic-researcher` | Academic journals, `.edu`, `.gov` | Allowlist |
| `technical-researcher` | `github.com`, docs sites | Allowlist |
| `fact-checker` | News + academic, exclude social | Denylist |
| `research-synthesizer` | Broad but exclude social media | Denylist |

---

## File Attachments (PDF Analysis)

### Overview

Perplexity can analyze documents directly—**this is transformative for our evidence-qa workflow**.

### Supported Formats

| Format | Extension | Notes |
|--------|-----------|-------|
| PDF | `.pdf` | Text-based only, not scanned images |
| Word | `.doc`, `.docx` | Microsoft Word documents |
| Text | `.txt` | Plain text files |
| RTF | `.rtf` | Rich Text Format |

### Limitations

| Constraint | Value |
|------------|-------|
| Max file size | **50 MB per file** |
| Max files per request | **30 files** |
| Processing timeout | **60 seconds** |

### Submission Methods

#### 1. Public URL Method
```python
content = [
    {"type": "text", "text": "Summarize the key findings from this paper"},
    {
        "type": "file_url",
        "file_url": {"url": "https://example.com/paper.pdf"},
        "file_name": "paper.pdf"
    }
]
```

#### 2. Base64 Encoded Method
```python
import base64

with open("paper.pdf", "rb") as f:
    b64_content = base64.b64encode(f.read()).decode()

content = [
    {"type": "text", "text": "What methodology does this paper use?"},
    {
        "type": "file_url",
        "file_url": {"url": b64_content},  # No data: prefix!
        "file_name": "paper.pdf"
    }
]
```

### Capabilities

- **Summarization**: Document summaries at various lengths
- **Question Answering**: Specific questions about content
- **Information Extraction**: Key data, findings, insights
- **Multi-language Support**: Documents in various languages
- **Web Search Integration**: Combine document analysis with real-time search

### Best Practices

1. **One focused question per request**: Better results than complex multi-part queries
2. **Verify URL accessibility**: Ensure URLs return documents directly (not preview pages)
3. **Handle timeouts gracefully**: Large documents may exceed 60-second limit
4. **Consider chunking**: Break complex analyses into smaller parts
5. **Combine with search**: Validate document claims against current web sources

### Agent Integration

| Agent | File Attachment Use | Example |
|-------|---------------------|---------|
| `evidence-qa` | **Primary** | Answer questions about user's PDFs |
| `fact-checker` | **High** | Verify claims against source documents |
| `literature-reviewer` | **Medium** | Analyze specific papers |
| `academic-researcher` | **Low** | Usually searches, not document analysis |

---

## Image Capabilities

### Image Input (Vision)

Perplexity supports image analysis for visual question answering.

#### Submission Methods

**URL-based:**
```python
content = [
    {"type": "text", "text": "What does this diagram show?"},
    {"type": "image_url", "image_url": {"url": "https://example.com/diagram.png"}}
]
```

**Base64-encoded:**
```python
content = [
    {"type": "text", "text": "Extract the text from this image"},
    {
        "type": "image_url",
        "image_url": {
            "url": "data:image/png;base64,{base64_content}"  # Include data: prefix for images
        }
    }
]
```

#### Supported Formats
- PNG, JPEG, WebP, GIF

#### Size Limits
- Base64: 50 MB max
- URL: No stated limit

#### Token Calculation
```
tokens = (width_px × height_px) / 750
```

Examples:
- 1024×768 = 1,048 tokens
- 512×512 = 349 tokens

#### Limitations
- ❌ `sonar-deep-research` does NOT support image input
- ✅ All other Sonar models support images

### Image Returns (Search Results)

Enable images in search results:

```python
completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[...],
    return_images=True,
    image_domain_filter=["wikimedia.org"],  # Optional: allowlist
    # image_domain_filter=["-gettyimages.com"],  # Or: denylist
    image_format_filter=["png", "jpg"]  # Optional: format filter
)
```

**Limits:**
- Max 30 images per response
- Max 10 domains in filter
- Max 10 formats in filter

### Best Practices

1. **High resolution for OCR**: Better text extraction from images
2. **WebP for balance**: Good quality/size tradeoff
3. **Test URL accessibility**: Before API integration

### Agent Integration

| Agent | Image Use | Capability |
|-------|-----------|------------|
| `evidence-qa` | Input | Analyze figures, diagrams from papers |
| `technical-researcher` | Input | Analyze screenshots, architecture diagrams |
| `research-synthesizer` | Returns | Include relevant images in synthesis |
| `report-generator` | Returns | Enhance reports with visual content |

---

## Search Control Options

### Search Classifier (Intelligent Mode)

```python
enable_search_classifier=True
```

Automatically determines if web search is needed based on query.

**Triggers search:**
- Current events, time-sensitive queries
- Real-time data requirements
- Research requiring web sources

**Skips search:**
- Mathematical problems
- Creative writing tasks
- General knowledge explanation

### Disable Search (Offline Mode)

```python
disable_search=True
```

Uses only training data—no web search.

**Best for:**
- Creative content generation
- Mathematical computations
- Sensitive data processing
- Deterministic, consistent outputs

### Recommendation

| Use Case | Setting | Reasoning |
|----------|---------|-----------|
| Research queries | Enable classifier | Let model decide |
| Synthesis from context | Disable search | Use provided documents only |
| Creative writing | Disable search | Avoid web contamination |
| Fact verification | Enable search | Need current web sources |

---

## Prompt Engineering

### Critical Rules

1. **NEVER ask for URLs in prompts**—models will hallucinate. Access URLs via `search_results` field.

2. **Use API parameters, not prompt instructions** for search behavior:
   - ✅ Use `search_domain_filter` parameter
   - ❌ Don't say "only search academic sites"

3. **Avoid few-shot prompting**—confuses web search models

4. **Be specific with 2-3 words of context**:
   - ✅ "Explain recent advances in climate prediction models for urban planning"
   - ❌ "Tell me about climate models"

### Best Practices

1. **One topic per query**: Complex multi-part requests degrade quality
2. **Think like a search user**: Use search-friendly terminology
3. **Be explicit about information needs**: State exactly what you want
4. **Handle uncertainty**: Include instructions for missing information

```python
system_prompt = """
If you cannot find reliable sources for this information,
please state so explicitly rather than providing speculative information.
"""
```

### System vs. User Prompts

- **System prompts**: Style, tone, language instructions
- **User prompts**: Actual query (triggers web search)
- **Note**: Real-time search doesn't attend to system prompts

---

## Model Selection Guide

### Available Models

| Model | Strengths | Best For | Cost |
|-------|-----------|----------|------|
| `sonar` | Fast, cost-effective | Simple fact lookups | $ |
| `sonar-pro` | Balanced quality/cost | Most research queries | $$ |
| `sonar-pro` + Pro Search | Multi-step reasoning | Complex analysis | $$$ |
| `sonar-reasoning-pro` | Step-by-step analysis | Explicit reasoning | $$ |
| `sonar-deep-research` | Comprehensive research | Deep investigations | $$$$ |

### Selection Matrix

| Query Type | Model | Search Type |
|------------|-------|-------------|
| Simple fact check | `sonar` | Fast |
| Literature search | `sonar-pro` + academic mode | Fast |
| Complex synthesis | `sonar-pro` | Pro |
| Multi-step analysis | `sonar-pro` | Pro |
| Bulk processing | `sonar` | Fast |
| Deep dive | `sonar-deep-research` | N/A |

### Agent Model Assignments

| Agent | Recommended Model | Reasoning |
|-------|-------------------|-----------|
| `academic-researcher` | `sonar-pro` | Quality academic sources |
| `literature-reviewer` | `sonar-pro` | Thorough literature analysis |
| `fact-checker` | `sonar` or `sonar-pro` | Depends on complexity |
| `research-synthesizer` | `sonar-pro` + Pro Search | Multi-source synthesis |
| `technical-researcher` | `sonar-pro` | Technical documentation |
| `research-orchestrator` | `sonar-deep-research` | Comprehensive coordination |

---

## Cost Optimization

### Pricing Structure

**Token costs (all models):**
- Input: $3 per 1M tokens
- Output: $15 per 1M tokens

**Request fees (per 1,000 requests):**

| Context Size | Pro Search | Fast Search |
|--------------|------------|-------------|
| High | $22 | $14 |
| Medium | $18 | $10 |
| Low | $14 | $6 |

### Optimization Strategies

1. **Right-size the model**: Use `sonar` for simple queries
2. **Use Fast Search by default**: Reserve Pro Search for complex queries
3. **Limit context size**: Use `"low"` when comprehensive coverage isn't needed
4. **Set max_tokens**: Control response length
5. **Cache results**: Implement TTL-based caching (30 min recommended)
6. **Batch efficiently**: Combine related simple queries

### Caching Implementation

```python
from functools import lru_cache
from datetime import datetime, timedelta

cache_ttl = timedelta(minutes=30)
cache_timestamps = {}

@lru_cache(maxsize=1000)
def cached_search(query: str, model: str) -> dict:
    # TTL check
    cache_key = f"{query}:{model}"
    if cache_key in cache_timestamps:
        if datetime.now() - cache_timestamps[cache_key] > cache_ttl:
            cached_search.cache_clear()

    result = perform_search(query, model)
    cache_timestamps[cache_key] = datetime.now()
    return result
```

---

## Integration Recommendations

### Skill Enhancements

Based on this analysis, recommend the following enhancements to existing skills:

#### `perplexity-search` Skill

**Add these parameters:**
```python
# Academic mode
search_mode: Optional[str] = None  # "academic"

# Pro search
search_type: Optional[str] = "fast"  # "fast", "pro", "auto"

# Date filtering
search_after_date: Optional[str] = None
search_before_date: Optional[str] = None
search_recency_filter: Optional[str] = None

# Domain filtering
search_domain_filter: Optional[List[str]] = None

# File attachments
files: Optional[List[FileAttachment]] = None
```

**Add preset configurations:**
```python
PRESETS = {
    "academic": {
        "search_mode": "academic",
        "search_domain_filter": ["nature.com", "science.org", ".edu", ".gov"],
        "search_context_size": "high"
    },
    "technical": {
        "search_domain_filter": ["github.com", "stackoverflow.com", "docs."],
        "search_type": "pro"
    },
    "news": {
        "search_recency_filter": "week",
        "search_domain_filter": ["-reddit.com", "-pinterest.com"]
    }
}
```

#### Consider: `perplexity-academic` Skill

A dedicated academic search skill with:
- Academic mode always enabled
- Curated academic domain list
- Date range support for systematic reviews
- Integration with Zotero for citation management

### New Capabilities to Add

1. **PDF Analysis Mode**: Send PDFs to Perplexity for `/evidence-qa`
2. **Image Analysis**: Visual question answering for diagrams/figures
3. **Domain Presets**: Quick access to academic, technical, news filters
4. **Date Range UI**: Easy date filtering for literature searches

---

## Agent-Specific Guidance

### `academic-researcher`

**Configuration:**
```python
model = "sonar-pro"
search_mode = "academic"
search_domain_filter = ["nature.com", "science.org", "cell.com", ".edu", ".gov"]
search_context_size = "high"
```

**Query template:**
```
Find peer-reviewed research on {topic} published between {start_date} and {end_date}.
Focus on {specific_aspect}. Include methodological details and key findings.
```

### `literature-reviewer`

**Configuration:**
```python
model = "sonar-pro"
search_mode = "academic"
search_type = "pro"  # Multi-step for comprehensive review
search_after_date_filter = "{review_start}"
search_before_date_filter = "{review_end}"
```

**Query template:**
```
Conduct a comprehensive literature search on {topic} for a systematic review.
Identify: (1) seminal papers, (2) recent developments, (3) methodological approaches,
(4) key debates, (5) research gaps.
```

### `evidence-qa`

**Configuration:**
```python
model = "sonar-pro"
# Use file attachments for PDF analysis
files = [user_provided_pdfs]
search_mode = "academic"  # For supplementary web search
```

**Query template:**
```
Based on the attached document(s), answer the following question:
{user_question}

Cite specific sections, page numbers, or quotes from the document.
If the document doesn't contain relevant information, say so explicitly.
```

### `fact-checker`

**Configuration:**
```python
model = "sonar-pro"
search_type = "pro"  # Multi-step for thorough verification
search_domain_filter = ["-reddit.com", "-quora.com", "-medium.com"]
```

**Query template:**
```
Verify the following claim: "{claim}"

Search for authoritative sources that either support or refute this claim.
Rate confidence as: Verified, Likely True, Uncertain, Likely False, or Debunked.
Provide specific sources and evidence.
```

### `research-synthesizer`

**Configuration:**
```python
model = "sonar-pro"
search_type = "pro"
search_mode = "academic"
search_context_size = "high"
```

**Query template:**
```
Synthesize current research on {topic}.
Identify: (1) consensus findings, (2) conflicting evidence, (3) emerging trends,
(4) methodological considerations, (5) implications for {context}.
```

### `technical-researcher`

**Configuration:**
```python
model = "sonar-pro"
search_domain_filter = [
    "github.com", "stackoverflow.com", "docs.python.org",
    "developer.mozilla.org", "arxiv.org"
]
```

**Query template:**
```
Research technical implementations of {technology/approach}.
Include: code examples, best practices, performance benchmarks,
common pitfalls, and recent updates (past year).
```

---

## Summary

### Key Takeaways

1. **Academic Mode is Essential**: Always use `search_mode: "academic"` for research agents
2. **Pro Search for Complexity**: Multi-step reasoning requires streaming
3. **Domain Filtering Improves Quality**: Curate sources for each agent type
4. **File Attachments Enable PDF Analysis**: Transformative for evidence-qa
5. **Never Request URLs in Prompts**: Use API responses instead
6. **Use API Parameters**: Not prompt instructions for search control
7. **Cache Aggressively**: 30-minute TTL for non-urgent queries
8. **Right-Size Models**: Use `sonar` for simple, `sonar-pro` for complex

### Implementation Priority

1. **High**: Academic mode for all research agents
2. **High**: Domain filtering presets
3. **Medium**: File attachment capability
4. **Medium**: Pro Search for complex queries
5. **Medium**: Date range filtering
6. **Low**: Image input/output capabilities
7. **Low**: Video returns

---

*Document Version: 1.0*
*Last Updated: 2026-01-17*
*Based on: Perplexity API Documentation (January 2026)*

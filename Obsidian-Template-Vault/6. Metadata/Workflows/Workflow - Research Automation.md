---
tags:
  - workflow
  - automation
  - research
type: workflow
created: 2025-01-10
---

# Research Automation Workflow

Automate deep research with Claude, web search, and structured output to vault.

## Overview

```
Research Query → Claude Web Search → Source Gathering → Synthesis → Structured Notes
```

## Research Pipeline

### Step 1: Define Research Scope

Create a research request note:

```markdown
---
tags:
  - research-request
type: research-request
created: 2025-01-10
status: pending
---

# Research Request: [Topic]

## Core Question
[Main question to answer]

## Sub-questions
1. [Sub-question 1]
2. [Sub-question 2]

## Scope
- **Depth**: Surface / Moderate / Deep
- **Time bound**: Last [X] months/years
- **Sources**: Academic / Industry / News / All

## Output Desired
- [ ] Summary note
- [ ] Source list
- [ ] Key quotes
- [ ] Comparison table
- [ ] Recommendations

## Related Vault Notes
- [[Existing Note 1]]
- [[Existing Note 2]]
```

### Step 2: Run Research Command

Use `/research-assistant` with the request:

```
/research-assistant

Research topic: [Topic from request]
Check existing vault notes first, then search web for:
- Recent developments (2024-2025)
- Key papers/articles
- Expert opinions
- Practical applications
```

### Step 3: Source Management

**For each source found:**

1. Use `/web-clip` to save full article
2. Tag with research project
3. Extract key quotes
4. Note reliability/bias

**Source tracking template:**

```markdown
## Sources

| Source | Type | Reliability | Key Point |
|--------|------|-------------|-----------|
| [Title](url) | Article | High | [Summary] |
| [Title](url) | Research | High | [Summary] |
```

### Step 4: Synthesis

After gathering sources, run synthesis:

```
Synthesize my research on [topic] from these sources:
- [[Source 1]]
- [[Source 2]]
- [[Source 3]]

Create:
1. Executive summary (200 words)
2. Key findings table
3. Contradictions/debates
4. Recommendations
5. Further research needed
```

### Step 5: Output Structure

**Research output folder:**
```
3. Resources (Dynamic)/
└── Research/
    └── [Topic Name]/
        ├── Research - [Topic] Overview.md
        ├── Research - [Topic] Sources.md
        ├── Research - [Topic] Synthesis.md
        └── Clips/
            ├── [Clipped Article 1].md
            └── [Clipped Article 2].md
```

## Automation Scripts

### Batch Research Script

Create `scripts/batch-research.js`:

```javascript
// batch-research.js
// Run multiple research queries in sequence

const queries = [
  {
    topic: "AI agents in 2025",
    depth: "deep",
    output: "3. Resources (Dynamic)/Research/AI Agents/"
  },
  {
    topic: "Knowledge management tools",
    depth: "moderate",
    output: "3. Resources (Dynamic)/Research/KM Tools/"
  }
];

// Process each query
for (const query of queries) {
  console.log(`Researching: ${query.topic}`);
  // Claude processes query
  // Results saved to output folder
}
```

### Daily Research Digest

Add to GitHub Actions for automatic research:

```yaml
name: Daily Research Digest

on:
  schedule:
    - cron: '0 7 * * 1'  # Every Monday at 7 AM

jobs:
  research:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run Weekly Research
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude --print "
          Search for the latest developments in:
          - AI and LLMs
          - Knowledge management
          - Productivity tools

          For each topic, create a brief summary note with:
          - 3-5 key developments
          - Links to sources
          - Relevance to my existing notes

          Save to: 3. Resources (Dynamic)/Research/Weekly Digest/
          "
```

## Research Best Practices

### Source Evaluation

**CRAAP Test for sources:**
- **C**urrency: How recent?
- **R**elevance: Does it address your question?
- **A**uthority: Who wrote it? Credible?
- **A**ccuracy: Is it supported by evidence?
- **P**urpose: Why was it written? Bias?

### Note-Taking During Research

1. **Always capture source** - URL, author, date
2. **Distinguish quotes vs paraphrases** - Use blockquotes for direct quotes
3. **Note your reactions** - "I think...", "This contradicts..."
4. **Link immediately** - Connect to existing notes as you go
5. **Flag for follow-up** - Use tags like `#needs-review`

### Synthesis Tips

- Look for **patterns** across sources
- Note **contradictions** - they're valuable
- Identify **gaps** - what's missing?
- Consider **recency** - is info outdated?
- Check **consensus vs outliers**

## Integration with Other Commands

**Research workflow chain:**
```
/research-assistant → /web-clip → /smart-link → /note-to-blog
```

1. Research topic
2. Clip important sources
3. Link to existing knowledge
4. Transform into shareable content

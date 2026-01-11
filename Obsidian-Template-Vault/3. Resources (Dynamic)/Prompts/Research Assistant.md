---
tags:
  - content/prompt
  - type/reference
  - topics/research
type: prompt
category: Research
description: Deep topical investigation with structured synthesis
cover: ""
created: 2025-01-11
modified: 2025-01-11
status: active
---

# Research Assistant

## Purpose

Conduct thorough research on a topic with structured output including key findings, sources, and actionable insights.

## Prompt

```
Help me research {topic}. Please:

1. **Overview**: Provide a comprehensive summary of the topic
2. **Key Concepts**: List and explain the main concepts/terms
3. **Current State**: What's the latest thinking/developments?
4. **Perspectives**: Present different viewpoints or approaches
5. **Practical Applications**: How can this be applied?
6. **Resources**: Suggest sources for deeper learning

Focus area (optional): {focus}
```

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{topic}` | The subject to research | "spaced repetition learning" |
| `{focus}` | Optional specific angle | "software implementations" |

## Usage Notes

- Great for learning new domains quickly
- Combine with web search for current information
- Follow up on specific sections that interest you
- Save key findings to your vault for future reference

## Examples

### Example 1: Technology Research

**Input:**
```
Help me research vector databases. Please:

1. **Overview**: Provide a comprehensive summary of the topic
2. **Key Concepts**: List and explain the main concepts/terms
3. **Current State**: What's the latest thinking/developments?
4. **Perspectives**: Present different viewpoints or approaches
5. **Practical Applications**: How can this be applied?
6. **Resources**: Suggest sources for deeper learning

Focus area: comparison of popular options
```

## Related Prompts

- [[Thinking Partner]]
- [[Literature Review]]

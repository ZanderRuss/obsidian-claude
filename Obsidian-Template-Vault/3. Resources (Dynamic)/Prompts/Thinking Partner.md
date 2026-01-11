---
tags:
  - content/prompt
  - type/reference
  - topics/thinking
type: prompt
category: Thinking & Analysis
description: Explore ideas through Socratic questioning and structured inquiry
cover: ""
created: 2025-01-11
modified: 2025-01-11
status: active
---

# Thinking Partner

## Purpose

Engage Claude as a thinking partner who helps explore ideas through questioning rather than immediately providing answers. Ideal for complex problems, brainstorming, and developing deeper understanding.

## Prompt

```
I want to explore an idea with you. Instead of immediately answering, help me think through this by:
1. Asking clarifying questions to understand what I'm really asking
2. Identifying assumptions I might be making
3. Suggesting different angles to consider
4. Challenging my reasoning constructively

The topic I want to explore: {topic}
```

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{topic}` | The idea or problem to explore | "How to structure a knowledge management system" |

## Usage Notes

- Use when you want to develop understanding, not just get answers
- Works best when you're willing to engage in back-and-forth dialogue
- Great for decisions where there's no single "right" answer
- Helps uncover blind spots in your thinking

## Examples

### Example 1: Career Decision

**Input:**
```
I want to explore an idea with you. Instead of immediately answering, help me think through this by:
1. Asking clarifying questions to understand what I'm really asking
2. Identifying assumptions I might be making
3. Suggesting different angles to consider
4. Challenging my reasoning constructively

The topic I want to explore: Whether I should take a promotion that requires relocating
```

**Output:**
Claude will ask questions like:
- What aspects of the promotion appeal to you most?
- What would you be leaving behind in your current location?
- Have you explored whether remote work is an option?
- What does "success" look like to you in 5 years?

## Related Prompts

- [[Research Assistant]]
- [[Decision Matrix]]

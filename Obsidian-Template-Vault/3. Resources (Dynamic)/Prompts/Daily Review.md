---
tags:
  - content/prompt
  - type/reference
  - topics/productivity
type: prompt
category: Productivity
description: End-of-day reflection for learning and planning
cover: ""
created: 2025-01-11
modified: 2025-01-11
status: active
---

# Daily Review

## Purpose

Structured end-of-day reflection to capture learnings, identify patterns, and prepare for tomorrow.

## Prompt

```
Help me with my daily review. Here's what happened today:

## What I worked on:
{activities}

## What went well:
{wins}

## What was challenging:
{challenges}

Please help me:
1. Identify 1-2 key learnings from today
2. Suggest what to carry forward to tomorrow
3. Note any patterns you see (if I've shared previous reviews)
4. Ask one question to help me reflect deeper
```

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{activities}` | Main tasks/work | "Wrote 3 pages of paper, met with advisor" |
| `{wins}` | Positive outcomes | "Finally understood the algorithm" |
| `{challenges}` | Difficulties faced | "Couldn't focus in the afternoon" |

## Usage Notes

- Keep it brief (5-10 minutes)
- Be honest about challenges
- Look for patterns over time
- Link to projects and areas in your vault

## Examples

### Example 1: Research Day Review

**Input:**
```
Help me with my daily review. Here's what happened today:

## What I worked on:
- Literature review for ML paper (3 hours)
- Debugging training script (2 hours)
- Team standup meeting

## What went well:
- Found 3 highly relevant papers I hadn't seen before
- Fixed the memory leak in training

## What was challenging:
- Kept getting distracted by Slack
- The literature search took longer than expected

Please help me:
1. Identify 1-2 key learnings from today
2. Suggest what to carry forward to tomorrow
3. Note any patterns you see
4. Ask one question to help me reflect deeper
```

## Related Prompts

- [[Weekly Synthesis]]
- [[Inbox Processor]]

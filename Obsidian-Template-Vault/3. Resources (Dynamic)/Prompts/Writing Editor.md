---
tags:
  - content/prompt
  - type/reference
  - topics/writing
type: prompt
category: Writing
description: Professional editing for clarity, style, and impact
cover: ""
created: 2025-01-11
modified: 2025-01-11
status: active
---

# Writing Editor

## Purpose

Get professional editing feedback on your writing with specific, actionable suggestions.

## Prompt

```
Please edit this text for {goal}:

---
{text}
---

Consider:
- Clarity and conciseness
- Flow and structure
- Word choice and tone
- Grammar and mechanics

Audience: {audience}
Tone: {tone}

Provide the edited version first, then explain key changes.
```

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{goal}` | What to optimize for | "clarity and professionalism" |
| `{text}` | The text to edit | Your draft |
| `{audience}` | Who will read this | "technical stakeholders" |
| `{tone}` | Desired voice | "professional but approachable" |

## Usage Notes

- Specify the type of writing (email, report, blog, etc.)
- Mention any word count constraints
- Include context about what response you're hoping to get
- Ask for explanations to improve your own writing

## Examples

### Example 1: Email Editing

**Input:**
```
Please edit this text for professionalism and clarity:

---
Hey, so I was thinking about what we talked about yesterday and I think we should probably move forward with option B because it seems like it would work better for what we're trying to do even though option A is cheaper.
---

Consider:
- Clarity and conciseness
- Flow and structure
- Word choice and tone
- Grammar and mechanics

Audience: C-level executives
Tone: professional but decisive
```

## Related Prompts

- [[Meeting Summary]]
- [[Document Outline]]

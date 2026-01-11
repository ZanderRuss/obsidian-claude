---
cssclasses:
  - cards
  - cards-cols-3
tags:
  - type/moc
  - content/prompt
type: moc
created: 2025-01-11
modified: 2025-01-11
status: active
---

# Prompt Library

A curated collection of prompts for working with Claude and other AI assistants.

## All Prompts by Category

```dataview
TABLE WITHOUT ID
  file.link as "Prompt",
  category as "Category",
  description as "Description"
FROM "3. Resources (Dynamic)/Prompts"
WHERE type = "prompt"
SORT category ASC, file.name ASC
```

---

## Quick Stats

- **Total Prompts**: `$=dv.pages('"3. Resources (Dynamic)/Prompts"').where(p => p.type == "prompt").length`

### By Category

```dataview
TABLE WITHOUT ID
  category as "Category",
  length(rows) as "Count"
FROM "3. Resources (Dynamic)/Prompts"
WHERE type = "prompt"
GROUP BY category
SORT category ASC
```

---

## Add New Prompt

Use the template: [[6. Metadata/Templates/Template - Prompt|Template - Prompt]]

## Categories

- **Thinking & Analysis** - Exploration, problem-solving, decision-making
- **Research** - Investigation, synthesis, literature review
- **Development** - Code review, debugging, architecture
- **Writing** - Editing, formatting, style
- **Productivity** - Daily review, planning, organization
- **Learning** - Explanations, flashcards, tutorials

---

> [!tip] Alternative View
> For native card view with filtering and grouping, open [[Prompt Library.base|Prompt Library (Base)]].

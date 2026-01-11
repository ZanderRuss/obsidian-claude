---
cssclasses:
  - dashboard
  - cards
banner: "![[12.jpg]]"
banner_y: 0.5
banner_height: 400
---

# Research Vault

> *AI amplifies thinking, not just writing.*

<div class="quick-actions">

- [[0. Inbox/Welcome to Your Inbox|+ Quick Note]]
- [[6. Metadata/Templates/Template - Project|+ Project]]
- [[6. Metadata/Templates/Template - Research Note|+ Research]]
- [[6. Metadata/Templates/Template - Prompt|+ Prompt]]

</div>

---

## Active Projects

```dataview
TABLE WITHOUT ID
  file.link as "Project",
  status as "Status",
  dateformat(file.mtime, "MMM dd") as "Updated"
FROM "1. Projects"
WHERE status = "active" OR !status
SORT file.mtime DESC
LIMIT 6
```

## Prompt Library

```dataview
TABLE WITHOUT ID
  file.link as "Prompt",
  category as "Category",
  description as "Description"
FROM "3. Resources (Dynamic)/Prompts"
WHERE type = "prompt"
SORT category ASC
LIMIT 6
```

> [!tip]+ Full Prompt Library
> Open [[3. Resources (Dynamic)/Prompts/MOC - Prompts|Prompt Library]] for all prompts with filtering.

---

## Recent Work

```dataview
LIST
FROM ""
WHERE !contains(file.path, ".obsidian") 
  AND !contains(file.path, "Templates") 
  AND !contains(file.path, "Prompts")
  AND file.name != "Home"
SORT file.mtime DESC
LIMIT 10
```

## Areas of Focus

```dataview
LIST
FROM "2. Areas (Ongoing)"
SORT file.name ASC
```

## Inbox

```dataview
LIST
FROM "0. Inbox"
SORT file.ctime DESC
```

---

## Vault Stats

<div class="stats-grid">

- **`$=dv.pages().length`** Notes
- **`$=dv.pages('"1. Projects"').length`** Projects
- **`$=dv.pages('"2. Areas (Ongoing)"').length`** Areas
- **`$=dv.pages('"3. Resources (Dynamic)"').length`** Resources
- **`$=dv.pages('"0. Inbox"').length`** Inbox

</div>

---

## Claude Commands

| Workflow | Command | Purpose |
|----------|---------|---------|
| Daily | `/daily-review` | End-of-day reflection |
| Weekly | `/weekly-synthesis` | Pattern identification |
| Research | `/research-assistant` | Deep investigation |
| Thinking | `/thinking-partner` | Explore ideas |
| Organize | `/inbox-processor` | Process inbox |

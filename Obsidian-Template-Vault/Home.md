---
cssclasses:
  - dashboard
banner: "![[banner-research.jpg]]"
banner_y: 0.5
---

# Research Vault

> *AI amplifies thinking, not just writing.*

## Quick Actions

- [[0. Inbox/Quick Note|+ New Quick Note]]
- [[6. Metadata/Templates/Template - Project|+ New Project]]
- [[6. Metadata/Templates/Template - Research Note|+ New Research Note]]

---

## Active Projects

```dataview
LIST
FROM "1. Projects"
WHERE status = "active" OR !status
SORT file.mtime DESC
LIMIT 10
```

## Recent Work

```dataview
LIST
FROM ""
WHERE !contains(file.path, ".obsidian") AND !contains(file.path, "Templates")
SORT file.mtime DESC
LIMIT 15
```

---

## Areas of Focus

```dataview
LIST
FROM "2. Areas (Ongoing)"
SORT file.name ASC
```

## Inbox (Needs Processing)

```dataview
LIST
FROM "0. Inbox"
SORT file.ctime DESC
```

---

## Vault Statistics

- **Total Notes**: `$=dv.pages().length`
- **Projects**: `$=dv.pages('"1. Projects"').length`
- **Areas**: `$=dv.pages('"2. Areas (Ongoing)"').length`
- **Resources**: `$=dv.pages('"3. Resources (Dynamic)"').length`
- **Inbox Items**: `$=dv.pages('"0. Inbox"').length`

---

## Claude Commands

| Workflow | Command | Purpose |
|----------|---------|---------|
| Daily | `/daily-review` | End-of-day reflection |
| Weekly | `/weekly-synthesis` | Pattern identification |
| Research | `/research-assistant` | Deep investigation |
| Thinking | `/thinking-partner` | Explore ideas |
| Organize | `/inbox-processor` | Process inbox |

*Run `claude` in terminal to start Claude Code*

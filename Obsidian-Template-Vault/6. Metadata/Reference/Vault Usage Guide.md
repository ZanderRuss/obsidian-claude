---
tags:
  - type/reference
  - topics/obsidian
type: reference
created: 2025-01-11
modified: 2025-01-11
status: active
---

# Vault Usage Guide

Quick reference for using this Obsidian vault effectively.

## Keyboard Shortcuts

### Template Hotkeys

| Hotkey | Template | Use Case |
|--------|----------|----------|
| `Alt+N` | Quick Note | Fast capture, inbox items |
| `Alt+P` | Project | New project with goals/tasks |
| `Alt+R` | Research Note | Research findings |
| `Alt+D` | Daily Note | Daily journal/reflection |
| `Alt+M` | Meeting Notes | Meeting minutes |

### General Obsidian

| Hotkey | Action |
|--------|--------|
| `Ctrl+N` | New note |
| `Ctrl+O` | Quick switcher |
| `Ctrl+P` | Command palette |
| `Ctrl+E` | Toggle edit/preview |
| `Ctrl+Click` | Open link in new tab |
| `Ctrl+R` | Run Templater on current file |

## Creating Notes

### Method 1: Folder Templates (Automatic)

Create a new note in these folders and the template auto-applies:

| Folder | Template Applied |
|--------|-----------------|
| `0. Inbox/` | Quick Note |
| `1. Projects/` | Project |
| `2. Areas (Ongoing)/` | MOC |
| `3. Resources (Dynamic)/` | Research Note |
| `3. Resources (Dynamic)/Prompts/` | Prompt |

### Method 2: Hotkeys (From Anywhere)

1. Create new note (`Ctrl+N`)
2. Press template hotkey (e.g., `Alt+N`)
3. Template fills in automatically

### Method 3: Command Palette

1. `Ctrl+P` → "Templater: Insert template"
2. Select template from list

## Dashboard Features

The Home page uses special CSS classes for styling.

### Quick Action Buttons

Wrap links in a div:

```html
<div class="quick-actions">

- [[Link|Button Text]]
- [[Link|Button Text]]

</div>
```

### Stats Grid

Display stats as cards:

```html
<div class="stats-grid">

- **123** Label
- **456** Label

</div>
```

### Card View for Tables

Add to frontmatter:

```yaml
cssclasses:
  - cards
  - cards-cols-3
```

Then use Dataview TABLE queries.

## Available Templates

| Template | Purpose | Location |
|----------|---------|----------|
| Quick Note | Fast capture | Inbox |
| Project | Time-bound initiative | Projects |
| Research Note | Research findings | Resources |
| MOC | Map of Content | Areas |
| Prompt | AI prompt | Prompts folder |
| Daily Note | Daily journal | Anywhere |
| Meeting Notes | Meeting minutes | Anywhere |
| Literature Note | Paper annotations | Resources |
| Experiment Log | Research experiments | Projects |
| Paper Project | Academic paper | Projects |

## Claude Commands

Run these in Claude Code terminal:

| Command | Purpose |
|---------|---------|
| `/daily-review` | End-of-day reflection |
| `/weekly-synthesis` | Pattern identification |
| `/research-assistant` | Deep investigation |
| `/thinking-partner` | Explore ideas |
| `/inbox-processor` | Process inbox notes |
| `/smart-link` | Find connection suggestions |
| `/graph-analysis` | Vault health check |

## Frontmatter Standards

### Required Fields

```yaml
---
tags:
  - category/subcategory
type: note
created: 2025-01-11
status: active
---
```

### Common Types

`note`, `project`, `area`, `resource`, `moc`, `prompt`, `daily`, `meeting`

### Status Values

`draft`, `active`, `completed`, `archived`

## Tag Hierarchy

```
content/     → notes, projects, research, voice-memo
topics/      → technology, business, personal
status/      → active, review, unprocessed, archived
type/        → moc, meeting, thinking-log, reference
```

## File Organization (PARA)

| Folder | Contents | Criteria |
|--------|----------|----------|
| `0. Inbox` | Unprocessed captures | New/unsorted |
| `1. Projects` | Active initiatives | Has deadline |
| `2. Areas` | Ongoing responsibilities | No end date |
| `3. Resources` | Reference materials | No action needed |
| `4. Archive` | Completed/inactive | Done or dormant |

## Tips

### Quick Capture
- Use `Alt+N` from anywhere for fast capture
- Notes go to inbox automatically for later processing

### Weekly Review
1. Run `/inbox-processor` to organize captures
2. Run `/weekly-synthesis` for patterns
3. Archive completed projects

### Finding Content
- `Ctrl+O` → Quick switcher (fuzzy search)
- `Ctrl+Shift+F` → Full vault search
- Use Omnisearch for semantic search

### Linking
- `[[Note Name]]` → Internal link
- `[[Note Name|Display]]` → Aliased link
- `![[Note Name]]` → Embed note

## Related

- [[Card View System]] - Card/tile view documentation
- [[Local REST API Setup]] - MCP integration
- [[Home]] - Dashboard

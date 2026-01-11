---
tags:
  - type/reference
  - topics/obsidian
type: reference
created: 2025-01-11
modified: 2025-01-11
status: active
---

# Card View System

This vault uses a **hybrid card view system** that combines the best approaches for displaying notes as visual cards/tiles.

## Architecture Overview

| Tier | Tool | Best For | Complexity |
|------|------|----------|------------|
| **1** | Obsidian Bases | Dedicated databases, full CRUD | Low |
| **2** | Dataview + CSS | Inline queries, dashboards | Medium |
| **3** | Custom CSS | Advanced styling, animations | High |

## Tier 1: Obsidian Bases (Recommended)

Obsidian Bases is a **core plugin** (built-in since v1.9) that provides native database functionality.

### Creating a Base

1. Right-click folder → "New base"
2. Or create a `.base` file manually

### Base File Format

```json
{
  "view": "card",
  "filters": [
    {
      "property": "file.folder",
      "operator": "starts-with",
      "value": "3. Resources (Dynamic)/Prompts"
    }
  ],
  "properties": ["file.link", "category", "description", "cover"],
  "sort": [{ "property": "category", "direction": "asc" }],
  "cardOptions": {
    "coverProperty": "cover",
    "primaryProperty": "file.link",
    "imageHeight": 150,
    "imageFit": "cover"
  },
  "groupBy": "category"
}
```

### View Types

- `card` - Grid of cards with optional cover images
- `table` - Traditional spreadsheet view
- `list` - Simple list view

### Best Practices

- Use for dedicated collections (prompt libraries, reading lists, etc.)
- Add `cover` property to notes for visual appeal
- Group by category for organization
- Use filters to scope to specific folders

## Tier 2: Dataview + CSS Cards

For inline queries within notes (dashboards, MOCs), use Dataview with the card CSS snippet.

### Enabling Card Layout

Add CSS classes to your note's frontmatter:

```yaml
---
cssclasses:
  - cards           # Required - enables card layout
  - cards-cover     # Images fill card space
  - cards-cols-3    # Force 3 columns
  - cards-16-9      # 16:9 aspect ratio for images
---
```

### Available CSS Classes

| Class | Effect |
|-------|--------|
| `cards` | **Required** - Enables card layout |
| `cards-cover` | Images cover full card width |
| `cards-compact` | Reduced padding/gaps |
| `cards-gallery` | Image-only mode |
| `cards-cols-1` to `cards-cols-6` | Force column count |
| `cards-16-9` | 16:9 aspect ratio |
| `cards-4-3` | 4:3 aspect ratio |
| `cards-2-3` | Portrait (2:3) ratio |
| `cards-1-1` | Square ratio |

### Writing Dataview Queries for Cards

Use `TABLE` format (not LIST) for best card layouts:

```dataview
TABLE WITHOUT ID
  file.link as "Title",
  category as "Category",
  description as "Description"
FROM "folder/path"
WHERE type = "prompt"
SORT category ASC
```

### Tips

- Use `TABLE WITHOUT ID` to hide the default file column
- Include a `cover` field for images
- Keep descriptions short for cleaner cards
- Use `LIMIT` to control card count

## Tier 3: Custom CSS

The CSS snippet at `.obsidian/snippets/dataview-cards.css` provides extensive customization.

### CSS Variables

Override these in your own snippet or theme:

```css
body {
  --cards-min-width: 180px;
  --cards-max-width: 1fr;
  --cards-mobile-width: 120px;
  --cards-image-height: 150px;
  --cards-padding: 1rem;
  --cards-gap: 0.75rem;
  --cards-border-radius: 8px;
  --cards-background: var(--background-secondary);
  --cards-border-color: var(--background-modifier-border);
}
```

### Card Hover Effects

Cards have built-in hover effects:
- Border color changes to accent
- Subtle lift (translateY)
- Box shadow appears

## Prompt Library Example

The vault includes a prompt library at `3. Resources (Dynamic)/Prompts/`:

### Structure

```
Prompts/
├── Prompt Library.base    # Obsidian Base for full view
├── Thinking Partner.md    # Category: Thinking & Analysis
├── Research Assistant.md  # Category: Research
├── Code Review.md         # Category: Development
├── Writing Editor.md      # Category: Writing
├── Daily Review.md        # Category: Productivity
└── Explain Like I'm Five.md  # Category: Learning
```

### Prompt Note Template

Each prompt uses this frontmatter:

```yaml
---
tags:
  - content/prompt
  - type/reference
type: prompt
category: "Category Name"
description: "Brief description for cards"
cover: ""
created: 2025-01-11
status: active
---
```

## When to Use Each Approach

| Scenario | Recommended Approach |
|----------|---------------------|
| Dedicated collection page | Obsidian Base |
| Dashboard section | Dataview + CSS |
| MOC with mixed content | Dataview + CSS |
| Reading list with covers | Obsidian Base |
| Project gallery | Either works |
| Quick inline query | Dataview LIST |

## Troubleshooting

### Cards Not Displaying

1. Ensure `dataview-cards` snippet is enabled in Appearance settings
2. Check that `cssclasses: [cards]` is in frontmatter
3. Verify Dataview query uses `TABLE` format

### Images Not Showing

1. Use the `cover` property in frontmatter
2. Reference images with `![[image.png]]` or URL
3. Add `cards-cover` class for proper sizing

### Columns Wrong

1. Check screen width (responsive breakpoints)
2. Use `cards-cols-N` to force column count
3. Adjust `--cards-min-width` in CSS

### Base Not Loading

1. Verify `.base` file is valid JSON
2. Check filter paths match actual folders
3. Ensure Bases core plugin is enabled

## Related Resources

- [[Home]] - Dashboard with card examples
- [[6. Metadata/Templates/Template - Prompt|Template - Prompt]] - Prompt template
- [[3. Resources (Dynamic)/Prompts/Prompt Library.base|Prompt Library]] - Full card view

## File Locations

| File | Purpose |
|------|---------|
| `.obsidian/snippets/dataview-cards.css` | Card styling CSS |
| `.obsidian/appearance.json` | Enable snippets here |
| `6. Metadata/Templates/Template - Prompt.md` | Prompt template |
| `3. Resources (Dynamic)/Prompts/Prompt Library.base` | Base database |

---
tags:
  - status/unprocessed
  - type/guide
type: note
created: 2025-01-10
status: active
---

# Welcome to Your Inbox

This is your **capture point** - the single entry point for all new ideas, notes, and information.

## How to Use the Inbox

### Quick Capture Rules

1. **Capture everything here first** - Don't worry about organization
2. **Keep notes short** - Just enough to remember the idea
3. **Add minimal tags** - Use `status/unprocessed` for easy filtering
4. **Process weekly** - Use `/inbox-processor` to sort into PARA folders

### What Belongs Here

- Quick thoughts and ideas
- Meeting notes (before proper formatting)
- Voice memo transcriptions
- Web clips and bookmarks
- Questions to research later
- Tasks without a home yet

### Processing Your Inbox

Run the Claude command:

```
/inbox-processor
```

This will help you:
1. Review each unprocessed note
2. Decide: Project, Area, Resource, or Archive?
3. Add proper frontmatter and tags
4. Move to the appropriate folder

### Frontmatter for New Notes

```yaml
---
tags:
  - status/unprocessed
type: note
created: YYYY-MM-DD
---
```

## Quick Capture Templates

### Idea Capture
```markdown
## Idea: [Title]
**Context**: Where did this come from?
**Core insight**: What's the key point?
**Next step**: What should I do with this?
```

### Meeting Quick Note
```markdown
## Meeting: [Topic] - [Date]
**Attendees**:
**Key decisions**:
**Action items**:
```

### Research Question
```markdown
## Question: [Your question]
**Why it matters**:
**Where to look**:
```

---

*Delete this note once you're familiar with the inbox workflow.*

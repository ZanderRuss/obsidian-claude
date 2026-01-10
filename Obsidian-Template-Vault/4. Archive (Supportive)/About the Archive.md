---
tags:
  - type/guide
  - status/active
type: note
created: 2025-01-10
status: active
---

# About the Archive

The archive is where completed, cancelled, or inactive items go to rest. It's not a graveyard - it's cold storage that keeps your active folders clean.

## What Goes Here

### Completed Projects
- Successfully finished work
- Delivered papers, submitted applications
- Shipped features, closed deals

### Cancelled Projects
- Projects that didn't work out
- Ideas that were explored but abandoned
- Work that's no longer relevant

### Inactive Areas
- Responsibilities you no longer have
- Roles you've moved on from
- Topics you're no longer actively pursuing

### Outdated Resources
- Information that's been superseded
- Old versions of documents
- Deprecated tools and processes

## Archiving Best Practices

### When to Archive

**Projects**: Archive when:
- [ ] All deliverables are complete
- [ ] No open tasks remain
- [ ] You've captured lessons learned
- [ ] It's been inactive for 6+ months

**Areas**: Archive when:
- [ ] You no longer have this responsibility
- [ ] The area has been absorbed into another
- [ ] It's no longer relevant to your life/work

**Resources**: Archive when:
- [ ] Information is outdated
- [ ] A better resource exists
- [ ] You haven't referenced it in 2+ years

### How to Archive

1. **Update the frontmatter**:
```yaml
status: archived
archived: 2025-01-10
archive_reason: Completed / Cancelled / Superseded
```

2. **Add final notes**:
   - What was accomplished?
   - What was learned?
   - Any follow-up needed?

3. **Move to Archive folder**

4. **Update any links** that pointed to this note

### Organizing the Archive

Consider organizing by year or type:
```
4. Archive (Supportive)/
├── 2024/
│   ├── Projects/
│   ├── Areas/
│   └── Resources/
├── 2025/
└── Cancelled/
```

## Finding Archived Content

### Search Tips

The archive is fully searchable. Use:
- Obsidian's global search
- `/smart-link` to find connections
- Dataview queries:

```dataview
LIST
FROM "4. Archive (Supportive)"
WHERE status = "archived"
SORT archived DESC
LIMIT 20
```

### Retrieving from Archive

If you need to reactivate something:

1. Move it back to the appropriate PARA folder
2. Update status to `active`
3. Remove `archived` date
4. Review and update content

## Why Archiving Matters

### Keeps Active Folders Clean
Less clutter = faster navigation = better focus

### Preserves History
You never lose work - it's just stored elsewhere

### Enables Reflection
Looking back helps you learn and grow

### Reduces Decision Fatigue
Clear criteria for what's active vs. inactive

---

## Archive Philosophy

> "The archive is not where ideas go to die. It's where completed work rests, lessons are preserved, and past efforts can be revisited when needed."

### Don't Be Afraid to Archive

- Archiving is not deleting
- You can always retrieve
- Clean folders = clear mind
- Regular archiving is healthy

### Weekly Archive Review

During your `/weekly-synthesis`:
1. Check for stale projects (no updates in 30+ days)
2. Look for completed work to archive
3. Review if any archived items should be reactivated

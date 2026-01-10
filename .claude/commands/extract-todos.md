# Extract TODOs

You are a task extraction assistant. Scan the vault for scattered tasks and consolidate them into an actionable overview.

## Process

### Step 1: Scan for Tasks

Search the entire vault for:
- Markdown checkboxes: `- [ ]` and `- [x]`
- TODO/FIXME comments
- Action items in meeting notes
- "Next steps" sections
- Commitments and promises mentioned in text

Search locations:
- `0. Inbox/` - Uncategorized tasks
- `1. Projects/` - Project-specific tasks
- `2. Areas (Ongoing)/` - Ongoing responsibilities
- Daily notes - Scattered daily tasks

### Step 2: Categorize Tasks

Group tasks by:

**By Status**
- Open (unchecked)
- Completed (checked)
- Blocked (has dependency)
- Stale (in old notes, possibly outdated)

**By Context**
- Project tasks (linked to specific project)
- Area tasks (ongoing responsibilities)
- Quick tasks (can be done in <15 min)
- Waiting for (dependent on others)
- Someday/Maybe (no urgency)

**By Priority**
- Urgent (mentioned as priority/deadline)
- Important (in active project)
- Normal (standard tasks)
- Low (nice-to-have)

### Step 3: Generate Report

```markdown
---
tags:
  - task-report
  - extraction
type: task-report
created: {{date}}
---

# Task Extraction Report

> Generated: {{date}}
> Total Open Tasks: [X]
> Completed (last 7 days): [Y]

## Urgent & Important

| Task | Source | Project/Area | Due |
|------|--------|--------------|-----|
| [Task] | [[Source Note]] | [[Project]] | [Date] |

## Active Project Tasks

### [[Project 1]]
- [ ] Task from [[Note A]]
- [ ] Task from [[Note B]]

### [[Project 2]]
- [ ] Task from [[Note C]]

## Quick Wins (< 15 min)

- [ ] [Quick task 1] - [[Source]]
- [ ] [Quick task 2] - [[Source]]

## Waiting For

| Task | Waiting On | Since | Source |
|------|------------|-------|--------|
| [Task] | [Person/Event] | [Date] | [[Note]] |

## Stale Tasks (> 30 days old)

These tasks may be outdated - review and either complete, update, or remove:

| Task | Age | Source | Recommendation |
|------|-----|--------|----------------|
| [Task] | 45 days | [[Old Note]] | Archive/Update/Do |

## Completed Recently

- [x] [Task 1] - [[Source]] - Completed [date]
- [x] [Task 2] - [[Source]] - Completed [date]

## Someday/Maybe

Low priority items captured but not scheduled:
- [ ] [Someday task 1]
- [ ] [Someday task 2]

## Statistics

| Metric | Count |
|--------|-------|
| Total Open | [X] |
| By Project | [breakdown] |
| Quick Wins | [X] |
| Stale (>30d) | [X] |
| Completed (7d) | [X] |

## Recommendations

1. **Focus on**: [Most important tasks]
2. **Clear out**: [Stale tasks to review]
3. **Consolidate**: [Tasks that should be grouped]
```

### Step 4: Offer Actions

After extraction, offer to:
1. Create a master task note with all open items
2. Clean up completed tasks from source notes
3. Archive or remove stale tasks
4. Move tasks to appropriate project notes
5. Create a daily focus list from urgent items

## Task Patterns to Recognize

Look for implicit tasks in:
- "I need to..." / "I should..."
- "Remember to..."
- "Follow up on..."
- "Don't forget..."
- Meeting action items
- Commitments to others
- Questions that need answers

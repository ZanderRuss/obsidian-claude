# MOC Generate

You are a Map of Content (MOC) specialist. Identify gaps in the vault's navigation structure and generate missing MOCs.

## Important: Use Specialized Agent

This command MUST use the `moc-agent` agent via the Task tool for comprehensive analysis:

```
Task tool with subagent_type="moc-agent"
```

## What is a MOC?

A Map of Content is a navigation note that:
- Links to all notes on a specific topic
- Provides context and structure
- Acts as an "index" or "hub" for a knowledge cluster
- Uses the naming convention: `MOC - Topic Name.md`

## Analysis Process

The moc-agent will:

### 1. Identify Note Clusters
- Find groups of 5+ related notes without a MOC
- Detect topics with scattered notes across folders
- Identify tag-based groupings needing navigation

### 2. Analyze Existing MOCs
- Check if existing MOCs are complete
- Find notes that should be in MOCs but aren't
- Identify stale MOC links (dead links)

### 3. Detect Orphaned Content
- Notes not linked from any MOC
- Content "islands" disconnected from main navigation
- Recently created notes needing integration

### 4. Suggest MOC Hierarchy
- Parent MOCs for broad topics
- Child MOCs for subtopics
- Cross-linking between related MOCs

## MOC Template

```markdown
---
tags:
  - type/moc
  - topic/{{topic}}
type: moc
created: {{date}}
status: active
---

# {{Topic Name}}

> Brief description of what this topic covers and why it matters.

## Overview

[2-3 sentences explaining the topic area]

## Core Notes

Essential notes on this topic:
- [[Note 1]] - [brief description]
- [[Note 2]] - [brief description]
- [[Note 3]] - [brief description]

## Subtopics

### [Subtopic A]
- [[Related Note A1]]
- [[Related Note A2]]

### [Subtopic B]
- [[Related Note B1]]
- [[Related Note B2]]

## Related Areas

- [[MOC - Related Topic 1]]
- [[MOC - Related Topic 2]]

## Resources

External references and resources:
- [[Resource Note 1]]
- [[Resource Note 2]]

---
*Last reviewed: {{date}}*
```

## Output Format

```markdown
# MOC Analysis Report

## Missing MOCs (Suggested)

| Topic | Note Count | Key Notes | Priority |
|-------|------------|-----------|----------|
| [Topic] | [X] | [[Note 1]], [[Note 2]] | High/Med/Low |

## Existing MOC Updates Needed

| MOC | Missing Notes | Stale Links |
|-----|---------------|-------------|
| [[MOC - X]] | [[Note A]], [[Note B]] | [[Deleted Note]] |

## Orphaned Notes (No MOC Coverage)

| Note | Suggested MOC | Location |
|------|---------------|----------|
| [[Note]] | [[MOC - Topic]] | `1. Projects/` |

## Recommended Actions

1. **Create**: [MOC name] covering [X] notes
2. **Update**: [MOC name] with [X] missing notes
3. **Restructure**: [MOC name] into sub-MOCs
```

## After Analysis

Offer to:
1. Create the suggested MOCs using the template
2. Update existing MOCs with missing notes
3. Add notes to appropriate MOCs
4. Create a master "Home" or "Index" MOC linking all MOCs

## Best Practices

- Keep MOCs focused (10-30 notes typically)
- Split large MOCs into sub-MOCs
- Review MOCs quarterly for staleness
- Link MOCs to each other for navigation

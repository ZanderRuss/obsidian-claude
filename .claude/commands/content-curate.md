# Content Curate

You are a content curation and quality specialist. Identify outdated content, suggest improvements, and consolidate similar notes.

## Important: Use Specialized Agent

This command MUST use the `content-curator` agent via the Task tool for comprehensive analysis:

```
Task tool with subagent_type="content-curator"
```

## Curation Goals

Maintain a high-quality knowledge base by:
- Keeping content current and accurate
- Eliminating redundancy
- Improving note quality
- Ensuring completeness

## Analysis Process

The content-curator agent will:

### 1. Identify Outdated Content
- Notes not modified in 6+ months that reference time-sensitive topics
- Notes with outdated links, tools, or references
- Notes marked as "draft" for extended periods
- Notes with stale "last reviewed" dates

### 2. Find Redundancy
- Multiple notes covering the same topic
- Near-duplicate content across notes
- Fragmented information that should be consolidated

### 3. Assess Note Quality
- Incomplete notes (stubs, placeholders)
- Notes lacking frontmatter
- Notes without links (isolation)
- Notes with unclear purpose or structure

### 4. Suggest Improvements
- Notes that could benefit from expansion
- Notes that need restructuring
- Notes that should be split or merged

## Output Format

```markdown
# Content Curation Report

## Summary
- Notes analyzed: [X]
- Issues found: [Y]
- Improvement opportunities: [Z]

## Outdated Content

### Needs Update (Time-Sensitive)
| Note | Last Modified | Issue | Action |
|------|---------------|-------|--------|
| [[Note]] | 2023-06-15 | References deprecated API | Update or archive |

### Stale Drafts
| Note | Age | Status | Recommendation |
|------|-----|--------|----------------|
| [[Draft Note]] | 8 months | draft | Complete or archive |

## Redundant Content

### Merge Candidates
| Primary Note | Merge These | Topic |
|--------------|-------------|-------|
| [[Main Note]] | [[Note A]], [[Note B]] | Topic X |

**Reasoning**: [Why these should be merged]

### Duplicate Information
| Content | Found In | Action |
|---------|----------|--------|
| [Description] | [[Note 1]], [[Note 2]] | Deduplicate |

## Quality Issues

### Incomplete Notes
| Note | Missing | Suggestion |
|------|---------|------------|
| [[Note]] | No frontmatter, no links | Add metadata, link to related |

### Isolated Notes (No Links)
| Note | Topic | Suggested Links |
|------|-------|-----------------|
| [[Orphan Note]] | Topic X | [[Related 1]], [[MOC - X]] |

## Improvement Opportunities

### Expand
| Note | Current State | Potential |
|------|---------------|-----------|
| [[Note]] | Brief stub | Could become comprehensive guide |

### Restructure
| Note | Issue | Suggestion |
|------|-------|------------|
| [[Note]] | Too long, unfocused | Split into 3 focused notes |

## Recommended Actions

### High Priority
1. [Action with highest impact]
2. [Next priority action]

### Quick Wins
- [Easy improvements]

### Longer Term
- [Larger restructuring projects]
```

## After Analysis

Offer to:
1. Merge redundant notes (preserving best content from each)
2. Archive truly outdated content
3. Add missing frontmatter to notes
4. Create links for isolated notes
5. Set up a content review schedule

## Content Quality Standards

### Every Note Should Have:
- Clear title reflecting content
- Frontmatter with tags, type, dates
- At least one outgoing link
- Purpose that's obvious from first paragraph

### Signs of Healthy Content:
- Regular updates (for evolving topics)
- Bidirectional links
- Part of at least one MOC
- Consistent formatting

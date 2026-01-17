# Metadata Fix

You are a metadata management specialist. Standardize frontmatter and ensure consistent file metadata across the vault.

## Important: Use Specialized Agent

This command MUST use the `metadata-agent` agent via the Task tool for comprehensive analysis:

```
Task tool with subagent_type="metadata-agent"
```

## Metadata Goals

Consistent metadata enables:
- Powerful Dataview queries
- Reliable filtering and search
- Automated organization
- Clear content lifecycle tracking

## Standard Frontmatter Template

```yaml
---
tags:
  - category/subcategory
type: note|project|moc|daily-note|research|voice-memo|web-clip|meeting
created: YYYY-MM-DD
modified: YYYY-MM-DD
status: draft|active|completed|archived
aliases:
  - alternate name
---
```

## Analysis Process

The metadata-agent will:

### 1. Audit Frontmatter
- Notes missing frontmatter entirely
- Notes with partial frontmatter
- Notes with non-standard fields
- Notes with incorrect field formats

### 2. Check Field Consistency
- `type` values used (are they consistent?)
- `status` values used (standardized set?)
- Date formats (ISO 8601: YYYY-MM-DD)
- Tag format (hierarchical, lowercase)

### 3. Validate Dates
- `created` dates that don't match file creation
- Missing `modified` dates
- Future dates (errors)

### 4. Analyze Custom Fields
- Identify common custom fields
- Suggest standardization
- Find one-off fields that may be errors

## Output Format

```markdown
# Metadata Audit Report

## Summary
- Notes analyzed: [X]
- Missing frontmatter: [Y]
- Incomplete frontmatter: [Z]
- Non-standard fields: [N]

## Missing Frontmatter

Notes with no YAML frontmatter:

| Note | Location | Suggested Type |
|------|----------|----------------|
| [[Note]] | `1. Projects/` | project |

## Incomplete Frontmatter

Notes missing required fields:

| Note | Has | Missing |
|------|-----|---------|
| [[Note]] | tags, type | created, status |

## Field Inconsistencies

### Type Values in Use
| Value | Count | Standard? |
|-------|-------|-----------|
| `note` | 45 | ✅ |
| `Note` | 3 | ❌ → `note` |
| `notes` | 2 | ❌ → `note` |

### Status Values in Use
| Value | Count | Standard? |
|-------|-------|-----------|
| `active` | 30 | ✅ |
| `in-progress` | 5 | ❌ → `active` |
| `done` | 8 | ❌ → `completed` |

### Date Format Issues
| Note | Field | Value | Should Be |
|------|-------|-------|-----------|
| [[Note]] | created | "Jan 15, 2024" | 2024-01-15 |

## Non-Standard Fields

Fields found that aren't in the standard template:

| Field | Count | Notes | Recommendation |
|-------|-------|-------|----------------|
| `project` | 15 | Links to project | Keep (useful) |
| `reviw` | 1 | Likely typo | Fix → `review` |

## Standardization Plan

### Phase 1: Add Missing Frontmatter
- [X] notes need frontmatter added

### Phase 2: Complete Partial Frontmatter
- [Y] notes need missing fields

### Phase 3: Fix Inconsistencies
- Normalize type values
- Normalize status values
- Fix date formats

### Phase 4: Custom Field Review
- Keep: [fields]
- Remove: [fields]
- Standardize: [fields]
```

## After Analysis

Offer to:
1. Add frontmatter to notes missing it (with inferred values)
2. Add missing fields to incomplete frontmatter
3. Normalize field values across the vault
4. Fix date formats
5. Create a metadata reference note documenting the standard

## Field Definitions

| Field | Required | Values | Purpose |
|-------|----------|--------|---------|
| `tags` | Yes | category/subcategory | Categorization |
| `type` | Yes | note, project, moc, etc. | Content type |
| `created` | Yes | YYYY-MM-DD | Creation date |
| `modified` | No | YYYY-MM-DD | Last edit date |
| `status` | Recommended | draft, active, completed, archived | Lifecycle stage |
| `aliases` | Optional | strings | Alternative names |

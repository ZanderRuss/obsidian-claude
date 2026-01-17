# Vault Review

You are a vault quality assurance specialist. Perform comprehensive cross-checking to validate consistency and quality across the vault.

## Important: Use Specialized Agent

This command MUST use the `review-agent` agent via the Task tool for comprehensive analysis:

```
Task tool with subagent_type="review-agent"
```

## Review Goals

Ensure the vault maintains:
- Consistency across all notes
- Quality standards throughout
- Structural integrity
- Accurate information

## Review Process

The review-agent will:

### 1. Structural Consistency

**Folder Organization**
- Notes in correct PARA locations
- No misplaced files
- Consistent folder naming

**Naming Conventions**
- MOCs follow `MOC - Topic.md` pattern
- Templates follow `Template - Type.md` pattern
- Daily notes use date format
- Consistent title casing

### 2. Content Quality

**Completeness**
- Notes with TODO markers still present
- Placeholder text (`[TBD]`, `...`, etc.)
- Incomplete sections

**Accuracy**
- Broken internal links
- Dead external links (if checkable)
- Outdated information

**Clarity**
- Notes with unclear purpose
- Ambiguous titles
- Missing context

### 3. Metadata Integrity

**Frontmatter**
- All required fields present
- Values follow standards
- No contradictions (e.g., status=completed but in Projects)

**Tags**
- Consistent formatting
- Valid hierarchy
- No orphan tags

### 4. Link Health

**Internal Links**
- Broken links (to non-existent notes)
- Circular references (if problematic)
- Bidirectional link balance

**External Resources**
- Referenced files exist
- Image links valid
- Attachment integrity

## Output Format

```markdown
# Vault Quality Review

## Overall Health Score: [X/100]

| Category | Score | Issues |
|----------|-------|--------|
| Structure | [X/25] | [summary] |
| Content | [X/25] | [summary] |
| Metadata | [X/25] | [summary] |
| Links | [X/25] | [summary] |

## Critical Issues 🔴

Must fix - impacts vault integrity:

| Issue | Location | Impact | Fix |
|-------|----------|--------|-----|
| Broken link | [[Note]] → [[Missing]] | Navigation broken | Create or remove |

## Warnings 🟡

Should fix - impacts quality:

| Issue | Location | Impact | Fix |
|-------|----------|--------|-----|
| Missing frontmatter | [[Note]] | Can't query | Add metadata |

## Suggestions 🟢

Nice to have - improvements:

| Suggestion | Location | Benefit |
|------------|----------|---------|
| Add aliases | [[Technical Note]] | Better discoverability |

## Detailed Findings

### Structure Review
- [X] notes in correct folders
- [Y] naming convention violations
- [Z] organizational improvements suggested

### Content Review
- [X] incomplete notes found
- [Y] notes with placeholder text
- [Z] clarity improvements needed

### Metadata Review
- [X] frontmatter issues
- [Y] tag inconsistencies
- [Z] date format problems

### Link Review
- [X] broken internal links
- [Y] orphaned notes
- [Z] missing bidirectional links

## PARA Compliance

| Folder | Expected Content | Violations |
|--------|------------------|------------|
| `0. Inbox` | Temp items | [X] old items should move |
| `1. Projects` | Active with deadline | [Y] completed items |
| `2. Areas` | Ongoing, no deadline | OK |
| `3. Resources` | Reference material | OK |
| `4. Archive` | Completed/inactive | [Z] still has active links |

## Action Plan

### Immediate (Today)
1. Fix [X] broken links
2. Move [Y] misplaced notes

### This Week
3. Complete [Z] incomplete notes
4. Add frontmatter to [N] notes

### This Month
5. Review [X] stale content
6. Restructure [Y] unclear notes

## Comparison to Last Review
(If previous review exists)

| Metric | Last Review | Now | Trend |
|--------|-------------|-----|-------|
| Health Score | 75 | 82 | 📈 +7 |
| Broken Links | 12 | 5 | 📈 -7 |
| Missing Metadata | 30 | 15 | 📈 -15 |
```

## After Review

Offer to:
1. Fix broken links (create notes or remove links)
2. Move misplaced notes to correct folders
3. Add missing frontmatter
4. Generate a recurring review schedule
5. Create a "Vault Health" dashboard note

## Review Frequency

| Review Type | Frequency | Focus |
|-------------|-----------|-------|
| Quick Check | Weekly | Broken links, inbox status |
| Standard | Monthly | All categories |
| Deep | Quarterly | + content accuracy, archive review |

## Quality Standards Reference

A quality vault has:
- <5% orphan notes
- <1% broken links
- 100% frontmatter coverage
- Clear folder organization
- Consistent naming
- Regular maintenance

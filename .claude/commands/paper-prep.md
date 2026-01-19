# /paper-prep

Set up tracking systems (citations, metrics, abbreviations, scope) before writing academic papers or thesis chapters. Prevents common quality issues.

## Usage

```
/paper-prep <project-path> [options]
```

## Options

- `--type <paper|thesis|chapter>` - Project type (auto-detected if not specified)
- `--skip-examples` - Don't include example entries in templates
- `--existing` - Add tracking to existing project folder

## Description

Initializes a project folder with tracking systems that prevent common academic writing issues:
- Missing citations
- Numeric inconsistencies
- Undefined abbreviations
- Over-generalization beyond evidence

## What It Creates

Creates `<project-path>/00-Tracking-Systems/` with five tracking files:

### 1. Citation-Tracker.md

Track all citations to ensure completeness.

```markdown
| Citation Key | Source Type | First Used | Sections | Verified | Notes |
|--------------|-------------|------------|----------|----------|-------|
| {example2024} | Journal | Introduction | Intro, Methods | [ ] | Primary methodology source |
```

### 2. Abbreviation-Tracker.md

Define all abbreviations on first use.

```markdown
| Abbreviation | Full Form | First Defined | Section | Verified |
|--------------|-----------|---------------|---------|----------|
| CLT | Cross-Laminated Timber | Methods | 4.1 | [ ] |
```

### 3. Key-Metrics-Table.md

Single source of truth for all quantitative values.

```markdown
| Metric | Canonical Value | Calculation | Reported As | Sections |
|--------|-----------------|-------------|-------------|----------|
| Carbon reduction | 38.2% | See Appendix-B | "38%" | Abstract, Results |
```

### 4. Study-Boundaries.md

Define what this study does and does NOT cover.

```markdown
## Population/Sample Scope
- [Define who/what is included]
- [Define exclusion criteria]

## Geographic Scope
- [Define geographic limits]

## Temporal Scope
- [Define time period]

## Methodological Limitations
- [List known limitations]

## What This Study Does NOT Claim
- [Explicit non-claims to prevent over-generalization]
```

### 5. README.md

Instructions for using the tracking systems during writing.

## Process

1. **Detect Project Type**
   - If `--type` specified, use that
   - Else if path contains "thesis": type = thesis
   - Else if path contains "chapter": type = chapter
   - Else: type = paper

2. **Create Tracking Folder**
   ```
   mkdir -p <project-path>/00-Tracking-Systems/
   ```

3. **Generate Files**
   - Create all 5 tracking files
   - If `--skip-examples`: Use empty templates
   - Else: Include example entries

4. **Customize by Type**
   - **thesis**: Add cross-chapter tracking fields
   - **chapter**: Add parent thesis reference
   - **paper**: Standard single-document tracking

5. **Report Success**
   ```
   Created 00-Tracking-Systems/
     - Citation-Tracker.md
     - Abbreviation-Tracker.md
     - Key-Metrics-Table.md
     - Study-Boundaries.md
     - README.md

   Next steps:
   1. Fill in Study-Boundaries.md before writing
   2. Run /paper-write or /thesis-write when ready
   ```

## Integration Points

### Called Before

- `/paper-write` - Paper orchestrator checks for tracking systems
- `/thesis-write` - Thesis orchestrator loads tracking context
- `/chapter-write` - Chapter coordinator uses parent tracking

### Validates With

- `document-validator` - Checks metrics against Key-Metrics-Table
- `citation-validator` - Verifies against Citation-Tracker
- `argument-validator` - Uses Study-Boundaries for claim validation

## Tracking File Templates

### Citation-Tracker.md (Full Template)

```markdown
# Citation Tracker

Track all citations to ensure completeness and verify sources.

## How to Use

1. Add each citation when you first use it
2. Update "Sections" as citation appears in more places
3. Mark "Verified" after checking source exists in Zotero/BibTeX
4. Run `/quality-check` to validate all citations before submission

## Citation Table

| Citation Key | Source Type | First Used | Sections | Verified | Notes |
|--------------|-------------|------------|----------|----------|-------|
| {example2024} | Journal | Introduction | Intro, Methods | [ ] | Primary methodology source |

## Source Types

- Journal: Peer-reviewed journal article
- Conference: Conference paper/proceedings
- Book: Book or book chapter
- Preprint: arXiv, bioRxiv, etc.
- Report: Technical report, white paper
- Web: Website, blog post
- Data: Dataset citation
```

### Abbreviation-Tracker.md (Full Template)

```markdown
# Abbreviation Tracker

Define all abbreviations on first use. Prevents undefined terms.

## How to Use

1. Add abbreviation when you first define it
2. Use format: "Full Term (ABBR)" on first use
3. Mark "Verified" after confirming consistency
4. Run `/quality-check` to find undefined abbreviations

## Abbreviation Table

| Abbreviation | Full Form | First Defined | Section | Verified |
|--------------|-----------|---------------|---------|----------|
| CLT | Cross-Laminated Timber | Methods | 4.1 | [ ] |

## Standard Abbreviations (No Definition Needed)

- e.g., i.e., etc., vs.
- Common units: kg, m, s, %
- Well-known: AI, ML, API, URL
```

### Key-Metrics-Table.md (Full Template)

```markdown
# Key Metrics Table

Single source of truth for all quantitative values. Prevents inconsistencies.

## How to Use

1. Add each key metric/statistic when calculated
2. Record the canonical (precise) value
3. Note how it's reported in text (may be rounded)
4. Track which sections reference this metric
5. Run `/quality-check` to detect numeric inconsistencies

## Metrics Table

| Metric | Canonical Value | Calculation | Reported As | Sections | Verified |
|--------|-----------------|-------------|-------------|----------|----------|
| Carbon reduction | 38.2% | See Appendix-B | "38%" | Abstract, Results | [ ] |

## Categories

### Primary Results
| Metric | Canonical Value | Calculation | Reported As | Sections | Verified |
|--------|-----------------|-------------|-------------|----------|----------|

### Sample/Population
| Metric | Canonical Value | Calculation | Reported As | Sections | Verified |
|--------|-----------------|-------------|-------------|----------|----------|

### Statistical Tests
| Metric | Canonical Value | Calculation | Reported As | Sections | Verified |
|--------|-----------------|-------------|-------------|----------|----------|
```

### Study-Boundaries.md (Full Template)

```markdown
# Study Boundaries

Define what this study does and does NOT cover. Prevents over-generalization.

## How to Use

1. Fill this in BEFORE writing begins
2. Reference when making claims in Results/Discussion
3. Use "What This Study Does NOT Claim" to check for over-reach
4. argument-validator uses this to flag unsupported claims

## Population/Sample Scope

**Included:**
- [Define who/what is included in the study]

**Excluded:**
- [Define explicit exclusion criteria]

**Sample Size:**
- [Record actual sample sizes]

## Geographic Scope

**Covered:**
- [Define geographic limits of the study]

**Not Covered:**
- [Explicitly note regions NOT included]

## Temporal Scope

**Time Period:**
- [Define time period of data/study]

**Not Applicable To:**
- [Time periods this cannot generalize to]

## Methodological Scope

**Methods Used:**
- [List methods employed]

**Methods NOT Used:**
- [Relevant methods that were not used]

**Limitations:**
- [Known methodological limitations]

## What This Study DOES Claim

1. [Primary claim 1 - be specific]
2. [Primary claim 2 - be specific]
3. [Primary claim 3 - be specific]

## What This Study Does NOT Claim

1. [Explicit non-claim to prevent over-generalization]
2. [Another explicit non-claim]
3. [Things readers might assume but shouldn't]

## Qualifier Language to Use

When writing claims, use appropriate hedging:
- "In our sample..." (not "In general...")
- "For the period studied..." (not "Always...")
- "Among participants who..." (not "Everyone...")
- "Our results suggest..." (not "This proves...")
```

### README.md (Full Template)

```markdown
# Tracking Systems

These files prevent common academic writing issues.

## Quick Reference

| File | Purpose | When to Update |
|------|---------|----------------|
| Citation-Tracker.md | Track all citations | When citing a source |
| Abbreviation-Tracker.md | Track abbreviations | When defining terms |
| Key-Metrics-Table.md | Single truth for numbers | When reporting statistics |
| Study-Boundaries.md | Define scope limits | Before writing; review in Discussion |

## Workflow

### Before Writing

1. Fill in Study-Boundaries.md completely
2. Review scope with collaborators if applicable

### During Writing

1. **Citing**: Add to Citation-Tracker.md
2. **Abbreviations**: Add to Abbreviation-Tracker.md on first use
3. **Numbers**: Check Key-Metrics-Table.md before writing any statistic

### Before Submission

1. Run `/quality-check` to validate:
   - All citations verified
   - All abbreviations defined
   - All metrics consistent
   - Claims within study boundaries

## Integration with Writing Commands

The paper-orchestrator and thesis-orchestrator automatically:
- Load these tracking systems as context
- Validate against them during quality gates
- Flag inconsistencies between trackers and document

## Related Commands

- `/paper-write` - Writes paper using these trackers
- `/thesis-write` - Writes thesis using these trackers
- `/quality-check` - Validates document against trackers
```

## Example

```
User: /paper-prep "1. Projects/NeurIPS-2024-Paper"

Claude:
Detecting project type... paper

Creating tracking systems...

Created 00-Tracking-Systems/
  - Citation-Tracker.md
  - Abbreviation-Tracker.md
  - Key-Metrics-Table.md
  - Study-Boundaries.md
  - README.md

Next steps:
1. Fill in Study-Boundaries.md before writing
2. Run /paper-write "1. Projects/NeurIPS-2024-Paper" when ready
```

```
User: /paper-prep "1. Projects/PhD-Thesis" --type thesis

Claude:
Project type: thesis

Creating tracking systems with cross-chapter tracking...

Created 00-Tracking-Systems/
  - Citation-Tracker.md (with chapter column)
  - Abbreviation-Tracker.md (with chapter column)
  - Key-Metrics-Table.md (with chapter tracking)
  - Study-Boundaries.md (thesis-level scope)
  - README.md

Note: Thesis tracking includes cross-chapter consistency fields.

Next steps:
1. Fill in Study-Boundaries.md before writing
2. Run /thesis-write "1. Projects/PhD-Thesis" when ready
```

```
User: /paper-prep "1. Projects/Existing-Paper" --existing --skip-examples

Claude:
Adding tracking to existing project...

Created 00-Tracking-Systems/
  - Citation-Tracker.md (empty template)
  - Abbreviation-Tracker.md (empty template)
  - Key-Metrics-Table.md (empty template)
  - Study-Boundaries.md (empty template)
  - README.md

Existing content preserved. Tracking folder added.

Next steps:
1. Review existing content and populate trackers
2. Fill in Study-Boundaries.md
3. Run /quality-check to validate
```

## Related Commands

- `/paper-write` - Write paper (uses tracking systems)
- `/thesis-write` - Write thesis (uses tracking systems)
- `/chapter-write` - Write chapter (uses parent tracking)
- `/quality-check` - Validate against trackers
- `/research-project-init` - Initialize full research project structure

## Agent Integration

This command creates files that are consumed by:
- **paper-orchestrator**: Loads tracking context before writing
- **thesis-orchestrator**: Uses tracking for cross-chapter consistency
- **document-validator**: Checks metrics consistency
- **citation-validator**: Verifies citation completeness
- **argument-validator**: Validates claims against Study-Boundaries

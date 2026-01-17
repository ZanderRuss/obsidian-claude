# Context Protocol Schema

**Version:** 1.0
**Created:** 2026-01-15
**Purpose:** Defines how information flows through the hierarchical agent system

---

## Overview

The context protocol defines structured data schemas for passing information between agents in the paper-writing pipeline. Each level in the hierarchy receives progressively more focused context, preventing context overflow while maintaining necessary information.

**Key Principles:**
1. **Hierarchical summarization** - Each level summarizes before passing down
2. **Progressive focus** - Lower levels receive more specific, less broad context
3. **Explicit dependencies** - All required context fields are documented
4. **Graceful degradation** - Optional fields have defined fallback behavior

---

## Context Hierarchy

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            CONTEXT HIERARCHY                                 │
└─────────────────────────────────────────────────────────────────────────────┘

ThesisContext (Full Document State)
    │
    │ Summarize to 500 words max
    │
    ▼
ChapterContext (Chapter-Level State)
    │
    │ Summarize to 300 words max
    │
    ▼
SectionContext (Section-Level State)
    │
    │ Minimal, focused context
    │
    ▼
Section Writer Output

Quality Context (Parallel Path)
    └── Document + any level context → QC Agents → QualityReport
```

---

## Schema: ThesisContext

**Used by:** thesis-orchestrator, chapter-coordinator (receives summarized version)
**Scope:** Entire thesis/paper document

```yaml
ThesisContext:
  # === Identification ===
  project_id: string                    # Unique thesis/paper identifier
  title: string                         # Document title
  document_type: "thesis" | "paper"     # Scale of document

  # === Research Core ===
  research_questions: string[]          # Core RQs (numbered list)
  contributions: string[]               # Claimed contributions (numbered)
  hypothesis: string?                   # Optional formal hypothesis

  # === Terminology ===
  terminology_glossary:                 # Shared vocabulary for consistency
    - term: string                      # The technical term
      definition: string                # Clear definition
      abbreviation: string?             # Optional abbreviation
      first_use_chapter: string?        # Where first introduced

  # === Style Guide ===
  style_guide:
    citation_style: string              # "APA" | "IEEE" | "Nature" | "Vancouver" | "Chicago" | custom
    methodology_type: string            # "experimental" | "analytical" | "empirical" | "theoretical" | "mixed_methods"
    tense_rules:
      methods: "past" | "present"
      results: "past" | "present"
      discussion: "past" | "present"
    formatting:
      heading_style: string             # "numbered" | "chapter-based" | "minimal"
      figure_prefix: string             # "Figure" | "Fig."
      table_prefix: string              # "Table"
      equation_numbering: string        # "right-aligned" | "centered"
    evidence_standards: object?         # Field-specific evidence requirements

  # === Structure ===
  chapter_structure:                    # Document outline
    - chapter_id: string
      chapter_title: string
      chapter_type: "introduction" | "literature_review" | "methodology" | "results" | "discussion" | "conclusion" | "appendix"
      word_budget: int
      sections: string[]                # Section titles within chapter

  # === Progress State ===
  chapter_summaries:                    # Updated as chapters complete
    - chapter_id: string
      status: "pending" | "in_progress" | "drafted" | "reviewed" | "complete"
      summary: string                   # 200-word max summary
      key_claims: string[]              # Main arguments made
      defined_terms: string[]           # Terms introduced in this chapter
      cross_references: string[]        # References to other chapters

  # === Bibliography ===
  bibliography_keys: string[]           # All citation keys available
  required_citations: string[]          # Citations that MUST appear

  # === Budget ===
  word_budget:
    total: int
    per_chapter: object                 # {chapter_id: int}

  # === Metadata ===
  venue: string?                        # Target venue if applicable
  submission_deadline: string?          # ISO8601 date if applicable
  created: string                       # ISO8601
  last_updated: string                  # ISO8601
```

### Required vs Optional Fields

| Field | Required | Default if Missing |
|-------|----------|-------------------|
| project_id | ✅ Yes | - |
| title | ✅ Yes | - |
| research_questions | ✅ Yes | - |
| contributions | ✅ Yes | - |
| terminology_glossary | ✅ Yes | Empty array (warn) |
| style_guide | ✅ Yes | - |
| style_guide.citation_style | ✅ Yes | - |
| style_guide.methodology_type | ✅ Yes | - |
| chapter_structure | ✅ Yes | - |
| bibliography_keys | 🟡 Optional | Empty array |
| word_budget | 🟡 Optional | Reasonable defaults |
| venue | 🟡 Optional | null |

---

## Schema: ChapterContext

**Used by:** chapter-coordinator, section writers (receives summarized version)
**Scope:** Single chapter within document

```yaml
ChapterContext:
  # === Parent Context (Summarized) ===
  parent_summary: string                # Compressed ThesisContext (500 words max)
  project_id: string                    # Inherited from parent
  document_title: string                # Inherited from parent

  # === Chapter Identification ===
  chapter_number: int
  chapter_id: string
  chapter_title: string
  chapter_type: string                  # Same as in chapter_structure

  # === Chapter Objectives ===
  chapter_objectives: string[]          # What this chapter must accomplish
  research_questions_addressed: string[] # Subset of RQs this chapter addresses
  contributions_supported: string[]      # Which contributions this chapter supports

  # === Section Structure ===
  section_assignments:
    - section_id: string
      section_title: string
      word_budget: int
      dependencies: string[]            # Section IDs that must complete first
      writer_type: string               # Which section writer agent to use
      status: "pending" | "in_progress" | "drafted" | "complete"

  # === Context for Continuity ===
  preceding_chapter_summary: string     # Summary of previous chapter (if any)
  following_chapter_preview: string     # Brief preview of next chapter (if any)

  # === Terminology (Filtered) ===
  terminology_subset:                   # Only terms relevant to this chapter
    - term: string
      definition: string
      abbreviation: string?

  # === Style (Inherited) ===
  style_guide:                          # Inherited from parent
    citation_style: string
    methodology_type: string
    tense_rules: object
    formatting: object

  # === Citations ===
  chapter_citations: string[]           # Citation keys relevant to this chapter
  required_citations: string[]          # Citations that MUST appear in this chapter

  # === Budget ===
  word_budget: int                      # Total for this chapter
  remaining_budget: int                 # After sections drafted
```

### Context Summarization: ThesisContext → ChapterContext

When creating ChapterContext from ThesisContext:

1. **Compress to 500 words max** for `parent_summary`:
   - Include document title and overall goal
   - Include research questions relevant to this chapter
   - Include contributions this chapter supports
   - Summarize style guide key points

2. **Filter terminology_glossary** to `terminology_subset`:
   - Include terms used in this chapter's content
   - Include terms defined in preceding chapters (for reference)
   - Exclude terms only used in later chapters

3. **Include only adjacent chapter context**:
   - `preceding_chapter_summary`: Summary of chapter N-1
   - `following_chapter_preview`: Brief note on chapter N+1

---

## Schema: SectionContext

**Used by:** Individual section writers
**Scope:** Single section within chapter

```yaml
SectionContext:
  # === Parent Context (Summarized) ===
  chapter_summary: string               # Compressed ChapterContext (300 words max)
  project_id: string                    # Inherited
  chapter_id: string                    # Inherited
  chapter_title: string                 # Inherited

  # === Section Identification ===
  section_id: string
  section_title: string
  section_number: string                # e.g., "3.2"

  # === Section Objectives ===
  section_objectives: string[]          # What this section must accomplish
  key_points: string[]                  # Main points to cover

  # === Context for Continuity ===
  preceding_section_summary: string     # Summary of previous section (if any)
  following_section_preview: string     # Brief preview of next section (if any)

  # === Source Material ===
  relevant_research_files: string[]     # Paths to source material
  relevant_notes: string[]              # Paths to related notes

  # === Citations ===
  required_citations: string[]          # Citations that MUST appear
  available_citations: string[]         # All citations available for use

  # === Terminology ===
  terminology_to_use: string[]          # Terms to use (for consistency)
  terms_to_define: string[]             # Terms to define in this section

  # === Style (Inherited) ===
  style_guide:
    citation_style: string
    methodology_type: string
    tense_for_section: string           # Specific tense for this section type

  # === Budget ===
  word_budget: int                      # Target word count for this section
```

### Context Summarization: ChapterContext → SectionContext

When creating SectionContext from ChapterContext:

1. **Compress to 300 words max** for `chapter_summary`:
   - Chapter title and objectives
   - How this section fits in the chapter
   - Key context from parent summary

2. **Include only immediate neighbors**:
   - `preceding_section_summary`: Section N-1 only
   - `following_section_preview`: Section N+1 only

3. **Focus bibliography**:
   - `required_citations`: Must-cite references
   - `available_citations`: Relevant subset for this section

---

## Schema: QualityReport

**Used by:** All quality control agents
**Scope:** Output of validation operations

```yaml
QualityReport:
  # === Identification ===
  report_id: string                     # Unique report identifier
  agent_id: string                      # Which QC agent generated this
  target_file: string                   # What was validated
  target_type: "section" | "chapter" | "document"

  # === Timing ===
  timestamp: string                     # ISO8601
  duration_ms: int                      # How long validation took

  # === Overall Result ===
  passed: boolean                       # Did it pass quality gate?
  score: float                          # 0.0 - 1.0 overall score

  # === Category Scores ===
  category_scores:
    consistency: float?                 # Terminology, style consistency
    cross_references: float?            # Figure, table, section refs
    argument_quality: float?            # Logic, evidence, hedging
    citation_accuracy: float?           # Citation format, completeness
    formatting: float?                  # Style guide compliance

  # === Issues ===
  issues:
    - issue_id: string
      severity: "critical" | "major" | "minor" | "suggestion"
      category: string                  # Which category
      location: string                  # File path + line/section
      description: string               # What the issue is
      recommendation: string            # How to fix
      auto_fixable: boolean             # Can be auto-corrected?

  # === Summary ===
  summary: string                       # Human-readable summary
  critical_count: int
  major_count: int
  minor_count: int
  suggestion_count: int

  # === Metadata ===
  context_used:                         # What context was available
    thesis_context: boolean
    chapter_context: boolean
    section_context: boolean
```

### QualityReport Severity Definitions

| Severity | Score Impact | Auto-Fix | Block Deployment |
|----------|--------------|----------|------------------|
| **critical** | -0.3 per issue | No | 🔴 Yes |
| **major** | -0.15 per issue | Sometimes | 🟠 Should fix |
| **minor** | -0.05 per issue | Often | 🟡 Recommended |
| **suggestion** | No impact | Usually | ⚪ Optional |

---

## Context Passing Protocol

### 1. Initialization

When starting a new document:

```yaml
1. User provides:
   - Research questions
   - Contributions
   - Target venue (optional)
   - Existing notes/research (optional)

2. thesis-orchestrator creates:
   - Full ThesisContext
   - Chapter structure based on document_type
   - Terminology glossary from existing notes

3. For each chapter:
   - Create ChapterContext from ThesisContext (summarized)
   - Spawn chapter-coordinator with context
```

### 2. Chapter Writing

```yaml
1. chapter-coordinator receives ChapterContext

2. For each section:
   - Create SectionContext from ChapterContext (summarized)
   - Spawn appropriate section writer

3. After section completes:
   - Update section status in ChapterContext
   - Create section_summary for next section's context

4. After all sections:
   - Consolidate into chapter
   - Create chapter_summary for parent
```

### 3. Quality Control

```yaml
1. After section/chapter/document complete:
   - Create QualityContext (document + level-specific context)
   - Spawn QC agents in parallel
   - Collect QualityReports

2. Evaluate reports:
   - If any critical issues: halt, report, await fix
   - If major issues: attempt auto-fix, re-check
   - If minor/suggestions: log for later, continue
```

### 4. Context Updates

```yaml
1. When chapter completes:
   - Update chapter_summaries in ThesisContext
   - Propagate to subsequent chapter contexts

2. When terminology changes:
   - Update terminology_glossary in ThesisContext
   - Filter to relevant chapter/section contexts

3. When cross-references added:
   - Update cross_references in chapter_summaries
   - Validate with cross-ref checker
```

---

## JSON Schema Files

For automated validation, JSON Schema files are provided:

- `context-schema-thesis.json` - ThesisContext validation
- `context-schema-chapter.json` - ChapterContext validation
- `context-schema-section.json` - SectionContext validation
- `context-schema-quality.json` - QualityReport validation

(See accompanying JSON files)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-15 | Initial context protocol schema |

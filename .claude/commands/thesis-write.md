# /thesis-write

Write a PhD thesis using the multi-agent paper writing pipeline.

## Usage

```
/thesis-write [project-path] [options]
```

## Options

- `--chapter <n>` - Write specific chapter only
- `--from-checkpoint` - Resume from last checkpoint
- `--outline-only` - Generate outline without full writing
- `--validate-only` - Run quality checks without writing

## Description

Orchestrates the complete thesis writing process using the hierarchical agent system:

1. **thesis-orchestrator** - Manages overall document coordination
2. **chapter-coordinator** - Coordinates sections within each chapter
3. **Section writers** - Specialized writers for each section type
4. **Quality control** - Validates consistency, arguments, citations

## Process

1. **Load Thesis Context**
   - Read ThesisContext from project folder
   - Verify all required metadata present
   - Load existing chapter drafts (if any)

2. **Validate Prerequisites**
   - Research notes available
   - Bibliography populated
   - Terminology glossary defined
   - Chapter outlines approved

3. **Chapter Writing Loop**
   ```
   For each chapter:
     1. Create ChapterContext (summarized thesis context)
     2. Spawn chapter-coordinator
     3. Chapter writes sections in parallel where possible
     4. Run quality checks
     5. Checkpoint progress
   ```

4. **Document Assembly**
   - Combine all chapters
   - Validate cross-references
   - Run final quality control
   - Generate complete thesis draft

5. **Export Options**
   - Markdown (for Obsidian)
   - LaTeX (via latex-specialist)
   - PDF (if LaTeX compilation enabled)

## Quality Gates

Each chapter must pass before proceeding:
- document-validator: score ≥ 0.8
- argument-validator: score ≥ 0.8
- citation-validator: score ≥ 0.8

If a chapter fails quality checks:
1. Attempt automatic fix (2 retries)
2. If still failing, checkpoint and pause
3. Request human review

## Output

```yaml
ThesisWriteOutput:
  chapters_completed: int
  total_word_count: int
  quality_report:
    overall_score: float
    chapter_scores: dict
  output_files:
    markdown: path
    latex: path?
    pdf: path?
  checkpoint: path
```

## Resume from Checkpoint

If writing is interrupted:
```
/thesis-write "Project Path" --from-checkpoint
```

This loads the last saved checkpoint and continues from there.

## Example Session

```
User: /thesis-write "1. Projects/Efficient Attention Thesis"

Claude:
Loading thesis context...
✓ 7 chapters defined
✓ 234 bibliography entries
✓ Terminology glossary (45 terms)

Starting thesis writing...

[Chapter 1: Introduction]
- Spawning introduction-writer...
- Writing: Background (800/1000 words) ████████░░ 80%
- Writing: Gap Statement (400/500 words) ████████ 100%
- Writing: Contributions (600/600 words) ████████ 100%
- Running quality checks...
- ✓ Chapter 1 passed (score: 0.87)

[Chapter 2: Literature Review]
- Spawning lit-review-writer...
...
```

## Related Commands

- `/thesis-init` - Initialize thesis project
- `/chapter-write` - Write single chapter
- `/quality-check` - Run quality validation
- `/paper-write` - For conference papers (simpler)

## Agent Integration

Invokes thesis-orchestrator which manages:
- chapter-coordinator (per chapter)
- Section writers (per section)
- Quality control agents (validation)
- Export agents (final output)

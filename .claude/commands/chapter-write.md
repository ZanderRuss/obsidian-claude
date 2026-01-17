# /chapter-write

Write a single thesis chapter using the chapter-coordinator agent.

## Usage

```
/chapter-write <project-path> --chapter <n>
/chapter-write <chapter-draft-path>
```

## Options

- `--chapter <n>` - Chapter number to write (1-7 typically)
- `--section <name>` - Write only specific section
- `--outline-only` - Generate detailed outline without prose
- `--context-from <path>` - Use context from specified file

## Description

Writes a single chapter of a thesis, coordinating multiple section writers for maximum quality. Useful for:
- Iterating on specific chapters
- Rewriting after reviewer feedback
- Writing chapters out of order

## Process

1. **Load Context**
   - Load ThesisContext from project
   - Create ChapterContext for target chapter
   - Summarize thesis-level context (300 words max)

2. **Section Planning**
   - Identify sections for chapter type
   - Assign word budgets
   - Map required citations

3. **Section Writing**
   ```
   Parallel where possible:
   - [Introduction sections] → background-writer
   - [Literature sections] → lit-review-writer
   - [Methods sections] → methodology-writer
   - [Results sections] → results-writer
   - [Discussion sections] → discussion-writer
   - [Conclusion sections] → conclusion-writer
   ```

4. **Assembly**
   - Merge section outputs
   - Verify transitions
   - Check cross-references

5. **Quality Control**
   - Run document-validator
   - Run argument-validator
   - Run citation-validator

## Chapter Types

| Chapter | Primary Writer | Model |
|---------|---------------|-------|
| Introduction | introduction-writer | opus |
| Literature Review | lit-review-writer | opus |
| Methodology | methodology-writer | sonnet |
| Results | results-writer | sonnet |
| Discussion | discussion-writer | opus |
| Conclusion | conclusion-writer | sonnet |

## Output

```yaml
ChapterOutput:
  chapter_number: int
  chapter_title: string
  sections:
    - section_id: string
      word_count: int
      quality_score: float
  total_word_count: int
  quality_report: QualityReport
  output_path: string
```

## Example

```
User: /chapter-write "1. Projects/Attention Thesis" --chapter 3

Claude:
Loading thesis context...
Target: Chapter 3 - Methodology

Sections to write:
- 3.1 Research Design (600 words)
- 3.2 Experimental Setup (800 words)
- 3.3 Evaluation Metrics (400 words)
- 3.4 Implementation Details (600 words)

Spawning methodology-writer...
[Progress bar and status updates]

Chapter 3 complete:
- Word count: 2,412 words
- Quality score: 0.89
- Saved to: .../03-Methodology/Methodology-Draft.md
```

## Section-Only Mode

Write a single section:
```
/chapter-write "Project Path" --chapter 3 --section "Experimental Setup"
```

Useful for targeted revisions.

## Related Commands

- `/thesis-write` - Write complete thesis
- `/paper-write` - Write conference paper
- `/quality-check` - Validate chapter

## Agent Integration

Invokes chapter-coordinator which:
- Creates SectionContext for each section
- Spawns appropriate section writers
- Runs quality validation
- Assembles final chapter

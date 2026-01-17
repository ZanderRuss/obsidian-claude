# /paper-write

Write a conference/journal paper using the paper-orchestrator agent.

## Usage

```
/paper-write <project-path> [options]
```

## Options

- `--venue <name>` - Target venue (NeurIPS, ACL, IEEE, etc.)
- `--deadline <date>` - Submission deadline
- `--outline-only` - Generate outline without full writing
- `--from-notes` - Start from existing research notes
- `--anonymize` - Prepare for double-blind submission

## Description

Orchestrates the complete paper writing process using a streamlined agent system optimized for shorter academic papers (8-30 pages).

Unlike thesis writing, paper-orchestrator directly coordinates section writers without an intermediate chapter-coordinator layer.

## Process

1. **Initialization**
   - Identify target venue
   - Load venue requirements (via venue-templates skill)
   - Determine page/word limits
   - Set up citation style

2. **Context Creation**
   - Extract research questions from notes
   - Define contributions (3-4 typically)
   - Build minimal terminology glossary
   - Calculate word budgets per section

3. **Writing Order**
   Papers are written in dependency order:
   ```
   1. Methodology (establishes what was done)
   2. Results (depends on methodology)
   3. Introduction (frames the work)
   4. Related Work (positions among existing)
   5. Discussion (interprets results)
   6. Conclusion (summarizes)
   7. Abstract (last - summarizes everything)
   ```

4. **Quality Control**
   - document-validator
   - argument-validator
   - citation-validator
   - formatting-validator (venue compliance)

5. **Export**
   - Markdown (for editing)
   - LaTeX (via latex-specialist)
   - PDF (if compilation enabled)

## Word Budgets (8-page paper)

```yaml
conference_8page:
  abstract: 150-200
  introduction: 600-800
  related_work: 600-800
  methodology: 1000-1200
  results: 800-1000
  discussion: 400-600
  conclusion: 200-300
```

## Output

```yaml
PaperOutput:
  title: string
  venue: string
  sections_completed: int
  total_word_count: int
  page_estimate: float
  quality_report:
    overall_score: float
    section_scores: dict
  output_files:
    markdown: path
    latex: path?
    pdf: path?
  anonymized: boolean
```

## Venue Templates

Common venues with pre-configured templates:
- NeurIPS, ICML, ICLR (ML)
- ACL, EMNLP, NAACL (NLP)
- CVPR, ICCV, ECCV (CV)
- IEEE Transactions
- Nature, Science, PLOS

## Example

```
User: /paper-write "1. Projects/Linear Attention Paper" --venue NeurIPS

Claude:
Loading project context...
Venue: NeurIPS 2026
Template: neurips_2026.sty
Page limit: 9 (+ unlimited refs)
Citation style: Numeric

Starting paper writing...

[Methodology]
- Spawning methodology-writer...
- Writing (1,100/1,200 words) ████████░░ 92%
- ✓ Complete

[Results]
- Spawning results-writer...
...

Paper complete:
- Word count: 4,215 words
- Page estimate: 8.3 pages
- Quality score: 0.91
- Saved to: drafts/paper-draft.md
- LaTeX: drafts/neurips_submission.tex
```

## Anonymization Mode

For double-blind submission:
```
/paper-write "Project" --venue NeurIPS --anonymize
```

This:
- Removes author names
- Anonymizes self-citations
- Removes acknowledgments
- Checks for identifying information

## Related Commands

- `/thesis-write` - For full thesis
- `/chapter-write` - For thesis chapters
- `/quality-check` - Validate paper
- `/paper-revise` - Handle reviewer feedback

## Agent Integration

Invokes paper-orchestrator which:
- Spawns section writers directly (no chapter layer)
- Manages word budgets
- Runs quality validation
- Coordinates with latex-specialist for export

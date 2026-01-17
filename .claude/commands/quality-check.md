# /quality-check

Run all quality control agents on a document.

## Usage

```
/quality-check <document-path> [options]
```

## Options

- `--validators <list>` - Specific validators to run (comma-separated)
- `--fix` - Attempt automatic fixes for issues
- `--strict` - Fail on warnings, not just errors
- `--report <path>` - Save report to specific location

## Description

Runs the full quality control pipeline on any academic document (paper, thesis, chapter, or section). Produces a consolidated report with actionable recommendations.

## Quality Control Agents

1. **document-validator** (haiku)
   - Terminology consistency
   - Abbreviation usage
   - Tense consistency
   - Cross-reference validation
   - Citation completeness

2. **argument-validator** (opus)
   - Claim-evidence relationships
   - Logical flow analysis
   - Fallacy detection
   - Hedging appropriateness
   - Contribution alignment

3. **citation-validator** (sonnet)
   - Citation completeness
   - Citation accuracy (via Zotero)
   - Format consistency
   - Citation density analysis

4. **plagiarism-checker** (sonnet)
   - Paraphrase quality
   - Attribution verification
   - Self-plagiarism detection
   - Web similarity check

5. **formatting-validator** (haiku)
   - Page/word limits
   - Font and margin requirements
   - Section requirements
   - Anonymization (if applicable)

## Process

1. **Load Document**
   - Parse document structure
   - Extract metadata (frontmatter, type, venue)
   - Identify document type

2. **Run Validators**
   ```
   Parallel execution:
   ├── document-validator ─┐
   ├── argument-validator  ├── Consolidate
   ├── citation-validator  │
   ├── plagiarism-checker ─┘
   └── formatting-validator (if venue specified)
   ```

3. **Consolidate Report**
   - Aggregate all issues
   - Categorize by severity
   - Generate recommendations
   - Calculate overall score

4. **Auto-Fix (if --fix)**
   - Apply automatic fixes for simple issues
   - Re-run affected validators
   - Report remaining issues

## Output

```yaml
QualityReport:
  document: string
  timestamp: ISO8601

  overall_score: float  # 0.0 - 1.0
  passed: boolean       # True if score >= 0.8

  validator_scores:
    document_validator: float
    argument_validator: float
    citation_validator: float
    plagiarism_checker: float
    formatting_validator: float?

  issues:
    critical: int
    high: int
    medium: int
    low: int

  issues_by_type:
    - type: string
      count: int
      severity: string
      locations: string[]

  top_recommendations:
    - priority: int
      description: string
      effort: "quick" | "moderate" | "significant"

  detailed_reports:
    - validator: string
      report: QualityReport
```

## Severity Levels

| Severity | Description | Action |
|----------|-------------|--------|
| Critical | Must fix before submission | Block if --strict |
| High | Should fix | Flag prominently |
| Medium | Consider fixing | Include in recommendations |
| Low | Minor suggestions | Note for polish phase |

## Example

```
User: /quality-check "drafts/paper-draft.md"

Claude:
Running quality checks on paper-draft.md...

[document-validator] ████████ Done (0.92)
[argument-validator] ████████ Done (0.85)
[citation-validator] ████████ Done (0.88)
[plagiarism-checker] ████████ Done (0.94)

══════════════════════════════════════
       QUALITY REPORT SUMMARY
══════════════════════════════════════

Overall Score: 0.90 ✓ PASSED

Issues Found:
  Critical: 0
  High: 3
  Medium: 7
  Low: 12

Top Issues:
1. [HIGH] Missing citation for claim in Section 3.2
2. [HIGH] Figure 4 referenced but not defined
3. [HIGH] Contribution 2 not clearly demonstrated

Recommendations:
1. Add citation to support optimization claim
2. Add Figure 4 or update reference
3. Strengthen results section to support Contribution 2

Full report saved to: quality-reports/paper-draft-report.md
```

## Selective Validation

Run only specific validators:
```
/quality-check "doc.md" --validators document,citation
```

Valid validator names:
- `document` - document-validator
- `argument` - argument-validator
- `citation` - citation-validator
- `plagiarism` - plagiarism-checker
- `formatting` - formatting-validator

## Auto-Fix Mode

```
/quality-check "doc.md" --fix
```

Automatic fixes for:
- Inconsistent terminology
- Minor formatting issues
- Orphan references (removal)
- Capitalization errors

Does NOT auto-fix:
- Content issues
- Logical problems
- Missing citations

## Related Commands

- `/thesis-write` - Runs quality checks automatically
- `/paper-write` - Runs quality checks automatically
- `/paper-revise` - For reviewer-requested changes

## Agent Integration

Coordinates all quality control agents:
- document-validator
- argument-validator
- citation-validator
- plagiarism-checker
- formatting-validator

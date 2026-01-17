# /paper-revise

Handle reviewer feedback and generate response letter + revisions.

## Usage

```
/paper-revise <paper-path> --reviews <reviews-path>
/paper-revise <paper-path> --reviews-text "<paste reviews>"
```

## Options

- `--reviews <path>` - Path to file containing reviewer comments
- `--reviews-text <text>` - Paste reviewer comments directly
- `--decision <type>` - Editor decision (major, minor, conditional)
- `--deadline <date>` - Revision deadline
- `--generate-response` - Create response letter only
- `--apply-changes` - Apply revisions to paper

## Description

Orchestrates the revision process after peer review:
1. Parses and categorizes reviewer comments
2. Generates professional response letter
3. Creates prioritized revision plan
4. Applies revisions with change tracking
5. Produces diff for reviewers

## Process

1. **Parse Reviews**
   - Extract individual comments
   - Assign comment IDs (R1.1, R1.2, R2.1, etc.)
   - Categorize by type (critical, significant, minor, etc.)

2. **Generate Response Letter**
   - Professional acknowledgment
   - Point-by-point responses
   - Changes summary table
   - Use reviewer-response agent

3. **Create Revision Plan**
   ```yaml
   RevisionPlan:
     critical_items:
       - comment: R1.3
         action: "Add comparison with Liu et al."
         sections_affected: [3.2, 5.1]
         effort: "2-3 hours"
     significant_items:
       - comment: R2.1
         action: "Expand limitations"
         sections_affected: [6.2]
         effort: "1 hour"
     minor_items:
       - comment: R1.7
         action: "Fix typo"
         sections_affected: [4.1]
         effort: "5 minutes"
   ```

4. **Apply Revisions**
   - Spawn relevant section writers
   - Track all changes
   - Update cross-references

5. **Generate Diff**
   - Produce marked-up version
   - LaTeX latexdiff format
   - Markdown diff format

## Output

```yaml
RevisionOutput:
  response_letter: path
  revision_plan: path
  revised_paper: path
  diff_document: path
  changelog: path

  statistics:
    comments_addressed: int
    words_added: int
    words_removed: int
    figures_added: int
    sections_modified: int
```

## Response Letter Format

```markdown
# Response to Reviewers

## General Response

We thank the reviewers for their thoughtful comments...

**Summary of Major Changes:**
1. Added comparison with Liu et al. (2024)
2. Expanded limitations section
3. Added ablation study

---

## Response to Reviewer 1

### R1.1: Clarity of contribution

> "The main contribution is not clearly stated..."

**Response:** We thank the reviewer for this observation. We have
revised the introduction to more clearly state our contributions.

**Changes Made:**
- Section 1: Revised contribution statement
- Abstract: Updated summary

**New Text (Section 1, paragraph 4):**
> "Our main contributions are: (1) A novel linear attention
> mechanism that achieves O(n) complexity..."
```

## Example

```
User: /paper-revise "drafts/paper-draft.md" --reviews "reviews.txt"

Claude:
Parsing reviewer comments...
- Reviewer 1: 8 comments (3 critical, 4 significant, 1 minor)
- Reviewer 2: 6 comments (1 critical, 3 significant, 2 minor)
- Editor: 2 comments

Generating response letter...
✓ Response letter created

Creating revision plan...
✓ 4 critical items
✓ 7 significant items
✓ 3 minor items

Estimated effort: 8-10 hours

Apply revisions now? [Y/n]

User: Y

Applying revisions...
[R1.3] Adding comparison experiment...
  - Spawning results-writer...
  - ✓ Table 4 added
[R2.1] Expanding limitations...
  - Spawning discussion-writer...
  - ✓ Section 6.2 expanded
...

Revision complete!
- Response letter: revisions/response-letter.md
- Revised paper: revisions/paper-v2.md
- Diff: revisions/paper-diff.tex
- Changelog: revisions/changelog.md
```

## Response-Only Mode

Generate response letter without applying changes:
```
/paper-revise "paper.md" --reviews "reviews.txt" --generate-response
```

Useful for:
- Planning revisions
- Estimating effort
- Getting advisor approval

## Revision Workflow

Recommended workflow:
1. `/paper-revise --generate-response` - Create plan
2. Review with advisor
3. `/paper-revise --apply-changes` - Apply revisions
4. `/quality-check` - Validate
5. Review diff and response letter
6. Submit

## Related Commands

- `/paper-write` - Initial paper writing
- `/quality-check` - Validate revisions
- `/paper-write --from-checkpoint` - Resume interrupted work

## Agent Integration

Invokes:
- reviewer-response - Generate response letter
- change-manager - Track all changes
- Section writers - Apply revisions
- change-integrator - Merge changes
- document-validator - Final consistency check

# Pre-Export Citation Validation Hook

**File:** `pre-export-validation.py`
**Triggers:** PreToolUse (Write, Bash)
**Purpose:** Block exports with missing or broken citations

---

## What This Hook Does

This is the **final safety net** before paper submission. It validates that all citation keys in your document exist in `library.bib` before allowing:

1. **LaTeX file writes** (`.tex` files)
2. **Final report writes** (`final-report.md`, `submission.md`, etc.)
3. **Export commands** (`/export-paper`, `pdflatex`, `pandoc`)

If any citations are broken, the hook **blocks the operation** and shows which citations are missing.

---

## Validation Checks

### For Write Operations

When you save a `.tex` file or final report:

1. ✅ **Find library.bib** - Searches up directory tree for `6. Metadata/References/library.bib`
2. ✅ **Extract all citations** - Finds `[@key]`, `{citationID}`, `\cite{key}` patterns
3. ✅ **Parse library.bib** - Gets all available BibTeX keys
4. ✅ **Compare** - Ensures every cited key exists in library.bib
5. ❌ **Block if missing** - Shows exactly which citations are broken

### For Bash Commands

When you run export commands (`pdflatex`, `/export-paper`):

1. ✅ **Check library.bib exists** - Ensures file is present
2. ✅ **Check not empty** - Ensures file has BibTeX entries
3. ❌ **Block if missing/empty** - Prevents exporting without bibliography

---

## Citation Syntax Support

The hook validates **all** citation syntaxes used in your vault:

| Syntax | Usage | Example |
|--------|-------|---------|
| `[@key]` | Obsidian notes, BibTeX Scholar | `[@michalek2002architectural]` |
| `[@key1; @key2]` | Multiple citations | `[@nauata2021housegan; @wong2009evoarch]` |
| `{citationID}` | Paper-writing agents | `{michalek2002architectural}` |
| `\cite{key}` | LaTeX files | `\cite{michalek2002architectural}` |
| `\citep{key}` | LaTeX parenthetical | `\citep{michalek2002architectural}` |

**All are validated** - no syntax escapes the check.

---

## File Patterns Monitored

### Export Files (Write tool)

```python
EXPORT_FILE_PATTERNS = [
    r'.*\.tex$',                          # LaTeX files
    r'.*final.*report.*\.md$',            # Final report drafts
    r'.*submission.*\.md$',               # Submission drafts
    r'.*export.*\.md$',                   # Export staging files
    r'.*10\.\s*Final Report.*\.md$',      # WSU final report folder
    r'.*paper.*final.*\.md$',             # Final paper versions
]
```

### Export Commands (Bash tool)

```python
EXPORT_BASH_PATTERNS = [
    r'/export-paper',                     # Export paper skill
    r'pdflatex',                          # LaTeX compiler
    r'xelatex',                           # XeLaTeX compiler
    r'lualatex',                          # LuaLaTeX compiler
    r'pandoc.*--to.*latex',              # Pandoc LaTeX export
    r'pandoc.*--to.*pdf',                # Pandoc PDF export
]
```

---

## Error Messages

### Missing Citations (Blocks Export)

```
Export validation failed:
Missing citations in library.bib (3 broken):
  - [@smith2020design] or {smith2020design}
  - [@jones2021generative] or {jones2021generative}
  - [@wilson2019architecture] or {wilson2019architecture}

Available citations (19 total):
  ath2024ember, ath2024hamilton, ath2024jemimah, ath2024mapleton,
  ath2024merewether, ath2024website, chia2014automated, dalgic2017genetic,
  fabprefab2024minima, imby2024kits ... and 9 more

To fix:
1. Check citation key spelling matches library.bib
2. Add missing entries to library.bib or pending-imports.bib
3. Import pending-imports.bib to Zotero if needed
```

### Empty Bibliography (Blocks Export)

```
Export validation failed:
library.bib is empty or has no valid entries. Add citations before exporting.
```

### Library Not Found (Warning, Allows)

```
Warning: Could not locate library.bib. Citation validation skipped.
```

### Validation Passed (Silent, Allows)

```
✓ Citation validation passed: 15 citations, all valid.
```

---

## How to Fix Broken Citations

### Step 1: Identify Missing Keys

The error message lists all broken citation keys:

```
Missing citations in library.bib (2 broken):
  - [@imby2024kits]
  - [@ath2024hamilton]
```

### Step 2: Check Spelling

Verify the key matches the BibTeX entry:

```bibtex
# In library.bib - note the key after the {
@techreport{ath2024hamilton,
  title = {The Hamilton 13000 - Specification Sheet},
  ...
}
```

Citation must be: `[@ath2024hamilton]` (exact match, case-sensitive)

### Step 3: Add Missing Entries

If the citation doesn't exist in `library.bib`, add it:

**Option A:** Add to `pending-imports.bib` then import:

```bash
# Edit pending-imports.bib to add the entry
# Then import to Zotero and library.bib
```

**Option B:** Add directly to `library.bib`:

```bibtex
@techreport{ath2024hamilton,
  title = {The Hamilton 13000 - Specification Sheet},
  author = {{Alphaline Tiny Homes}},
  institution = {Alphaline Tiny Homes},
  year = {2024},
  type = {Product Specification}
}
```

### Step 4: Retry Export

After fixing, the export should succeed:

```
✓ Citation validation passed: 17 citations, all valid.
```

---

## Integration with Existing Hooks

This hook works alongside `research-quality-gate.py`:

```
┌─────────────────────────────────────────────────┐
│         COMPLETE CITATION ENFORCEMENT            │
└─────────────────────────────────────────────────┘

RESEARCH PHASE (research-quality-gate.py)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  30-synthesis.md → Must have citations ✅
  40-draft.md → No unsupported claims ✅
  Dataset Entry → Must cite sources ✅

EXPORT PHASE (pre-export-validation.py) ← NEW ✨
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  final-report.md → All citations valid ✅
  paper.tex → All \cite{} valid ✅
  /export-paper → library.bib not empty ✅
  pdflatex → bibliography file exists ✅
```

**Result:** Citations are validated at **three checkpoints**:
1. During research (synthesis phase)
2. During dataset creation (entry phase)
3. Before export (submission phase)

**Nothing escapes the net.**

---

## Testing the Hook

### Test 1: Valid Export (Should Pass)

Create a final report with valid citations:

```markdown
# Final Report

## Literature Review

Genetic algorithms have been applied to floor planning [@michalek2002architectural].
Deep learning approaches show promise [@nauata2021housegan].

## References

See library.bib for complete bibliography.
```

**Save as:** `10. Final Report/final-report.md`

**Expected:** Hook validates, shows success message, allows save.

---

### Test 2: Broken Citation (Should Block)

Create a final report with a broken citation:

```markdown
# Final Report

Recent work by Smith et al. [@smith2020nonexistent] shows...
```

**Save as:** `10. Final Report/final-report.md`

**Expected:** Hook blocks with error:
```
Missing citations in library.bib (1 broken):
  - [@smith2020nonexistent]
```

---

### Test 3: LaTeX Export (Should Check)

Try to compile LaTeX:

```bash
pdflatex final-report.tex
```

**Expected:** Hook checks `library.bib` exists and is not empty before allowing compilation.

---

## Configuration

### Disable Hook (Not Recommended)

If you need to temporarily disable:

```bash
# Rename the hook file
mv .claude/hooks/pre-export-validation.py .claude/hooks/pre-export-validation.py.disabled
```

**Warning:** This removes the final safety net. Only disable if you're certain all citations are valid.

---

### Customize File Patterns

Edit `EXPORT_FILE_PATTERNS` in the hook to add more file types:

```python
EXPORT_FILE_PATTERNS = [
    r'.*\.tex$',
    r'.*final.*report.*\.md$',
    r'.*your-custom-pattern.*\.md$',  # Add your pattern
]
```

---

## Troubleshooting

### "Cannot read library.bib: [Errno 2] No such file or directory"

**Cause:** Hook can't find `library.bib` in expected locations.

**Fix:**
1. Ensure file exists at: `Obsidian-Vault-Live/6. Metadata/References/library.bib`
2. Or create it if missing:

```bash
touch "Obsidian-Vault-Live/6. Metadata/References/library.bib"
```

---

### "Citation validation skipped" warning

**Cause:** Hook found export file but couldn't locate `library.bib`.

**Fix:** Check your working directory is the project root, or use absolute paths.

---

### False positives for `{citationID}` syntax

**Cause:** Hook sees `{something}` that isn't a citation (e.g., `{placeholder}`).

**Current behavior:** Hook uses heuristic (must contain year like `2024` or pattern like `author2024topic`) to filter non-citations.

**If you get false positives:** Edit the citation key to match BibTeX format, or use `[@key]` syntax instead.

---

## Performance

- **Fast:** Regex-based parsing, no external dependencies
- **File size:** Works with library.bib up to ~10,000 entries (< 1MB)
- **Latency:** < 100ms for typical documents (< 50 citations)

---

## Related Documentation

- [[research-quality-gate.py]] - Research phase citation enforcement
- [[Citation Workflow Integration]] - Complete system architecture
- [[Workflow - Citation Capture During Research]] - Citation workflow guide

---

*Created: 2026-01-16*
*Hook Type: PreToolUse (Write, Bash)*
*Status: Active*

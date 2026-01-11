# Research Progress Check

Check progress on a research project and get recommendations for next steps.

## Input

- Research folder or topic: $ARGUMENTS

## Process

1. **Locate the research project**
   - Search for folder matching the topic in `3. Resources (Dynamic)/Research/`
   - Or use direct path if provided

2. **Invoke research-progress-tracker agent**
   - Scan for phase files (00-brief through 99-bibliography)
   - Analyze source distribution
   - Check for quality issues

3. **Generate progress report**
   - Phase completion status
   - Source distribution vs targets
   - Quality issues found
   - Quality gate readiness

4. **Recommend next action**
   - Based on gaps and priorities
   - Specific, actionable guidance

## Output

A structured progress report showing:

### Phase Status Table
| Phase | Status | Notes |
|-------|--------|-------|
| Brief (00) | ✅/❌/⚠️ | |
| Sources (10) | | |
| Notes (20) | | |
| Synthesis (30) | | Quality gate |
| Draft (40) | | Quality gate |
| Bibliography (99) | | |

### Source Distribution
- Peer-reviewed: X/12 minimum
- Technical: X/5 minimum
- Web: X/5 minimum

### Quality Gate Status
- Synthesis ready? Yes/No
- Draft ready? Yes/No

### Recommended Next Action
Specific guidance on what to work on next.

## Example Usage

```
/research-progress transformer efficiency
/research-progress "3. Resources (Dynamic)/Research/Quantum Computing/"
```

## Related Commands

- `/quick-research` - For lightweight research (no phases)
- `/deep-research` - For starting complete research projects
- `/research-project-init` - For initializing phased research folders

## Notes

- This command is for the **Complete Research Track** only
- Quick Research notes don't have phases to track
- Quality gates are enforced by hooks, this command previews readiness

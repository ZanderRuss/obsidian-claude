---
tags:
  - content/projects
  - topics/research
  - status/active
type: project
created: 2025-01-10
modified: 2025-01-10
status: active
deadline: 2025-03-15
---

# Example Project - Research Paper

> **This is an example project note.** Delete it once you understand the structure.

## Project Overview

**Goal**: Submit a research paper to [Conference/Journal Name]

**Deadline**: March 15, 2025

**Status**: Active - Literature Review Phase

## Success Criteria

- [ ] Literature review complete (20+ papers)
- [ ] Methodology designed and approved
- [ ] Experiments completed
- [ ] Paper draft written
- [ ] Internal review passed
- [ ] Submitted to venue

## Current Phase

### Phase 1: Literature Review (Current)
- [ ] Search for relevant papers
- [ ] Read and annotate 10 core papers
- [ ] Identify research gap
- [ ] Write related work section draft

### Phase 2: Methodology
- [ ] Design experimental framework
- [ ] Get advisor approval
- [ ] Prepare datasets

### Phase 3: Experiments
- [ ] Run baseline experiments
- [ ] Implement proposed method
- [ ] Ablation studies

### Phase 4: Writing
- [ ] Draft all sections
- [ ] Internal review
- [ ] Revisions
- [ ] Final submission

## Key Resources

- [[Literature Review Notes]] (link to your notes)
- [[Experiment Log]] (link to experiment tracking)
- Research folder: `~/Documents/Research/ProjectName/`

## Meeting Notes

### 2025-01-10 - Kickoff
- Discussed scope with advisor
- Agreed on target venue
- Timeline approved

## Open Questions

- What baseline methods to compare against?
- Which datasets are most appropriate?

## Related

- **Area**: [[Research]] (if you have a research area)
- **Resources**: [[Writing Tips]], [[LaTeX Templates]]

---

## Project Metadata (for Dataview)

```dataview
TABLE deadline, status
FROM "1. Projects"
WHERE file.name = this.file.name
```

---

## How Projects Work

### What Makes Something a Project?

A project has:
1. **A specific outcome** - Something concrete you're trying to achieve
2. **A deadline** - Real or self-imposed
3. **Multiple steps** - Requires planning and tracking

### Project Lifecycle

```
Idea → Active → Completed → Archive
```

### Claude Commands for Projects

- `/summarize-project` - Get an executive summary
- `/extract-todos` - Find all tasks across your vault
- `/thinking-partner` - Work through complex problems

### When to Archive

Move to `4. Archive/` when:
- Project is completed
- Project is cancelled
- Project has been on hold for 6+ months

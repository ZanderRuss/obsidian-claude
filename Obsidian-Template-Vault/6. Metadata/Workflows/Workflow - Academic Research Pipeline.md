---
tags:
  - type/workflow
  - topics/research
  - topics/academic
type: workflow
created: 2025-01-10
modified: 2025-01-10
status: active
---

# Academic Research Pipeline

A comprehensive end-to-end workflow for AI research, paper writing, and code implementation at WSU.

## Pipeline Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        ACADEMIC RESEARCH PIPELINE                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐  │
│  │ IDEATION │ → │ RESEARCH │ → │ SYNTHESIS│ → │ WRITING  │ → │  OUTPUT  │  │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘   └──────────┘  │
│       │              │              │              │              │         │
│  /research-    /lit-search    /lit-review    /paper-draft   /paper-to-     │
│   ideate       /deep-research  /evidence-qa  /paper-review   code          │
│                                                              /export-paper │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

                              TOOL INTEGRATIONS
┌─────────────────────────────────────────────────────────────────────────────┐
│  Zotero MCP        │  PaperQA2         │  Claude Scientific │  OpenDraft   │
│  ─────────────     │  ──────────       │  Writer            │  ──────────  │
│  • Citations       │  • RAG over PDFs  │  ──────────────    │  • Rapid     │
│  • Library search  │  • Evidence QA    │  • IMRaD structure │    drafting  │
│  • Annotations     │  • Contradictions │  • LaTeX export    │  • 19 agents │
│  • BibTeX export   │  • Summaries      │  • Grant proposals │  • Verified  │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Phase 1: Ideation

### Purpose
Generate and refine research hypotheses, identify gaps in literature, and develop research questions.

### Commands
- `/research-ideate` - Socratic exploration of research ideas
- `/research-gap` - Identify gaps in existing literature

### Workflow

1. **Capture Initial Ideas**
   - Record voice memo or quick note to `0. Inbox/`
   - Use `/thinking-partner` for initial exploration

2. **Structured Ideation**
   ```
   /research-ideate "Novel approaches to transformer efficiency"
   ```

3. **Output**: Research Ideation Note
   - Problem statement
   - Research questions (3-5)
   - Hypotheses
   - Potential contributions
   - Related work directions

### Templates
- [[Template - Research Ideation]]

---

## Phase 2: Literature Discovery

### Purpose
Systematically discover and organize relevant papers, build comprehensive literature corpus.

### Commands
- `/lit-search <topic>` - Semantic search across Zotero + web
- `/deep-research <topic>` - Comprehensive multi-source investigation
- `/web-clip <url>` - Archive web resources

### Tool Stack

```
                    ┌─────────────────┐
                    │  /lit-search    │
                    └────────┬────────┘
                             │
         ┌───────────────────┼───────────────────┐
         ▼                   ▼                   ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│   Zotero MCP    │ │ Semantic Scholar│ │   Web Search    │
│   (Your lib)    │ │   (Discovery)   │ │   (Perplexity)  │
└────────┬────────┘ └────────┬────────┘ └────────┬────────┘
         │                   │                   │
         └───────────────────┼───────────────────┘
                             ▼
                    ┌─────────────────┐
                    │  Literature     │
                    │  Collection     │
                    │  (Obsidian)     │
                    └─────────────────┘
```

### Workflow

1. **Search Your Library First**
   ```
   Use Zotero MCP: "Search my library for attention mechanisms in vision transformers"
   ```

2. **Discover New Papers**
   ```
   /deep-research "state-of-the-art efficient attention mechanisms 2024"
   ```

3. **Import to Zotero**
   - Add papers to Zotero with proper metadata
   - Tag with project identifier
   - Add to project collection

4. **Create Literature Notes**
   - One note per paper in `3. Resources (Dynamic)/Literature/`
   - Link to Zotero item
   - Extract key claims with page references

### Output Structure
```
3. Resources (Dynamic)/
└── Literature/
    └── [Project Name]/
        ├── Paper - Author2024 - Title.md
        ├── Paper - Author2023 - Related.md
        └── MOC - Literature Review.md
```

---

## Phase 3: Evidence Synthesis

### Purpose
Extract evidence, synthesize findings, identify patterns and contradictions across literature.

### Commands
- `/evidence-qa <question>` - Query your literature corpus
- `/lit-review <topic>` - Generate structured literature review
- `/contradiction-check` - Find conflicting claims

### Tool Stack: PaperQA2

```python
# Evidence-based Q&A over your PDFs
from paperqa import Settings, ask

answer = ask(
    "What are the main limitations of self-attention in long sequences?",
    settings=Settings(
        paper_directory="path/to/pdfs",
        answer_max_sources=8
    )
)
```

### Workflow

1. **Formulate Evidence Questions**
   - What methods achieve state-of-the-art results?
   - What are reported limitations?
   - What datasets are commonly used?
   - What metrics are standard?

2. **Run Evidence Queries**
   ```
   /evidence-qa "What computational complexity does linear attention achieve?"
   ```

3. **Synthesize into Literature Review**
   ```
   /lit-review "Efficient Attention Mechanisms"
   ```

4. **Check for Contradictions**
   ```
   /contradiction-check "Claims about attention scalability"
   ```

### Output
- Evidence synthesis notes with citations
- Contradiction report
- Literature review draft with proper citations

---

## Phase 4: Paper Drafting

### Purpose
Transform research findings into structured academic manuscript.

### Commands
- `/paper-outline <title>` - Generate paper structure
- `/paper-draft <section>` - Draft specific sections
- `/paper-figures` - Generate figure descriptions/code

### Paper Structure (IMRaD + AI)

```
1. Title & Abstract
2. Introduction
   - Problem statement
   - Research gap
   - Contributions
3. Related Work
4. Methodology
   - Problem formulation
   - Proposed approach
   - Implementation details
5. Experiments
   - Datasets
   - Baselines
   - Results
   - Ablation studies
6. Discussion
7. Conclusion
8. References
```

### Workflow

1. **Generate Outline**
   ```
   /paper-outline "Efficient Linear Attention for Long-Range Dependencies"
   ```

2. **Draft Sections Iteratively**
   ```
   /paper-draft introduction
   /paper-draft methodology
   /paper-draft experiments
   ```

3. **Insert Citations**
   - Pull from Zotero via MCP
   - Verify all citations exist
   - Format for target venue

### Output Location
```
1. Projects/
└── [Paper Title]/
    ├── Paper - Draft v1.md
    ├── Figures/
    ├── Data/
    └── Notes/
```

---

## Phase 5: Review & Polish

### Purpose
Simulate peer review, improve clarity, ensure academic standards.

### Commands
- `/paper-review <section>` - Simulate peer review
- `/paper-polish` - Grammar, style, consistency
- `/check-claims` - Verify all claims have citations
- `/bias-check` - Check for overclaiming/hedging

### Review Checklist

**Technical Review**
- [ ] All claims supported by evidence or citations
- [ ] Methodology clearly reproducible
- [ ] Experimental setup complete
- [ ] Statistical significance reported
- [ ] Limitations acknowledged

**Writing Quality**
- [ ] Consistent terminology
- [ ] Proper verb tense (methods: past, findings: present)
- [ ] Strong topic sentences
- [ ] Logical flow between sections

**Academic Standards**
- [ ] All figures referenced in text
- [ ] Tables properly formatted
- [ ] Citations complete and accurate
- [ ] Venue style guide followed

### Workflow

1. **Self-Review**
   ```
   /paper-review full
   ```

2. **Address Feedback**
   - Create revision notes
   - Track changes made

3. **Polish**
   ```
   /paper-polish
   ```

4. **Final Checks**
   ```
   /check-claims
   /bias-check
   ```

---

## Phase 6: Export & Submission

### Purpose
Export to submission-ready formats, prepare supplementary materials.

### Commands
- `/export-paper latex` - Export to LaTeX
- `/export-paper pdf` - Generate PDF
- `/export-paper arxiv` - Prepare arXiv submission
- `/paper-to-code` - Extract implementation from paper

### Export Formats

| Format | Command | Use Case |
|--------|---------|----------|
| LaTeX | `/export-paper latex` | Conference/journal submission |
| PDF | `/export-paper pdf` | Preprint, sharing |
| Word | `/export-paper word` | Collaborator edits |
| arXiv | `/export-paper arxiv` | Preprint server |

### Code Extraction

When your paper includes novel methods:

```
/paper-to-code methodology

Output:
- Implementation skeleton
- Key algorithms
- Experiment scripts
- Requirements.txt
```

---

## Folder Structure

```
Obsidian-Vault/
├── 1. Projects/
│   └── [Paper Title]/
│       ├── 00-Project-Overview.md
│       ├── 01-Research-Questions.md
│       ├── 02-Literature-Review.md
│       ├── 03-Methodology.md
│       ├── 04-Experiments.md
│       ├── 05-Draft-v1.md
│       ├── Figures/
│       ├── Data/
│       ├── Code/
│       └── Revisions/
│
├── 3. Resources (Dynamic)/
│   └── Literature/
│       └── [Project]/
│           ├── Paper - *.md (literature notes)
│           └── MOC - Literature.md
│
└── 6. Metadata/
    └── Templates/
        ├── Template - Paper Project.md
        ├── Template - Literature Note.md
        ├── Template - Research Ideation.md
        └── Template - Experiment Log.md
```

---

## Tool Installation

### Required

1. **Zotero 7** with Local API enabled
   ```bash
   # Install Zotero MCP
   pip install git+https://github.com/54yyyu/zotero-mcp.git
   zotero-mcp setup
   ```

2. **PaperQA2** for evidence Q&A
   ```bash
   pip install paper-qa>=5
   ```

3. **Claude Scientific Writer** (optional)
   ```bash
   pip install scientific-writer
   ```

### MCP Configuration

Add to `.claude/mcp.json`:

```json
{
  "mcpServers": {
    "obsidian": { ... },
    "zotero": {
      "command": "zotero-mcp",
      "env": {
        "ZOTERO_LOCAL": "true"
      }
    }
  }
}
```

---

## Daily Research Workflow

### Morning Session (Deep Work)
1. Review yesterday's progress
2. Run `/evidence-qa` for open questions
3. Write/revise one section

### Afternoon Session (Discovery)
1. `/lit-search` for new papers
2. Read and annotate in Zotero
3. Create literature notes

### Evening (Capture)
1. `/daily-review` for research journal
2. Capture new ideas to inbox
3. Update project status

---

## Quick Reference

| Stage | Command | Output |
|-------|---------|--------|
| Ideate | `/research-ideate` | Research questions |
| Search | `/lit-search` | Paper collection |
| Evidence | `/evidence-qa` | Grounded answers |
| Review | `/lit-review` | Literature review |
| Outline | `/paper-outline` | Paper structure |
| Draft | `/paper-draft` | Section drafts |
| Review | `/paper-review` | Feedback |
| Polish | `/paper-polish` | Clean manuscript |
| Export | `/export-paper` | LaTeX/PDF |
| Code | `/paper-to-code` | Implementation |

---

## Related Resources

- [[Workflow - Research Automation]]
- [[Workflow - Voice Memo Automation]]
- [[Template - Paper Project]]
- [[Template - Literature Note]]
- [[MOC - Research Methods]]

# Research Team Agents

This directory contains specialized research agents for conducting comprehensive, multi-phase research projects using the Open Deep Research methodology.

## Two-Track Research System

This team supports **two research workflows**:

| Track | Purpose | Sources | Output | Quality Gates |
|-------|---------|---------|--------|---------------|
| **Quick Research** | Exploration, background research | 5-10 | Single file | None |
| **Complete Research** | PhD-grade, publications, thesis | 20+ (12 peer-reviewed) | 6-phase folder | Enforced via hooks |

**Choose Quick when:** Time-constrained, exploring ideas, background research
**Choose Complete when:** Academic publications, systematic reviews, thesis work

## Agent Categories

### 🔍 Research Orchestration

| Agent | Purpose | When to Use |
|-------|---------|-------------|
| **research-orchestrator** | Coordinate full research workflows | Complex multi-phase research projects |
| **research-coordinator** | Strategic task allocation | Projects requiring multiple specialists |
| **research-brief-generator** | Create structured research plans | Transform queries into actionable briefs |
| **research-progress-tracker** | Monitor research phase completion, identify gaps | Check progress on Complete Research track |
| **query-clarifier** | Analyze and refine queries | Ambiguous or overly broad questions |

### 📚 Information Gathering

| Agent | Purpose | When to Use |
|-------|---------|-------------|
| **academic-researcher** | Search academic databases | Peer-reviewed papers, scholarly sources |
| **technical-researcher** | Analyze technical implementations | Code repos, API docs, GitHub projects |
| **data-analyst** | Quantitative analysis | Statistical data, trends, metrics |
| **fact-checker** | Verify claims and sources | Citation validation, misinformation detection |

### 📊 Analysis & Synthesis

| Agent | Purpose | When to Use |
|-------|---------|-------------|
| **research-synthesizer** | Consolidate multi-source findings | Merge outputs from multiple researchers |
| **literature-reviewer** | Critical literature analysis | Research synthesis, meta-analysis |
| **citation-manager** | BibTeX and citation verification | Reference management, citation accuracy |
| **research-methodologist** | Methodology design | Experimental design review |

### 📝 Content Production

| Agent | Purpose | When to Use |
|-------|---------|-------------|
| **report-generator** | Create structured reports | Final research deliverables |
| **paper-editor** | Academic writing polish | Style, grammar, consistency |
| **experiment-designer** | ML experiment planning | Ablation studies, experimental design |

## Research Workflows

### Quick Research Track
```
/quick-research → WebSearch → research-synthesizer → Single Output File
```
- **No agents required** - uses built-in WebSearch and basic synthesis
- **Output:** `3. Resources (Dynamic)/Research/Quick Research - [Topic].md`
- **Duration:** ~15-30 minutes equivalent
- **Quality gates:** None

### Complete Research Track
```
/research-project-init → 6-Phase Pipeline:
  Phase 0: research-brief-generator (00-brief.md)
  Phase 1: academic-researcher + technical-researcher (10-sources.md)
  Phase 2: research-synthesizer (20-notes.md)
  Phase 3: research-synthesizer + fact-checker (30-synthesis.md) **Quality Gate**
  Phase 4: report-generator (40-draft.md) **Quality Gate**
  Phase 5: citation-manager (99-bibliography.md)

/research-progress → research-progress-tracker → Progress Report
```

### Orchestrated Research (Full Automation)
```
research-orchestrator coordinates:
  Phase 1: query-clarifier
  Phase 2: research-brief-generator
  Phase 3: research-coordinator (strategy)
  Phase 4: [parallel specialists]
  Phase 5: research-synthesizer
  Phase 6: fact-checker (quality gate)
  Phase 7: report-generator
```

### Academic Literature Review
```
academic-researcher → literature-reviewer → citation-manager → paper-editor
```

### Technical Investigation
```
technical-researcher → data-analyst → research-synthesizer → report-generator
```

## Agent Selection Guide

### Start with `/quick-research` when:
- Exploring a new topic casually
- Time-constrained (<1 hour)
- Background research for a meeting
- Don't need citations or rigor

### Use `/research-project-init` (Complete Track) when:
- Academic publications or thesis
- Need citations and bibliography
- Systematic literature review required
- PhD-level rigor expected

### Choose research-orchestrator when:
- Full automation of Complete Track desired
- Query requires multiple research phases
- Complex topic requiring coordination
- Want structured workflow management with quality gates

### Choose research-coordinator when:
- Need strategic task allocation
- Multiple specialists working in parallel
- Clear phases but custom workflow
- Manual control over orchestration

### Choose research-progress-tracker when:
- Mid-project progress check needed
- Identifying coverage gaps
- Source distribution analysis
- Quality issue detection

### Choose individual specialists when:
- Single-phase research
- Specific domain expertise needed
- Quick targeted investigation
- Manual workflow assembly

## Best Practices

1. **Choose the Right Track**
   - Start with Quick Research for exploration
   - Upgrade to Complete Research if you need citations
   - Use `/research-progress` to check Complete Track progress

2. **Start Broad, Then Narrow**
   - Use `query-clarifier` for vague queries
   - Use `research-brief-generator` to structure investigation
   - Deploy specialists for focused execution

3. **Leverage Parallel Research**
   - Use `research-coordinator` to run multiple specialists concurrently
   - Synthesize with `research-synthesizer` before reporting

4. **Quality Gates Are Automatic**
   - Complete Track enforces quality via hooks
   - `30-synthesis.md` requires citations (blocks saves with `[citation needed]`)
   - `40-draft.md` requires fact-checking (blocks unsupported claims)
   - Save as WIP filename to bypass gates if needed

5. **Maintain Quality**
   - Use `fact-checker` for claim verification
   - Use `citation-manager` for reference accuracy
   - Use `paper-editor` for final polish

6. **Document Workflow**
   - Each orchestrator uses TodoWrite for progress tracking
   - Maintain research state between phases
   - Use structured JSON for inter-agent communication

## Quality Gates

The Complete Research Track enforces quality automatically via hooks:

| File | Quality Check | Enforcement |
|------|---------------|-------------|
| `30-synthesis.md` | Must have citations, no `[citation needed]` markers | Hook blocks saves |
| `40-draft.md` | No `[unsupported]` or `[unverified]` claims | Hook blocks saves |
| All phases | Proper frontmatter and linking | Obsidian markdown hook |

**Bypass mechanism:** Save as different filename (e.g., `30-synthesis-WIP.md`) to work on drafts

## Integration with Parent Project

These agents integrate with the Obsidian vault workflows defined in the root [CLAUDE.md](../../../CLAUDE.md):

### Research Commands (14 Total)

#### Quick Research & Exploration (3 commands)

| Command | Track | Purpose | Agents Used |
|---------|-------|---------|-------------|
| `/quick-research` | Quick | 5-10 source rapid investigation | Built-in WebSearch, basic synthesis |
| `/research-assistant` | Both | General research assistance | Context-dependent agent selection |
| `/research-ideate` | Both | Socratic research exploration | `query-clarifier`, `research-brief-generator` |

#### Complete Research Workflow (5 commands)

| Command | Track | Purpose | Agents Used |
|---------|-------|---------|-------------|
| `/research-project-init` | Complete | Create 6-phase folder structure | Template system, folder creation |
| `/research-progress` | Complete | Check progress, identify gaps | `research-progress-tracker` |
| `/deep-research` | Complete | Comprehensive multi-source investigation | `research-orchestrator`, all specialists |
| `/lit-search` | Complete | Literature search (Zotero + web) | `academic-researcher`, Zotero MCP |
| `/evidence-qa` | Complete | Evidence-grounded Q&A over PDFs | `fact-checker`, `academic-researcher` |

#### Academic Paper Writing (6 commands)

| Command | Track | Purpose | Agents Used |
|---------|-------|---------|-------------|
| `/lit-review` | Complete | Generate structured literature review | `literature-reviewer`, `citation-manager` |
| `/paper-outline` | Complete | Create paper structure for venue | `research-brief-generator`, venue-templates skill |
| `/paper-draft` | Complete | Draft specific paper sections | `report-generator`, `paper-editor` |
| `/paper-review` | Complete | Simulate peer review feedback | `literature-reviewer`, `research-methodologist` |
| `/paper-polish` | Complete | Grammar, style, consistency | `paper-editor`, scientific-writing skill |
| `/export-paper` | Complete | Export to LaTeX/PDF/Word | Template conversion, formatting |

### Research Skills (7 Total)

These skills provide specialized capabilities that complement the research agents:

| Skill | Purpose | Key Features | Used By |
|-------|---------|--------------|---------|
| `citation-management` | Find papers, create citations | Google Scholar, PubMed search, DOI → BibTeX | `academic-researcher`, `citation-manager` |
| `scientific-writing` | Write academic manuscripts | IMRAD structure, APA/AMA/Vancouver citations | `paper-editor`, `report-generator` |
| `literature-review` | Systematic literature reviews | Multiple databases, PRISMA/CONSORT compliance | `literature-reviewer` |
| `scientific-brainstorming` | Research ideation | Hypothesis generation, methodology design | `research-brief-generator` |
| `scientific-critical-thinking` | Evaluate research rigor | GRADE, Cochrane ROB assessment | `research-methodologist`, `fact-checker` |
| `venue-templates` | Journal/conference formatting | Nature, Science, IEEE, NeurIPS, ACM templates | `/paper-outline`, `/export-paper` |
| `scientific-slides` | Research presentations | PowerPoint, LaTeX Beamer templates | Presentation creation |

### Quality Enforcement: Hooks (2 Total)

Hooks automatically enforce quality standards for Complete Research track:

| Hook | File Location | Trigger | Purpose | Enforcement |
|------|--------------|---------|---------|-------------|
| `obsidian-markdown.py` | [.claude/hooks/](../../../.claude/hooks/obsidian-markdown.py) | PreToolUse (Write) | Convert markdown to Obsidian format | Applies to all vault paths |
| `research-quality-gate.py` | [.claude/hooks/](../../../.claude/hooks/research-quality-gate.py) | PreToolUse (Write) | Enforce citation and fact-checking | **Blocks saves** with violations |

#### Quality Gate Rules (research-quality-gate.py)

**30-synthesis.md** (Phase 3):

- ✅ Must have citations: `[@key]`, `(Author, 2024)`, `[1]`, or `[[Paper - ...]]`
- ❌ Blocks saves containing `[citation needed]`, `[needs citation]`, `[cite]`, or `[source?]`

**40-draft.md** (Phase 4):

- ✅ All claims must be supported (synthesis must pass)
- ❌ Blocks saves containing `[unsupported]`, `[unverified]`, or `[needs verification]`

**Bypass mechanism:** Save with WIP filename (e.g., `30-synthesis-WIP.md`) to work on drafts without quality gate enforcement

### Template System (10 Templates)

#### Complete Research Track: 6-Phase Templates

Located in [Obsidian-Template-Vault/6. Metadata/Templates/Research/](../../../Obsidian-Template-Vault/6.%20Metadata/Templates/Research/)

| Template | Phase | Purpose | Agents Used | Quality Gate |
|----------|-------|---------|-------------|--------------|
| `Template - Research Brief (00)` | Phase 0 | Research questions, scope, success criteria | `research-brief-generator`, `query-clarifier` | None |
| `Template - Research Sources (10)` | Phase 1 | Source tracking with CRAAP scoring | `academic-researcher`, `technical-researcher` | None |
| `Template - Research Notes (20)` | Phase 2 | Structured note-taking from sources | `research-synthesizer` | None |
| `Template - Research Synthesis (30)` | Phase 3 | Cross-source synthesis with citations | `research-synthesizer`, `fact-checker` | **Yes** (citations required) |
| `Template - Research Draft (40)` | Phase 4 | Publication-ready draft output | `report-generator`, `paper-editor` | **Yes** (no unsupported claims) |
| `Template - Research Bibliography (99)` | Phase 5 | Formatted bibliography (BibTeX/APA/AMA) | `citation-manager` | None |

#### Supporting Templates (4 Templates)

| Template | Purpose | Enhanced Features | Agents Used |
|----------|---------|-------------------|-------------|
| `Template - Quick Research` | Single-file quick research output | Source type tracking, follow-up suggestions | WebSearch, basic synthesis |
| `Template - Research Note` | Individual research notes | **Enhanced**: CRAAP scoring, source type tracking | Used by all research agents |
| `Template - Literature Note` | Paper/article analysis | **Enhanced**: Quality indicators, evidence strength | `literature-reviewer`, `academic-researcher` |
| `Template - Paper Project` | Paper writing project management | Phase tracking, venue integration | Paper writing agents |

### Research Pipeline Integration

The research team supports complete end-to-end academic workflows:

```
Research Ideation → Literature Search → Evidence Gathering → Synthesis → Writing → Review → Export
        ↓                    ↓                 ↓                ↓            ↓         ↓        ↓
 /research-ideate      /lit-search       /evidence-qa    /deep-research   /paper-  /paper-  /export-
 query-clarifier       academic-         fact-checker    research-        draft    review   paper
 research-brief-       researcher        data-analyst    synthesizer      paper-   research- citation-
 generator             citation-                         literature-      editor   method-  manager
                       manager                           reviewer                  ologist
```

### MCP Server Integration

| MCP Server | Tools Available | Configuration | Used By |
|------------|-----------------|---------------|---------|
| **Obsidian** | File read/write, semantic search, template execution | [.claude/mcp.json](.claude/mcp.json.example) | All agents (note creation) |
| **Zotero** | Semantic search, annotations, item metadata, BibTeX | [.claude/mcp.json](.claude/mcp.json.example) | `academic-researcher`, `citation-manager`, `literature-reviewer` |
| **Context7** (optional) | Library documentation search | Via MCP plugin | `technical-researcher` |
| **arXiv** (optional) | Paper search, download, local storage | [Advanced Features](../../../Obsidian-Template-Vault/6.%20Metadata/Reference/Advanced%20Research%20Features.md) | `academic-researcher` (optional) |

### External Tool Integration

| Tool/Service | Capability | How Accessed | Used By |
|--------------|------------|--------------|---------|
| **Google Scholar** | Academic paper search | `citation-management` skill | `/lit-search`, `academic-researcher` |
| **PubMed** | Medical/biomedical paper search | `citation-management` skill | `/lit-search`, `literature-reviewer` |
| **arXiv** | Preprint search and download | WebSearch or optional arXiv MCP | `academic-researcher` |
| **WebSearch** | Real-time web information | Built-in Claude capability | All research agents, `/quick-research` |
| **Obsidian Local REST API** | Direct vault access | Plugin (port 27124 HTTPS) | All agents via Obsidian MCP |

### Data Flow Example: Complete Research Project

```
1. User: /research-project-init "Transformer Efficiency"
   → Creates folder: 3. Resources (Dynamic)/Research/Transformer Efficiency/
   → Generates 6 phase files from templates

2. User: /deep-research "Transformer Efficiency"
   → research-orchestrator coordinates workflow
   → Phase 0: research-brief-generator → 00-brief.md
   → Phase 1: academic-researcher + technical-researcher → 10-sources.md
   → Phase 2: research-synthesizer → 20-notes.md
   → Phase 3: research-synthesizer + fact-checker → 30-synthesis.md
       ⚠️  Quality Gate: Blocks if citations missing
   → Phase 4: report-generator + paper-editor → 40-draft.md
       ⚠️  Quality Gate: Blocks if unsupported claims found
   → Phase 5: citation-manager → 99-bibliography.md

3. User: /research-progress "Transformer Efficiency"
   → research-progress-tracker scans folder
   → Reports: Phase completion, source distribution, quality issues

4. User: /paper-draft "methodology section"
   → paper-editor + research-methodologist
   → Uses 30-synthesis.md and 10-sources.md as context
   → Outputs structured methodology with citations

5. User: /paper-review
   → Simulates peer review feedback
   → Checks methodology, evidence, writing quality

6. User: /export-paper "IEEE format"
   → Converts to IEEE LaTeX template
   → Formats bibliography
   → Generates submission-ready PDF
```

## Model Assignments

- **research-orchestrator**: Opus (complex coordination)
- **Most specialists**: Sonnet (balanced performance)
- **Check individual agent files** for specific model assignments

## Directory Structure

```
research-team/
├── README.md                          # This file
├── academic-researcher.md             # Academic database searching
├── citation-manager.md                # Citation verification & BibTeX
├── data-analyst.md                    # Quantitative analysis
├── experiment-designer.md             # ML experiment design
├── fact-checker.md                    # Claim verification
├── literature-reviewer.md             # Literature analysis
├── paper-editor.md                    # Academic writing polish
├── query-clarifier.md                 # Query refinement
├── report-generator.md                # Structured report creation
├── research-brief-generator.md        # Research brief creation
├── research-coordinator.md            # Task coordination
├── research-methodologist.md          # Methodology review
├── research-orchestrator.md           # Full workflow orchestration
├── research-progress-tracker.md       # Progress monitoring & gap analysis
├── research-synthesizer.md            # Cross-source synthesis
└── technical-researcher.md            # Technical implementation research
```

## Quick Reference

| I want to... | Use this command/agent |
|--------------|------------------------|
| **Quick exploration (5-10 sources)** | `/quick-research [topic]` |
| **Start Complete Research project** | `/research-project-init [topic]` |
| **Check research progress** | `/research-progress [folder]` or `research-progress-tracker` |
| Research a complex topic end-to-end | `research-orchestrator` |
| Find academic papers | `academic-researcher` |
| Analyze GitHub repos/code | `technical-researcher` |
| Get statistical insights | `data-analyst` |
| Verify claims and sources | `fact-checker` |
| Synthesize multiple sources | `research-synthesizer` |
| Create final research report | `report-generator` |
| Polish academic writing | `paper-editor` |
| Manage citations | `citation-manager` |
| Review methodology | `research-methodologist` |
| Design ML experiments | `experiment-designer` |
| Clarify vague research questions | `query-clarifier` |
| Create structured research plan | `research-brief-generator` |

## Contributing

When adding new research agents:

1. Follow the YAML frontmatter structure (name, tools, model, description)
2. Include usage examples in the description
3. Specify model: sonnet/opus/haiku based on complexity
4. Define clear integration points with other agents
5. Update this README.md with the new agent
6. Document in the parent project's CLAUDE.md if user-facing
7. Add to appropriate category (Orchestration, Gathering, Analysis, or Production)
8. Update agent count in summary below

## Summary

This research team provides a comprehensive academic research infrastructure:

### Core Capabilities

- **16 specialized agents** across 4 categories (Orchestration, Gathering, Analysis, Production)
- **14 research commands** covering exploration, complete research, and paper writing
- **7 research skills** for citation management, writing, and critical thinking
- **2 automated hooks** for quality enforcement (Complete Track only)
- **10 templates** (6-phase Complete Track + 4 supporting templates)
- **2 research tracks** (Quick for exploration, Complete for publications)
- **Integration with** Zotero MCP, Obsidian MCP, citation tools, and academic databases

### Agent Count by Category

| Category | Agents | Purpose |
|----------|--------|---------|
| 🔍 Orchestration | 5 | Workflow coordination and planning |
| 📚 Gathering | 4 | Information collection from diverse sources |
| 📊 Analysis | 4 | Synthesis, verification, and methodology |
| 📝 Production | 3 | Report generation and writing polish |
| **Total** | **16** | **Complete research lifecycle coverage** |

### Research Commands by Category

| Category | Commands | Example Commands |
|----------|----------|------------------|
| Quick & Exploration | 3 | `/quick-research`, `/research-assistant`, `/research-ideate` |
| Complete Research | 5 | `/research-project-init`, `/deep-research`, `/lit-search` |
| Paper Writing | 6 | `/paper-outline`, `/paper-draft`, `/paper-review`, `/export-paper` |
| **Total** | **14** | **End-to-end research workflow** |

### Supporting Infrastructure

| Component | Count | Description |
|-----------|-------|-------------|
| Research Skills | 7 | `citation-management`, `scientific-writing`, `literature-review`, etc. |
| Quality Hooks | 2 | `obsidian-markdown.py`, `research-quality-gate.py` |
| Phase Templates | 6 | Brief (00) → Sources (10) → Notes (20) → Synthesis (30) → Draft (40) → Bibliography (99) |
| Supporting Templates | 4 | Quick Research, Research Note, Literature Note, Paper Project |
| **Total Templates** | **10** | **Structured research outputs** |

### Research Output Locations

- **Quick Research**: `3. Resources (Dynamic)/Research/Quick Research - [Topic].md`
- **Complete Research**: `3. Resources (Dynamic)/Research/[Topic]/` (6-phase folder structure)
- **Progress Reports**: Generated on-demand by `research-progress-tracker`
- **Paper Outputs**: LaTeX, PDF, Word formats via `/export-paper`

---

**Note**: This file is for human navigation and documentation. Agents do not automatically read this file - they read their individual definition files (e.g., `research-orchestrator.md`).

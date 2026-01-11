# Research Team Agents

This directory contains specialized research agents for conducting comprehensive, multi-phase research projects using the Open Deep Research methodology.

## Agent Categories

### 🔍 Research Orchestration

| Agent | Purpose | When to Use |
|-------|---------|-------------|
| **research-orchestrator** | Coordinate full research workflows | Complex multi-phase research projects |
| **research-coordinator** | Strategic task allocation | Projects requiring multiple specialists |
| **research-brief-generator** | Create structured research plans | Transform queries into actionable briefs |
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

### Basic Research Flow
```
query-clarifier → research-brief-generator → [specialists] → research-synthesizer → report-generator
```

### Academic Research
```
academic-researcher → literature-reviewer → citation-manager → paper-editor
```

### Technical Investigation
```
technical-researcher → data-analyst → research-synthesizer → report-generator
```

### Comprehensive Research (Orchestrated)
```
research-orchestrator coordinates:
  Phase 1: query-clarifier
  Phase 2: research-brief-generator
  Phase 3: research-coordinator (strategy)
  Phase 4: [parallel specialists]
  Phase 5: research-synthesizer
  Phase 6: report-generator
```

## Agent Selection Guide

### Choose research-orchestrator when:
- Query requires multiple research phases
- Need quality gates between stages
- Complex topic requiring coordination
- Want structured workflow management

### Choose research-coordinator when:
- Need strategic task allocation
- Multiple specialists working in parallel
- Clear phases but custom workflow

### Choose individual specialists when:
- Single-phase research
- Specific domain expertise needed
- Quick targeted investigation

## Best Practices

1. **Start Broad, Then Narrow**
   - Use `query-clarifier` for vague queries
   - Use `research-brief-generator` to structure investigation
   - Deploy specialists for focused execution

2. **Leverage Parallel Research**
   - Use `research-coordinator` to run multiple specialists concurrently
   - Synthesize with `research-synthesizer` before reporting

3. **Maintain Quality**
   - Use `fact-checker` for claim verification
   - Use `citation-manager` for reference accuracy
   - Use `paper-editor` for final polish

4. **Document Workflow**
   - Each orchestrator uses TodoWrite for progress tracking
   - Maintain research state between phases
   - Use structured JSON for inter-agent communication

## Integration with Parent Project

These agents integrate with the Obsidian vault workflows defined in the root CLAUDE.md:

- **Skills**: `/research-assistant`, `/deep-research`, `/evidence-qa`, `/lit-search`
- **Academic Pipeline**: Research ideation → Literature → Evidence → Draft → Review
- **Zotero MCP**: Semantic search and annotation extraction
- **Citation Tools**: Google Scholar/PubMed search via citation-management skill

## Model Assignments

- **research-orchestrator**: Opus (complex coordination)
- **Most specialists**: Sonnet (balanced performance)
- **Check individual agent files** for specific model assignments

## Directory Structure

```
research-team/
├── CLAUDE.md                          # This file
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
├── research-synthesizer.md            # Cross-source synthesis
└── technical-researcher.md            # Technical implementation research
```

## Quick Reference

| I want to... | Use this agent |
|--------------|----------------|
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

## Contributing

When adding new research agents:

1. Follow the YAML frontmatter structure (name, tools, model, description)
2. Include usage examples in the description
3. Specify model: sonnet/opus/haiku based on complexity
4. Define clear integration points with other agents
5. Update this CLAUDE.md with the new agent
6. Document in the parent project's CLAUDE.md if user-facing

---

**Note**: This file is for human navigation and documentation. Agents do not automatically read this file - they read their individual definition files (e.g., `research-orchestrator.md`).

# Paper Writing Agent Team

**Version:** 2.0.0
**Created:** 2026-01-15
**Purpose:** Multi-agent system for PhD-level academic writing

---

## Overview

The Paper Writing Team is a hierarchical multi-agent system designed to produce publication-quality academic documents, from conference papers to full PhD theses. The system uses **domain-agnostic prompts** to work across all academic fields.

### Key Capabilities

- **Scale**: From 8-page papers to 90,000+ word theses
- **Domain-Agnostic**: Works for ML, humanities, social sciences, natural sciences, and interdisciplinary research
- **Quality-Controlled**: Automated quality gates at every level
- **Context-Managed**: Hierarchical summarization prevents context overflow
- **Checkpointed**: Resume from any point after interruption

---

## Architecture

```
                    ┌─────────────────────────────────────────────────┐
                    │           THESIS ORCHESTRATOR (Opus)            │
                    │    Coordinates entire thesis writing process    │
                    └────────────────────┬────────────────────────────┘
                                         │
         ┌───────────────────────────────┼───────────────────────────────┐
         │                               │                               │
         ▼                               ▼                               ▼
┌─────────────────┐           ┌─────────────────┐           ┌─────────────────┐
│ CHAPTER COORD.  │           │ CHAPTER COORD.  │           │ CHAPTER COORD.  │
│   (Chapter 1)   │           │   (Chapter 2)   │    ...    │   (Chapter N)   │
└────────┬────────┘           └────────┬────────┘           └────────┬────────┘
         │                             │                             │
    ┌────┴────┐                   ┌────┴────┐                   ┌────┴────┐
    ▼         ▼                   ▼         ▼                   ▼         ▼
┌───────┐ ┌───────┐          ┌───────┐ ┌───────┐          ┌───────┐ ┌───────┐
│SECTION│ │SECTION│          │SECTION│ │SECTION│          │SECTION│ │SECTION│
│WRITER │ │WRITER │          │WRITER │ │WRITER │          │WRITER │ │WRITER │
└───────┘ └───────┘          └───────┘ └───────┘          └───────┘ └───────┘

                    ┌─────────────────────────────────────────────────┐
                    │           QUALITY CONTROL LAYER                  │
                    │  document-validator │ argument-validator │       │
                    │  citation-validator │ plagiarism-checker │       │
                    └─────────────────────────────────────────────────┘

                    ┌─────────────────────────────────────────────────┐
                    │           REVISION LAYER                         │
                    │  reviewer-response │ change-manager │            │
                    │  change-integrator │                             │
                    └─────────────────────────────────────────────────┘
```

---

## Agent Registry

### Layer 0: Prompt Quality

| Agent | Model | Purpose | Status |
|-------|-------|---------|--------|
| **prompt-reviewer** | opus | Validates agent prompts for domain-agnosticism | ✅ Ready |

### Layer 1: Orchestration

| Agent | Model | Purpose | Status |
|-------|-------|---------|--------|
| **thesis-orchestrator** | opus | Coordinates entire thesis writing | ✅ Ready |
| **chapter-coordinator** | opus | Coordinates single chapter writing | ✅ Ready |
| **paper-orchestrator** | opus | Coordinates single paper writing | ✅ Ready |

### Layer 2: Section Writers

| Agent | Model | Purpose | Status |
|-------|-------|---------|--------|
| **introduction-writer** | opus | Introduction sections | ✅ Ready |
| **methodology-writer** | sonnet | Methodology/methods sections | ✅ Ready |
| **results-writer** | sonnet | Results/experiments sections | ✅ Ready |
| **discussion-writer** | opus | Discussion sections | ✅ Ready |
| **conclusion-writer** | sonnet | Conclusion sections | ✅ Ready |
| **abstract-writer** | sonnet | Abstracts | ✅ Ready |
| **lit-review-writer** | opus | Literature review sections | ✅ Ready |
| **figure-designer** | sonnet | Figure captions, table descriptions | ✅ Ready |

### Layer 3: Quality Control

| Agent | Model | Purpose | Status |
|-------|-------|---------|--------|
| **document-validator** | haiku | Consistency, cross-references | ✅ Ready |
| **argument-validator** | opus | Logic, evidence, claims | ✅ Ready |
| **citation-validator** | sonnet | Citation accuracy, completeness | ✅ Ready |
| **plagiarism-checker** | sonnet | Paraphrase quality, attribution | ✅ Ready |

### Layer 4: Revision

| Agent | Model | Purpose | Status |
|-------|-------|---------|--------|
| **reviewer-response** | opus | Generate reviewer response letters | ✅ Ready |
| **change-manager** | haiku | Track revisions, generate diffs | ✅ Ready |
| **change-integrator** | sonnet | Merge revisions, resolve conflicts | ✅ Ready |

### Layer 5: Export

| Agent | Model | Purpose | Status |
|-------|-------|---------|--------|
| **latex-specialist** | sonnet | Convert to LaTeX | ✅ Ready |
| **formatting-validator** | haiku | Venue compliance checking | ✅ Ready |

---

## Context Protocol

Information flows through the hierarchy via structured context objects:

```
ThesisContext (Full Document)
    │
    │ Summarize to 500 words
    ▼
ChapterContext (Per Chapter)
    │
    │ Summarize to 300 words
    ▼
SectionContext (Per Section)
```

See: [protocols/context-schema.md](protocols/context-schema.md)

### Key Context Types

| Type | Used By | Max Size |
|------|---------|----------|
| ThesisContext | Orchestrators | Full document state |
| ChapterContext | Chapter-coordinator, Writers | 500 word parent summary |
| SectionContext | Section writers | 300 word chapter summary |
| QualityReport | QC agents | Validation output |

---

## Quality Assurance

### Prompt Quality (Phase 0)

All agent prompts must pass:
1. **prompt-reviewer** agent (score ≥ 0.8)
2. **5 domain scenario tests** (all pass)
3. **Human review** (for opus agents)

See: [protocols/prompt-checklist.md](protocols/prompt-checklist.md)

### Document Quality (Runtime)

Every section/chapter passes through QC agents:
- **document-validator**: Terminology, style, cross-references
- **argument-validator**: Logic, evidence, hedging
- **citation-validator**: Format, completeness

### Quality Gate Thresholds

| Score | Action |
|-------|--------|
| ≥ 0.8 | Pass, continue |
| 0.6-0.8 | Pass with warnings |
| 0.4-0.6 | Attempt fix, retry |
| < 0.4 | Halt, require intervention |

---

## Commands

| Command | Purpose | Invokes |
|---------|---------|---------|
| `/thesis-write` | Write complete thesis | thesis-orchestrator |
| `/chapter-write` | Write single chapter | chapter-coordinator |
| `/paper-write` | Write single paper | paper-orchestrator |
| `/quality-check` | Run quality control | QC agents |
| `/paper-revise` | Handle reviewer feedback | Revision agents |
| `/thesis-init` | Initialize thesis project | Template system |

---

## Usage Examples

### Writing a Conference Paper

```
User: /paper-write

Claude: I'll help you write a conference paper. Let me gather some information:
- Target venue: NeurIPS 2026
- Project folder: 1. Projects/Efficient-Attention

[paper-orchestrator initializes]
[Section writers execute in order]
[Quality checks run]

Output: Complete paper draft in project folder
```

### Writing a Thesis Chapter

```
User: /chapter-write --chapter methodology

Claude: I'll write the Methodology chapter.
[chapter-coordinator analyzes objectives]
[Section writers produce content]
[Quality validation]

Output: Complete chapter with quality report
```

### Running Quality Check

```
User: /quality-check --file drafts/paper-draft.md

[document-validator, argument-validator, citation-validator run in parallel]

Output: Consolidated quality report with actionable issues
```

---

## Domain Agnosticism

This system is designed to work across ALL academic fields:

| Domain | Methodology Type | Example Venues |
|--------|-----------------|----------------|
| Machine Learning | experimental | NeurIPS, ICML, CVPR |
| Humanities | analytical | PhD Thesis, Journal articles |
| Social Science | empirical | Nature Human Behaviour |
| Natural Science | experimental | Nature, Science |
| Interdisciplinary | mixed_methods | PhD Thesis |

### How It Works

1. **No hard-coded field names** in prompts
2. **Terminology from glossary** only
3. **Citation style from context**
4. **Methodology language adapts** to context
5. **Tested against 5 domain scenarios** before deployment

See: [protocols/domain-patterns.md](protocols/domain-patterns.md)

---

## File Structure

```
.claude/agents/paper-writing/
├── README.md                      # This file
├── prompt-reviewer.md             # Prompt quality agent
├── thesis-orchestrator.md         # Thesis coordination
├── chapter-coordinator.md         # Chapter coordination
├── paper-orchestrator.md          # Paper coordination
├── protocols/
│   ├── prompt-template.md         # Prompt structure standard
│   ├── domain-patterns.md         # Domain abstraction patterns
│   ├── prompt-checklist.md        # Prompt quality checklist
│   ├── prompt-iteration-process.md # Development workflow
│   ├── context-schema.md          # Context type documentation
│   └── context-schema.json        # JSON Schema definitions
└── tests/
    └── domain-scenarios/
        ├── README.md
        ├── ml-paper-scenario.json
        ├── humanities-thesis-scenario.json
        ├── social-science-scenario.json
        ├── natural-science-scenario.json
        └── interdisciplinary-scenario.json
```

### Agent Format

All agents use the **official Claude Code frontmatter format**:

```markdown
---
name: agent-name
description: Brief description of when to use this agent
tools: Read, Write, Edit
model: opus|sonnet|haiku
---

# Agent Name

[Agent content with preserved metadata in table format]

## Agent Metadata

| Property | Value |
|----------|-------|
| Layer | orchestration|section_writer|quality_control|revision|export |
| Trigger | Spawning condition |
| Priority | Critical|High|Medium |
| Version | 1.0.0 |
| Created | 2026-01-15 |
```

**Key fields:**
- **Frontmatter**: Machine-readable configuration (name, description, tools, model)
- **Metadata table**: Human-readable context about agent architecture (layer, trigger, priority, version)

---

## Development Roadmap

### ✅ Phase 0: Prompt Engineering Framework (Complete)
- Prompt template standard
- Domain abstraction patterns
- Quality checklist
- 5 domain test scenarios
- prompt-reviewer agent

### ✅ Phase 1: Core Orchestration (Complete)
- Context protocol schema
- thesis-orchestrator
- chapter-coordinator
- paper-orchestrator

### ✅ Phase 2: Section Writers (Complete)
- introduction-writer
- methodology-writer
- results-writer
- discussion-writer
- conclusion-writer
- abstract-writer
- lit-review-writer
- figure-designer

### ✅ Phase 3: Quality Control (Complete)
- document-validator
- argument-validator
- citation-validator
- plagiarism-checker

### ✅ Phase 4: Revision (Complete)
- reviewer-response
- change-manager
- change-integrator

### ✅ Phase 5: Export (Complete)
- latex-specialist
- formatting-validator

### ✅ Phase 6: Commands & Templates (Complete)
- `/thesis-init`, `/thesis-write`, `/chapter-write` commands
- `/paper-write`, `/quality-check`, `/paper-revise` commands
- 9 thesis templates in Obsidian vault

### ✅ Phase 7: Quality Hooks (Complete)
- thesis-consistency.py hook
- cross-reference.py hook
- Extended research-quality-gate.py with thesis chapter checks

---

## Related Documentation

- [Build Plan](../../plans/BUILD-PLAN-phd-paper-pipeline.md) - Full implementation plan
- [Research Team](../research-team/README.md) - Research phase agents
- [CLAUDE.md](../../../CLAUDE.md) - Main project documentation

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-15 | Initial documentation with Phase 0-1 complete |
| 2.0.0 | 2026-01-15 | All 21 agents complete, commands, templates, hooks |

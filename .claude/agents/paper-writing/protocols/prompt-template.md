# Prompt Template Standard

**Version:** 1.0
**Created:** 2026-01-15
**Purpose:** Canonical structure all paper-writing agent prompts must follow

---

## Overview

This document defines the standard structure for all agent prompts in the paper-writing pipeline. Following this template ensures:
- **Domain-agnosticism**: Agents work across ML, humanities, social sciences, and all fields
- **Consistency**: All agents communicate using shared protocols
- **Maintainability**: Clear structure makes prompts easier to review and update
- **Quality**: Standardized output formats integrate seamlessly

---

## Required Sections

Every agent prompt MUST include these sections in order:

### 1. Identity & Role

```markdown
## Identity & Role

You are a {role} within a hierarchical academic writing system. You specialize
in {capability} and produce {output_type} that integrates with the larger
document structure.

**Reporting to:** {parent_agent}
**Spawns:** {child_agents} (if applicable)
**Model:** {recommended_model}
```

**Guidelines:**
- Define the agent's specific function within the hierarchy
- Clarify relationships with other agents
- Specify model recommendation (opus for nuanced/coordination, sonnet for structured, haiku for pattern-matching)

---

### 2. Context Reception

```markdown
## Context Reception

You will receive a `{ContextType}` object containing:
- **{field_name}**: {description of what this field contains and how to use it}
- **{field_name}**: {description}
...

You MUST use values from context rather than making assumptions about the domain.
```

**Guidelines:**
- List ALL context fields the agent will receive
- Explain the purpose of each field
- Emphasize context-driven decisions over assumptions

**Context Types:**
| Context Type | Used By | Parent Context |
|--------------|---------|----------------|
| `ThesisContext` | thesis-orchestrator, chapter-coordinator | None (top-level) |
| `ChapterContext` | chapter-coordinator, section writers | ThesisContext summary |
| `SectionContext` | section writers | ChapterContext summary |
| `QualityContext` | QC agents | Document + SectionContext |

---

### 3. Domain Adaptability

```markdown
## Domain Adaptability

This agent MUST work across all academic domains without modification.

### Mandatory Practices:
- **Terminology**: Use ONLY terms from `terminology_glossary` - never assume field-specific vocabulary
- **Citation Style**: Follow `style_guide.citation_style` exactly - never default to a specific format
- **Methodology Language**: Adapt to `methodology_type`:
  - "experimental" → sciences, engineering
  - "analytical" → humanities, law
  - "empirical" → social sciences
  - "theoretical" → mathematics, philosophy
  - "mixed_methods" → interdisciplinary
- **Evidence Standards**: Match the field's norms as indicated in context

### Anti-Patterns (NEVER DO):
- ❌ Hard-code field names (ML, biology, history, etc.)
- ❌ Assume citation style (APA, IEEE, Nature)
- ❌ Use field-specific jargon not in glossary
- ❌ Reference "typical" patterns for any discipline
- ❌ Make claims not supported by provided context
```

**Guidelines:**
- Every agent must include this section verbatim (with agent-specific anti-patterns added)
- This is the PRIMARY defense against domain-specific bias

---

### 4. Rhetorical Framework

```markdown
## Rhetorical Framework

{Domain-agnostic structural patterns for this section type}

### Structure:
1. **{Phase Name}** ({purpose})
   - NOT: "{hard-coded example}"
   - YES: "{context-driven example referencing `field_name`}"

2. **{Phase Name}** ({purpose})
   - ...
```

**Guidelines:**
- Define structural patterns, NOT content prescriptions
- Use "NOT/YES" examples to clarify domain-agnostic approach
- Reference context fields directly in the "YES" examples

**Example for Introduction Writer:**
```markdown
### Structure:
1. **Establish Context** (broad → narrow)
   - NOT: "Describe the ML landscape"
   - YES: "Establish the broader context relevant to `research_questions[0]`"

2. **Identify Gap**
   - NOT: "Explain what existing models lack"
   - YES: "Articulate the gap that `contributions` addresses"

3. **State Contribution**
   - Use language appropriate to field (from `style_guide.methodology_type`)
   - Reference `contributions` list directly

4. **Roadmap**
   - NOT: "The remainder of this paper presents our neural architecture..."
   - YES: "Preview subsequent sections using `chapter_summaries` or section structure"
```

---

### 5. Output Requirements

```markdown
## Output Requirements

### Format
- **Type**: {markdown | JSON | structured text}
- **Template**: {reference to output template if applicable}

### Constraints
- **Word Budget**: Respect `word_budget` from context (±10% tolerance)
- **Citations**: Use keys from `required_citations` and `bibliography_keys`
- **Cross-references**: Follow `style_guide.formatting` patterns
- **Terminology**: All technical terms from `terminology_glossary` only

### Deliverables
1. {Primary output description}
2. {Secondary output if applicable}
3. {Metadata/status updates if applicable}
```

**Guidelines:**
- Be specific about format expectations
- Reference context fields for constraints
- Define clear deliverables

---

### 6. Quality Criteria

```markdown
## Quality Criteria

The output will be validated against these criteria:

### Critical (Must Pass)
- [ ] All terminology matches `terminology_glossary`
- [ ] Citation format matches `style_guide.citation_style`
- [ ] Word count within 10% of `word_budget`
- [ ] All `required_citations` appear in text

### High Priority
- [ ] Transitions reference adjacent sections appropriately
- [ ] Claims have supporting evidence or citations
- [ ] No logical fallacies or overclaiming

### Medium Priority
- [ ] {Agent-specific quality criteria}
```

**Guidelines:**
- Use measurable, domain-independent criteria
- Organize by priority level
- Include both universal and agent-specific criteria

---

### 7. Error Handling

```markdown
## Error Handling

### Missing Context
If required context fields are missing:
1. {What to do for field_name}
2. {What to do for other_field}

### Ambiguous Instructions
If instructions conflict or are unclear:
1. Prioritize {higher-level guidance}
2. Flag ambiguity in output metadata

### Budget Overflow
If word budget is exceeded:
1. Identify lowest-priority content
2. Condense or defer to appendix
3. Flag in output metadata
```

**Guidelines:**
- Define graceful degradation for common error scenarios
- Specify escalation paths when applicable

---

### 8. Integration Notes

```markdown
## Integration Notes

### Upstream Dependencies
- Receives context from: {parent agent}
- Requires: {list of required inputs}

### Downstream Consumers
- Output consumed by: {child agents or consolidation}
- Format compatibility: {what format is expected by consumers}

### Parallel Execution
- Can run in parallel with: {sibling agents if applicable}
- Sequential dependencies: {what must complete first}
```

**Guidelines:**
- Clarify the agent's position in the pipeline
- Define dependencies explicitly

---

## Template Skeleton

Use this skeleton when creating new agent prompts:

```markdown
---
name: agent-name
description: Brief description of when to use this agent (include trigger keywords)
tools: Read, Write, Edit
model: opus|sonnet|haiku
---

# Agent Name Agent

You are a {role} within a hierarchical academic writing system...

## Agent Metadata

| Property | Value |
|----------|-------|
| Layer | orchestration|section_writer|quality_control|revision|export |
| Trigger | When/how this agent is spawned |
| Priority | Critical|High|Medium |
| Version | 1.0.0 |
| Created | YYYY-MM-DD |

## Context Reception

You will receive a `{ContextType}` object containing:
- ...

## Domain Adaptability

This agent MUST work across all academic domains...

## Rhetorical Framework

### Structure:
1. **{Phase}** ...

## Output Requirements

### Format
- **Type**: ...

### Constraints
- ...

### Deliverables
1. ...

## Quality Criteria

### Critical (Must Pass)
- [ ] ...

## Error Handling

### Missing Context
...

## Integration Notes

### Upstream Dependencies
...
```

**Format notes:**
- **Frontmatter** (lines 1-6): Machine-readable configuration for Claude Code
- **Metadata table**: Human-readable architectural context (preserved from original format)
- All agents must use this standardized structure

---

## Validation

All prompts must pass the [Prompt Quality Checklist](prompt-checklist.md) before deployment.

All prompts must be reviewed by the [prompt-reviewer](../prompt-reviewer.md) agent with score ≥ 0.8.

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-15 | Initial template standard |

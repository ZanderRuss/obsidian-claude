# Prompt Quality Checklist

**Version:** 1.0
**Created:** 2026-01-15
**Purpose:** Mandatory validation checklist for all agent prompts

---

## Overview

Every agent prompt in the paper-writing pipeline MUST satisfy ALL criteria in this checklist before deployment. This ensures domain-agnosticism, integration compatibility, and quality output.

**Passing Score:** ≥ 0.8 (80% of applicable criteria)
**Critical Criteria:** Must pass ALL critical items regardless of overall score

---

## Scoring Guide

| Category | Weight | Description |
|----------|--------|-------------|
| **Critical** | 2x | Must pass. Failure blocks deployment |
| **High** | 1.5x | Should pass. Exceptions require justification |
| **Medium** | 1x | Recommended. Minor deductions for failure |

---

## Domain Independence (Critical)

These criteria are **BLOCKING** - failure on ANY item prevents deployment.

### DI-1: No Hard-Coded Field Names
- [ ] No mention of specific fields (ML, NLP, biology, history, psychology, etc.)
- [ ] No field-specific conferences/journals (NeurIPS, CVPR, Nature, etc.) in prompt logic
- [ ] Field references only appear in examples marked as "Example: {domain}"

**How to check:** Search for common field names; verify all domain references are in example blocks

### DI-2: No Assumed Citation Style
- [ ] No hard-coded citation formats (APA, IEEE, Nature, Vancouver, Chicago)
- [ ] All citation formatting references `style_guide.citation_style`
- [ ] Examples show placeholder: `[citation per style_guide]`

**How to check:** Search for citation format strings; verify style_guide references

### DI-3: No Assumed Methodology
- [ ] No hard-coded methodology terms (experiment, model, dataset, hypothesis)
- [ ] All methodology language references `methodology_type` or uses adaptors
- [ ] Uses methodology_adaptors lookup for verbs and nouns

**How to check:** Search for methodology terms; verify adaptor/context usage

### DI-4: Terminology from Glossary Only
- [ ] No technical terms assumed in prompt
- [ ] All terminology references `terminology_glossary`
- [ ] Prompt instructs agent to use ONLY glossary terms

**How to check:** Identify technical terms; verify glossary references

### DI-5: Context-Driven Examples
- [ ] Examples use placeholder variables: `{field_name}`, `[from context]`
- [ ] NOT specific domain examples that could bias the agent
- [ ] If specific examples given, multiple domains represented

**How to check:** Review all examples; verify they don't assume a single domain

---

## Context Utilization (Critical)

### CU-1: Explicit Context Field Listing
- [ ] All context fields the agent receives are explicitly listed
- [ ] Each field's purpose is explained
- [ ] Required vs optional fields are distinguished

**How to check:** Compare context reception section against context schema

### CU-2: Context-Driven Decisions
- [ ] All content decisions derive from context, not defaults
- [ ] No "typically" or "usually" without context fallback
- [ ] Agent doesn't generate content not derived from inputs

**How to check:** Search for assumption language; verify context derivation

### CU-3: Graceful Degradation
- [ ] Handles missing optional context gracefully
- [ ] Specifies fallback behavior for each optional field
- [ ] Doesn't fail silently on missing required context

**How to check:** Simulate missing fields; verify fallback instructions exist

### CU-4: Glossary Usage
- [ ] Explicitly instructs to use `terminology_glossary` for all technical terms
- [ ] Provides examples of glossary lookup
- [ ] Warns against introducing terms not in glossary

**How to check:** Verify terminology_glossary references and instructions

---

## Structural Clarity (High Priority)

### SC-1: Section Completeness
- [ ] All 8 required sections present (per prompt-template.md)
- [ ] Sections in correct order
- [ ] No extraneous sections that could confuse

**Required sections:**
1. Identity & Role
2. Context Reception
3. Domain Adaptability
4. Rhetorical Framework
5. Output Requirements
6. Quality Criteria
7. Error Handling
8. Integration Notes

**How to check:** Compare against template; verify section presence

### SC-2: Rhetorical Framework
- [ ] Clear structural patterns defined (NOT content prescriptions)
- [ ] Uses NOT/YES examples to clarify approach
- [ ] References context fields in YES examples

**How to check:** Review rhetorical framework; verify pattern vs content distinction

### SC-3: Measurable Output Requirements
- [ ] Word budget constraints specified
- [ ] Output format clearly defined
- [ ] Deliverables enumerated

**How to check:** Verify quantifiable constraints exist

### SC-4: Verifiable Quality Criteria
- [ ] Criteria are measurable (not subjective)
- [ ] Organized by priority level
- [ ] Agent-specific criteria included

**How to check:** Review criteria for measurability

---

## Integration Compatibility (High Priority)

### IC-1: Context Schema Reference
- [ ] References appropriate context type (Thesis/Chapter/Section)
- [ ] Context type matches agent's position in hierarchy
- [ ] Summarization rules followed if passing context down

**How to check:** Verify context type against agent hierarchy

### IC-2: Output Format Compatibility
- [ ] Output format matches what downstream agents expect
- [ ] Uses standard schemas (QualityReport, SectionOutput, etc.)
- [ ] Metadata format consistent with pipeline

**How to check:** Trace output to consuming agents; verify format match

### IC-3: Cross-Reference Convention
- [ ] Cross-references follow `style_guide.formatting` patterns
- [ ] Internal references use consistent format
- [ ] External citations use keys from bibliography

**How to check:** Review cross-reference instructions

### IC-4: Parallel Execution Awareness
- [ ] Specifies what can run in parallel
- [ ] Documents sequential dependencies
- [ ] Doesn't assume sequential-only execution

**How to check:** Review integration notes for parallelization info

---

## Robustness (Medium Priority)

### RB-1: Minimal Context Operation
- [ ] Can produce useful output with minimal context
- [ ] Graceful degradation documented
- [ ] Core functionality preserved with reduced context

**How to check:** Simulate minimal context scenario

### RB-2: Edge Case Handling
- [ ] Short sections handled (< 100 words)
- [ ] No citations needed scenario handled
- [ ] Empty optional fields handled

**How to check:** Identify edge cases; verify handling instructions

### RB-3: Error Condition Documentation
- [ ] Common errors listed
- [ ] Recovery instructions provided
- [ ] Escalation path defined

**How to check:** Review error handling section

### RB-4: Word Budget Flexibility
- [ ] Handles underrun (section shorter than budget)
- [ ] Handles overrun (content exceeds budget)
- [ ] Prioritization guidance for condensation

**How to check:** Verify budget overflow/underflow handling

---

## Scoring Calculation

```
Score = (Σ weighted_passed / Σ weighted_total)

Where:
- Critical items: weight = 2
- High items: weight = 1.5
- Medium items: weight = 1

Total possible:
- 9 Critical items × 2 = 18
- 8 High items × 1.5 = 12
- 4 Medium items × 1 = 4
- Total: 34 weighted points

Passing threshold: 0.8 × 34 = 27.2 points
```

---

## Review Process

### Self-Review (Author)

Before submitting for review:
1. Complete this checklist
2. Mark each item as passed (✓) or failed (✗)
3. Calculate score
4. If < 0.8 or any Critical fails, revise and re-check

### Automated Review (prompt-reviewer agent)

The prompt-reviewer agent will:
1. Parse the prompt structure
2. Check for hard-coded terms
3. Verify context field usage
4. Score against this checklist
5. Generate `PromptReviewReport`

### Human Review (for Critical Agents)

For orchestrators and opus-model agents:
1. Domain expert reviews output samples
2. Checks for subtle biases
3. Approves for production

---

## Checklist Template

Copy and complete for each agent:

```markdown
## Prompt Review: {agent-name}

**Reviewer:** {name}
**Date:** {date}
**Prompt Version:** {version}

### Domain Independence (Critical)
- [ ] DI-1: No hard-coded field names
- [ ] DI-2: No assumed citation style
- [ ] DI-3: No assumed methodology
- [ ] DI-4: Terminology from glossary only
- [ ] DI-5: Context-driven examples

### Context Utilization (Critical)
- [ ] CU-1: Explicit context field listing
- [ ] CU-2: Context-driven decisions
- [ ] CU-3: Graceful degradation
- [ ] CU-4: Glossary usage

### Structural Clarity (High)
- [ ] SC-1: Section completeness
- [ ] SC-2: Rhetorical framework quality
- [ ] SC-3: Measurable output requirements
- [ ] SC-4: Verifiable quality criteria

### Integration Compatibility (High)
- [ ] IC-1: Context schema reference
- [ ] IC-2: Output format compatibility
- [ ] IC-3: Cross-reference convention
- [ ] IC-4: Parallel execution awareness

### Robustness (Medium)
- [ ] RB-1: Minimal context operation
- [ ] RB-2: Edge case handling
- [ ] RB-3: Error condition documentation
- [ ] RB-4: Word budget flexibility

### Scoring
- Critical passed: {x}/9
- High passed: {x}/8
- Medium passed: {x}/4
- Weighted score: {score}/34
- **PASS/FAIL**: {result}

### Notes
{Any observations, recommended improvements, or justifications for exceptions}
```

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-15 | Initial checklist |

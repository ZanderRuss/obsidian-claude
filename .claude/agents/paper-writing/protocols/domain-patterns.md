# Domain Abstraction Patterns Library

**Version:** 1.0
**Created:** 2026-01-15
**Purpose:** Patterns that enable agents to work across all academic domains

---

## Overview

This library contains domain-agnostic patterns that replace field-specific language. Use these patterns to ensure your agent prompts work for:
- Machine Learning / Computer Science
- Humanities / Arts
- Social Sciences
- Natural Sciences
- Interdisciplinary Research

---

## Language Substitution Table

Replace hard-coded terms with context-driven alternatives:

### Methodology Language

| Hard-coded (BAD) | Context-driven (GOOD) | Notes |
|------------------|----------------------|-------|
| "neural network architecture" | "methodological approach as specified in `methodology_type`" | Never assume computational methods |
| "experimental results show" | "findings demonstrate" (neutral) | Or check `methodology_type` for appropriate verb |
| "p < 0.05" | "statistical evidence as appropriate to `evidence_standards`" | Not all fields use p-values |
| "training data" | "primary sources/data" | Adapts to field |
| "hyperparameters" | "methodological parameters" | Generalizes |
| "ablation study" | "component analysis" | Generalizes |
| "baseline model" | "comparison approach" / "baseline method" | Field-neutral |
| "our model" | "our approach" / "this method" | Avoid assuming computational |

### Results Language

| Hard-coded (BAD) | Context-driven (GOOD) | Notes |
|------------------|----------------------|-------|
| "accuracy/F1/BLEU" | "evaluation metrics as defined in `methodology`" | Metrics vary by field |
| "outperforms" | "improves upon" / "exceeds" | Field-neutral comparison |
| "state-of-the-art" | "current best-performing" / "leading approaches" | Less jargon |
| "benchmark dataset" | "evaluation corpus" / "test collection" | Generalizes |

### Discussion Language

| Hard-coded (BAD) | Context-driven (GOOD) | Notes |
|------------------|----------------------|-------|
| "related work in NLP" | "prior work addressing `research_questions`" | Context-driven |
| "future work on models" | "future directions" | Field-neutral |
| "limitations of our approach" | "limitations" (universal) | Works everywhere |

### Citation Language

| Hard-coded (BAD) | Context-driven (GOOD) | Notes |
|------------------|----------------------|-------|
| "(Author, Year)" | "Use format from `style_guide.citation_style`" | Never assume APA |
| "[1]" | "Use format from `style_guide.citation_style`" | Never assume IEEE |
| "as shown by Smith et al." | "as demonstrated in prior work [citation]" | Style-agnostic |

---

## Methodology Type Adaptors

Use these adaptors to generate appropriate language based on `methodology_type`:

```yaml
methodology_adaptors:
  experimental:  # Sciences, engineering, ML
    action_verb: "conducted"
    evidence_term: "results"
    validation_term: "experiments"
    contribution_verb: "demonstrate"
    study_noun: "experiment"
    data_noun: "data"
    example_context: "We conducted experiments on three datasets..."

  analytical:  # Humanities, law, philosophy
    action_verb: "analyzed"
    evidence_term: "findings"
    validation_term: "analysis"
    contribution_verb: "argue"
    study_noun: "analysis"
    data_noun: "sources"
    example_context: "Through close reading of primary sources..."

  empirical:  # Social sciences, psychology, education
    action_verb: "investigated"
    evidence_term: "observations"
    validation_term: "study"
    contribution_verb: "show"
    study_noun: "study"
    data_noun: "observations"
    example_context: "Our study of 500 participants reveals..."

  theoretical:  # Mathematics, theoretical physics, philosophy
    action_verb: "developed"
    evidence_term: "proofs/arguments"
    validation_term: "derivation"
    contribution_verb: "prove"
    study_noun: "framework"
    data_noun: "axioms"
    example_context: "We develop a theoretical framework that..."

  mixed_methods:  # Interdisciplinary
    action_verb: "examined"
    evidence_term: "evidence"
    validation_term: "investigation"
    contribution_verb: "establish"
    study_noun: "investigation"
    data_noun: "data/sources"
    example_context: "Combining quantitative analysis with..."
```

### Usage in Prompts

```markdown
## Rhetorical Framework

When writing the methodology section:
1. Use `methodology_adaptors[context.methodology_type].action_verb` for describing research actions
2. Refer to outputs as `methodology_adaptors[context.methodology_type].evidence_term`
3. Describe validation using `methodology_adaptors[context.methodology_type].validation_term`
```

---

## Rhetorical Patterns by Section

### Introduction Patterns (Domain-Agnostic)

```
Pattern: Funnel Structure
1. Broad Context → Specific Problem
   "The field of [DOMAIN from context] has seen..."
   → "[SPECIFIC_AREA from research_questions] remains..."
   → "This [STUDY_TYPE from methodology_type] addresses..."

Pattern: Gap-Contribution Bridge
1. Establish what exists (cite from bibliography_keys)
2. Identify what's missing (derive from research_questions)
3. State what this work provides (from contributions)
```

### Literature Review Patterns (Domain-Agnostic)

```
Pattern: Thematic Organization
- Group sources by theme (from lit_review_themes in context)
- NOT by chronology or author
- Synthesize across sources, don't summarize each

Pattern: Critical Positioning
- For each theme:
  1. What has been established (synthesis of sources)
  2. What gaps remain (from research_questions)
  3. How this work relates (from contributions)
```

### Methodology Patterns (Domain-Agnostic)

```
Pattern: Reproducibility First
1. What was done (using methodology_type adaptor language)
2. How it was done (sufficient detail to replicate)
3. Why these choices (justify methodological decisions)
4. What could affect results (acknowledge limitations)

Pattern: Parallel Structure
- If multiple methods/experiments/analyses:
  - Use consistent heading structure
  - Use consistent description format
  - Use consistent reporting format
```

### Results Patterns (Domain-Agnostic)

```
Pattern: Evidence → Interpretation
1. Present finding (objective)
2. Contextualize (what does it mean)
3. Connect (how does it relate to research_questions)

Pattern: Structured Reporting
- Main findings first (answering research_questions)
- Supporting findings second
- Negative/null findings third (important for completeness)
```

### Discussion Patterns (Domain-Agnostic)

```
Pattern: Synthesis Pyramid
1. Summarize key findings (from results)
2. Interpret meaning (what do findings suggest)
3. Compare with literature (from bibliography_keys)
4. Discuss implications (for field/practice/theory)
5. Acknowledge limitations (honest assessment)
6. Suggest future directions

Pattern: Contribution Verification
- For each contribution in contributions list:
  - Show evidence that supports it
  - Qualify if needed (hedging)
  - Connect to broader implications
```

### Conclusion Patterns (Domain-Agnostic)

```
Pattern: Mirror Introduction
1. Restate problem (from research_questions)
2. Summarize approach (from methodology_type)
3. Highlight contributions (from contributions)
4. State implications
5. End with forward-looking statement

Pattern: Concise Closure
- No new information
- No new citations
- No hedging (be confident)
- Clear final statement
```

---

## Evidence Standards by Field

```yaml
evidence_standards:
  quantitative:
    statistical_significance: required
    effect_sizes: recommended
    confidence_intervals: recommended
    replication: valued

  qualitative:
    triangulation: recommended
    member_checking: valued
    thick_description: required
    reflexivity: required

  theoretical:
    logical_consistency: required
    formal_proofs: valued (if applicable)
    counterexample_consideration: required

  historical:
    primary_sources: required
    source_criticism: required
    contextualization: required

  mixed:
    integration: required
    complementarity: valued
    sequential_connection: recommended
```

---

## Common Anti-Patterns to Avoid

### Hard-Coded Domain Assumptions

❌ **BAD:**
```
"In machine learning, the standard approach is to split data into training, validation, and test sets."
```

✅ **GOOD:**
```
"Following standard practice in `methodology_type`, we structured our approach to ensure valid evaluation..."
```

### Assumed Citation Style

❌ **BAD:**
```
"As shown in [1], previous work has..."
```

✅ **GOOD:**
```
"As demonstrated in prior work `[citation per style_guide.citation_style]`, ..."
```

### Field-Specific Jargon

❌ **BAD:**
```
"We fine-tuned the transformer on downstream tasks."
```

✅ **GOOD:**
```
"We adapted the approach to specific applications, following the methodology described in Section X."
```

### Assumed Metric Types

❌ **BAD:**
```
"Our model achieves 94.2% accuracy on the test set."
```

✅ **GOOD:**
```
"Using the evaluation metrics appropriate to this field (specified in methodology), our approach achieves [metric: value]."
```

---

## Pattern Application Examples

### Example: Writing an Introduction

**Context received:**
```yaml
methodology_type: empirical
research_questions:
  - "How does social media use affect adolescent well-being?"
contributions:
  - "Longitudinal dataset of 2,000 adolescents"
  - "Causal model linking usage patterns to outcomes"
terminology_glossary:
  - term: "well-being"
    definition: "Composite measure including life satisfaction and mental health indicators"
```

**Pattern application:**
```
The relationship between digital technology and [well-being per glossary] has emerged
as a critical area of inquiry in [field implied by methodology_type: social science].
While prior work has examined [synthesize from bibliography_keys], the question of
[research_questions[0]] remains underexplored.

This [study_noun per adaptor: study] addresses this gap by [contributions[0]] and
developing [contributions[1]]. Our [evidence_term per adaptor: observations] suggest...
```

---

## Validation Checklist

Before finalizing any agent prompt, verify:

- [ ] No hard-coded field names appear in the prompt
- [ ] All methodology language uses adaptors or context fields
- [ ] Citation style references `style_guide.citation_style`
- [ ] Terminology references `terminology_glossary`
- [ ] Evidence standards reference context, not assumptions
- [ ] Examples use context field placeholders, not specific domains

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-15 | Initial patterns library |

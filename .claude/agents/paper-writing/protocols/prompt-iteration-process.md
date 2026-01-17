# Prompt Iteration Process

**Version:** 1.0
**Created:** 2026-01-15
**Purpose:** Defines how agent prompts are developed, reviewed, and improved

---

## Overview

This document defines the complete workflow for developing, reviewing, testing, and iterating on agent prompts in the paper-writing pipeline. Following this process ensures all agents achieve domain-agnosticism and integration quality before deployment.

---

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        PROMPT DEVELOPMENT WORKFLOW                           │
└─────────────────────────────────────────────────────────────────────────────┘

1. DRAFT
   │
   ├── Write initial prompt following prompt-template.md
   ├── Self-check against prompt-checklist.md
   └── Commit to feature branch
                    │
                    ▼
2. AUTOMATED REVIEW
   │
   ├── Run prompt-reviewer agent
   ├── Must score ≥ 0.8 on domain_independence and context_utilization
   ├── Fix any critical/high severity issues
   └── Iterate until passed=true AND approved_for_testing=true
                    │
                    ▼
3. DOMAIN TESTING
   │
   ├── Run agent against all 5 domain scenarios:
   │   ├── ml-paper-scenario.json
   │   ├── humanities-thesis-scenario.json
   │   ├── social-science-scenario.json
   │   ├── natural-science-scenario.json
   │   └── interdisciplinary-scenario.json
   ├── Verify output for each scenario:
   │   ├── Uses only terminology from glossary
   │   ├── Citation format matches style_guide
   │   ├── Methodology language matches type
   │   ├── All must_include elements present
   │   └── No must_not_include elements present
   └── All 5 scenarios must pass
                    │
                    ▼
4. HUMAN REVIEW (for critical agents)
   │
   ├── Required for: orchestrators, opus-model agents
   ├── Domain expert reviews sample outputs
   ├── Checks for subtle biases
   └── Signs off for production
                    │
                    ▼
5. PRODUCTION DEPLOYMENT
   │
   ├── Merge to main branch
   ├── Add to agent registry
   ├── Update documentation
   └── Monitor for domain-specific failures
                    │
                    ▼
6. ITERATION (ongoing)
   │
   ├── Collect feedback from usage
   ├── Analyze failure patterns
   ├── Prioritize improvements
   └── Return to DRAFT for revisions
```

---

## Phase 1: Draft

### 1.1 Start from Template

Always start from the template skeleton in [prompt-template.md](prompt-template.md):

```bash
# Copy template skeleton
cp protocols/prompt-template.md agents/paper-writing/new-agent.md
```

### 1.2 Fill Required Sections

Complete all 8 required sections:

| Section | What to Include |
|---------|-----------------|
| Identity & Role | Agent function, hierarchy position, model |
| Context Reception | All context fields used, with explanations |
| Domain Adaptability | Mandatory section (copy from template) + agent-specific anti-patterns |
| Rhetorical Framework | Structure patterns with NOT/YES examples |
| Output Requirements | Format, constraints, deliverables |
| Quality Criteria | Measurable criteria by priority |
| Error Handling | Graceful degradation for common issues |
| Integration Notes | Dependencies, consumers, parallelization |

### 1.3 Self-Check

Before submitting for review, complete the self-check:

```markdown
## Pre-Review Self-Check

- [ ] No hard-coded field names (ML, biology, history, etc.)
- [ ] No assumed citation style (always reference style_guide)
- [ ] No assumed methodology (always reference methodology_type or adaptors)
- [ ] All terminology from glossary_terminology
- [ ] All 8 sections present
- [ ] NOT/YES examples in rhetorical framework
- [ ] Output format specified
- [ ] Error handling documented
```

### 1.4 Commit to Branch

Create a feature branch for the new agent:

```bash
git checkout -b feat/paper-writing-new-agent
git add agents/paper-writing/new-agent.md
git commit -m "feat(paper-writing): add new-agent draft"
```

---

## Phase 2: Automated Review

### 2.1 Run prompt-reviewer

Invoke the prompt-reviewer agent:

```
Review the agent prompt at: .claude/agents/paper-writing/new-agent.md

Perform a full review checking domain independence, context utilization,
structural clarity, integration compatibility, and robustness.

Generate a PromptReviewReport.
```

### 2.2 Review Gates

The prompt must pass these gates:

| Gate | Requirement | Blocking? |
|------|-------------|-----------|
| Domain Independence | score ≥ 0.8 | 🔴 Yes |
| Context Utilization | score ≥ 0.8 | 🔴 Yes |
| Critical Issues | count = 0 | 🔴 Yes |
| Structural Clarity | score ≥ 0.7 | 🟠 Should fix |
| Integration | score ≥ 0.7 | 🟠 Should fix |
| Robustness | score ≥ 0.6 | 🟡 Recommended |

### 2.3 Fix Issues and Re-Review

For each issue in the report:

1. Read the description and recommendation
2. Locate the problematic section
3. Apply the fix
4. Re-run prompt-reviewer
5. Repeat until passed=true

### 2.4 Document Changes

Track revisions in the agent file:

```markdown
## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-15 | Initial draft |
| 1.0.1 | 2026-01-15 | Fixed domain independence issues from review |
| 1.1.0 | 2026-01-16 | Added error handling section |
```

---

## Phase 3: Domain Testing

### 3.1 Prepare Test Context

Load each scenario's ThesisContext:

```bash
# Load scenario
cat tests/domain-scenarios/ml-paper-scenario.json | jq '.context.ThesisContext'
```

### 3.2 Run Agent with Each Scenario

For each of the 5 scenarios:

1. Provide the scenario's ThesisContext to the agent
2. Request the agent's primary output (e.g., introduction text)
3. Save output for validation

### 3.3 Validate Outputs

Check each output against the scenario's validation_criteria:

```markdown
## Domain Testing Results

### ML Paper Scenario
- [ ] Uses only terms from terminology_glossary
- [ ] Citation format: NeurIPS (superscript numbers)
- [ ] Methodology language: experimental
- [ ] All must_include elements present
- [ ] No must_not_include elements present

### Humanities Thesis Scenario
- [ ] Uses only terms from terminology_glossary
- [ ] Citation format: Chicago Notes-Bibliography
- [ ] Methodology language: analytical
- [ ] All must_include elements present
- [ ] No must_not_include elements present

### Social Science Scenario
- [ ] Uses only terms from terminology_glossary
- [ ] Citation format: Nature
- [ ] Methodology language: empirical
...
```

### 3.4 Pass Criteria

**All 5 scenarios must pass.** Any failure requires:
1. Analyze which domain assumptions caused failure
2. Update prompt to be more domain-agnostic
3. Re-run prompt-reviewer
4. Re-run domain testing

---

## Phase 4: Human Review

### 4.1 When Required

Human review is required for:
- Orchestrator agents (thesis-orchestrator, chapter-coordinator, paper-orchestrator)
- All opus-model agents (require nuanced judgment)
- Any agent touching sensitive content (ethics, bias detection)

### 4.2 Review Process

1. **Sample Output Review**: Reviewer reads 3-5 sample outputs from domain testing
2. **Bias Check**: Look for subtle domain assumptions not caught by automated review
3. **Quality Assessment**: Evaluate output quality against expectations
4. **Sign-Off**: Approve or request revisions

### 4.3 Sign-Off Record

Document human review:

```markdown
## Human Review Sign-Off

**Reviewer:** [Name]
**Date:** [Date]
**Agent:** [agent-name]

### Review Summary
- Reviewed outputs from [X] scenarios
- Quality assessment: [Excellent/Good/Acceptable/Needs Work]
- Bias concerns: [None/Minor/Major]

### Decision
- [x] Approved for production
- [ ] Revisions required (see notes)

### Notes
[Any specific feedback or required changes]
```

---

## Phase 5: Production Deployment

### 5.1 Merge to Main

```bash
git checkout main
git merge feat/paper-writing-new-agent
git push origin main
```

### 5.2 Update Agent Registry

Add to the paper-writing README:

```markdown
## Agent Registry

| Agent | Model | Layer | Status |
|-------|-------|-------|--------|
| prompt-reviewer | opus | Prompt Quality | ✅ Production |
| new-agent | sonnet | Section Writer | ✅ Production |
```

### 5.3 Update Documentation

Update relevant documentation:
- CLAUDE.md: Add to Available Agents if user-facing
- README.md: Add to paper-writing team docs
- Commands: Update any commands that use the agent

### 5.4 Notify Team

Announce deployment and usage instructions.

---

## Phase 6: Iteration

### 6.1 Monitor for Failures

Track domain-specific failures in production:
- Which scenarios fail most often?
- What error patterns emerge?
- User feedback on quality

### 6.2 Prioritize Improvements

```markdown
## Improvement Backlog

| Issue | Domain | Severity | Status |
|-------|--------|----------|--------|
| Overclaims in discussion | Humanities | High | Open |
| Citation format edge cases | Natural Science | Medium | Open |
```

### 6.3 Iterate

For each improvement:
1. Create feature branch
2. Update prompt
3. Re-run full review process
4. Deploy updated version

---

## Quick Reference: Review Commands

```bash
# Run prompt-reviewer
Task: Review .claude/agents/paper-writing/new-agent.md with prompt-reviewer

# Run domain tests (manual)
# For each scenario in tests/domain-scenarios/*.json:
#   1. Load ThesisContext
#   2. Run agent
#   3. Validate output

# Check review gate status
# passed = domain_independence >= 0.8 AND context_utilization >= 0.8 AND critical_issues = 0
```

---

## Appendix: Common Issues and Fixes

### Issue: Hard-coded field name

**Problem:**
```markdown
"In machine learning papers, the introduction typically..."
```

**Fix:**
```markdown
"Following the conventions of the field specified in `methodology_type`..."
```

### Issue: Assumed citation style

**Problem:**
```markdown
"Format citations as (Author, Year)"
```

**Fix:**
```markdown
"Format citations according to `style_guide.citation_style`"
```

### Issue: Technical jargon without glossary

**Problem:**
```markdown
"Describe the model architecture and training procedure"
```

**Fix:**
```markdown
"Describe the methodological approach using terms from `terminology_glossary`"
```

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-15 | Initial iteration process |

# Domain Test Scenarios

This directory contains test scenarios for validating agent prompts across different academic domains.

## Purpose

Every agent in the paper-writing pipeline must be tested against **all 5 scenarios** before deployment. This ensures domain-agnosticism - agents work equally well for ML papers, humanities theses, social science studies, and more.

## Available Scenarios

| File | Domain | Venue Type | Methodology |
|------|--------|------------|-------------|
| `ml-paper-scenario.json` | Machine Learning | Conference (NeurIPS) | Experimental |
| `humanities-thesis-scenario.json` | Humanities | PhD Thesis | Analytical |
| `social-science-scenario.json` | Social Science | Journal (Nature Human Behaviour) | Empirical |
| `natural-science-scenario.json` | Natural Science | Journal (Nature) | Experimental |
| `interdisciplinary-scenario.json` | Interdisciplinary | PhD Thesis | Mixed Methods |

## Scenario Structure

Each scenario provides:

```json
{
  "scenario_id": "unique identifier",
  "scenario_name": "Human-readable name",
  "domain": "academic field",
  "venue": "publication target",
  "methodology_type": "experimental|analytical|empirical|theoretical|mixed_methods",
  "description": "What this scenario tests",

  "context": {
    "ThesisContext": {
      // Full context as would be passed to agents
    }
  },

  "validation_criteria": {
    "must_include": ["required elements"],
    "must_not_include": ["forbidden elements"],
    "expected_structure": "document structure",
    "tone": "expected voice",
    "word_count_tolerance": 0.1
  },

  "test_expectations": {
    // Per-agent expectations
  }
}
```

## How to Use

### Manual Testing

1. Load scenario context
2. Pass to agent being tested
3. Review output against `validation_criteria`
4. Check agent-specific `test_expectations`

### Automated Testing (Future)

```bash
# Run all scenarios against an agent
python test_agent.py --agent introduction-writer --scenarios all

# Run specific scenario
python test_agent.py --agent introduction-writer --scenario ml-paper-neurips
```

## Adding New Scenarios

When adding a new domain scenario:

1. Follow the JSON structure above
2. Include diverse terminology in glossary
3. Set appropriate methodology_type
4. Define realistic validation_criteria
5. Add test_expectations for relevant agents

## Validation Checklist

For each agent × scenario combination, verify:

- [ ] Output uses only terms from `terminology_glossary`
- [ ] Citation style matches `style_guide.citation_style`
- [ ] Methodology language matches `methodology_type`
- [ ] Word count within tolerance
- [ ] All `must_include` elements present
- [ ] No `must_not_include` elements present
- [ ] Structure matches expectations
- [ ] Tone is appropriate

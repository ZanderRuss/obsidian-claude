# Query Strategies for Effective AI Search

## Core Principles

### 1. Be Specific and Detailed

**Good queries:**
- "What are the latest clinical trial results for CAR-T cell therapy in treating B-cell lymphoma published in 2024?"
- "Compare the efficacy and safety profiles of mRNA vaccines versus viral vector vaccines for COVID-19"
- "Explain AlphaFold3 improvements over AlphaFold2 with specific accuracy metrics from 2023-2024 research"

**Poor queries:**
- "Tell me about cancer treatment" (too broad)
- "CRISPR" (too vague)
- "vaccines" (lacks specificity)

### 2. Include Time Constraints

AI search excels at finding current information:
- "What papers were published in Nature Medicine in 2024 about long COVID?"
- "What are the latest developments (past 6 months) in large language model efficiency?"
- "What was announced at NeurIPS 2024 regarding AI safety?"

### 3. Specify Domain and Sources

For high-quality results, mention source preferences:
- "According to peer-reviewed publications in high-impact journals..."
- "Based on FDA-approved treatments..."
- "From clinical trial registries like clinicaltrials.gov..."

---

## Query Templates by Domain

### Scientific Literature

```
What does recent research (YEAR_RANGE) say about TOPIC?
Focus on peer-reviewed studies and include specific METRICS.
```

Example:
```
What does recent research (2023-2024) say about the role of gut microbiome
in Parkinson's disease? Focus on peer-reviewed studies and include specific
bacterial species identified.
```

### Technical Documentation

```
How to implement FEATURE using TECHNOLOGY? Include considerations for
CONSTRAINTS and best practices for REQUIREMENTS.
```

Example:
```
How to implement real-time data streaming from Kafka to PostgreSQL using Python?
Include considerations for handling backpressure and ensuring exactly-once semantics.
```

### Comparative Analysis

```
Compare OPTION_A versus OPTION_B for USE_CASE in terms of CRITERIA.
Include benchmarks from recent studies.
```

Example:
```
Compare PyTorch versus TensorFlow for implementing transformer models in terms
of ease of use, performance, and ecosystem support. Include benchmarks from
recent studies.
```

### Clinical Research

```
What is the evidence for INTERVENTION in treating CONDITION in POPULATION?
Focus on STUDY_TYPE and report OUTCOMES.
```

Example:
```
What is the evidence for intermittent fasting in managing type 2 diabetes in adults?
Focus on randomized controlled trials and report HbA1c changes and weight loss outcomes.
```

### Trend Analysis

```
What are the key trends in FIELD over the past TIME_PERIOD?
Highlight improvements in ASPECTS, with specific examples.
```

Example:
```
What are the key trends in single-cell RNA sequencing technology over the past 5 years?
Highlight improvements in throughput, cost, and resolution, with specific examples.
```

---

## Provider-Specific Tips

### Claude WebSearch (Default)

- Works best with natural language queries
- Automatically provides source citations
- Good at synthesizing multiple sources

### OpenAI

- Include "current" or "latest" for recent information
- Works well with structured queries
- Can follow complex multi-part questions

### Anthropic

- Benefits from explicit reasoning requests
- Good at handling nuanced topics
- Responds well to "think step by step" prompts

### Google Gemini

- Leverages Google Search for grounding
- Good for broad web coverage
- Include specific domains for targeted results

### Perplexity

- Optimized for real-time information
- Excellent for scientific literature
- Include publication types for better filtering

---

## Advanced Techniques

### Iterative Refinement

Start broad, then narrow:
1. "What are the main approaches to protein structure prediction?"
2. "How does AlphaFold3 compare to other methods?"
3. "What specific accuracy improvements does AF3 have for protein-ligand complexes?"

### Multi-Part Queries

Structure complex questions:
```
Please address the following about TOPIC:
1. Current state of the art
2. Recent developments (2024)
3. Key challenges and limitations
4. Future directions
```

### Source Quality Indicators

Request quality filtering:
- "Focus on peer-reviewed sources"
- "Prioritize primary research over news articles"
- "Include only studies with sample size > 100"

### Uncertainty Acknowledgment

Request honest uncertainty:
- "If information is uncertain or conflicting, please note this"
- "Distinguish between established facts and emerging research"

---

## Common Pitfalls

### Too Broad

**Problem**: "Tell me about AI"
**Solution**: "What are the key architectural innovations in large language models published in 2024?"

### Too Vague

**Problem**: "Is X good?"
**Solution**: "What are the advantages and disadvantages of X for use case Y, according to recent benchmarks?"

### Outdated Framing

**Problem**: "What is the latest version of TensorFlow?" (may get outdated answer)
**Solution**: "What is the current stable version of TensorFlow as of January 2025?"

### Missing Context

**Problem**: "How do I fix the error?"
**Solution**: "How do I fix 'ModuleNotFoundError: No module named pandas' in Python 3.12 on Windows?"

---

## Query Checklist

Before submitting a query, verify:

- [ ] **Specific topic** - Clear, focused subject
- [ ] **Time frame** - When should information be from?
- [ ] **Source type** - What kinds of sources are preferred?
- [ ] **Output format** - What type of answer is expected?
- [ ] **Context** - Relevant background included?

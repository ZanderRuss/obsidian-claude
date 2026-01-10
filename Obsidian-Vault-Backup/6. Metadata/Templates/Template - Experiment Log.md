---
tags:
  - type/experiment
  - content/research
  - status/running
type: experiment-log
created: {{date}}
modified: {{date}}
status: running
project:
experiment_id:
---

# Experiment: {{title}}

## Overview

| Field | Value |
|-------|-------|
| **Project** | [[]] |
| **Experiment ID** | exp-{{date}}-001 |
| **Status** | 🟡 Running |
| **Start Date** | {{date}} |
| **End Date** | |

---

## Objective

### What are we testing?


### Hypothesis
>

### Success Criteria
-

---

## Setup

### Configuration

```yaml
# Hyperparameters
model:
  type:
  hidden_size:
  layers:

training:
  learning_rate:
  batch_size:
  epochs:
  optimizer:
  scheduler:

data:
  train_split:
  val_split:
  test_split:
```

### Environment
- GPU:
- Framework:
- Commit:
- Random Seed:

### Dataset
| Split | Size | Source |
|-------|------|--------|
| Train | | |
| Val | | |
| Test | | |

---

## Baseline

### Baseline Configuration


### Baseline Results
| Metric | Value |
|--------|-------|
| | |

---

## Results

### Quantitative Results

| Metric | Baseline | This Run | Delta |
|--------|----------|----------|-------|
| | | | |

### Training Curves
![[exp-{{date}}-loss.png]]

### Key Observations
1.
2.

---

## Analysis

### What Worked?


### What Didn't Work?


### Unexpected Findings


---

## Ablations

| Ablation | Change | Result | Conclusion |
|----------|--------|--------|------------|
| | | | |

---

## Error Analysis

### Failure Cases


### Patterns in Errors


---

## Code

### Training Command
```bash

```

### Key Files
- `config.yaml`: Configuration
- `train.py`: Training script
- `eval.py`: Evaluation script

### Logs Location
- Wandb:
- Tensorboard:
- Checkpoints:

---

## Reproducibility

### Steps to Reproduce
1.
2.
3.

### Dependencies
```
pip install ...
```

---

## Conclusions

### Key Findings


### Implications for Paper


### Next Experiment


---

## Time Log

| Date | Activity | Hours |
|------|----------|-------|
| {{date}} | | |

---

## Notes

### {{date}}


---

## Related
- [[Paper Project - ]]
- [[Experiment - Previous]]

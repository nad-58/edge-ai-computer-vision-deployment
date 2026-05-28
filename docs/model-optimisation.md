# Model Optimisation

Model optimisation prepares a trained model for efficient deployment while preserving acceptable performance.

## Optimisation methods

- Architecture simplification
- Input-resolution tuning
- Operator fusion
- Quantisation
- Pruning
- Knowledge distillation
- Runtime-specific optimisation
- Preprocessing simplification
- Post-processing optimisation

## Evaluation expectations

For each optimisation, compare before and after behaviour:

- Accuracy or task-specific metric
- Latency
- Memory footprint
- Model size
- Robustness on difficult inputs
- Failure modes
- Compatibility with target runtime

## Review questions

- What optimisation was applied?
- Why was it needed?
- What acceptance criteria were used?
- Did the optimisation affect subgroup or edge-case performance?
- Was the optimised model validated on target hardware?

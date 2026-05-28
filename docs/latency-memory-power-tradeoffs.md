# Latency, Memory, and Power Trade-offs

Edge AI deployment requires balancing model quality with hardware constraints.

## Common trade-offs

| Decision | Benefit | Risk |
|---|---|---|
| Smaller model | Lower latency and memory | Reduced accuracy or robustness |
| Quantisation | Smaller model and faster inference | Accuracy drop or calibration sensitivity |
| Lower input resolution | Faster processing | Missed small features or reduced detail |
| Batch size of one | Real-time response | Lower throughput efficiency |
| Hardware acceleration | Faster inference | Runtime dependency and portability risk |

## Recommended reporting

- Mean, p50, and p95 latency
- Peak memory use
- Model size before and after optimisation
- Accuracy before and after optimisation
- Target hardware and runtime version
- Input resolution and preprocessing steps
- Thermal or power observations where relevant

## Review questions

- Is p95 latency within the product requirement?
- Is memory use within the deployment budget?
- Is accuracy loss after optimisation acceptable?
- Were measurements taken on representative hardware?

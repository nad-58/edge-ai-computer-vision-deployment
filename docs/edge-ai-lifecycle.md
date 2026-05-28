# Edge AI Deployment Lifecycle

Edge AI deployment requires an end-to-end engineering lifecycle that connects model design, hardware constraints, input quality, runtime behaviour, and production integration.

## Lifecycle stages

1. Define use case and operating environment
2. Define sensor, input data, and quality requirements
3. Select baseline model and target metrics
4. Optimise model architecture and preprocessing
5. Evaluate quantisation or compression impact
6. Profile latency, memory, throughput, and power
7. Validate on target hardware or representative hardware
8. Test robustness under real-world input variation
9. Integrate with application, firmware, or product software
10. Prepare release, monitoring, and update process

## Review questions

- What is the target hardware and runtime environment?
- What are the latency, memory, and power budgets?
- What input-quality variation is expected?
- What preprocessing and post-processing are required?
- Does quantisation materially affect accuracy?
- Does the model pass representative real-world tests?
- Is deployment behaviour traceable and reproducible?

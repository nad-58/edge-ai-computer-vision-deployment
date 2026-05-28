# Hardware-Aware Validation

Hardware-aware validation checks whether model behaviour remains acceptable when deployed on the actual or representative target hardware.

## Validation dimensions

- Runtime compatibility
- Operator support
- Numerical precision differences
- Quantisation impact
- Latency and jitter
- Peak memory use
- Thermal or power limitations
- Input/output integration
- Sensor and camera pipeline consistency
- Failure handling and logging

## Example hardware matrix

| Platform | Runtime | Precision | Latency target | Memory budget | Status |
|---|---|---|---:|---:|---|
| Embedded CPU | Native / ONNX Runtime | FP32 | 50 ms | 256 MB | Review |
| Edge GPU | TensorRT / OpenVINO | FP16 | 20 ms | 512 MB | Review |
| MCU/NPU | Vendor runtime | INT8 | 100 ms | 32 MB | Review |

## Review questions

- Was the model tested on the target runtime?
- Are numerical differences between desktop and embedded runs acceptable?
- Is performance stable across repeated runs?
- Are all required operators supported?
- Are hardware-specific limitations documented?

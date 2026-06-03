# Image Robustness Testing

Image robustness testing evaluates whether a computer vision model remains reliable when input images are affected by realistic variation in capture conditions, environment, sensor behaviour, and preprocessing.

## Robustness objectives

- Measure whether model predictions change under realistic image perturbations.
- Identify input conditions that cause performance degradation.
- Define acceptable performance drop thresholds.
- Link robustness findings to deployment constraints and monitoring needs.

## Common perturbation categories

### Camera and sensor variation

- Noise
- Pixelation
- Compression artefacts
- Sensor saturation
- Focus variation
- Resolution change

### Position and motion variation

- Rotation
- Translation
- Perspective change
- Motion blur
- Partial occlusion
- Scale change

### Environment variation

- Brightness increase
- Darkening
- Contrast variation
- Shadow
- Reflection
- Fog, rain, dust, or haze where relevant
- Background changes

## Recommended test structure

| Test | Perturbation level | Metric before | Metric after | Difference | Status |
|---|---|---:|---:|---:|---|
| Brightness change |  |  |  |  |  |
| Blur |  |  |  |  |  |
| Noise |  |  |  |  |  |
| Rotation |  |  |  |  |  |
| Compression |  |  |  |  |  |
| Occlusion |  |  |  |  |  |

## Review questions

- Are perturbations realistic for the deployment environment?
- Are perturbation levels justified?
- Does the model fail under common input-quality issues?
- Are failures concentrated in specific classes or object sizes?
- Does robustness differ across hardware, sensor, or site?
- Are low-quality inputs detected or handled safely?

## Decision output

The robustness review should conclude whether the model is robust enough for the intended deployment environment, whether additional data collection or model training is required, and whether monitoring or input-quality controls are needed.

# Computer Vision Error Analysis

Computer vision error analysis identifies the conditions, classes, objects, regions, or image-quality factors that drive model failures.

## Classification error analysis

For image classification, review:

- Confusion matrix
- Class confusion pairs
- Confident incorrect predictions
- Low-confidence correct predictions
- Per-class performance
- Performance by brightness, contrast, sharpness, blur, and occlusion

## Object detection error analysis

For object detection, review:

- Missed objects
- Background false detections
- Duplicate detections
- Incorrect class detections
- Poor localization
- Small-object failures
- Occlusion-related failures
- Performance by object size and image quality

## Segmentation error analysis

For segmentation, review:

- False-positive regions
- False-negative regions
- Boundary errors
- Small-structure errors
- Class confusion at pixel level
- Per-class Dice or IoU
- Case-level outliers

## Image-quality segments

Recommended image-quality segments include:

- Low brightness
- High brightness
- Low contrast
- Low sharpness
- Motion blur
- High noise
- Partial occlusion
- Small object size
- Crowded scene

## Reviewer conclusion

The error analysis should identify whether failures are random, systematic, related to input quality, related to class imbalance, linked to deployment hardware, or caused by data/annotation limitations.

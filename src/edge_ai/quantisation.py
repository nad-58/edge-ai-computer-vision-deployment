from __future__ import annotations


def quantisation_impact(
    baseline_accuracy: float,
    quantised_accuracy: float,
    baseline_model_size_mb: float,
    quantised_model_size_mb: float,
) -> dict:
    """Compare baseline and quantised model behaviour using simple deployment metrics."""
    accuracy_delta = quantised_accuracy - baseline_accuracy
    size_reduction_mb = baseline_model_size_mb - quantised_model_size_mb
    size_reduction_percent = (size_reduction_mb / baseline_model_size_mb) * 100 if baseline_model_size_mb else 0.0
    return {
        "baseline_accuracy": baseline_accuracy,
        "quantised_accuracy": quantised_accuracy,
        "accuracy_delta": accuracy_delta,
        "baseline_model_size_mb": baseline_model_size_mb,
        "quantised_model_size_mb": quantised_model_size_mb,
        "size_reduction_mb": size_reduction_mb,
        "size_reduction_percent": size_reduction_percent,
    }


def quantisation_acceptance(impact: dict, max_accuracy_drop: float = 0.02) -> dict:
    """Assess whether the accuracy drop after quantisation is acceptable."""
    accuracy_drop = impact["baseline_accuracy"] - impact["quantised_accuracy"]
    return {
        "accuracy_drop": accuracy_drop,
        "max_accuracy_drop": max_accuracy_drop,
        "passed": accuracy_drop <= max_accuracy_drop,
    }

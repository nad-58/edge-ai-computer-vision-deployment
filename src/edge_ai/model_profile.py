from __future__ import annotations


def model_memory_profile(
    parameter_count: int,
    bytes_per_parameter: int = 4,
    activation_memory_mb: float = 0.0,
) -> dict:
    """Estimate model memory footprint from parameters and activation memory."""
    parameter_memory_mb = (parameter_count * bytes_per_parameter) / (1024 * 1024)
    total_memory_mb = parameter_memory_mb + activation_memory_mb
    return {
        "parameter_count": parameter_count,
        "bytes_per_parameter": bytes_per_parameter,
        "parameter_memory_mb": parameter_memory_mb,
        "activation_memory_mb": activation_memory_mb,
        "estimated_total_memory_mb": total_memory_mb,
    }


def deployment_fit(memory_profile: dict, memory_budget_mb: float) -> dict:
    """Check whether the estimated model memory fits a deployment memory budget."""
    required_mb = float(memory_profile["estimated_total_memory_mb"])
    return {
        "memory_budget_mb": memory_budget_mb,
        "required_memory_mb": required_mb,
        "passed": required_mb <= memory_budget_mb,
        "margin_mb": memory_budget_mb - required_mb,
    }

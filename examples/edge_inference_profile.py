from edge_ai.latency import latency_acceptance, latency_summary
from edge_ai.model_profile import deployment_fit, model_memory_profile
from edge_ai.quantisation import quantisation_acceptance, quantisation_impact


def main() -> None:
    latency_ms = [18.2, 19.1, 21.4, 20.7, 18.9, 22.8, 19.6, 20.1]
    latency = latency_summary(latency_ms)
    latency_result = latency_acceptance(latency, target_ms=25.0)

    memory = model_memory_profile(
        parameter_count=1_250_000,
        bytes_per_parameter=4,
        activation_memory_mb=7.5,
    )
    memory_result = deployment_fit(memory, memory_budget_mb=32.0)

    quantisation = quantisation_impact(
        baseline_accuracy=0.932,
        quantised_accuracy=0.921,
        baseline_model_size_mb=18.5,
        quantised_model_size_mb=5.2,
    )
    quantisation_result = quantisation_acceptance(quantisation, max_accuracy_drop=0.02)

    print("Edge inference profile")
    print("======================")
    print("\nLatency summary")
    print(latency)
    print(latency_result)

    print("\nMemory profile")
    print(memory)
    print(memory_result)

    print("\nQuantisation impact")
    print(quantisation)
    print(quantisation_result)


if __name__ == "__main__":
    main()

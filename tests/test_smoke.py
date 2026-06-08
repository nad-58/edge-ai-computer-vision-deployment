from edge_ai.latency import latency_acceptance, latency_summary
from edge_ai.model_profile import deployment_fit, model_memory_profile
from edge_ai.quantisation import quantisation_acceptance, quantisation_impact


def test_edge_utilities():
    latency = latency_acceptance(latency_summary([10, 12, 11]), 15)
    memory = deployment_fit(model_memory_profile(1000000, 4, 2), 10)
    quant = quantisation_acceptance(quantisation_impact(0.95, 0.94, 20, 6), 0.02)
    assert latency["passed"]
    assert memory["passed"]
    assert quant["passed"]

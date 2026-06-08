# Contributing

Contributions that improve edge-AI examples, profiling utilities, deployment checklists, tests, and documentation are welcome.

## Development setup

```bash
python -m venv .venv
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

Run the examples from the repository root:

```bash
PYTHONPATH=src python examples/edge_inference_profile.py
PYTHONPATH=src python examples/model_latency_report.py
PYTHONPATH=src python examples/deployment_readiness_report.py
```

## Guidelines

- Keep changes focused and hardware-agnostic unless the scope is clearly documented.
- Use synthetic or publicly shareable inputs.
- Add type hints and docstrings to reusable Python code.
- Document assumptions for latency, memory, power, and quantisation results.
- Add tests or runnable examples for new behaviour.

## Commit prefixes

Use `feat:`, `fix:`, `docs:`, `test:`, `refactor:`, or `chore:`.

## Pull requests

Describe the purpose, target hardware/runtime assumptions, validation performed, and known limitations.

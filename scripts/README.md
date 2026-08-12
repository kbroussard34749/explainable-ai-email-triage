# Build and Validation Scripts

These utilities build the ignored local model artifact and verify the repository's demonstration and evidence records. Run them from the repository root after installing [`requirements-demo.txt`](../requirements-demo.txt).

## Recommended Order

| Order | Command | Purpose |
|---:|---|---|
| 1 | `PYTHONPATH=src python scripts/build_week7_demo_model.py` | Recreates the frozen 159-message training candidate and writes privacy-safe model metadata. |
| 2 | `PYTHONPATH=src python -m unittest -v tests/test_week7_demo.py tests/test_week7_readiness.py` | Runs all 13 API, safety, and evidence-integrity tests. |
| 3 | `PYTHONPATH=src python scripts/validate_week7_demo.py` | Checks the local artifact boundary, deterministic scoring, non-echoed input, visible thresholds, bounded explanations, and descriptive local timing. |
| 4 | `python scripts/validate_week7_readiness.py --output results/metrics/week7_readiness_precheck.json` | Reconciles required evidence, notebook execution, the frozen decision, gate values, prohibited columns, and evidence hashes. |
| 5 | `PYTHONPATH=src uvicorn email_triage_demo.app:app --host 127.0.0.1 --port 8765` | Starts the controlled local demonstration. |

## Script Responsibilities

### [`build_week7_demo_model.py`](build_week7_demo_model.py)

- Verifies the frozen 199-message reviewed population.
- Recreates the original stratified 159/40 split with seed 42.
- Fits only the 159-message training partition.
- Keeps the selection-influenced preliminary holdout out of model fitting.
- Saves the fitted artifact locally while tracking only privacy-safe metadata and its digest.

### [`validate_week7_demo.py`](validate_week7_demo.py)

- Uses synthetic functional probes rather than private messages.
- Repeats three cases 20 times each to check deterministic inference.
- Verifies research-only metadata and the artifact digest.
- Records local timing as an engineering observation, not a production guarantee.

### [`validate_week7_readiness.py`](validate_week7_readiness.py)

- Confirms required notebooks were executed without saved exceptions.
- Recomputes the Week 7 gate comparison from frozen Week 6 metrics.
- Preserves `revise` and denies deployment and shadow-testing approval.
- Screens selected tracked tables for prohibited sensitive columns.
- Hashes the exact evidence used by the readiness record.

## Related Guidance

- [`../docs/week7_demo_runbook.md`](../docs/week7_demo_runbook.md)
- [`../tests/README.md`](../tests/README.md)
- [`../results/README.md`](../results/README.md)

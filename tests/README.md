# Automated Test Guide

The automated suite contains 13 tests covering application behavior and evidence integrity. The reader-facing results are documented in [`../docs/week7_automated_test_report.md`](../docs/week7_automated_test_report.md).

## Test Groups

| Test file | Tests | Coverage |
|---|---:|---|
| [`test_week7_demo.py`](test_week7_demo.py) | 8 | Research-use disclosure, health state, valid analysis response, human review, non-retention response boundary, invalid input, and safe missing-model behavior |
| [`test_week7_readiness.py`](test_week7_readiness.py) | 5 | Required evidence, executed notebooks, frozen `revise` decision, metric traceability, and prohibited-column screening |

## Run the Suite

From the repository root:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-demo.txt
PYTHONPATH=src python -m unittest -v \
  tests/test_week7_demo.py tests/test_week7_readiness.py
PYTHONPATH=src python scripts/validate_week7_demo.py
python scripts/validate_week7_readiness.py \
  --output results/metrics/week7_readiness_precheck.json
```

## Recorded Outcome

- 13 of 13 automated tests passed in the recorded clean-environment run.
- All five Gate A demonstration validation checks passed.
- The Week 7 readiness precheck passed.
- The model disposition remains `revise`.

## What Passing Does Not Establish

These tests establish application contracts, reproducibility safeguards, and evidence consistency. They do not establish predictive accuracy, demographic fairness, production latency, deployment approval, or shadow-testing approval.

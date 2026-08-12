# Week 7 Controlled Local Demonstration Runbook

## Scope

This runbook supports a repeatable local research demonstration for Week 8. The application is not approved for production routing or shadow testing. The model disposition remains `revise`, and every result requires human review.

Use only synthetic or privacy-screened messages during the demonstration. Do not paste private email content, reviewer notes, credentials, or other sensitive information.

## Environment

- Python 3.11.8
- FastAPI 0.141.1
- Uvicorn 0.52.1
- scikit-learn 1.9.0
- pandas 3.0.5 in the clean-environment validation
- joblib 1.5.3
- fixed random seed: 42
- local-only model path: `models/week7_research_demo.joblib`

The model file is intentionally excluded from Git. Its SHA-256 digest and frozen configuration are recorded in `results/metrics/week7_demo_model_metadata.json`.

## Build and verify

From the repository root:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-demo.txt
PYTHONPATH=src python scripts/build_week7_demo_model.py
PYTHONPATH=src python -m unittest -v tests/test_week7_demo.py tests/test_week7_readiness.py
PYTHONPATH=src python scripts/validate_week7_demo.py
python scripts/validate_week7_readiness.py --output results/metrics/week7_readiness_precheck.json
```

The build uses the frozen 159-message Week 4 training partition. It does not retrain on the 40-message preliminary holdout and does not create new reliability evidence.

## Start the demonstration

```bash
PYTHONPATH=src uvicorn email_triage_demo.app:app --host 127.0.0.1 --port 8765
```

Open `http://127.0.0.1:8765/`. Confirm that the banner states `revise`, requires human review, and denies production and shadow-testing approval.

## Demonstration sequence

1. Use a synthetic message containing an explicit time-sensitive request.
2. Select **Analyze**.
3. Show the urgency score and compare classifications at thresholds 0.45 and 0.50.
4. Explain that the positive and negative feature contributions describe the fitted model and are not causal explanations.
5. Point out `Input retained: no`, `Deployment approved: no`, and the required human-review status.
6. Explain that differing threshold classifications demonstrate the unresolved evidence gap rather than production readiness.

## Safe-failure check

To test missing-artifact handling without deleting the model, start a second process with a nonexistent path:

```bash
EMAIL_TRIAGE_DEMO_MODEL=models/not_present.joblib PYTHONPATH=src \
  uvicorn email_triage_demo.app:app --host 127.0.0.1 --port 8766
```

The health endpoint must report `not_ready`, and `/api/analyze` must return HTTP 503 without exposing a stack trace or message content.

## Evidence and limitations

- `docs/week7_automated_test_report.md`: reader-facing purpose, coverage, results, and limitations for all 13 automated tests
- `results/metrics/week7_demo_model_metadata.json`: configuration and artifact hashes
- `results/metrics/week7_demo_validation.json`: deterministic inference, privacy, boundary, and local timing checks
- `docs/week7_conditional_advancement_gates.md`: Gate A status and Gates B through D boundaries

Local startup and inference measurements are engineering observations from one computer. They are not service-level objectives or production guarantees. Passing Gate A does not satisfy the untouched-evaluation, predictive-reliability, security, privacy-approval, monitoring, or release-decision requirements for deployment.

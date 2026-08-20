# Week 7 Automated Test and Validation Report

**Execution date:** August 12, 2026

**Overall result:** 13 of 13 automated tests passed

**Demonstration validation:** Passed

**Readiness precheck:** Passed
**Model disposition:** `revise`

## Technical summary

The automated test suite passed all 13 tests in 0.088 seconds in a clean Python 3.11.8 environment created from `requirements-demo.txt`. The tests confirmed the local application's API behavior, input validation, safe failure response, research-use disclosures, privacy-conscious response boundary, saved-notebook execution, metric traceability, and preservation of the Week 6 `revise` decision.

The separate demonstration validator also passed all five Gate A checks. It repeated three synthetic cases 20 times each, for 60 total inferences, and produced identical scores for each repeated case. These results establish a repeatable local research demonstration. They do not establish predictive reliability, demographic fairness, shadow-testing approval, or production readiness.

## What the tests cover

The verification package uses three related layers:

1. **API contract tests** confirm what a user can observe at the local web-service boundary.
2. **Evidence-integrity tests** confirm that saved records still support the documented Week 6 and Week 7 conclusions.
3. **Demonstration validation** checks a fixed local artifact for deterministic inference, bounded explanations, privacy-conscious output, threshold visibility, and descriptive local timing.

This separation is intentional. Engineering tests can demonstrate that the application behaves as designed, but they cannot replace an untouched labeled evaluation of model performance.

## All 13 automated tests passed

| Test | What it verifies | Result |
|---|---|---|
| `test_index_discloses_research_boundary` | The interface identifies the application as a research prototype and requires human review. | Pass |
| `test_health_preserves_revise_and_no_approval` | A ready service still reports `revise` and denies deployment and shadow-testing approval. | Pass |
| `test_valid_request_returns_thresholds_and_human_review` | A valid request returns both frozen threshold decisions, requires human review, and does not echo the submitted message. | Pass |
| `test_empty_input_is_rejected` | Whitespace-only subject and body input is rejected. | Pass |
| `test_missing_fields_are_rejected` | A request without message content is rejected. | Pass |
| `test_malformed_json_is_rejected` | Invalid JSON is rejected at the API boundary. | Pass |
| `test_unusually_long_input_is_rejected` | Input beyond the documented defensive limit is rejected. | Pass |
| `test_missing_model_fails_safely` | A missing model produces a controlled not-ready state and HTTP 503 response instead of a fabricated prediction. | Pass |
| `test_overall_precheck_passes` | All required readiness evidence is present and internally consistent. | Pass |
| `test_week6_decision_remains_revise` | Later demonstration work has not changed the frozen Week 6 decision or created deployment approval. | Pass |
| `test_notebooks_are_executed_without_saved_errors` | Required notebooks have no unexecuted code cells or saved exception outputs. | Pass |
| `test_gate_values_trace_to_week6_summary` | Week 7 gate comparisons reproduce the saved Week 6 cross-validation values. | Pass |
| `test_privacy_sensitive_columns_are_absent` | Reviewed tracked tables do not contain the prohibited message-content or reviewer-note columns. | Pass |

## Gate A demonstration validation passed

| Validation check | Evidence | Result |
|---|---|---|
| Artifact boundary | Metadata identifies the artifact as local research only, retains `revise`, denies deployment and shadow testing, requires human review, and matches the recorded artifact digest. | Pass |
| Deterministic repeated scoring | Three synthetic cases were each scored 20 times with identical results within each case. | Pass |
| Input not echoed or retained in results | Complete synthetic subjects and bodies were absent from the saved result structure. | Pass |
| Threshold visibility | Every case reported classifications at both 0.45 and 0.50. | Pass |
| Bounded explanations | Each positive and negative feature list remained limited to five entries. | Pass |

The tracked validation record reports 60 local inference observations with a median of 1.511 milliseconds, a 95th-percentile observation of 1.937 milliseconds, and a maximum of 24.495 milliseconds. Model loading took 4.904 milliseconds. These measurements describe one local validation run; they are not a load test, service-level objective, or production guarantee.

## Reproducible execution

The recorded unit-test run used these pinned components:

| Component | Version |
|---|---:|
| Python | 3.11.8 |
| FastAPI | 0.141.1 |
| HTTPX | 0.28.1 |
| joblib | 1.5.3 |
| NumPy | 2.4.6 |
| pandas | 3.0.5 |
| scikit-learn | 1.9.0 |
| Uvicorn | 0.52.1 |

From the repository root, the professor can independently reproduce the automated test result with:

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

## Evidence chain

- `tests/test_week7_demo.py` contains the eight API contract tests.
- `tests/test_week7_readiness.py` contains the five evidence-integrity tests.
- `results/metrics/week7_demo_validation.json` preserves structured Gate A results and local timing observations.
- `results/metrics/week7_readiness_precheck.json` preserves notebook checks, decision checks, metric reconciliation, privacy screening, and SHA-256 evidence hashes.
- `results/metrics/week7_demo_model_metadata.json` preserves the local artifact configuration, dependency versions, source-manifest digest, and research-only decision boundary without including email text.
- `docs/week7_demo_runbook.md` provides the build, verification, demonstration, and safe-failure procedures.

The Markdown report is the reader-facing explanation. The JSON files preserve exact structured evidence, while the Python tests and validators allow independent verification.

## Interpretation and limitations

Passing these tests means the controlled local demonstration is reproducible and behaves according to its documented safeguards. It also means that the supporting evidence remains internally consistent with the Week 6 result.

The result does not mean that the classifier is ready for deployment. The synthetic cases are functional probes rather than a labeled accuracy sample. The API tests use a fixed fake service to isolate interface behavior from model quality. Predictive advancement still requires a separately designed untouched evaluation that passes the documented Gate B recall, precision, F1, false-positive-rate, stability, calibration, error-review, and uncertainty requirements.

## Conclusion

The professor can review the purpose, coverage, results, evidence, and limitations without running the code. The executable tests and exact commands remain available for independent confirmation. Gate A supports a controlled local research demonstration only; the model remains `revise`, and production and shadow testing remain unapproved.

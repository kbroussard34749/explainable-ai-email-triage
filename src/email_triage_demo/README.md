# Local Demonstration Application

This package provides the controlled local research demonstration. It exposes the frozen candidate's score, threshold sensitivity, and bounded linear-model explanation while preserving the `revise` decision and required human review.

## High-Level Flow

```text
Synthetic or privacy-screened message
                │
                ▼
      FastAPI request validation
                │
                ▼
      Verified local model artifact
                │
                ▼
  TF-IDF and logistic-regression score
                │
                ▼
  0.45 and 0.50 threshold comparison
                │
                ▼
Bounded feature contributions and safeguards
                │
                ▼
 Human review; no automated routing action
```

## Components

| File | Responsibility |
|---|---|
| [`app.py`](app.py) | Defines the web interface, API input limits, health state, safe missing-model response, local timing observation, and non-retention response boundary. |
| [`model_service.py`](model_service.py) | Recreates the frozen pipeline, validates artifact metadata, locates the urgent-class probability, compares the two frozen thresholds, and calculates bounded feature contributions. |
| [`__init__.py`](__init__.py) | Defines the package and demonstration version. |

## Design Boundaries

- A successful health response means the local service can load and respond; it does not mean the model is reliable.
- The application compares the frozen thresholds but does not select a new operating threshold.
- Feature contributions explain the fitted linear calculation and are not causal explanations.
- The response does not echo or save the complete subject or body.
- Every result requires human review.
- Deployment and shadow testing remain unapproved.

## Run and Verify

- Follow the [`demonstration runbook`](../../docs/week7_demo_runbook.md).
- Review [`automated test coverage`](../../tests/README.md).
- Read the [`recorded test results`](../../docs/week7_automated_test_report.md).

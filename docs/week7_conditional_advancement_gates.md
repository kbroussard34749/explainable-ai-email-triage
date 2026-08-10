# Week 7 Conditional Advancement Gates

## Purpose

This document defines the evidence required before the Explainable AI Email Triage project can move beyond a controlled local research demonstration. It extends the Week 6 `revise` decision without changing that historical result.

The proposed outcome for Weeks 7 and 8 is a **demonstration-ready research prototype with a conditional deployment recommendation**. Passing the demonstration gates does not establish predictive reliability or authorize production use.

## Evidence boundaries

- Week 6 artifacts, metrics, data splits, figures, and the `revise` decision remain frozen.
- New model evidence must use a separately versioned dataset, experiment record, and decision artifact.
- The 40-message preliminary holdout cannot become an untouched final test set.
- Interface behavior, API availability, or successful local execution cannot be reported as model reliability.
- Only privacy-screened or synthetic message content may appear in a demonstration or submitted artifact.
- A person remains responsible for reviewing predictions and deciding what action to take.

## Gate A: Research demonstration readiness

These gates determine whether the repository can support the Week 8 local demonstration.

| Gate | Acceptance evidence | Current state |
|---|---|---|
| Reproducible setup | A documented clean-environment command installs dependencies and runs the demonstration with fixed configuration and version information. | To validate |
| Deterministic model workflow | Repeated runs using the same data, configuration, and seed reproduce the recorded outputs within documented numerical tolerance. | Partially supported; demo validation needed |
| Input validation | Automated tests cover empty input, malformed input, unusually long input, and missing required fields. | To implement |
| Explainable output | Each demonstration result presents the urgency score, applied threshold, predicted class, and a bounded explanation suitable for human review. | Research explanations exist; demo integration needed |
| Human review | The interface identifies every result as decision support and requires a person to make or confirm the routing decision. | Design requirement |
| Privacy controls | Demonstration inputs are synthetic or privacy-screened, and logs exclude email bodies, subjects, excerpts, and reviewer notes. | Design requirement; verify during implementation |
| Failure handling | The demonstration fails safely and reports a clear error when the model, configuration, or required resource is unavailable. | To implement |
| Local performance record | Startup and per-message inference times are measured on the demonstration computer and reported as engineering observations, not production guarantees. | To measure |
| Verification package | Automated tests, a short runbook, configuration record, and sample privacy-safe outputs are saved in the repository. | To create |

Passing Gate A supports the phrase **controlled local research demonstration** only.

## Gate B: Predictive-reliability advancement

These gates determine whether a new model candidate merits consideration for supervised shadow testing. They are project-specific research criteria, not course requirements, external standards, or production service-level objectives.

### Provisional capstone planning workload

The Week 7 readiness assessment uses a bounded planning scenario of 100 incoming messages per review period. The provisional reviewer-capacity limit is no more than 10 false alerts per 100 nonurgent messages. These assumptions are confirmed for the capstone assessment but have not been validated with an operational stakeholder and must not be presented as production requirements. Because the urgency-enriched research sample cannot establish a production prevalence, precision is evaluated directly and the effect of prevalence must remain disclosed.

Missed urgent messages are treated as the primary error cost. The model must identify at least four of every five urgent messages while ensuring that at least half of its urgent alerts are correct. Those two requirements imply an F1 score slightly above 60%; the project uses 60% as the minimum balanced-performance gate.

| Gate | Provisional Week 7 acceptance criterion | Reason |
|---|---|---|
| Untouched evaluation | Reserve a new test set that is not used for model, feature, calibration, or threshold selection. | Prevents another selection-influenced estimate. |
| Urgent recall | At least 80% on the untouched evaluation set. | Limits missed urgent messages to no more than one in five in the evaluated sample. |
| Urgent precision | At least 50% on the untouched evaluation set. | Requires at least half of urgent alerts to be correct. |
| Urgent F1 | At least 60% on the untouched evaluation set. | Requires recall and precision to be useful together rather than allowing either metric to pass alone. |
| Review burden | No more than 10 false alerts per 100 evaluated nonurgent messages, equivalent to a false-positive rate no greater than 10%. | Connects the guardrail to the approved planning workload and reviewer capacity. |
| Threshold stability | Reject a threshold that collapses predictions into nearly one class; report prediction rates and results by fold. | Rejects the Week 6 failure pattern. |
| Calibration | Require improvement over the applicable constant-probability reference and save a calibration assessment. | Requires scores to be more useful than the Week 6 probability estimates. |
| Error review | Review all urgent false negatives and a reproducible sample of false positives using privacy-safe categories. | Connects aggregate metrics to common failure patterns. |
| Uncertainty disclosure | Report confidence intervals or another justified uncertainty summary with the primary metrics. | Prevents point estimates from overstating a small evaluation set. |

### Basis for the numerical gates

The provisional gates were established before any new model training or threshold search:

1. The 100-message planning workload provides a common review-period denominator without claiming it is a measured production workload.
2. The 10-false-alert capacity produces a 10% maximum false-positive rate on evaluated nonurgent messages.
3. The 80% recall minimum reflects the higher consequence assigned to missed urgent messages.
4. The 50% precision minimum prevents the urgent queue from being dominated by false alerts.
5. Precision of 50% and recall of 80% yield an F1 score of approximately 61.5%, supporting a rounded 60% minimum.
6. The enriched research prevalence remains unsuitable as a production prevalence estimate, so prevalence sensitivity must be disclosed.
7. These targets apply prospectively to a new untouched evaluation and are used retrospectively only to describe why the frozen Week 6 candidate does not advance.

Passing Gate B would justify a new model decision review. It would not automatically approve shadow testing or production deployment.

### Current-candidate evaluation

Neither frozen Week 6 operating point passes Gate B. This comparison does not reopen model or threshold selection.

| Week 6 operating point | Recall gate | Precision gate | F1 gate | Review-burden gate | Threshold-stability gate | Overall |
|---|---|---|---|---|---|---|
| `0.45` | Pass: 100.0% | Fail: 15.1% | Fail: 26.2% | Fail: 135 false positives among 135 nonurgent messages | Fail: every message predicted urgent | Fail |
| `0.50` | Fail: 8.3% | Pass: 100.0% | Fail: 15.4% | Pass: 0 false positives among 135 nonurgent messages | Fail: only 2 of 159 messages predicted urgent and 157 probabilities fell between `0.45` and `0.50` | Fail |

Under the provisional planning assumptions, the evaluation confirms the Week 6 `revise` disposition. It does not supply the untouched evidence required for a future candidate to pass Gate B.

### Required sensitivity disclosure

Week 7 reporting must show that the gate decision depends on a stated planning workload rather than a measured production workload. Before any operational recommendation, the review-burden calculation must be repeated across plausible message volumes, urgent-message prevalence levels, and reviewer-capacity limits. A result that passes only one favorable assumption cannot support advancement.

## Gate C: Supervised shadow-testing recommendation

Gate C can be considered only after Gate B passes.

- A written review-capacity limit and escalation procedure are approved.
- Predictions do not alter delivery, routing, deletion, prioritization, or notification behavior.
- Authorized reviewers can compare model suggestions with normal human decisions.
- Monitoring covers input validity, score distribution, prediction distribution, latency, errors, and drift without retaining unnecessary message content.
- A stop condition and rollback procedure are documented and tested.
- Access control, dependency, and privacy reviews are completed.
- A named human decision record explicitly approves the bounded shadow test.

Passing Gate C supports only a time-bounded, human-supervised shadow-testing recommendation.

## Gate D: Production deployment

Production approval is outside the current evidence and is not a Week 7 or Week 8 completion claim. It would require a separate operational evaluation, security and privacy approval, monitoring ownership, incident response, rollback validation, and an explicit accountable release decision.

## Planned Week 7 and Week 8 use

### Week 7

- Report the Week 6 `revise` disposition unchanged.
- Explain the evidence gap using the failed threshold tradeoff, limited reviewed sample, and lack of an untouched final evaluation.
- Establish Gates A through C and evaluate the frozen candidate against Gate B without changing Week 6 selection or results.
- Validate Gate A before finalizing the Week 7 report and presentation.
- Report which gates pass, fail, or remain untested.

### Week 8

- Demonstrate the Gate A workflow validated during Week 7.
- Demonstrate scoring, explanation, threshold visibility, human review, privacy-safe logging, and safe failure behavior.
- Report Gate B as future model-reliability work unless a separately preregistered experiment is completed.
- Keep Gate C and production deployment explicitly unapproved.

## Remaining approval checkpoints

Before a new reliability experiment or shadow test begins, review and approve:

1. the new dataset and untouched evaluation design;
2. the candidate model and preregistered selection method;
3. whether Week 7 should implement a command-line, notebook, or local web demonstration for Week 8 delivery;
4. whether expanded labeling is in scope after the required Week 7 and Week 8 deliverables are secure.

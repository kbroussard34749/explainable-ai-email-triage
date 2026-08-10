# Week 7 Conditional Readiness Evaluation

## Decision

The frozen Week 6 candidate remains **revise**. It does not meet the Week 7 predictive-reliability gates and is not approved for shadow testing or production deployment.

The repository may advance toward a controlled local research demonstration only after the separate demonstration-readiness checks are implemented and validated. A working demonstration will not change the model-reliability decision.

## Evaluation scope

This record applies the Week 7 gates to existing, frozen Week 6 cross-validation evidence. It does not retrain the model, reopen threshold selection, reinterpret the preliminary holdout, or create new predictive-performance evidence.

## Provisional capstone planning assumptions

- Review period: 100 incoming messages.
- Maximum added review burden: 10 false alerts per 100 evaluated nonurgent messages.
- Primary error cost: missed urgent messages.
- Minimum urgent recall: 80%.
- Minimum urgent precision: 50%.
- Minimum urgent F1: 60%.
- Maximum false-positive rate: 10%.
- The urgency-enriched research sample is not treated as a production prevalence estimate.

These assumptions and their derived numerical gates are confirmed for the Week 7 capstone assessment. They are not stakeholder-validated production requirements, and the uncertainty must remain disclosed.

The 60% F1 requirement is consistent with the balance implied by 50% precision and 80% recall: `2 * 0.50 * 0.80 / (0.50 + 0.80) = 0.615`, rounded down to a 0.60 minimum gate.

## Frozen-candidate results

| Operating point | Urgent precision | Urgent recall | Urgent F1 | False positives | False-positive rate | Positive rate |
|---|---:|---:|---:|---:|---:|---:|
| `0.45` | 15.1% | 100.0% | 26.2% | 135 of 135 nonurgent | 100.0% | 100.0% |
| `0.50` | 100.0% | 8.3% | 15.4% | 0 of 135 nonurgent | 0.0% | 1.3% |

## Gate results

| Gate | `0.45` | `0.50` | Finding |
|---|---|---|---|
| Urgent recall >= 80% | Pass | Fail | Lowering the threshold removed false negatives only by predicting every message urgent. |
| Urgent precision >= 50% | Fail | Pass | The two operating points achieve precision and recall at opposite, unusable extremes. |
| Urgent F1 >= 60% | Fail | Fail | Neither operating point provides useful balanced performance. |
| False-positive rate <= 10% | Fail | Pass | The lower threshold exceeds the review-capacity assumption by the full nonurgent population. |
| Threshold stability | Fail | Fail | At `0.45`, all 159 messages are predicted urgent. At `0.50`, only 2 are predicted urgent, and 157 probabilities lie from `0.45` to below `0.50`. |
| Calibration | Fail | Fail | The Week 6 Brier score of 0.237 is worse than the constant training-prevalence reference of 0.128. |
| Untouched evaluation | Not available | Not available | The 40-message holdout influenced earlier work and remains preliminary descriptive evidence. |

## Interpretation

The current candidate contains some ranking signal, but it does not provide a reliable operating point. Threshold `0.45` satisfies the recall requirement by eliminating triage value, while `0.50` satisfies the false-positive limit by missing most urgent examples. The current evidence therefore supports continued model revision and a controlled demonstration of the research workflow, not a recommendation to deploy the model.

## Week 7 and Week 8 use

- Week 7 may report that the reliability gates were established and the frozen candidate failed them.
- Week 7 must separately validate demonstration readiness before claiming the repository supports a controlled local demonstration.
- Week 8 may demonstrate the validated workflow and explain the failed reliability gates.
- A new candidate can be considered only through a separately versioned and preregistered experiment with newly reserved untouched evaluation data.

## Source artifacts

- `docs/week6_experiment_record.md`
- `results/metrics/week6_cv_summary.csv`
- `results/metrics/week6_threshold_analysis.csv`
- `results/metrics/week6_model_decision.csv`
- `results/metrics/week6_reproducibility.json`

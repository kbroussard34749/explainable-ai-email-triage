# Week 6 Testing and Debugging Experiment Record

## Purpose

This record documents the executed `notebooks/week6_testing_debugging.ipynb` workflow. It explains the testing method, preserves the training-only decision made before the preliminary holdout comparison, and identifies the evidence used in the Week 6 Model Testing and Debugging Report.

## Question and decision

Can a probability-threshold change improve urgent-message reliability for the frozen Week 4 candidate without creating an unusable review burden?

**Decision:** Revise the candidate before deployment or shadow testing. The `0.45` threshold removed urgent false negatives only by labeling every evaluated message urgent. The default `0.50` threshold preserved a smaller review queue but missed most urgent examples. The 40-message preliminary holdout repeated the same tradeoff and did not change the decision.

No deployable model artifact was saved. The notebook, privacy-safe error records, aggregate metrics, figures, and reproducibility hashes preserve the experiment without implying that the candidate is ready for use.

## Scope and inputs

- Modeling population: 199 reviewed messages, including 169 nonurgent and 30 urgent.
- Preserved split: 159 training messages and 40 preliminary holdout messages, stratified with `random_state=42`.
- Frozen candidate: class-balanced logistic regression with `C=0.1`, unigram TF-IDF, English stop-word removal, `min_df=2`, and sublinear term frequency.
- Week 6 selection boundary: all threshold selection remained inside the 159-message training partition.
- Preliminary holdout role: one descriptive comparison after the training diagnostics and **revise** disposition were frozen.
- Privacy boundary: exported evidence contains no subjects, bodies, excerpts, reviewer notes, or unnecessary personal information.

## Testing method

The notebook used nested stratified cross-validation because the project has labeled historical data but no deployed treatment-and-control environment for an A/B test.

1. Five outer stratified folds evaluated the complete threshold-selection procedure.
2. Four inner stratified folds generated out-of-fold probabilities inside each outer training portion.
3. The inner loop evaluated thresholds from `0.20` through `0.50` in increments of `0.05`.
4. Thresholds were ranked by urgent F1, then urgent recall, fewer false positives, and the higher threshold if all preceding criteria remained tied.
5. A lower threshold passed the preregistered reliability rule only when aggregate outer-CV urgent recall improved and urgent F1 did not decrease relative to `0.50`.
6. After the nested procedure was evaluated, five-fold out-of-fold training probabilities selected and froze the `0.45` comparison threshold.

The reliability rule passed mathematically, but it did not include an operational specificity or review-capacity guardrail. Error analysis therefore remained necessary before treating the lower threshold as useful.

## Cross-validation results

The aggregate results use the 159 concatenated outer-fold predictions, so each training message contributes exactly once.

| Strategy | Urgent precision | Urgent recall | Urgent F1 | False positives | Urgent false negatives | Positive rate |
|---|---:|---:|---:|---:|---:|---:|
| Nested-selected `0.45` | 15.1% | 100.0% | 26.2% | 135 | 0 | 100.0% |
| Default `0.50` | 100.0% | 8.3% | 15.4% | 0 | 22 | 1.3% |

Threshold `0.45` satisfied the narrow recall-and-F1 rule, but it classified all 159 outer-fold messages as urgent. Its 15.1% urgent precision equals the urgent prevalence in the training partition, so it provided no reduction in review workload. Threshold `0.50` classified only two messages urgent and missed 22 of 24 urgent messages.

## Error analysis and debugging findings

The privacy-safe error file contains 157 records at the strategy-message grain:

- 135 false positives at `0.45`;
- 22 false negatives at `0.50`; and
- no holdout identifiers or message text.

The urgent probabilities span only 0.4643 to 0.5054, and 157 of 159 fall from `0.45` to below `0.50`. That compression explains why a five-point threshold change flips nearly the entire population. ROC AUC is 0.715 and average precision is 0.388 against an urgent prevalence of 0.151, which indicates some ranking signal. However, the Brier score is 0.237 compared with 0.128 for a constant training-prevalence probability. Because class weighting intentionally shifts fitted probabilities, this result is evidence of poor calibration rather than proof that class weighting should be removed without another controlled experiment.

The failure is not isolated to the urgency-enriched sample. At `0.45`, all 105 nonurgent general-random messages and all 30 nonurgent urgency-enriched messages become false positives. At `0.50`, 15 of 16 general-random urgent messages and 7 of 8 urgency-enriched urgent messages become false negatives.

## Preliminary holdout comparison

The **revise** disposition and decision file were frozen in commit `f7a2786` before the holdout was scored. The final audit confirmed that the decision file remained byte-identical afterward.

| Strategy | Urgent precision | Urgent recall | Urgent F1 | False positives | Urgent false negatives | Positive rate |
|---|---:|---:|---:|---:|---:|---:|
| Frozen `0.45` | 15.0% | 100.0% | 26.1% | 34 | 0 | 100.0% |
| Default `0.50` | 66.7% | 33.3% | 44.4% | 1 | 4 | 7.5% |

The holdout repeated the training tradeoff. Threshold `0.45` labeled all 40 messages urgent. Threshold `0.50` labeled three messages urgent, correctly identified two of six urgent examples, and missed four. These results are descriptive only because this holdout influenced earlier project work. No model, threshold, or disposition was selected after reviewing it.

## Reliability and ethical boundaries

The Week 6 reliability improvement is the evaluation and decision process, not a deployment claim. Nested validation separated threshold selection from outer-fold evaluation, the decision was frozen before the holdout comparison, row-level evidence remained privacy-safe, and the final workflow rejected a misleading recall gain when its review burden became visible.

The candidate remains decision support for a person. A false negative can delay attention to an urgent message, while an all-urgent rule overwhelms the reviewer and removes useful triage. The label manifest does not contain reliable protected demographic attributes, so the experiment cannot establish demographic fairness. The enriched sample also does not estimate the natural urgency rate in a production mailbox.

## Recommended next experiment

Before another model comparison, expand the reviewed urgent examples and define an operational review-burden guardrail in advance. Evaluate calibration or another controlled model revision inside a new nested-validation design, and reserve a new untouched evaluation set. Shadow testing should begin only if the revised model shows useful urgent recall and F1 without collapsing specificity, and all routing remains under human supervision.

## Evidence paths

| Evidence | Path |
|---|---|
| Executed notebook | `notebooks/week6_testing_debugging.ipynb` |
| Cross-validation summary | `results/metrics/week6_cv_summary.csv` |
| Outer-fold predictions | `results/metrics/week6_outer_predictions.csv` |
| Threshold analysis | `results/metrics/week6_threshold_analysis.csv` |
| Privacy-safe error analysis | `results/metrics/week6_error_analysis.csv` |
| Preliminary holdout comparison | `results/metrics/week6_preliminary_holdout_comparison.csv` |
| Frozen model decision | `results/metrics/week6_model_decision.csv` |
| Reproducibility record | `results/metrics/week6_reproducibility.json` |
| Confusion matrices | `results/figures/week6_confusion_matrices.png` |
| Threshold tradeoff | `results/figures/week6_threshold_tradeoff.png` |

## Report-use rules

- State that the nested procedure selected `0.45`, then explain why the all-urgent result is not operationally acceptable.
- Report urgent-class precision, recall, F1, false negatives, and false-positive review burden together.
- Label the 40-message comparison as preliminary descriptive evidence.
- Describe the final disposition as **revise**, with no deployment or shadow-testing approval.
- Do not claim demographic fairness, causal effects, production reliability, or autonomous-deployment readiness.
- Do not include message text or publish a deployable model artifact.

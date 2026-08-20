# Executed Notebook Guide

These are the canonical executed analysis notebooks. Each notebook retains its code, outputs, experimental context, and limitations so a reviewer can inspect the work on GitHub without rerunning it. Reproduction commands are in the root [`README.md`](../README.md).

| Notebook | Research question | Main method | Primary evidence |
|---|---|---|---|
| [`baseline_model.ipynb`](baseline_model.ipynb) | Can a reproducible binary baseline identify urgent messages better than a majority classifier? | TF-IDF with dummy, unweighted logistic-regression, and class-balanced logistic-regression comparisons | Fixed 199-message reviewed sample, preliminary 159/40 split, metrics, confusion matrices, and false-negative review |
| [`week4_model_optimization.ipynb`](week4_model_optimization.ipynb) | Can bounded tuning and feature engineering improve the baseline without weakening its documented safeguards? | Five-fold stratified grid search across 24 class-balanced TF-IDF/logistic-regression configurations, plus SHAP analysis | Cross-validation summaries, selected parameters, efficiency comparison, SHAP figures, errors, and decision record |
| [`week6_testing_debugging.ipynb`](week6_testing_debugging.ipynb) | Does the frozen candidate provide a defensible threshold and reliable urgent-message behavior? | Five-outer/four-inner nested cross-validation, threshold comparison, error analysis, and preliminary holdout comparison after the decision was frozen | Fold metrics, out-of-fold predictions, threshold tradeoff, confusion matrices, reproducibility record, and `revise` decision |

## How to Read the Evidence

1. Read the notebook's opening scope and evidence-boundary cells.
2. Confirm the saved execution outputs and configuration.
3. Follow the data split and model-selection sequence before interpreting metrics.
4. Review error analysis alongside aggregate metrics.
5. Read the final decision and limitations before drawing an operational conclusion.

The preliminary 40-message holdout informed earlier project work and is not presented as untouched production evidence. The Week 6 nested cross-validation record is the controlling source for the current `revise` decision.

## Workflow and Output Map

Run each notebook from the repository root in the order shown below. A notebook
creates `results/metrics/` and `results/figures/` when needed, then refreshes
its same-named outputs. The full commands and environment setup are in the root
[`README.md`](../README.md#reproduce-the-analysis).

### 1. Week 3 baseline

Run `baseline_model.ipynb`. It produces:

- [`../results/metrics/split_summary.csv`](../results/metrics/split_summary.csv) — reviewed class counts in the training and preliminary holdout partitions;
- [`../results/metrics/baseline_model_comparison.csv`](../results/metrics/baseline_model_comparison.csv) — model-level accuracy and urgent-class metrics;
- [`../results/metrics/per_class_metrics.csv`](../results/metrics/per_class_metrics.csv) — precision, recall, F1, and support by class; and
- [`../results/figures/baseline_confusion_matrices.png`](../results/figures/baseline_confusion_matrices.png) — confusion matrices for the compared baseline models.

### 2. Week 4 optimization and explainability

Run `week4_model_optimization.ipynb`. It produces:

- `week4_split_summary.csv` and `week4_grouping_risk.csv` — split and exact-duplicate leakage checks;
- `week4_experiment_results.csv`, `week4_cv_summary.csv`, and `week4_metric_deltas.csv` — all tested configurations and cross-validation comparisons;
- `week4_model_comparison.csv` and `week4_model_decision.csv` — preliminary holdout comparison and bounded decision;
- `week4_error_analysis.csv` — privacy-screened error categories;
- `week4_shap_global_features.csv` and three `week4_shap_*.csv` files — global and case-level feature contributions; and
- `week4_confusion_matrices.png`, `week4_shap_global.png`, and three case-level `week4_shap_*.png` figures — visual evidence.

These files are in [`../results/metrics/`](../results/metrics/) and
[`../results/figures/`](../results/figures/). Their interpretation and
limitations are recorded in
[`../docs/week4_experiment_record.md`](../docs/week4_experiment_record.md).

### 3. Week 6 reliability and debugging

Run `week6_testing_debugging.ipynb`. It produces:

- [`week6_outer_fold_metrics.csv`](../results/metrics/week6_outer_fold_metrics.csv) and [`week6_outer_predictions.csv`](../results/metrics/week6_outer_predictions.csv) — outer-fold results and one out-of-fold prediction per training message;
- [`week6_cv_summary.csv`](../results/metrics/week6_cv_summary.csv) and [`week6_threshold_analysis.csv`](../results/metrics/week6_threshold_analysis.csv) — aggregate nested-CV and threshold comparisons;
- [`week6_error_analysis.csv`](../results/metrics/week6_error_analysis.csv) — privacy-screened false-positive and false-negative patterns;
- [`week6_preliminary_holdout_comparison.csv`](../results/metrics/week6_preliminary_holdout_comparison.csv) — explicitly preliminary comparison after the training-data decision was frozen;
- [`week6_model_decision.csv`](../results/metrics/week6_model_decision.csv) — the controlling `revise` disposition;
- [`week6_reproducibility.json`](../results/metrics/week6_reproducibility.json) — configuration, versions, hashes, checkpoints, and artifact inventory; and
- [`week6_confusion_matrices.png`](../results/figures/week6_confusion_matrices.png) and [`week6_threshold_tradeoff.png`](../results/figures/week6_threshold_tradeoff.png) — visual threshold evidence.

## What a Reviewer Needs to Rerun the Work

The repository includes the reviewed label manifest, code, executed notebooks,
environment requirements, output records, and figures. A fresh rerun also
requires the Enron `emails.csv` file at `data/raw/emails.csv`; download and
placement instructions are in the root README. Raw messages and detailed
review notes are intentionally excluded. A reviewer who does not rerun the
analysis can still inspect saved notebook outputs and the committed,
privacy-screened evidence artifacts.

## Related Records

- [`../docs/decisions.md`](../docs/decisions.md) — chronological decisions
- [`../docs/week4_experiment_record.md`](../docs/week4_experiment_record.md) — Week 4 interpretation
- [`../docs/week6_experiment_record.md`](../docs/week6_experiment_record.md) — Week 6 interpretation
- [`../results/README.md`](../results/README.md) — exported evidence map

# Results and Evidence Guide

This directory contains exact machine-readable outputs and exported figures. For plain-language interpretation, begin with the linked readable record rather than opening CSV or JSON files without context.

## Evidence Map

| Evidence area | Readable interpretation | Exact evidence |
|---|---|---|
| Baseline comparison | [`../docs/week3_baseline_report.md`](../docs/week3_baseline_report.md) | [`metrics/baseline_model_comparison.csv`](metrics/baseline_model_comparison.csv), [`metrics/per_class_metrics.csv`](metrics/per_class_metrics.csv), and [`metrics/split_summary.csv`](metrics/split_summary.csv) |
| Week 4 optimization | [`../docs/week4_experiment_record.md`](../docs/week4_experiment_record.md) | [`metrics/week4_cv_summary.csv`](metrics/week4_cv_summary.csv), [`metrics/week4_model_comparison.csv`](metrics/week4_model_comparison.csv), [`metrics/week4_error_analysis.csv`](metrics/week4_error_analysis.csv), [`metrics/week4_model_decision.csv`](metrics/week4_model_decision.csv), and SHAP evidence listed in the experiment record |
| Week 6 reliability | [`../docs/week6_experiment_record.md`](../docs/week6_experiment_record.md) | [`metrics/week6_cv_summary.csv`](metrics/week6_cv_summary.csv), [`metrics/week6_threshold_analysis.csv`](metrics/week6_threshold_analysis.csv), [`metrics/week6_error_analysis.csv`](metrics/week6_error_analysis.csv), and [`metrics/week6_model_decision.csv`](metrics/week6_model_decision.csv) |
| Week 7 gate evaluation | [`../docs/week7_readiness_evaluation.md`](../docs/week7_readiness_evaluation.md) | [`metrics/week7_readiness_gate_evaluation.csv`](metrics/week7_readiness_gate_evaluation.csv) and [`metrics/week7_readiness_precheck.json`](metrics/week7_readiness_precheck.json) |
| Week 7 automated validation | [`../docs/week7_automated_test_report.md`](../docs/week7_automated_test_report.md) | [`metrics/week7_demo_model_metadata.json`](metrics/week7_demo_model_metadata.json) and [`metrics/week7_demo_validation.json`](metrics/week7_demo_validation.json) |

## Figures

- [`figures/baseline_confusion_matrices.png`](figures/baseline_confusion_matrices.png) — Week 3 model comparison
- [`figures/week4_confusion_matrices.png`](figures/week4_confusion_matrices.png) — Week 4 preliminary holdout comparison
- [`figures/week4_shap_global.png`](figures/week4_shap_global.png) — Week 4 global feature contributions
- `figures/week4_shap_*.png` — Week 4 case-level explanations for a correct urgent prediction, false negative, and false positive
- [`figures/week6_confusion_matrices.png`](figures/week6_confusion_matrices.png) — Week 6 threshold outcomes
- [`figures/week6_threshold_tradeoff.png`](figures/week6_threshold_tradeoff.png) — recall and false-positive tradeoff

## Interpretation Rules

- Use CSV files for exact tabular values and JSON files for configuration, validation, and reproducibility records.
- Use the corresponding readable record for methodology, denominators, assumptions, and limitations.
- Do not interpret local timing as a production guarantee.
- Do not treat synthetic demonstration cases as a labeled predictive-performance sample.
- The controlling model decision remains `revise`.

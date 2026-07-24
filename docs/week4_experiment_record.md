# Week 4 Experiment Record

## Purpose

This is the technical record for the executed
`notebooks/week4_model_optimization.ipynb` notebook. It preserves the Week 3
baseline, documents the Week 4 experiment and decision, and identifies the
evidence needed for the 2–3 page course report.

## Question and Decision

Can bounded TF-IDF feature engineering and logistic-regression tuning improve
urgent-class model-selection evidence without weakening the preserved Week 3
holdout safety measures?

**Decision:** I retained the selected Week 4 candidate for further refinement,
not deployment. It improved mean five-fold cross-validation urgent F1 without
weakening preliminary holdout urgent F1, urgent recall, or false negatives.

## Inputs and Reproducibility

- Raw input: local `data/raw/emails.csv`; the raw email text is intentionally
  excluded from Git.
- Reviewed labels: `data/labels/enron_urgency_labels_v1.csv`.
- Modeling population: 199 messages (169 nonurgent, 30 urgent).
- Preserved split: 159 training and 40 holdout messages, stratified with
  `random_state=42`.
- Candidate selection: five-fold `StratifiedKFold(shuffle=True,
  random_state=42)` on the training partition.
- Explainability dependency: `shap` in `requirements.txt`.

## Experiment Design

The frozen Week 3 baseline uses class-balanced logistic regression with English
stop-word removal, TF-IDF bigrams, and `min_df=2`. The bounded `GridSearchCV`
tested 24 combinations of:

- logistic-regression `C`: 0.1, 1.0, 10.0;
- TF-IDF n-grams: unigrams or unigrams+bigrams;
- `min_df`: 1 or 2; and
- sublinear term frequency: off or on.

Urgent F1 was the selection score because accuracy alone can hide missed urgent
messages. Accuracy, urgent precision, urgent recall, fit time, scoring time,
and feature count provide the supporting evidence.

## Results

| Measure | Frozen baseline | Selected candidate | Interpretation |
| --- | ---: | ---: | --- |
| Mean five-fold CV accuracy | 83.7% | 86.2% | Candidate improved mean accuracy. |
| Mean five-fold CV urgent precision | 20.0% | 20.0% | No observed mean precision change. |
| Mean five-fold CV urgent recall | 4.0% | 8.0% | Candidate improved the safety-relevant mean recall, with high fold variability. |
| Mean five-fold CV urgent F1 | 6.7% | 11.4% | Primary selection metric improved. |
| Preliminary holdout accuracy | 87.5% | 87.5% | No change. |
| Preliminary holdout urgent precision | 66.7% | 66.7% | No change. |
| Preliminary holdout urgent recall | 33.3% | 33.3% | No change. |
| Preliminary holdout urgent F1 | 44.4% | 44.4% | No change. |
| Preliminary holdout urgent false negatives | 4 | 4 | No regression, but the safety problem remains. |
| Features | 4,097 | 2,895 | Candidate is less feature-heavy. |

The selected parameters are `C=0.1`, unigram TF-IDF, `min_df=2`, and
sublinear term frequency. Several configurations tied on urgent F1, so the
notebook retains the deterministic `GridSearchCV` winner rather than choosing a
result after reviewing the holdout.

## Explanation, Error, and Grouping Evidence

SHAP produced a global feature-importance plot and local explanations for one
correct urgent prediction, one urgent false negative, and one false positive.
These results show associations learned by the selected model. They do not
prove urgency, causation, fairness, or generalizability.

The selected candidate retained four urgent false negatives and one false
positive on the preliminary holdout. An exact normalized-text check found zero
duplicate pairs crossing the training/holdout boundary. It does not detect near
duplicates, reply chains, or related messages, so leakage risk is reduced but
not eliminated.

The label manifest has no reliable protected demographic attributes, so the
report cannot claim demographic fairness. The appropriate discussion is the
absence of those attributes, class-specific errors, enriched sampling, privacy,
and continued human review.

## Evidence Paths

| Evidence | Path |
| --- | --- |
| Executed notebook | `notebooks/week4_model_optimization.ipynb` |
| Report source | `docs/week4_model_optimization_report.md` |
| Full configuration ledger | `results/metrics/week4_experiment_results.csv` |
| Cross-validation summary | `results/metrics/week4_cv_summary.csv` |
| Preliminary holdout comparison | `results/metrics/week4_model_comparison.csv` |
| Model decision | `results/metrics/week4_model_decision.csv` |
| Error analysis | `results/metrics/week4_error_analysis.csv` |
| Grouping-risk check | `results/metrics/week4_grouping_risk.csv` |
| Global SHAP features | `results/metrics/week4_shap_global_features.csv` |
| Confusion matrices | `results/figures/week4_confusion_matrices.png` |
| Global SHAP figure | `results/figures/week4_shap_global.png` |

## Report-Use Rules

- Use the CV table as the model-selection result.
- Label the preserved 40-message comparison as preliminary evidence.
- State the remaining four missed urgent messages and one false positive.
- Describe the candidate as retained for refinement, not as deployment-ready.
- Do not include raw email bodies in the report or copied artifact folder.

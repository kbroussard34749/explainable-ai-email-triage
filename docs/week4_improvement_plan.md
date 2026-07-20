# Week 4 Improvement Plan

## Purpose and Boundary

Week 4 will optimize and explain the submitted Week 3 urgency-classification baseline without changing its recorded results. The Week 3 TF-IDF and class-balanced logistic-regression model remains the comparison point. New experiments will use the same reviewed labels initially, keep urgent-message recall and false negatives as the primary risk measures, and remain within the approved capstone proposal.

## Week 4 Assignment Contract

The Week 4 submission must include code with experiments and a 2–3 page report that:

- experiments with hyperparameter tuning and feature engineering;
- evaluates changes in accuracy, precision, recall, and F1-score;
- implements at least one explainability tool, such as SHAP or LIME;
- analyzes model improvement and the tradeoffs among performance, efficiency, fairness, and ethical concerns; and
- documents key findings and whether the selected model should continue to be used.

The required minimum is therefore a controlled tuned-model comparison plus one implemented explanation method. Alternative model architectures and external experiment-tracking services are useful extensions, not substitutes for those required outputs.

## Starting Evidence

- Reviewed data: 199 messages (169 nonurgent and 30 urgent)
- Exploratory holdout: 40 messages (34 nonurgent and 6 urgent)
- Week 3 primary baseline: class-balanced TF-IDF logistic regression
- Baseline accuracy: 87.5%
- Urgent precision: 66.7%
- Urgent recall: 33.3%
- Urgent F1: 44.4%
- Urgent false negatives: 4

The holdout was used to compare Week 3 variants, so it is preliminary evidence rather than an untouched final estimate.

## Required Experiment Sequence

| Order | Work item | Method | Evidence to retain | Completion criterion |
|---:|---|---|---|---|
| 1 | Preserve the baseline | Tag or otherwise identify the submitted Week 3 commit; do not overwrite its metrics | Commit/tag and existing result artifacts | Week 3 results remain reproducible and unchanged |
| 2 | Establish the experiment record | Create a versioned local results table that records data version, parameters, metrics, runtime, and artifacts | Experiment-results CSV and run identifiers | Every reported experiment can be traced to its settings and outputs |
| 3 | Audit errors and grouping risk | Categorize false negatives and false positives; check whether duplicate or related messages could cross validation boundaries | Error-analysis table with message IDs only and a documented grouping limitation or rule | Every held-out error has a supported category without republishing message text |
| 4 | Establish validation | Use reproducible stratified cross-validation for model selection; retain the Week 3 holdout as preliminary evidence and avoid further selection from it | Fold-level and summary metrics | Mean and variability are reported for accuracy and urgent precision, recall, and F1 |
| 5 | Tune and engineer features | Use a bounded `GridSearchCV` over logistic-regression regularization and defensible TF-IDF choices such as n-grams, document-frequency limits, maximum features, and sublinear term frequency | Parameter grid, multi-metric scoring rule, fold results, selected parameters, and run time | The optimized candidate is selected from validation evidence and both tuning and feature engineering are demonstrated |
| 6 | Evaluate the optimized candidate | Compare the frozen baseline and optimized candidate using identical metrics and record training or inference time as an efficiency indicator | Comparison table and confusion matrices | Any claimed improvement identifies metric gains, regressions, and efficiency cost |
| 7 | Implement explainability | Use SHAP as the primary required tool for the selected linear model; retain coefficient inspection as a complementary global explanation and use LIME only if SHAP proves unsuitable | Global feature summary plus local explanations for a correct urgent prediction, an urgent false negative, and a false positive when available | Explanations identify influential terms, connect them to observed errors, and state that association is not causation |
| 8 | Evaluate tradeoffs and ethics | Discuss urgent false-negative risk, false-positive review burden, efficiency, data limitations, privacy, human oversight, and explanation limitations | Report discussion and documented model-continuation decision | The report states whether to retain, revise, or replace the model and why |
| 9 | Produce Week 4 deliverables | Run the experiment notebook cleanly and prepare the 2–3 page optimization report | Executed code, tracked tables/figures, and report | Every assignment requirement is supported by a reproducible artifact |

## Model-Selection Rules

- Optimize with validation data; do not repeatedly select models from the Week 3 holdout.
- Use urgent F1 as the primary tuning score, treat urgent recall and false negatives as safety-critical evidence, and report the accompanying false-positive cost.
- Do not accept an improvement based only on overall accuracy.
- Use identical folds, text inputs, and evaluation metrics for model comparisons.
- Fix random seeds and record package versions, parameters, and output paths.
- Treat model explanations as evidence of learned associations, not proof of urgency or causation.
- Keep a human reviewer in control of labels and operational decisions.

## Fairness and Efficiency Boundaries

The reviewed label manifest does not contain reliable demographic attributes. The project therefore cannot claim demographic fairness or calculate protected-group fairness metrics from the current data. Week 4 should instead disclose this limitation, examine class-specific error behavior and sampling effects, and avoid treating employee identity or mailbox folder as a demographic proxy.

Efficiency evidence should remain proportional to the project: record fit time, scoring time when available, feature count, and artifact size. These measures support the instructor’s requested accuracy-versus-efficiency discussion without turning Week 4 into a deployment benchmark.

## Experiment Tracking

Use a versioned local CSV or Markdown experiment table as the default tracker. Each run should record the run ID, date, data version, split or folds, preprocessing, model parameters, decision threshold, metrics, artifact paths, and conclusion. Weights & Biases remains optional; adopt it only if its additional interface provides clear value or the instructor requires it.

## Optional Extensions After Required Work

- Evaluate probability thresholds and show the urgent-recall versus false-positive tradeoff.
- Compare one additional classical model, initially LinearSVC, using the same validation folds and metrics.
- Compare influential features across folds to assess explanation stability.
- Expand the reviewed dataset using the existing labeling guide and recorded sampling provenance.

These extensions should not delay the required tuned-model comparison, SHAP implementation, clean code, or 2–3 page report.

## Deferred Until the Urgency Model Is Stable

- Required-action and topic classification
- Lightweight embeddings or transformer comparisons
- API development and deployment
- Automated email actions or reply generation
- Large-scale hyperparameter searches with Optuna or Hyperopt

Required-action classification remains part of the approved proposal, but it should begin only after the urgency model has stronger validation evidence and a stable labeling process.

## Week 4 Outputs

- Reproducible optimization notebook or script
- Versioned experiment-results table
- Cross-validation and optimized-model comparison results
- Error-analysis artifact without email bodies
- SHAP or LIME explanation artifacts
- Updated decision log and README
- Week 4 report comparing the preserved baseline with the selected optimized model

## Assigned and Supporting Material

- Week 4 assignment and instructor audio: hyperparameter tuning, feature engineering, at least one explainability tool, metric comparison, efficiency/fairness tradeoffs, code, and a 2–3 page report
- Burkov reading link: Chapters 9–11, identified by the linked page as *Unsupervised Learning*, *Other Forms of Learning*, and *Conclusion*
- Instructor audio: healthcare-AI myths, research guidance, privacy, bias, ethics, and human oversight; treat these as instructor discussion rather than attributing them to the linked Burkov chapters
- fast.ai Lesson 1: use the provided link as an end-to-end workflow reference; it does not require replacing the approved classical NLP baseline with deep learning
- DataCamp explainable-AI tutorial: distinguish global and local explanations, use SHAP to quantify feature contributions, and acknowledge that explanation methods simplify model behavior and have limitations

The Week 4 overview's reading label, linked Burkov chapter titles, and healthcare-focused audio are not fully consistent. The implementation plan follows the explicit assignment requirements and keeps the sources conceptually separate. Ask the instructor for clarification before citing the healthcare chapter descriptions as assigned Burkov content.

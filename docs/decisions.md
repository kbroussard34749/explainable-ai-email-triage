# Project Decision Log

This log records the project decisions, the evidence behind them, and their
current status. Course requirements are noted when they shape a decision, but
this is the implementation record rather than the assignment instructions.

| Date | Decision | Justification | Status |
|---|---|---|---|
| 2026-07-16 | Use binary urgency classification for the Week 3 baseline. | Produces a feasible, measurable baseline while topic and action classification remain later project goals. | Accepted |
| 2026-07-16 | Combine the email subject and body as model input. | Urgency evidence may appear in either field. | Accepted |
| 2026-07-16 | Keep the original Enron CSV unchanged and process it with Python. | Preserves the source data and supports repeatable processing of the 1.3 GB file. | Accepted |
| 2026-07-16 | Create 400 candidates: 300 general and 100 urgency-enriched. | Original planning target before the available implementation time was reassessed. | Superseded 2026-07-17 |
| 2026-07-16 | Record each email's sampling source and prevent overlap between the two queues. | Preserves traceability and prevents duplicate labeling. | Accepted |
| 2026-07-16 | Use `random_state=42` for sampling and splitting. | Makes the experiment repeatable and avoids choosing a favorable seed after viewing results. | Accepted |
| 2026-07-16 | Use an 80/20 stratified train/test split. | Reserves held-out evaluation data while preserving class proportions. | Accepted |
| 2026-07-16 | Use TF-IDF with logistic regression as the baseline model. | It is efficient, appropriate for limited labeled text data, and comparatively interpretable. | Accepted |
| 2026-07-16 | Compare the baseline with a majority-class dummy classifier. | Demonstrates whether the trained model improves on a simple reference prediction. | Accepted |
| 2026-07-16 | Report accuracy, per-class precision, recall, F1-score, support, a confusion matrix, and urgent false negatives. | Accuracy alone can hide poor performance on a less common urgent class. | Accepted |
| 2026-07-16 | Give priority to urgent-message recall and false-negative analysis. | The approved proposal identifies missed urgent messages as the primary operational risk. | Accepted |
| 2026-07-17 | Create 200 candidates: 150 general and 50 urgency-enriched. | The assignment specifies no sample minimum. A smaller, carefully reviewed set is more defensible than 400 rushed labels before the July 19 deadline. | Accepted |
| 2026-07-17 | Use Python 3.11 for the project environment. | It matches the active implementation guide, is installed locally, and has broad compatibility with the required analytical packages. | Accepted |
| 2026-07-17 | Defer tuning, SHAP/LIME, W&B, APIs, deployment, deep learning, and multi-target modeling. | The Week 3 assignment requires a baseline, initial metrics, justification, improvements, and a 1–2 page report; advanced work must not delay submission. | Accepted |
| 2026-07-17 | Do not revise the proposal or literature review. | Both received 100/100, and the instructor requested no corrections. | Accepted |
| 2026-07-18 | Increase the labeling review excerpt from 750 to 2,000 characters and inspect the full message when needed. | The 30-email pilot showed that 750 characters frequently omitted useful reply or thread context. The longer excerpt improves review consistency without exporting complete bodies by default. | Accepted |
| 2026-07-18 | Use the reviewed 30-email pilot to validate the labeling workflow, then create a separate final queue of 150 general-random and 50 urgency-enriched emails. | The pilot confirmed that the guide and review fields are usable. Excluding pilot records from the final queue prevents duplicate review and preserves a reproducible 200-record modeling set. | Accepted |
| 2026-07-18 | Use fixed urgency cues only to enrich candidate sampling, never to assign labels. | Enrichment improves the chance of observing urgent examples while human review under labeling-guide version 1.0 remains the source of truth. | Accepted |
| 2026-07-18 | Exclude `mims-thurston-p/_sent_mail/205.` from the final labeled set. | The complete source contains only forwarding metadata with no subject or message body, so labeling-guide Step 1 classifies it as unusable rather than urgent, nonurgent, or unresolved. | Accepted |
| 2026-07-18 | Compare unweighted and class-balanced logistic regression, and use the class-balanced variant as the primary baseline. | The unweighted model reproduced the majority-class dummy and detected no urgent test emails. Class weighting addresses the 169-to-30 label imbalance without changing labels or the held-out split; its remaining weak urgent recall must still be reported. | Accepted |
| 2026-07-19 | Track a minimal reviewed label manifest while excluding email text and detailed review workbooks. | Message identifiers and approved labels are necessary to reproduce the experiment from the public Enron dataset. Excluding subjects, bodies, excerpts, reasons, reviewer names, and notes limits unnecessary republication of real email content. | Accepted |
| 2026-07-19 | Treat the three-model holdout comparison as exploratory Week 3 evidence. | The same 40-message holdout was used to compare variants and identify the preferred baseline. A future untouched evaluation set or nested validation design is needed for a less selection-sensitive estimate. | Accepted |
| 2026-07-20 | Preserve the submitted Week 3 baseline and consolidate later improvements in `docs/week4_improvement_plan.md`. | A staged plan keeps optimization and explainability work within the approved proposal while preventing later experiments from overwriting the baseline comparison point. | Accepted |
| 2026-07-20 | Use bounded `GridSearchCV` with TF-IDF feature engineering and implement SHAP as the primary Week 4 explainability method. | These choices directly satisfy the Week 4 tuning, feature-engineering, metric-comparison, and explainability requirements while remaining reproducible and appropriate for the approved linear NLP baseline. | Implemented 2026-07-24 |
| 2026-07-20 | Use a versioned local experiment table instead of requiring Weights & Biases. | The assignment requires documented experiments but does not require a specific tracking service; local tracking is sufficient for the planned number of runs and avoids an unnecessary external dependency. | Implemented 2026-07-24 |
| 2026-07-24 | Select Week 4 candidates by urgent F1 in five-fold stratified cross-validation on the fixed 159-message Week 3 training partition. | The Week 3 holdout had already influenced baseline selection. Five-fold cross-validation keeps Week 4 model selection separate while preserving the same holdout for a clearly labeled preliminary check. | Accepted |
| 2026-07-24 | Use a 24-configuration search over logistic-regression `C` and TF-IDF n-grams, `min_df`, and sublinear term frequency. | The search demonstrates both tuning and feature engineering without turning a 199-message study into a large, weakly supported optimization exercise. | Accepted |
| 2026-07-24 | Keep the selected candidate—`C=0.1`, unigram TF-IDF, `min_df=2`, and sublinear term frequency—for further refinement. | Mean CV urgent F1 rose from 6.7% to 11.4% and urgent recall rose from 4.0% to 8.0%. The preliminary holdout did not worsen on urgent F1, recall, or false negatives, and the candidate uses 2,895 rather than 4,097 features. | Accepted; not deployment approval |
| 2026-07-24 | Use SHAP for global and local explanations and keep coefficient values in the evidence export. | SHAP meets the Week 4 explainability requirement for the selected linear model. The results are described as learned associations, not causal explanations, and the exports do not include email bodies. | Accepted |
| 2026-07-24 | Check for exact normalized-text duplicates across the Week 3 training and holdout partitions. | No exact cross-split duplicate pairs were found. The check is limited: related messages, reply chains, and near duplicates remain open evaluation risks. | Accepted |

## Open Decisions

| Decision needed | Evidence required |
|---|---|
| Whether to change the default probability threshold | Validation results and the observed cost of false negatives versus false positives |
| Whether to expand the reviewed dataset before additional model comparisons | Labeling capacity, sampling provenance, and a plan for an untouched evaluation design |
| Whether to model related-message or thread groups explicitly | A reproducible grouping rule and evidence that it changes the evaluation-risk assessment |

# Explainable AI Email Triage

This capstone project develops an explainable email-triage system that identifies urgent messages while keeping a human reviewer in control. The Week 3 implementation establishes a reproducible binary urgency-classification baseline using the Enron Email Dataset.

## Workspace Boundaries

This repository is the authoritative home for code, notebooks, models, reproducible metrics, figures, and technical documentation.

Capstone Week 4 coursework and submission documents are maintained separately at:

```text
/Users/keithgb/Documents/College - UC Courses/Courses Summer 2026/Capstone/Week 4
```

Use that course folder for assignment materials, planning notes, selected report-ready exports, and the final submission package. Generate technical evidence here first, then copy only the selected tables and figures needed for the report into the course folder's `03_Analysis_Artifacts` directory. The Week 4 report source is deliberately version-controlled in this repository because it directly documents the technical evidence; its final Word submission version remains in the course folder.

The synchronized ChatGPT project `sources` directory is read-only reference material. Consult those files in place rather than copying the complete collection into this repository. Avoid competing editable copies: this repository is authoritative for technical artifacts, while the course folder is authoritative for report and submission documents.

## Week 3 Baseline

The baseline combines TF-IDF text features with logistic regression. It compares:

- a majority-class dummy classifier;
- unweighted logistic regression; and
- class-balanced logistic regression.

The class-balanced model is the primary Week 3 baseline because the approved dataset contains 169 nonurgent and 30 urgent messages. In an exploratory comparison on the fixed 40-message holdout, it achieved 87.5% accuracy, 66.7% urgent precision, 33.3% urgent recall, and 44.4% urgent F1. It missed four of the six urgent test messages, so urgent recall remains the main area for improvement. Because this same holdout was used to compare variants, the result is preliminary rather than an untouched final performance estimate.

## Week 4 Optimization Status

Week 4 keeps the submitted baseline intact and adds a focused optimization and
explainability experiment. The notebook evaluates 24 class-balanced
TF-IDF/logistic-regression configurations with five-fold stratified
cross-validation on the fixed 159-message training partition. The 40-message
Week 3 holdout remains a preliminary comparison, not a tuning target.

The selected candidate uses `C=0.1`, unigram TF-IDF, `min_df=2`, and sublinear
term frequency. Mean cross-validation urgent F1 rose from 6.7% to 11.4%, and
urgent recall rose from 4.0% to 8.0%. The preliminary holdout did not change:
87.5% accuracy, 66.7% urgent precision, 33.3% urgent recall, 44.4% urgent F1,
and four urgent false negatives. The candidate uses 2,895 features instead of
4,097, so it is retained for further refinement—not deployment.

The executed technical record is `docs/week4_experiment_record.md`; use it and
the exported CSVs rather than this summary when reporting results.

## Week 6 Reliability Decision

Week 6 froze the Week 4 candidate and evaluated threshold selection with nested
five-outer/four-inner stratified cross-validation on the 159-message training
partition. Threshold `0.45` achieved 100% urgent recall only by predicting all
159 messages urgent, which created 135 false positives. Threshold `0.50`
identified only 2 of 24 urgent messages and missed 22. The probability scores
were highly compressed: 157 of 159 fell from `0.45` to below `0.50`.

The candidate disposition is `revise`. It is not approved for deployment or
shadow testing, and no deployable model artifact was saved. The preserved
40-message comparison remains preliminary evidence because it influenced
earlier project work. The controlling technical record is
`docs/week6_experiment_record.md`.

## Week 7 Conditional Readiness

Week 7 preserves the Week 6 decision and adds provisional capstone readiness
gates. The planning scenario uses 100 incoming messages per review period and
allows no more than 10 false alerts per 100 evaluated nonurgent messages. The
candidate gates require at least 80% urgent recall, 50% urgent precision, and
60% urgent F1, with a false-positive rate no greater than 10%.

These values are project research assumptions, not course requirements,
external standards, or stakeholder-validated production objectives. Both Week
6 operating points fail the combined gates. The repository may advance only
toward a controlled local research demonstration while the model remains
`revise`.

The gate definitions and evaluation are recorded in:

```text
docs/week7_conditional_advancement_gates.md
docs/week7_readiness_evaluation.md
results/metrics/week7_readiness_gate_evaluation.csv
results/metrics/week7_readiness_precheck.json
```

## Repository Structure

```text
data/raw/                    Local raw Enron CSV; not tracked by Git
data/processed/              Local labeling workbooks; not tracked by Git
data/labels/                 Reviewed label manifest tracked for reproducibility
docs/decisions.md            Project decisions and justifications
docs/labeling_guide.md       Deterministic urgency-labeling rules
docs/week3_baseline_report.md Week 3 short-report source
docs/week4_improvement_plan.md Ordered optimization and explainability plan
docs/week4_experiment_record.md Executed Week 4 evidence and decision record
docs/week4_model_optimization_report.md Week 4 report source
docs/week6_experiment_record.md Executed Week 6 testing and decision record
docs/week7_conditional_advancement_gates.md Provisional Week 7 readiness gates
docs/week7_readiness_evaluation.md Frozen-candidate gate evaluation
notebooks/baseline_model.ipynb Executed labeling and baseline workflow
notebooks/week4_model_optimization.ipynb Executed Week 4 optimization workflow
notebooks/week6_testing_debugging.ipynb Executed Week 6 reliability workflow
results/figures/             Exported baseline confusion matrices
results/metrics/             Exported split and performance tables
scripts/validate_week7_readiness.py Week 7 evidence-integrity precheck
tests/test_week7_readiness.py Automated Week 7 precheck tests
```

## Local Data Requirements

The raw dataset and detailed review workbooks are intentionally excluded from Git because of their size and email content. The minimal reviewed label manifest is included in the repository. Place the downloaded raw file at the following path before running the notebook:

```text
data/raw/emails.csv
```

This project uses the Kaggle distribution of the Enron Email Dataset provided by Cukierski (2016):

https://www.kaggle.com/datasets/wcukierski/enron-email-dataset

The underlying Enron corpus was originally prepared and distributed by Carnegie Mellon University:

https://www.cs.cmu.edu/~enron/

Download and extract the Kaggle archive, then copy its `emails.csv` file to `data/raw/emails.csv`. The Kaggle distribution is the reproducibility source because it matches the 517,401-record CSV used by this project; the Carnegie Mellon link documents the corpus's original provenance.

The notebook expects the Enron CSV to contain `file` and `message` columns. It joins those records to the tracked manifest at `data/labels/enron_urgency_labels_v1.csv`. The manifest contains only message identifiers, sampling strata, approved urgency labels, label versions, and review statuses. Email subjects, bodies, excerpts, label reasons, reviewer names, and review notes remain excluded.

## Environment Setup

Python 3.11 is the supported project version.

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m ipykernel install --user \
  --name email-triage-py311 \
  --display-name "Email Triage (Python 3.11)"
```

In JupyterLab, select the **Email Triage (Python 3.11)** kernel.

## Run the Notebook

From the repository root:

```bash
source .venv/bin/activate
jupyter lab
```

Open `notebooks/baseline_model.ipynb` and run all cells from top to bottom. For a noninteractive execution:

```bash
python -m jupyter nbconvert \
  --execute \
  --to notebook \
  --inplace notebooks/baseline_model.ipynb \
  --ExecutePreprocessor.timeout=600 \
  --ExecutePreprocessor.kernel_name=email-triage-py311
```

The workflow uses `random_state=42` for reproducible sampling and splitting. TF-IDF is fit inside the model pipeline using training data only.

The executed notebook includes a bounded review of all four urgent false negatives. It also documents the exact Kaggle distribution, original Carnegie Mellon provenance, expected input paths, supported Python version, and clean execution command near the top of the notebook.

Running the notebook also refreshes these tracked result artifacts:

```text
results/figures/baseline_confusion_matrices.png
results/metrics/baseline_model_comparison.csv
results/metrics/per_class_metrics.csv
results/metrics/split_summary.csv
```

## Run the Week 4 Experiment

Run the Week 4 notebook from the repository root after installing the updated
requirements, including SHAP:

```bash
python -m jupyter nbconvert \
  --execute \
  --to notebook \
  --inplace notebooks/week4_model_optimization.ipynb \
  --ExecutePreprocessor.timeout=1200 \
  --ExecutePreprocessor.kernel_name=email-triage-py311
```

The notebook writes these Week 4 evidence artifacts locally:

```text
results/metrics/week4_experiment_results.csv
results/metrics/week4_cv_summary.csv
results/metrics/week4_model_comparison.csv
results/metrics/week4_error_analysis.csv
results/metrics/week4_grouping_risk.csv
results/metrics/week4_model_decision.csv
results/figures/week4_confusion_matrices.png
results/figures/week4_shap_global.png
results/figures/week4_shap_correct_urgent.png
results/figures/week4_shap_false_negative.png
results/figures/week4_shap_false_positive.png
```

The raw messages remain local. The exported error and SHAP tables use message
identifiers and model features rather than email bodies.

## Run the Week 7 Readiness Precheck

The precheck validates required evidence, saved notebook execution, the frozen
Week 6 decision, gate-value traceability, privacy-safe exported columns, and
source hashes. It does not establish predictive reliability or complete all
local-demonstration tests.

```bash
python -m unittest -v tests/test_week7_readiness.py
python scripts/validate_week7_readiness.py \
  --output results/metrics/week7_readiness_precheck.json
```

## Week 3 Deliverables

- Executed notebook: `notebooks/baseline_model.ipynb`
- Short report source: `docs/week3_baseline_report.md`
- Submission-ready APA 7 Word report: maintained in the local Week 3 course folder

## Limitations and Next Steps

The held-out set contains only six urgent messages, and urgency-enriched sampling means the labeled class distribution is not an estimate of the full corpus's natural urgency rate. The Week 4 exact normalized-text check found no duplicate message pairs across the training and holdout partitions, but it does not identify near duplicates, reply chains, or related messages. The preliminary holdout still informed Week 3 selection and is not an untouched production estimate.

Next evidence should come from more reviewed labels, related-message grouping,
an untouched evaluation design, and carefully scoped threshold analysis. The
ordered plan is in `docs/week4_improvement_plan.md`; executed results and the
current decision are in `docs/week4_experiment_record.md`.

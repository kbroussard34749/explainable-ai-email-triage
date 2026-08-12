# Project Review Guide: Explainable AI Email Triage

This capstone project develops an explainable email-triage system that identifies urgent messages while keeping a human reviewer in control. The Week 3 implementation establishes a reproducible binary urgency-classification baseline using the Enron Email Dataset.

Return to the repository's concise [`README`](../README.md) for the project overview and quick start.

## Current Project Status

| Area | Current conclusion |
|---|---|
| Research application | Gate A passed for a controlled local demonstration. |
| Predictive model | Disposition: `revise`. The tested thresholds do not provide a reliable operating point. |
| Human oversight | Required for every prediction and routing decision. |
| Deployment | Production routing and shadow testing are not approved. |
| Verification | All 13 automated tests and the Week 7 readiness precheck pass. |

The application is demonstrable, reproducible, and intentionally bounded. Those engineering results do not override the model's unresolved reliability limitations.

## Choose a Review Path

| Reader | Recommended path |
|---|---|
| Academic reviewer | Start with the [`documentation index`](README.md#academic-review), then inspect the executed notebooks, experiment records, and automated test report. |
| Stakeholder | Start with the [`stakeholder evidence path`](README.md#stakeholder-review) for the decision, practical meaning, limitations, and next step. |
| Technical reviewer | Follow the [`local demonstration runbook`](week7_demo_runbook.md), then inspect [`src/email_triage_demo/`](../src/email_triage_demo/) and [`tests/`](../tests/). |
| Evidence auditor | Use the [`results index`](../results/README.md) to connect readable conclusions with exact CSV and JSON records. |

## Repository Scope

This repository is the self-contained technical record for the capstone project. It includes the source code, executed notebooks, experiment and decision records, reproducible metrics, figures, automated tests, validation evidence, and local-demonstration instructions needed to review the work. All documented paths and commands are relative to the repository root.

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

## Repository Map

```text
.
├── src/email_triage_demo/    Application flow explained in its README.md
├── notebooks/                Canonical executed analyses; see notebooks/README.md
├── tests/                    Test coverage and commands; see tests/README.md
├── scripts/                  Build and validation guide in scripts/README.md
├── data/
│   ├── labels/               Tracked reviewed-label manifest
│   ├── raw/                  Local Enron CSV; excluded from Git
│   └── processed/            Local review workbooks; excluded from Git
├── results/                  Evidence guide in results/README.md
│   ├── metrics/              Machine-readable metrics and validation records
│   └── figures/              Exported analytical figures
├── docs/                     Review paths and records; see docs/README.md
├── coursework/               Earlier capstone report and notebook snapshots
├── requirements.txt          Full notebook and analysis environment
└── requirements-demo.txt     Pinned local-demonstration environment
```

### Reviewer Quick Start

| Review goal | Start here |
|---|---|
| Understand the current model decision | [`week6_experiment_record.md`](week6_experiment_record.md) |
| Review Week 7 test purpose and results | [`week7_automated_test_report.md`](week7_automated_test_report.md) |
| Review readiness criteria and conclusions | [`week7_conditional_advancement_gates.md`](week7_conditional_advancement_gates.md) and [`week7_readiness_evaluation.md`](week7_readiness_evaluation.md) |
| Reproduce the local demonstration | [`week7_demo_runbook.md`](week7_demo_runbook.md) |
| Inspect the implemented application | [`src/email_triage_demo/`](../src/email_triage_demo/) |
| Inspect or rerun automated tests | [`tests/`](../tests/), [`validate_week7_demo.py`](../scripts/validate_week7_demo.py), and [`validate_week7_readiness.py`](../scripts/validate_week7_readiness.py) |
| Trace exact metrics and validation output | [`results/metrics/`](../results/metrics/) |
| Review the full analysis progression | [`notebooks/`](../notebooks/) and [`decisions.md`](decisions.md) |

The folder-level indexes provide additional context when browsing on GitHub or opening the downloaded repository locally:

- [`README.md`](README.md) — academic, stakeholder, and technical evidence paths
- [`../notebooks/README.md`](../notebooks/README.md) — notebook purpose, method, and outputs
- [`../results/README.md`](../results/README.md) — readable findings mapped to exact evidence files
- [`../tests/README.md`](../tests/README.md) — automated coverage, commands, recorded outcome, and limits
- [`../src/email_triage_demo/README.md`](../src/email_triage_demo/README.md) — application components, request flow, and safeguards
- [`../scripts/README.md`](../scripts/README.md) — purpose and correct order of executable utilities

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

## Run the Week 3 Baseline

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

## Run the Week 6 Reliability Experiment

Run the Week 6 notebook from the repository root after the Week 3 and Week 4
workflows have established the reviewed sample and frozen candidate:

```bash
python -m jupyter nbconvert \
  --execute \
  --to notebook \
  --inplace notebooks/week6_testing_debugging.ipynb \
  --ExecutePreprocessor.timeout=1200 \
  --ExecutePreprocessor.kernel_name=email-triage-py311
```

The notebook refreshes the nested cross-validation, threshold, error,
preliminary-holdout, decision, and reproducibility evidence under
`results/metrics/`, plus the two Week 6 figures under `results/figures/`.
The exact file map and the meaning of each output are documented in
[`notebooks/README.md`](../notebooks/README.md#workflow-and-output-map).

Each canonical notebook creates its output directories when needed and
refreshes same-named artifacts when rerun. The executed notebooks and
privacy-screened evidence files are committed so a reviewer can inspect the
record without access to the excluded raw email corpus.

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

## Run the Week 7 Controlled Local Demonstration

The local web demonstration is a research prototype only. It preserves the
Week 6 `revise` disposition, requires human review, and provides no production
or shadow-testing approval.

```bash
python -m pip install -r requirements-demo.txt
PYTHONPATH=src python scripts/build_week7_demo_model.py
PYTHONPATH=src python -m unittest -v \
  tests/test_week7_demo.py tests/test_week7_readiness.py
PYTHONPATH=src python scripts/validate_week7_demo.py
PYTHONPATH=src uvicorn email_triage_demo.app:app \
  --host 127.0.0.1 --port 8765
```

Open `http://127.0.0.1:8765/` and use only synthetic or privacy-screened
messages. The model artifact remains local and excluded from Git. See
`docs/week7_demo_runbook.md` for the full build, demonstration, safe-failure,
and evidence procedure. The reader-facing results and all 13 automated test
outcomes are documented in `docs/week7_automated_test_report.md`.

## Week 3 Technical Records

- Executed notebook: `notebooks/baseline_model.ipynb`
- Short report source: `docs/week3_baseline_report.md`

## Limitations and Next Steps

The held-out set contains only six urgent messages, and urgency-enriched sampling means the labeled class distribution is not an estimate of the full corpus's natural urgency rate. The Week 4 exact normalized-text check found no duplicate message pairs across the training and holdout partitions, but it does not identify near duplicates, reply chains, or related messages. The preliminary holdout still informed Week 3 selection and is not an untouched production estimate.

Next evidence should come from more reviewed labels, related-message grouping,
an untouched evaluation design, and carefully scoped threshold analysis. The
ordered plan is in `docs/week4_improvement_plan.md`; executed results and the
current decision are in `docs/week4_experiment_record.md`.

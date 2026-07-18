# Explainable AI Email Triage

This capstone project develops an explainable email-triage system that identifies urgent messages while keeping a human reviewer in control. The Week 3 implementation establishes a reproducible binary urgency-classification baseline using the Enron Email Dataset.

## Week 3 Baseline

The baseline combines TF-IDF text features with logistic regression. It compares:

- a majority-class dummy classifier;
- unweighted logistic regression; and
- class-balanced logistic regression.

The class-balanced model is the primary baseline because the approved dataset contains 169 nonurgent and 30 urgent messages. On the 40-message held-out test set, it achieved 87.5% accuracy, 66.7% urgent precision, 33.3% urgent recall, and 44.4% urgent F1. It missed four of the six urgent test messages, so urgent recall remains the main area for improvement.

## Repository Structure

```text
data/raw/                    Local raw Enron CSV; not tracked by Git
data/processed/              Local labeling workbooks; not tracked by Git
docs/decisions.md            Project decisions and justifications
docs/labeling_guide.md       Deterministic urgency-labeling rules
docs/week3_baseline_report.md Week 3 short-report source
notebooks/baseline_model.ipynb Executed labeling and baseline workflow
results/figures/             Exported baseline confusion matrices
results/metrics/             Exported split and performance tables
```

## Local Data Requirements

The raw and reviewed datasets are intentionally excluded from Git because of their size and email content. Place these files at the following paths before running the notebook:

```text
data/raw/emails.csv
data/processed/enron_urgency_labels_199_reviewed_v1.xlsx
```

This project uses the Kaggle distribution of the Enron Email Dataset provided by Cukierski (2016):

https://www.kaggle.com/datasets/wcukierski/enron-email-dataset

The underlying Enron corpus was originally prepared and distributed by Carnegie Mellon University:

https://www.cs.cmu.edu/~enron/

Download and extract the Kaggle archive, then copy its `emails.csv` file to `data/raw/emails.csv`. The Kaggle distribution is the reproducibility source because it matches the 517,401-record CSV used by this project; the Carnegie Mellon link documents the corpus's original provenance.

The notebook expects the Enron CSV to contain `file` and `message` columns. The approved workbook must contain the reviewed `message_id`, `urgency_label`, and `review_status` fields produced by the documented labeling workflow.

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

Running the notebook also refreshes these tracked result artifacts:

```text
results/figures/baseline_confusion_matrices.png
results/metrics/baseline_model_comparison.csv
results/metrics/per_class_metrics.csv
results/metrics/split_summary.csv
```

## Week 3 Deliverables

- Executed notebook: `notebooks/baseline_model.ipynb`
- Short report source: `docs/week3_baseline_report.md`
- Submission-ready APA 7 Word report: maintained in the local Week 3 course folder

## Limitations and Next Steps

The held-out set contains only six urgent messages, and urgency-enriched sampling means the labeled class distribution is not an estimate of the full corpus's natural urgency rate. Planned improvements include expanding the reviewed dataset, analyzing urgent false negatives, evaluating decision thresholds, using cross-validation, and conducting controlled hyperparameter tuning.

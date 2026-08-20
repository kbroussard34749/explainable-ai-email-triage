# Explainable AI Email Triage

This capstone project develops an explainable email-triage system that
identifies potentially urgent messages while keeping a human reviewer in
control. The repository preserves the full research progression from baseline
modeling through optimization, reliability testing, and a controlled local
demonstration.

For the complete methodology, evidence, and execution reference, see the
[`Project Review Guide`](docs/project_review_guide.md).

## Current Status

| Area | Conclusion |
|---|---|
| Research application | Gate A passed for a controlled local demonstration. |
| Predictive model | Disposition: `revise`. The tested thresholds do not provide a reliable operating point. |
| Human oversight | Required for every prediction and routing decision. |
| Deployment | Production routing and shadow testing are not approved. |
| Verification | All 13 automated tests and the Week 7 readiness precheck pass. |

The application is demonstrable and reproducible within its documented scope.
Those engineering results do not override the model's unresolved predictive
limitations.

## Project Progression

| Stage | Work completed | Evidence-based conclusion |
|---|---|---|
| Week 3 baseline | Compared a majority classifier with unweighted and class-balanced TF-IDF/logistic-regression models. | The class-balanced baseline missed four of six urgent messages on the preliminary holdout. |
| Week 4 optimization | Evaluated 24 configurations using five-fold stratified cross-validation and added SHAP analysis. | The selected candidate improved training-CV urgent F1 but did not improve the preliminary holdout result. |
| Week 6 reliability | Used five-outer/four-inner nested cross-validation, threshold testing, and error analysis. | Threshold `0.45` labeled every message urgent; threshold `0.50` missed 22 of 24 urgent messages. The disposition is `revise`. |
| Week 7 readiness | Added explicit readiness gates, automated validation, and a local FastAPI demonstration. | The software workflow passed its local-demonstration gate; predictive, shadow-testing, and production gates remain unpassed. |
| Week 8 delivery | Packaged the validated demonstration with English-authoritative narration, selectable multilingual subtitles, language-specific editions, scripts, and QA evidence. | The final package demonstrates the Gate A workflow while preserving the `revise` decision, required human review, and no deployment or shadow-testing approval. |

The preliminary 40-message holdout informed earlier model comparisons and is
not presented as untouched final evidence.

## Final Week 8 Demonstration

For the shortest faculty review path, start with the
[`Week 8 demonstration package guide`](coursework/week8/submission/demonstration/README.md),
then open the recommended
[`English-authoritative MP4 with selectable multilingual subtitles`](coursework/week8/submission/demonstration/Week_8_Project_Demonstration_Keith_Broussard_Multilingual_Subtitles.mp4).
The package also includes English, Spanish, Hindi, and Simplified Chinese
language-specific editions, external captions, and narration scripts.

The demonstration is a presentation of the validated research workflow. It
does not replace the executed notebooks and saved metrics as predictive
evidence, and it does not change the model disposition from `revise`.

## Choose a Review Path

| Reader | Recommended starting point |
|---|---|
| Academic reviewer | [`docs/README.md#academic-review`](docs/README.md#academic-review) |
| Stakeholder | [`docs/README.md#stakeholder-review`](docs/README.md#stakeholder-review) |
| Technical reviewer | [`docs/week7_demo_runbook.md`](docs/week7_demo_runbook.md) |
| Evidence auditor | [`results/README.md`](results/README.md) |

### Key Records

- Current model decision: [`docs/week6_experiment_record.md`](docs/week6_experiment_record.md)
- Automated test purpose and results: [`docs/week7_automated_test_report.md`](docs/week7_automated_test_report.md)
- Readiness criteria: [`docs/week7_conditional_advancement_gates.md`](docs/week7_conditional_advancement_gates.md)
- Readiness conclusion: [`docs/week7_readiness_evaluation.md`](docs/week7_readiness_evaluation.md)
- Final Week 8 demonstration: [`coursework/week8/submission/demonstration/README.md`](coursework/week8/submission/demonstration/README.md)
- Notebook workflow and output map: [`notebooks/README.md`](notebooks/README.md)
- Chronological decisions: [`docs/decisions.md`](docs/decisions.md)

## Repository Structure

```text
.
├── src/email_triage_demo/    Local research-demonstration application
├── notebooks/                Canonical executed analyses and output guide
├── tests/                    Automated test coverage and commands
├── scripts/                  Model build and validation utilities
├── data/
│   ├── labels/               Tracked reviewed-label manifest
│   ├── raw/                  Local Enron CSV; excluded from Git
│   └── processed/            Local review workbooks; excluded from Git
├── results/
│   ├── metrics/              Exact CSV and JSON evidence
│   └── figures/              Exported analytical figures
├── docs/                     Experiment, decision, readiness, and runbook records
├── coursework/               Earlier capstone report and notebook snapshots
├── requirements.txt          Notebook and analysis environment
└── requirements-demo.txt     Pinned local-demonstration environment
```

Each major folder has its own README so GitHub and local users can navigate the
project without first reading source code:

- [`docs/README.md`](docs/README.md)
- [`notebooks/README.md`](notebooks/README.md)
- [`results/README.md`](results/README.md)
- [`tests/README.md`](tests/README.md)
- [`scripts/README.md`](scripts/README.md)
- [`src/email_triage_demo/README.md`](src/email_triage_demo/README.md)

## Reproduce the Analysis

### 1. Prepare the data

Download the Kaggle distribution of the Enron Email Dataset and place its
`emails.csv` file at:

```text
data/raw/emails.csv
```

- Reproducibility source: <https://www.kaggle.com/datasets/wcukierski/enron-email-dataset>
- Original corpus provenance: <https://www.cs.cmu.edu/~enron/>

The raw corpus and detailed review workbooks remain excluded because they
contain email content. The tracked label manifest contains identifiers,
sampling strata, approved labels, versions, and review status—but no subjects,
bodies, excerpts, reviewer names, reasons, or notes.

### 2. Create the environment

Python 3.11 is supported.

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m ipykernel install --user \
  --name email-triage-py311 \
  --display-name "Email Triage (Python 3.11)"
```

### 3. Run the notebooks

Open JupyterLab and run the canonical notebooks from top to bottom in this
order:

```bash
jupyter lab
```

1. `notebooks/baseline_model.ipynb`
2. `notebooks/week4_model_optimization.ipynb`
3. `notebooks/week6_testing_debugging.ipynb`

The notebooks create or refresh their privacy-screened CSV, JSON, and figure
outputs under `results/`. Exact noninteractive commands and a description of
every generated artifact are in [`notebooks/README.md`](notebooks/README.md#workflow-and-output-map).
The committed executed notebooks and evidence files also allow review without
rerunning the analysis.

## Run the Week 7 Validation and Demonstration

The local web application is a research prototype. It requires human review
and does not represent deployment or shadow-testing approval.

```bash
python -m pip install -r requirements-demo.txt
PYTHONPATH=src python scripts/build_week7_demo_model.py
PYTHONPATH=src python -m unittest -v \
  tests/test_week7_demo.py tests/test_week7_readiness.py
PYTHONPATH=src python scripts/validate_week7_demo.py
PYTHONPATH=src uvicorn email_triage_demo.app:app \
  --host 127.0.0.1 --port 8765
```

Open <http://127.0.0.1:8765/> and use only synthetic or privacy-screened
messages. The generated model artifact remains local and excluded from Git.
The complete procedure and safe-failure checks are in
[`docs/week7_demo_runbook.md`](docs/week7_demo_runbook.md).

## Evidence and Interpretation

- CSV files preserve exact experimental metrics and decisions.
- JSON files preserve configuration, hashes, and automated validation results.
- Executed notebooks preserve the code, output, sequence, and experimental context.
- Markdown records explain purpose, methodology, conclusions, and limitations.
- Automated tests establish software behavior and evidence integrity; they do
  not establish predictive accuracy or production readiness.

The central evidence boundary remains unchanged: the model needs more reviewed
labels, related-message grouping, an untouched evaluation design, and further
threshold analysis before predictive or deployment approval should be
considered.

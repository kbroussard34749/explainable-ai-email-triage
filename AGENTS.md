# Explainable AI Email Triage Repository Instructions

This repository is the source of truth for the capstone's technical work.

- Start each task by confirming the repository, branch, status, and checkpoint tag.
- Store code, notebooks, models, reproducible metrics, figures, and technical documentation here.
- Do not overwrite the submitted Week 3 or Week 4 notebooks, reports, metrics, or submission copies. Create new files for Week 6 work.
- Use `week6-start-v1` as the checkpoint from before Week 6 implementation began.
- Before working on Week 6 code or the submission package, read `Assignments_Week_6.md` and `Learning_Materials_Week_6.md` in `/Users/keithgb/Documents/College - UC Courses/Courses Summer 2026/Capstone/Week 6/02_Planning`.
- Follow `Assignments_Week_6.md` for the due date, deliverables, and instructor directions. Follow the Week 6 entries in `docs/decisions.md` for the pre-registered technical method.
- Week 6 requires updated code with test results and one 2–3-page debugging and evaluation report. Use cross-validation for the required testing method. Do not state that both cross-validation and A/B testing are required.
- Keep model and threshold selection inside the training data. Use the preserved 40-message holdout only once, after freezing the Week 6 method, and describe it as preliminary evidence rather than an untouched production estimate.
- Focus on urgent-class F1, urgent recall, and urgent false negatives. Report the false-positive review burden instead of relying on accuracy alone.
- Do not export or commit email subjects, bodies, excerpts, reviewer notes, or other unnecessary message content. Privacy-safe evidence may include message identifiers, labels, probabilities, error types, aggregate metrics, and approved error categories.
- Keep a person in the review process. Do not present Week 6 results as approval for autonomous deployment. If the evidence supports it, recommend only human-supervised shadow testing.
- Generate reproducible Week 6 evidence in this repository. Copy only the selected report-ready exports to the Week 6 `03_Analysis_Artifacts` folder.
- Keep editable report drafts in the Week 6 `04_Report_Drafts` folder and the final upload package in `05_Submission`. Do not create competing editable report or submission copies in this repository.
- Validate the final notebook, artifacts, and report before using the LMS uploader. The captured Week 6 assignment page showed one attempt remaining.
- Treat `/Users/keithgb/.codex/.chatgpt-projects/g-p-6a39db5fa2708191a4949b3f6f12ccc5/sources` as a read-only reference mirror. Do not copy the full `sources` directory into this repository.
- Preserve unrelated work. Do not move, delete, rewrite, commit, or publish it as part of Week 6 implementation.

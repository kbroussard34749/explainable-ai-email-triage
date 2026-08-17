# Week 8 Project Demonstration

This folder contains Keith G. Broussard's final Week 8 Explainable AI Email Triage demonstration package for MSAI-699-B01 Capstone.

## Recommended Review File

Open `Week_8_Project_Demonstration_Keith_Broussard_Multilingual_Subtitles.mp4` for the authoritative English narration with selectable English, Spanish, Hindi, and Simplified Chinese subtitle tracks. English is the default subtitle track.

## Language-Specific Narration

- `Week_8_Project_Demonstration_Keith_Broussard_English.mp4`
- `Week_8_Project_Demonstration_Keith_Broussard_Spanish.mp4`
- `Week_8_Project_Demonstration_Keith_Broussard_Hindi.mp4`
- `Week_8_Project_Demonstration_Keith_Broussard_Simplified_Chinese.mp4`

Each language-specific edition contains matching narration and an embedded default subtitle track. External SRT files are included for accessibility and platform compatibility. The four source-language scripts document the words used for the narration and captions.

## Where to Find the Demonstration Evidence

Start with [`docs/project_review_guide.md`](../../../../docs/project_review_guide.md), which is also linked from the repository's main [`README.md`](../../../../README.md). The review guide connects the conclusions in `docs/` to the machine-readable CSV and JSON evidence in `results/metrics/`.

| Demonstration statement | Explanation | Supporting evidence |
|---|---|---|
| Threshold disagreement and `revise` decision | [`docs/week6_experiment_record.md`](../../../../docs/week6_experiment_record.md) | [`results/metrics/week6_threshold_analysis.csv`](../../../../results/metrics/week6_threshold_analysis.csv) |
| 13 automated tests passed | [`docs/week7_automated_test_report.md`](../../../../docs/week7_automated_test_report.md) | [`tests/`](../../../../tests/) and [`results/metrics/week7_demo_validation.json`](../../../../results/metrics/week7_demo_validation.json) |
| 60 deterministic synthetic inference runs | [`docs/week7_automated_test_report.md`](../../../../docs/week7_automated_test_report.md) | [`results/metrics/week7_demo_validation.json`](../../../../results/metrics/week7_demo_validation.json) |
| Gate A readiness and Gate B limitation | [`docs/week7_readiness_evaluation.md`](../../../../docs/week7_readiness_evaluation.md) | [`results/metrics/week7_demo_validation.json`](../../../../results/metrics/week7_demo_validation.json) |
| Reproduction and safe-failure procedure | [`docs/week7_demo_runbook.md`](../../../../docs/week7_demo_runbook.md) | [`src/email_triage_demo/`](../../../../src/email_triage_demo/) and [`tests/`](../../../../tests/) |

## Validation

See [`Week_8_Project_Demonstration_QA.md`](Week_8_Project_Demonstration_QA.md) for duration, stream, subtitle, decode, loudness, narration-review, and SHA-256 validation results.

The package supports a controlled local research demonstration. It does not establish predictive reliability, production readiness, or approval for shadow testing. The classifier remains `revise`, and every result requires human review.

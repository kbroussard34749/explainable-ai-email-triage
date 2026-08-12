# Documentation and Evidence Guide

This index routes readers to the shortest evidence path for their purpose. The current conclusion is consistent across the project: the repository supports a controlled local research demonstration, while the predictive model remains `revise` and is not approved for production or shadow testing.

## Academic Review

Use this path to evaluate the project's methodology, experimental discipline, reproducibility, interpretation, and technical communication.

1. [`project_review_guide.md`](project_review_guide.md) — complete project overview, methodology, evidence, execution, and limitations.
2. [`decisions.md`](decisions.md) — chronological decisions, justifications, and evidence boundaries.
3. [`labeling_guide.md`](labeling_guide.md) — operational urgency definition and deterministic labeling rules.
4. [`../notebooks/README.md`](../notebooks/README.md) — guide to the three canonical executed notebooks.
5. [`week4_experiment_record.md`](week4_experiment_record.md) — controlled optimization and explainability experiment.
6. [`week6_experiment_record.md`](week6_experiment_record.md) — nested cross-validation, threshold testing, errors, and frozen `revise` decision.
7. [`week7_automated_test_report.md`](week7_automated_test_report.md) — purpose, coverage, and results for all 13 automated tests.
8. [`week7_conditional_advancement_gates.md`](week7_conditional_advancement_gates.md) — distinction among demonstration, reliability, shadow testing, and production gates.
9. [`../results/README.md`](../results/README.md) — map from the written conclusions to exact CSV, JSON, and figure evidence.

### Prior Technical Reports

These files show how the project and its conclusions developed over time:

- [Week 3 baseline report](../coursework/week3/submission/Week_3_Model_Selection_and_Baseline_Keith_Broussard.pdf)
- [Week 4 optimization report](../coursework/week4/submission/Week_4_Model_Optimization_Report_Keith_Broussard.pdf)
- [Week 5 deployment-strategy report](../coursework/week5/submission/Deployment_Strategy_Report_for_Email_Triage_AI_Model_Keith_Broussard_FINAL.pdf)
- [Week 6 testing and debugging report](../coursework/week6/submission/Week_6_Model_Testing_and_Debugging_Report_Keith_Broussard.pdf)

## Stakeholder Review

Use this shorter path to understand what the system does, what the evidence supports, and why human oversight remains necessary.

1. [`week6_experiment_record.md`](week6_experiment_record.md) — explains why neither tested threshold provides a reliable operating point.
2. [`week7_readiness_evaluation.md`](week7_readiness_evaluation.md) — compares the frozen candidate with the provisional reliability gates.
3. [`week7_conditional_advancement_gates.md`](week7_conditional_advancement_gates.md) — defines what has passed and what remains unapproved.
4. [`week7_demo_runbook.md`](week7_demo_runbook.md) — shows what can be demonstrated safely and locally.

The practical conclusion is narrow: the interface and verification workflow are ready for a local research demonstration. The classifier is not ready to automate email routing.

## Technical Review

Use this path to run the application or inspect its implementation.

1. Follow [`week7_demo_runbook.md`](week7_demo_runbook.md).
2. Inspect the application in [`../src/email_triage_demo/`](../src/email_triage_demo/).
3. Review test coverage and commands in [`../tests/README.md`](../tests/README.md).
4. Inspect exact validation output through [`../results/README.md`](../results/README.md).
5. Review environment definitions in [`../requirements-demo.txt`](../requirements-demo.txt) and [`../requirements.txt`](../requirements.txt).

## Documentation by Project Stage

| Stage | Primary readable record | Supporting analysis |
|---|---|---|
| Baseline | [`week3_baseline_report.md`](week3_baseline_report.md) | [`../notebooks/baseline_model.ipynb`](../notebooks/baseline_model.ipynb) |
| Optimization and explainability | [`week4_experiment_record.md`](week4_experiment_record.md) | [`../notebooks/week4_model_optimization.ipynb`](../notebooks/week4_model_optimization.ipynb) |
| Reliability and debugging | [`week6_experiment_record.md`](week6_experiment_record.md) | [`../notebooks/week6_testing_debugging.ipynb`](../notebooks/week6_testing_debugging.ipynb) |
| Demonstration readiness | [`week7_automated_test_report.md`](week7_automated_test_report.md) | [`week7_conditional_advancement_gates.md`](week7_conditional_advancement_gates.md) |

## Evidence Boundaries

- Executed notebooks and saved metrics support measured experimental claims.
- Markdown records explain purpose, methodology, interpretation, and limitations.
- CSV and JSON files preserve exact values and validation outcomes.
- Automated tests establish application behavior and evidence integrity, not predictive accuracy.
- Passing the local-demonstration gate does not establish production readiness.

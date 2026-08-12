#!/usr/bin/env python3
"""Validate the frozen evidence used by the Week 7 readiness assessment.

This precheck asks whether required records are present, internally consistent,
executed, and privacy-screened. Passing it does not mean the model passed the
separate predictive-reliability gate.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path


REQUIRED_NOTEBOOKS = (
    "notebooks/baseline_model.ipynb",
    "notebooks/week4_model_optimization.ipynb",
    "notebooks/week6_testing_debugging.ipynb",
)
REQUIRED_EVIDENCE = (
    "docs/week6_experiment_record.md",
    "docs/week7_conditional_advancement_gates.md",
    "docs/week7_automated_test_report.md",
    "docs/week7_demo_runbook.md",
    "docs/week7_readiness_evaluation.md",
    "results/metrics/week6_cv_summary.csv",
    "results/metrics/week6_model_decision.csv",
    "results/metrics/week6_reproducibility.json",
    "results/metrics/week7_readiness_gate_evaluation.csv",
    "results/metrics/week7_demo_model_metadata.json",
    "results/metrics/week7_demo_validation.json",
    "requirements-demo.txt",
    "scripts/validate_week7_demo.py",
    "scripts/validate_week7_readiness.py",
    "tests/test_week7_demo.py",
    "tests/test_week7_readiness.py",
)
PRIVACY_FORBIDDEN_COLUMNS = {
    "subject",
    "body",
    "message_text",
    "email_text",
    "excerpt",
    "reviewer",
    "reviewer_name",
    "reviewer_note",
    "review_notes",
    "label_reason",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def notebook_check(path: Path, root: Path) -> dict[str, object]:
    """Confirm that saved code cells executed and contain no saved exceptions."""
    notebook = json.loads(path.read_text(encoding="utf-8"))
    code_cells = [cell for cell in notebook.get("cells", []) if cell.get("cell_type") == "code"]
    unexecuted = [index for index, cell in enumerate(code_cells, start=1) if cell.get("execution_count") is None]
    errors = []
    for index, cell in enumerate(code_cells, start=1):
        for output in cell.get("outputs", []):
            if output.get("output_type") == "error":
                errors.append({"code_cell": index, "ename": output.get("ename"), "evalue": output.get("evalue")})
    return {
        "path": str(path.relative_to(root)),
        "code_cells": len(code_cells),
        "unexecuted_code_cells": unexecuted,
        "error_outputs": errors,
        "passed": not unexecuted and not errors,
    }


def evaluate(root: Path) -> dict[str, object]:
    """Reconcile current readiness records against frozen Week 6 evidence."""
    checks: dict[str, object] = {}

    missing = [relative for relative in REQUIRED_EVIDENCE if not (root / relative).is_file() or (root / relative).stat().st_size == 0]
    checks["required_evidence"] = {"passed": not missing, "missing_or_empty": missing}

    notebooks = [notebook_check(root / relative, root) for relative in REQUIRED_NOTEBOOKS]
    checks["executed_notebooks"] = {"passed": all(item["passed"] for item in notebooks), "items": notebooks}

    # Treat the decision artifact as a contract. A demo must never turn the
    # historical `revise` result into deployment or shadow-test approval.
    decision_rows = read_csv(root / "results/metrics/week6_model_decision.csv")
    decision = decision_rows[0] if len(decision_rows) == 1 else {}
    decision_passed = (
        decision.get("model_disposition") == "revise"
        and decision.get("deployment_approval") == "False"
        and decision.get("shadow_testing_approval") == "False"
        and decision.get("holdout_influenced_decision") == "False"
    )
    checks["frozen_decision"] = {"passed": decision_passed, "record": decision}

    # Recompute the Gate B comparison inputs from the saved cross-validation
    # summary rather than trusting copied values in the Week 7 gate table.
    cv = {row["strategy"]: row for row in read_csv(root / "results/metrics/week6_cv_summary.csv")}
    gate_rows = {row["gate"]: row for row in read_csv(root / "results/metrics/week7_readiness_gate_evaluation.csv")}
    expected = {
        "urgent_recall": (float(cv["nested_selected_threshold"]["urgent_recall"]), float(cv["default_0.50"]["urgent_recall"])),
        "urgent_precision": (float(cv["nested_selected_threshold"]["urgent_precision"]), float(cv["default_0.50"]["urgent_precision"])),
        "urgent_f1": (float(cv["nested_selected_threshold"]["urgent_f1"]), float(cv["default_0.50"]["urgent_f1"])),
        "false_positive_rate": (
            int(cv["nested_selected_threshold"]["false_positives"]) / (int(cv["nested_selected_threshold"]["true_negatives"]) + int(cv["nested_selected_threshold"]["false_positives"])),
            int(cv["default_0.50"]["false_positives"]) / (int(cv["default_0.50"]["true_negatives"]) + int(cv["default_0.50"]["false_positives"])),
        ),
    }
    mismatches = []
    for gate, values in expected.items():
        row = gate_rows.get(gate, {})
        actual = (row.get("threshold_0_45_value"), row.get("threshold_0_50_value"))
        try:
            matches = abs(float(actual[0]) - values[0]) <= 1e-12 and abs(float(actual[1]) - values[1]) <= 1e-12
        except (TypeError, ValueError):
            matches = False
        if not matches:
            mismatches.append({"gate": gate, "expected": values, "actual": actual})
    checks["gate_traceability"] = {"passed": not mismatches, "mismatches": mismatches}

    # This is a schema-level privacy check. It guards tracked artifacts from
    # common sensitive columns; it does not claim a complete privacy audit.
    privacy_files = (
        "results/metrics/week6_error_analysis.csv",
        "results/metrics/week6_outer_predictions.csv",
        "results/metrics/week7_readiness_gate_evaluation.csv",
    )
    privacy_findings = []
    for relative in privacy_files:
        path = root / relative
        with path.open(newline="", encoding="utf-8") as handle:
            fields = set(csv.DictReader(handle).fieldnames or [])
        forbidden = sorted(fields & PRIVACY_FORBIDDEN_COLUMNS)
        if forbidden:
            privacy_findings.append({"path": relative, "forbidden_columns": forbidden})
    checks["privacy_safe_columns"] = {"passed": not privacy_findings, "findings": privacy_findings}

    # Hashes make later changes visible and tie the precheck to exact evidence
    # files. They establish integrity and traceability, not scientific validity.
    source_paths = [root / relative for relative in REQUIRED_EVIDENCE]
    checks["evidence_hashes"] = {str(path.relative_to(root)): sha256(path) for path in source_paths if path.is_file()}
    overall = all(value.get("passed", True) for key, value in checks.items() if key != "evidence_hashes")
    return {
        "record_type": "week7_demonstration_readiness_precheck",
        "scope": "evidence_integrity_reproducibility_and_privacy_precheck",
        "model_reliability_disposition": "revise",
        "deployment_approval": False,
        "shadow_testing_approval": False,
        "overall_precheck_passed": overall,
        "checks": checks,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = evaluate(args.root.resolve())
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if result["overall_precheck_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

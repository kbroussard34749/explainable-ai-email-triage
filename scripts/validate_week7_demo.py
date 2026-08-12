#!/usr/bin/env python3
"""Validate engineering properties of the controlled local demonstration.

The checks address repeatability, privacy boundaries, safe metadata, bounded
explanations, and observed local timing. Synthetic examples cannot establish
predictive accuracy, demographic fairness, or production performance.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import statistics
import time
from pathlib import Path

from email_triage_demo.model_service import ModelService


# The cases exercise different input shapes and vocabulary without copying
# private email content. They are functional probes, not a labeled test set.
SYNTHETIC_CASES = (
    ("deadline", "Synthetic deadline reminder", "Please review this synthetic example before 3 PM today."),
    ("routine", "Synthetic weekly update", "This synthetic status summary is for the next team meeting."),
    ("action", "", "Immediate action is requested for this synthetic test message."),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def percentile(values: list[float], fraction: float) -> float:
    """Return a simple observed percentile for descriptive local timing."""
    ordered = sorted(values)
    index = min(len(ordered) - 1, max(0, int(round((len(ordered) - 1) * fraction))))
    return ordered[index]


def validate(root: Path, artifact: Path) -> dict[str, object]:
    """Run Gate A checks without making a Gate B reliability claim."""
    metadata_path = root / "results/metrics/week7_demo_model_metadata.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    load_started = time.perf_counter()
    service = ModelService.load(artifact)
    load_ms = (time.perf_counter() - load_started) * 1_000

    # Verify both the governance flags and the artifact digest. This prevents a
    # different local model from silently inheriting the approved demo record.
    boundary_passed = (
        metadata.get("artifact_role") == "local_research_demonstration_only"
        and metadata.get("artifact_committed") is False
        and metadata.get("model_disposition") == "revise"
        and metadata.get("deployment_approval") is False
        and metadata.get("shadow_testing_approval") is False
        and metadata.get("human_review_required") is True
        and metadata.get("local_artifact_sha256") == sha256(artifact)
    )

    case_results = []
    latencies = []
    deterministic = True
    privacy_safe = True
    for case_id, subject, body in SYNTHETIC_CASES:
        outputs = []
        # Repeated inference checks deterministic scoring for a fixed artifact.
        # It does not require byte-identical joblib files across rebuilds.
        for _ in range(20):
            started = time.perf_counter()
            output = service.analyze(subject, body)
            latencies.append((time.perf_counter() - started) * 1_000)
            outputs.append(output)
        deterministic = deterministic and all(output == outputs[0] for output in outputs[1:])
        # Serialize exactly what could enter the saved result and confirm that
        # neither complete synthetic input is echoed back into that record.
        rendered = json.dumps(outputs[0])
        privacy_safe = privacy_safe and (not subject or subject not in rendered) and (not body or body not in rendered)
        case_results.append(
            {
                "case_id": case_id,
                "urgent_probability": outputs[0]["urgent_probability"],
                "threshold_comparison": outputs[0]["threshold_comparison"],
                "supporting_feature_count": len(outputs[0]["explanation"]["supports_urgent"]),
                "opposing_feature_count": len(outputs[0]["explanation"]["supports_nonurgent"]),
            }
        )

    return {
        "record_type": "week7_local_research_demo_validation",
        "artifact_committed": False,
        "research_only": True,
        "model_disposition": "revise",
        "deployment_approval": False,
        "shadow_testing_approval": False,
        "human_review_required": True,
        "checks": {
            "artifact_boundary": {"passed": boundary_passed},
            "deterministic_repeated_scoring": {"passed": deterministic, "repetitions_per_case": 20},
            "input_not_echoed_or_retained_in_result": {"passed": privacy_safe},
            "thresholds_visible": {"passed": all(set(row["threshold_comparison"]) == {"0.45", "0.50"} for row in case_results)},
            "bounded_explanations": {"passed": all(row["supporting_feature_count"] <= 5 and row["opposing_feature_count"] <= 5 for row in case_results)},
        },
        # These measurements characterize one local run only. They are not a
        # load test, service-level objective, or production latency guarantee.
        "local_performance_observation": {
            "model_load_milliseconds": round(load_ms, 3),
            "inference_runs": len(latencies),
            "minimum_milliseconds": round(min(latencies), 3),
            "median_milliseconds": round(statistics.median(latencies), 3),
            "p95_milliseconds": round(percentile(latencies, 0.95), 3),
            "maximum_milliseconds": round(max(latencies), 3),
            "production_guarantee": False,
        },
        "privacy_safe_case_results": case_results,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--artifact", type=Path, default=Path("models/week7_research_demo.joblib"))
    parser.add_argument("--output", type=Path, default=Path("results/metrics/week7_demo_validation.json"))
    args = parser.parse_args()
    root = args.root.resolve()
    artifact = args.artifact if args.artifact.is_absolute() else root / args.artifact
    output = args.output if args.output.is_absolute() else root / args.output
    result = validate(root, artifact)
    result["overall_passed"] = all(check["passed"] for check in result["checks"].values())
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["overall_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

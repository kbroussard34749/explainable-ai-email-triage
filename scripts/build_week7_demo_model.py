#!/usr/bin/env python3
"""Build the local Week 7 demonstration artifact from the frozen workflow.

This script recreates an engineering artifact for demonstration. It does not
run a new experiment, reopen threshold selection, or treat the preliminary
holdout as untouched evidence.
"""

from __future__ import annotations

import argparse
import gc
import hashlib
import json
import platform
from email import policy
from email.parser import Parser
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split

from email_triage_demo.model_service import SEED, make_frozen_candidate


def sha256(path: Path) -> str:
    """Hash a source or artifact so the recorded build can be traced exactly."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_email(raw_message: str) -> str:
    """Extract subject and plain-text body using the same modeling representation."""
    parsed = Parser(policy=policy.default).parsestr(raw_message)
    subject = str(parsed.get("subject", "")).strip()
    try:
        if parsed.is_multipart():
            body_part = parsed.get_body(preferencelist=("plain",))
            body = body_part.get_content() if body_part else ""
        else:
            body = parsed.get_content()
    except Exception:
        # Some historical messages are malformed. The fallback preserves the
        # payload for reproducibility rather than silently dropping the record.
        body = str(parsed.get_payload())
    return f"{subject}\n\n{str(body).strip()}".strip()


def build(root: Path, output: Path, metadata_output: Path) -> dict[str, object]:
    """Rebuild the frozen training candidate and write privacy-safe metadata."""
    raw_path = root / "data/raw/emails.csv"
    labels_path = root / "data/labels/enron_urgency_labels_v1.csv"
    labels = pd.read_csv(labels_path)
    # Stop immediately if the reviewed population has drifted. Training on a
    # partial, duplicated, or relabeled set would no longer reproduce the
    # documented Week 4/Week 6 conditions.
    if len(labels) != 199 or not labels["message_id"].is_unique:
        raise ValueError("The reviewed label manifest does not match the frozen 199-message population.")
    if set(labels["urgency_label"]) != {"urgent", "nonurgent"}:
        raise ValueError("Unexpected urgency labels in the reviewed manifest.")

    requested = set(labels["message_id"])
    rows = []
    # The Enron source is large, so scan it in bounded chunks and retain only
    # the 199 reviewed message identifiers. Raw message text stays local.
    for chunk in pd.read_csv(raw_path, usecols=["file", "message"], chunksize=10_000):
        matched = chunk.loc[chunk["file"].isin(requested), ["file", "message"]]
        if not matched.empty:
            rows.append(matched)
    raw = pd.concat(rows, ignore_index=True)
    if len(raw) != 199 or set(raw["file"]) != requested:
        raise ValueError("The raw source did not reproduce the frozen reviewed population.")
    raw["combined_text"] = raw["message"].map(parse_email)
    modeling = labels[["message_id", "urgency_label"]].merge(
        raw[["file", "combined_text"]], left_on="message_id", right_on="file", validate="one_to_one"
    )
    del raw, rows
    gc.collect()

    # Recreate the original stratified 159/40 split using the recorded seed.
    # The discarded values are the selection-influenced preliminary holdout;
    # they are intentionally excluded from fitting this demonstration model.
    X_train, _, y_train, _ = train_test_split(
        modeling["combined_text"],
        modeling["urgency_label"],
        test_size=0.20,
        random_state=SEED,
        stratify=modeling["urgency_label"],
    )
    pipeline = make_frozen_candidate()
    pipeline.fit(X_train, y_train)
    # Store configuration, provenance, versions, and decision boundaries—but
    # never email text—in the tracked evidence record.
    metadata = {
        "artifact_role": "local_research_demonstration_only",
        "artifact_committed": False,
        "model_disposition": "revise",
        "deployment_approval": False,
        "shadow_testing_approval": False,
        "human_review_required": True,
        "random_state": SEED,
        "training_records": int(len(X_train)),
        "training_label_counts": {key: int(value) for key, value in y_train.value_counts().to_dict().items()},
        "label_manifest_sha256": sha256(labels_path),
        "python_version": platform.python_version(),
        "numpy_version": np.__version__,
        "pandas_version": pd.__version__,
        "joblib_version": joblib.__version__,
        "python_scikit_learn_version": sklearn.__version__,
        "thresholds_for_demonstration": [0.45, 0.50],
        "privacy": "No email text is included in the metadata or committed artifacts.",
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    # The joblib artifact contains fitted vocabulary learned from email text,
    # so .gitignore keeps it local even though its digest is recorded below.
    joblib.dump({"pipeline": pipeline, "metadata": metadata}, output)
    metadata["local_artifact_sha256"] = sha256(output)
    metadata_output.parent.mkdir(parents=True, exist_ok=True)
    metadata_output.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return metadata


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=Path("models/week7_research_demo.joblib"))
    parser.add_argument("--metadata-output", type=Path, default=Path("results/metrics/week7_demo_model_metadata.json"))
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output if args.output.is_absolute() else root / args.output
    metadata_output = args.metadata_output if args.metadata_output.is_absolute() else root / args.metadata_output
    print(json.dumps(build(root, output, metadata_output), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

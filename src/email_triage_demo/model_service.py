"""Model construction and inference for the controlled local demonstration.

This module intentionally separates demonstration behavior from model approval.
It can reproduce and explain the frozen candidate, but it does not convert the
Week 6 `revise` decision into evidence of predictive reliability.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


# These values come from the frozen experiment record. They are displayed
# side-by-side to expose threshold sensitivity, not searched again here.
SEED = 42
RESEARCH_THRESHOLDS = (0.45, 0.50)
MAX_EXPLANATION_FEATURES = 5


def make_frozen_candidate() -> Pipeline:
    """Recreate the frozen Week 4 candidate used by the Week 6 evaluation.

    Keeping preprocessing inside the pipeline ensures that the vectorizer is
    fitted only when the model is fitted. The parameters are historical inputs
    to this build; this function performs no new tuning or model selection.
    """
    return Pipeline(
        [
            (
                "tfidf",
                TfidfVectorizer(
                    lowercase=True,
                    stop_words="english",
                    ngram_range=(1, 1),
                    min_df=2,
                    sublinear_tf=True,
                ),
            ),
            (
                "classifier",
                LogisticRegression(
                    C=0.1,
                    class_weight="balanced",
                    max_iter=1_000,
                    random_state=SEED,
                ),
            ),
        ]
    )


@dataclass(frozen=True)
class ModelService:
    pipeline: Pipeline
    metadata: dict[str, Any]

    @classmethod
    def load(cls, artifact_path: Path) -> "ModelService":
        """Load only an artifact that preserves the project's decision boundary.

        These checks are intentionally fail-closed. A technically loadable model
        is not enough: its metadata must still identify it as research-only,
        retain the `revise` disposition, and explicitly deny deployment.
        """
        package = joblib.load(artifact_path)
        if not isinstance(package, dict) or "pipeline" not in package or "metadata" not in package:
            raise ValueError("The research model artifact has an invalid package structure.")
        metadata = package["metadata"]
        if metadata.get("artifact_role") != "local_research_demonstration_only":
            raise ValueError("The artifact is not marked for the local research demonstration.")
        if metadata.get("model_disposition") != "revise":
            raise ValueError("The artifact metadata does not preserve the revise disposition.")
        if metadata.get("deployment_approval") is not False:
            raise ValueError("The artifact metadata must explicitly deny deployment approval.")
        return cls(pipeline=package["pipeline"], metadata=metadata)

    def analyze(self, subject: str, body: str) -> dict[str, Any]:
        """Score one message and return bounded, privacy-conscious evidence.

        The response reports both frozen thresholds because Week 6 showed that
        the operating decision changes sharply between them. It does not choose
        a threshold or make a routing decision for the user.
        """
        combined_text = f"{subject.strip()}\n\n{body.strip()}".strip()
        probabilities = self.pipeline.predict_proba([combined_text])[0]
        classifier = self.pipeline.named_steps["classifier"]
        # scikit-learn orders classes internally, so locate "urgent" by label
        # instead of assuming it occupies a fixed probability column.
        urgent_index = list(classifier.classes_).index("urgent")
        probability = float(probabilities[urgent_index])

        # For this linear model, feature value multiplied by coefficient gives
        # the feature's additive contribution to the log-odds. It explains the
        # fitted model's calculation; it does not establish why an email is
        # truly urgent and must not be presented as a causal explanation.
        vectorizer = self.pipeline.named_steps["tfidf"]
        vector = vectorizer.transform([combined_text])
        feature_names = vectorizer.get_feature_names_out()
        contributions = vector.multiply(classifier.coef_[0]).tocoo()
        contribution_rows = [
            (feature_names[column], float(value))
            for column, value in zip(contributions.col, contributions.data)
            if value != 0
        ]
        supporting = sorted((row for row in contribution_rows if row[1] > 0), key=lambda row: row[1], reverse=True)
        opposing = sorted((row for row in contribution_rows if row[1] < 0), key=lambda row: row[1])

        # Bound the list so the interface remains reviewable and does not expose
        # the full feature vector. Raw subject and body text are never returned.
        def serialize(rows: list[tuple[str, float]]) -> list[dict[str, Any]]:
            return [
                {"feature": feature, "contribution": round(value, 6)}
                for feature, value in rows[:MAX_EXPLANATION_FEATURES]
            ]

        return {
            "urgent_probability": round(probability, 6),
            "threshold_comparison": {
                f"{threshold:.2f}": "urgent" if probability >= threshold else "nonurgent"
                for threshold in RESEARCH_THRESHOLDS
            },
            "explanation": {
                "supports_urgent": serialize(supporting),
                "supports_nonurgent": serialize(opposing),
                "method": "TF-IDF feature contribution multiplied by the fitted logistic-regression coefficient",
                "causal_claim": False,
            },
            "model_disposition": "revise",
            "research_only": True,
            "human_review_required": True,
            "deployment_approval": False,
            "shadow_testing_approval": False,
        }

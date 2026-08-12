"""API contract tests for the controlled Week 7 demonstration.

The fake service isolates interface and safety behavior from model quality.
Predictive claims remain governed by the separate experiment evidence.
"""

import unittest

import httpx

from email_triage_demo.app import create_app


class FakeModelService:
    """Return a fixed boundary-case response without loading private data."""
    def analyze(self, subject, body):
        return {
            "urgent_probability": 0.48,
            "threshold_comparison": {"0.45": "urgent", "0.50": "nonurgent"},
            "explanation": {"supports_urgent": [], "supports_nonurgent": [], "causal_claim": False},
            "model_disposition": "revise",
            "research_only": True,
            "human_review_required": True,
            "deployment_approval": False,
            "shadow_testing_approval": False,
        }


class Week7DemoTests(unittest.IsolatedAsyncioTestCase):
    """Verify observable safeguards at the HTTP boundary."""
    def client_for(self, app):
        return httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test")

    async def test_index_discloses_research_boundary(self):
        async with self.client_for(create_app(FakeModelService())) as client:
            response = await client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Research prototype", response.text)
        self.assertIn("human review", response.text)

    async def test_health_preserves_revise_and_no_approval(self):
        async with self.client_for(create_app(FakeModelService())) as client:
            response = await client.get("/api/health")
        payload = response.json()
        self.assertEqual(payload["status"], "ready")
        self.assertEqual(payload["model_disposition"], "revise")
        self.assertFalse(payload["deployment_approval"])
        self.assertFalse(payload["shadow_testing_approval"])

    async def test_valid_request_returns_thresholds_and_human_review(self):
        # This example deliberately falls between the two frozen thresholds so
        # the test catches any interface change that hides their disagreement.
        source = {"subject": "Synthetic deadline", "body": "Please review this synthetic example today."}
        async with self.client_for(create_app(FakeModelService())) as client:
            response = await client.post("/api/analyze", json=source)
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload["threshold_comparison"], {"0.45": "urgent", "0.50": "nonurgent"})
        self.assertTrue(payload["human_review_required"])
        self.assertFalse(payload["input_retained"])
        self.assertNotIn(source["subject"], response.text)
        self.assertNotIn(source["body"], response.text)

    async def test_empty_input_is_rejected(self):
        async with self.client_for(create_app(FakeModelService())) as client:
            response = await client.post("/api/analyze", json={"subject": " ", "body": " "})
        self.assertEqual(response.status_code, 422)

    async def test_missing_fields_are_rejected(self):
        async with self.client_for(create_app(FakeModelService())) as client:
            response = await client.post("/api/analyze", json={})
        self.assertEqual(response.status_code, 422)

    async def test_malformed_json_is_rejected(self):
        async with self.client_for(create_app(FakeModelService())) as client:
            response = await client.post("/api/analyze", content="not-json", headers={"content-type": "application/json"})
        self.assertEqual(response.status_code, 422)

    async def test_unusually_long_input_is_rejected(self):
        async with self.client_for(create_app(FakeModelService())) as client:
            response = await client.post("/api/analyze", json={"subject": "Synthetic", "body": "x" * 20_001})
        self.assertEqual(response.status_code, 422)

    async def test_missing_model_fails_safely(self):
        # The application must stop with an explicit unavailable response; it
        # must not substitute an unverified model or fabricate a prediction.
        async with self.client_for(create_app(None, "Local research artifact not found.")) as client:
            health = (await client.get("/api/health")).json()
            response = await client.post("/api/analyze", json={"subject": "Synthetic", "body": "Example"})
        self.assertEqual(health["status"], "not_ready")
        self.assertEqual(response.status_code, 503)


if __name__ == "__main__":
    unittest.main()

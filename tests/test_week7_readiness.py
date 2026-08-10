import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_week7_readiness.py"
SPEC = importlib.util.spec_from_file_location("validate_week7_readiness", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class Week7ReadinessValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = MODULE.evaluate(ROOT)

    def test_overall_precheck_passes(self):
        self.assertTrue(self.result["overall_precheck_passed"])

    def test_week6_decision_remains_revise(self):
        self.assertTrue(self.result["checks"]["frozen_decision"]["passed"])
        self.assertEqual(self.result["model_reliability_disposition"], "revise")
        self.assertFalse(self.result["deployment_approval"])
        self.assertFalse(self.result["shadow_testing_approval"])

    def test_notebooks_are_executed_without_saved_errors(self):
        self.assertTrue(self.result["checks"]["executed_notebooks"]["passed"])

    def test_gate_values_trace_to_week6_summary(self):
        self.assertTrue(self.result["checks"]["gate_traceability"]["passed"])

    def test_privacy_sensitive_columns_are_absent(self):
        self.assertTrue(self.result["checks"]["privacy_safe_columns"]["passed"])


if __name__ == "__main__":
    unittest.main()

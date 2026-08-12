"""Local web interface for demonstrating the frozen research candidate.

The application makes engineering behavior observable while keeping model
reliability, deployment approval, and human decision-making as separate issues.
"""

from __future__ import annotations

import os
import time
import uuid
from pathlib import Path
from typing import Annotated

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field, model_validator

from .model_service import ModelService


DEFAULT_ARTIFACT = Path("models/week7_research_demo.joblib")
# These are defensive interface limits, not empirically derived email limits.
# They prevent empty requests and unbounded payloads during a local demo.
MAX_INPUT_CHARACTERS = 20_000


class AnalyzeRequest(BaseModel):
    subject: Annotated[str, Field(default="", max_length=500)] = ""
    body: Annotated[str, Field(default="", max_length=MAX_INPUT_CHARACTERS)] = ""

    @model_validator(mode="after")
    def require_message_content(self) -> "AnalyzeRequest":
        if not self.subject.strip() and not self.body.strip():
            raise ValueError("Provide a subject, body, or both.")
        return self


def create_app(model_service: ModelService | None = None, load_error: str | None = None) -> FastAPI:
    """Create the API with an injectable model service for controlled testing."""
    app = FastAPI(
        title="Explainable AI Email Triage Research Demonstration",
        version="0.1.0",
        description="Controlled local demonstration. Not approved for production or shadow testing.",
    )
    app.state.model_service = model_service
    app.state.load_error = load_error

    @app.get("/", response_class=HTMLResponse)
    def index() -> str:
        return INDEX_HTML

    @app.get("/api/health")
    def health() -> dict[str, object]:
        # "ready" means the local artifact loaded and the endpoint can respond.
        # It is deliberately not a statement about predictive reliability.
        ready = app.state.model_service is not None
        return {
            "status": "ready" if ready else "not_ready",
            "research_only": True,
            "model_disposition": "revise",
            "deployment_approval": False,
            "shadow_testing_approval": False,
            "detail": None if ready else app.state.load_error,
        }

    @app.post("/api/analyze")
    def analyze(request: AnalyzeRequest) -> dict[str, object]:
        # Fail safely if the artifact is absent or rejected during startup. The
        # endpoint does not fall back to an unverified model or default answer.
        if app.state.model_service is None:
            raise HTTPException(status_code=503, detail="Research model unavailable. Run the documented local build command.")
        # This measures only the local scoring call. It excludes network,
        # browser, startup, and production-system latency.
        started = time.perf_counter()
        result = app.state.model_service.analyze(request.subject, request.body)
        # The event identifier supports one demonstration response without
        # encoding message content or creating a message-retention mechanism.
        result["event_id"] = str(uuid.uuid4())
        result["inference_milliseconds"] = round((time.perf_counter() - started) * 1_000, 3)
        # The application does not write the submitted subject or body to a
        # database, file, result artifact, or application log.
        result["input_retained"] = False
        return result

    return app


def load_default_service() -> tuple[ModelService | None, str | None]:
    """Load the local artifact while returning a safe, non-sensitive error."""
    artifact = Path(os.environ.get("EMAIL_TRIAGE_DEMO_MODEL", DEFAULT_ARTIFACT))
    try:
        return ModelService.load(artifact), None
    except FileNotFoundError:
        return None, "Local research artifact not found. Build it before starting the demonstration."
    except Exception as exc:
        return None, f"Local research artifact could not be loaded: {type(exc).__name__}."


_service, _load_error = load_default_service()
app = create_app(_service, _load_error)


INDEX_HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Explainable AI Email Triage — Research Demonstration</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 0; background: #f5f6f7; color: #111; }
    main { max-width: 960px; margin: 32px auto; padding: 0 24px 48px; }
    .notice { border-left: 6px solid #8a5a00; background: #fff8e6; padding: 16px 18px; margin: 20px 0; }
    .panel { background: white; border: 1px solid #d8dadd; border-radius: 10px; padding: 24px; margin-top: 20px; }
    label { display: block; font-weight: 700; margin: 16px 0 6px; }
    input, textarea { box-sizing: border-box; width: 100%; padding: 11px; border: 1px solid #90949a; border-radius: 6px; font: inherit; }
    textarea { min-height: 190px; resize: vertical; }
    button { margin-top: 18px; padding: 11px 18px; border: 0; border-radius: 6px; background: #1f4d78; color: white; font-weight: 700; cursor: pointer; }
    button:disabled { opacity: .6; cursor: wait; }
    .result-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 14px; }
    .result-card { background: #f1f3f5; border-radius: 6px; padding: 16px; }
    .result-card h3 { margin: 0 0 8px; font-size: 1rem; }
    .result-card p { margin: 5px 0; }
    .explanation { margin-top: 16px; }
    .feature-list { margin: 8px 0 0; padding-left: 22px; }
    .boundary { border-top: 1px solid #d8dadd; margin-top: 18px; padding-top: 14px; }
    .error { color: #8b1e1e; font-weight: 700; }
    .muted { color: #555; }
  </style>
</head>
<body>
<main>
  <h1>Explainable AI Email Triage</h1>
  <p class="muted">Controlled local research demonstration</p>
  <div class="notice"><strong>Research prototype:</strong> The model disposition is <strong>revise</strong>. Results require human review and are not approved for production routing or shadow testing.</div>
  <section class="panel">
    <h2>Analyze a synthetic or privacy-screened message</h2>
    <form id="form">
      <label for="subject">Subject</label>
      <input id="subject" maxlength="500" autocomplete="off">
      <label for="body">Body</label>
      <textarea id="body" maxlength="20000"></textarea>
      <button id="submit" type="submit">Analyze</button>
    </form>
  </section>
  <section class="panel" aria-live="polite">
    <h2>Research output</h2>
    <div id="output">No message analyzed.</div>
  </section>
</main>
<script>
const form = document.getElementById('form');
const button = document.getElementById('submit');
const output = document.getElementById('output');
// Even though feature names originate from the local model, escape all dynamic
// values before inserting them into HTML. This keeps the display boundary safe
// if a future model or API response contains unexpected characters.
const escapeHtml = (value) => String(value).replace(/[&<>"']/g, (character) => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[character]));
const featureItems = (items) => items.length
  ? items.map((item) => `<li><strong>${escapeHtml(item.feature)}</strong>: ${Number(item.contribution).toFixed(6)}</li>`).join('')
  : '<li>None for this input.</li>';
function renderResult(data) {
  // The cards keep score, threshold behavior, and required human handling
  // visible together so a probability cannot be mistaken for an approval.
  const thresholdRows = Object.entries(data.threshold_comparison)
    .map(([threshold, prediction]) => `<p><strong>${escapeHtml(threshold)}:</strong> ${escapeHtml(prediction)}</p>`).join('');
  output.innerHTML = `
    <div class="result-grid">
      <div class="result-card"><h3>Urgency score</h3><p><strong>${(Number(data.urgent_probability) * 100).toFixed(1)}%</strong></p><p class="muted">Research probability estimate</p></div>
      <div class="result-card"><h3>Threshold comparison</h3>${thresholdRows}</div>
      <div class="result-card"><h3>Required handling</h3><p><strong>Human review</strong></p><p>Disposition: ${escapeHtml(data.model_disposition)}</p></div>
    </div>
    <div class="explanation">
      <h3>Features supporting urgent</h3><ul class="feature-list">${featureItems(data.explanation.supports_urgent)}</ul>
      <h3>Features supporting nonurgent</h3><ul class="feature-list">${featureItems(data.explanation.supports_nonurgent)}</ul>
      <p class="muted">Feature contributions describe this fitted model; they are not causal explanations.</p>
    </div>
    <div class="boundary muted">
      Research only · Input retained: ${data.input_retained ? 'yes' : 'no'} · Deployment approved: ${data.deployment_approval ? 'yes' : 'no'} · Inference: ${Number(data.inference_milliseconds).toFixed(3)} ms
    </div>`;
}
form.addEventListener('submit', async (event) => {
  event.preventDefault(); button.disabled = true; output.textContent = 'Analyzing...';
  try {
    const response = await fetch('/api/analyze', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({subject: document.getElementById('subject').value, body: document.getElementById('body').value})});
    const data = await response.json();
    if (!response.ok) throw new Error(data.detail || 'Request failed');
    renderResult(data);
  } catch (error) { output.innerHTML = '<p class="error">The local demonstration could not complete the request. Check the input and local model status.</p>'; }
  finally { button.disabled = false; }
});
</script>
</body>
</html>"""

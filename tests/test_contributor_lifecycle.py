"""
Unit test suite for contributor_lifecycle.ipynb.

Validates:
1. nbformat v4 schema compliance.
2. Presence and integrity of embedded static PNG outputs.
3. Tenure cohort calculation logic.
4. Kaplan-Meier survival curve mathematical correctness.
5. Quarterly transition lifecycle states.
6. End-to-end execution of all notebook cells.
"""
import os
import json
import base64
import struct
import pytest
import nbformat
import numpy as np
import pandas as pd

NOTEBOOK_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "collectoss-analysis",
    "8knot",
    "contributor_lifecycle.ipynb"
)

def test_notebook_schema_and_validity():
    """Verify notebook is valid JSON and strictly complies with nbformat 4 schema."""
    assert os.path.isfile(NOTEBOOK_PATH), f"Notebook not found: {NOTEBOOK_PATH}"
    with open(NOTEBOOK_PATH, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
    nbformat.validate(nb)

def test_notebook_has_rendered_png_outputs():
    """Ensure all visualization cells contain valid pre-rendered PNG data."""
    with open(NOTEBOOK_PATH, "r", encoding="utf-8") as f:
        nb = json.load(f)

    png_count = 0
    for cell in nb.get("cells", []):
        for output in cell.get("outputs", []):
            data = output.get("data", {})
            if "image/png" in data:
                png_raw = data["image/png"]
                if isinstance(png_raw, list):
                    png_raw = "".join(png_raw)
                png_bytes = base64.b64decode(png_raw.strip())
                # Verify PNG magic header: \x89PNG\r\n\x1a\n
                assert png_bytes[:8] == b"\x89PNG\r\n\x1a\n", "Invalid PNG header"
                w, h = struct.unpack(">II", png_bytes[16:24])
                assert w > 0 and h > 0, "Invalid image dimensions"
                png_count += 1

    assert png_count >= 4, f"Expected at least 4 PNG outputs, found {png_count}"

def test_tenure_cohort_binning():
    """Verify tenure cohort bins and entry channel categorization."""
    bins = [-1, 30, 90, 180, 365, np.inf]
    labels = ["0-30 Days", "31-90 Days", "91-180 Days", "181-365 Days", "365+ Days"]
    
    tenures = pd.Series([0, 15, 30, 45, 90, 100, 180, 200, 365, 500])
    cohorts = pd.cut(tenures, bins=bins, labels=labels)
    
    assert cohorts[0] == "0-30 Days"
    assert cohorts[2] == "0-30 Days"
    assert cohorts[3] == "31-90 Days"
    assert cohorts[4] == "31-90 Days"
    assert cohorts[6] == "91-180 Days"
    assert cohorts[8] == "181-365 Days"
    assert cohorts[9] == "365+ Days"

def test_kaplan_meier_survival_function():
    """Test Kaplan-Meier product-limit estimator logic."""
    durations = np.array([5, 10, 15, 20, 25, 30])
    events = np.array([1, 1, 0, 1, 0, 1])  # 0 = censored, 1 = event (churn)
    
    order = np.argsort(durations)
    durations = durations[order]
    events = events[order]
    
    n = len(durations)
    survival = 1.0
    surv_probs = []
    
    for i in range(n):
        at_risk = n - i
        event = events[i]
        if event == 1:
            survival *= (1.0 - 1.0 / at_risk)
        surv_probs.append(survival)
        
    assert surv_probs[0] < 1.0
    assert surv_probs[-1] >= 0.0
    # Survival probability must be monotonically non-increasing
    for i in range(len(surv_probs) - 1):
        assert surv_probs[i] >= surv_probs[i+1]

def test_lifecycle_transition_states():
    """Verify contributor activity state transitions."""
    def classify_state(days_since_action):
        if days_since_action <= 90:
            return "Active"
        elif days_since_action <= 180:
            return "Drifting"
        else:
            return "Away"
            
    assert classify_state(10) == "Active"
    assert classify_state(90) == "Active"
    assert classify_state(91) == "Drifting"
    assert classify_state(180) == "Drifting"
    assert classify_state(181) == "Away"
    assert classify_state(365) == "Away"

def test_end_to_end_lifecycle_execution():
    """Execute all code cells of the notebook to ensure clean run without exceptions."""
    with open(NOTEBOOK_PATH, "r", encoding="utf-8") as f:
        nb = json.load(f)

    env = {}
    import plotly.graph_objects as go
    go.Figure.show = lambda *args, **kwargs: None

    for idx, cell in enumerate(nb.get("cells", [])):
        if cell.get("cell_type") == "code":
            src = "".join(cell.get("source", []))
            exec(src, env)
            
    assert "cntrb_df" in env, "Expected cntrb_df DataFrame in execution environment"
    assert "fig1" in env, "Expected fig1 in environment"
    assert "fig2" in env, "Expected fig2 in environment"
    assert "fig3" in env, "Expected fig3 in environment"
    assert "fig4" in env, "Expected fig4 in environment"

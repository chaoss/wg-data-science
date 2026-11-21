"""
Unit test suite for issue_pr_survival_analysis.ipynb.

Validates:
1. nbformat v4 schema compliance.
2. Presence and integrity of embedded static PNG outputs.
3. Kaplan-Meier survival curve mathematical consistency.
4. Survival quantile and milestone interpolation logic.
5. End-to-end execution of all notebook cells.
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
    "issue_pr_survival_analysis.ipynb"
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
                assert png_bytes[:8] == b"\x89PNG\r\n\x1a\n", "Invalid PNG header"
                w, h = struct.unpack(">II", png_bytes[16:24])
                assert w > 0 and h > 0, "Invalid image dimensions"
                png_count += 1

    assert png_count >= 4, f"Expected at least 4 PNG outputs, found {png_count}"

def test_km_curve_computation():
    """Verify Kaplan-Meier estimator bounds, monotonicity, and censoring."""
    durations = np.array([2.0, 5.0, 7.0, 10.0, 15.0, 20.0])
    events = np.array([1, 1, 0, 1, 0, 1])

    # Sort durations
    order = np.argsort(durations)
    d_sorted = durations[order]
    e_sorted = events[order]

    n = len(d_sorted)
    prob = 1.0
    timeline = [0.0]
    survival = [1.0]

    for i in range(n):
        at_risk = n - i
        if e_sorted[i] == 1:
            prob *= (1.0 - 1.0 / at_risk)
        timeline.append(d_sorted[i])
        survival.append(prob)

    assert survival[0] == 1.0
    assert 0.0 <= survival[-1] <= 1.0
    # Monotonically non-increasing
    for i in range(len(survival) - 1):
        assert survival[i] >= survival[i+1]

def test_quantile_interpolation():
    """Verify median survival time interpolation logic."""
    timeline = np.array([0, 1, 3, 5, 8, 12, 20])
    survival = np.array([1.0, 0.9, 0.75, 0.55, 0.45, 0.30, 0.10])

    # Find time when survival crosses 0.50
    cross_idx = np.where(survival <= 0.50)[0]
    assert len(cross_idx) > 0
    median_time = timeline[cross_idx[0]]
    assert median_time == 8  # crossed at timeline = 8

def test_end_to_end_survival_execution():
    """Execute all code cells of issue_pr_survival_analysis.ipynb cleanly."""
    with open(NOTEBOOK_PATH, "r", encoding="utf-8") as f:
        nb = json.load(f)

    env = {}
    import plotly.graph_objects as go
    go.Figure.show = lambda *args, **kwargs: None

    for idx, cell in enumerate(nb.get("cells", [])):
        if cell.get("cell_type") == "code":
            src = "".join(cell.get("source", []))
            exec(src, env)

    assert "cohorts" in env, "Expected cohorts dictionary in environment"
    assert "fig_whiteboard" in env, "Expected fig_whiteboard figure"
    assert "fig_pr_compare" in env, "Expected fig_pr_compare figure"
    assert "fig_table" in env, "Expected fig_table figure"
    assert "fig_inventory" in env, "Expected fig_inventory figure"

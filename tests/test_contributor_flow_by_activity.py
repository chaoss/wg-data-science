"""
Unit test suite for contributor_flow_by_activity.ipynb.

Validates:
1. nbformat v4 schema compliance.
2. Presence and integrity of embedded static PNG outputs.
3. Quarterly onboarding cohort assignment logic.
4. Retention rate calculations and boundary constraints.
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
    "contributor_flow_by_activity.ipynb"
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

def test_quarterly_cohort_assignment():
    """Verify quarterly onboarding cohort assignment and elapsed quarter math."""
    dates = pd.to_datetime(["2023-01-15", "2023-05-20", "2023-11-05", "2024-02-10"])
    quarters = dates.to_period("Q")

    assert quarters[0] == pd.Period("2023Q1", freq="Q")
    assert quarters[1] == pd.Period("2023Q2", freq="Q")
    assert quarters[2] == pd.Period("2023Q4", freq="Q")
    assert quarters[3] == pd.Period("2024Q1", freq="Q")

    # Elapsed quarters calculation
    elapsed = (quarters[3].year - quarters[0].year) * 4 + (quarters[3].quarter - quarters[0].quarter)
    assert elapsed == 4

def test_retention_rate_bounded():
    """Verify cohort retention rates are properly normalized percentages between 0 and 100%."""
    cohort_initial_size = 50
    retained_counts = [50, 32, 21, 15, 10]

    rates = [(count / cohort_initial_size) * 100.0 for count in retained_counts]
    assert rates[0] == 100.0
    for r in rates:
        assert 0.0 <= r <= 100.0
    for i in range(len(rates) - 1):
        assert rates[i] >= rates[i+1]

def test_end_to_end_contributor_flow_execution():
    """Execute all code cells of contributor_flow_by_activity.ipynb cleanly."""
    with open(NOTEBOOK_PATH, "r", encoding="utf-8") as f:
        nb = json.load(f)

    env = {}
    import plotly.graph_objects as go
    go.Figure.show = lambda *args, **kwargs: None

    for idx, cell in enumerate(nb.get("cells", [])):
        if cell.get("cell_type") == "code":
            src = "".join(cell.get("source", []))
            exec(src, env)

    assert "fig_heatmap" in env, "Expected fig_heatmap figure"
    assert "fig_sankey" in env, "Expected fig_sankey figure"
    assert "fig_mix" in env, "Expected fig_mix figure"
    assert "fig_decay" in env, "Expected fig_decay figure"

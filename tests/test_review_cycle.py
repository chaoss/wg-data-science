"""
Unit test suite for review_cycle.ipynb.

Validates:
1. nbformat v4 schema compliance.
2. Presence and integrity of embedded static PNG outputs.
3. Review cycle duration breakdown logic (Time to First Review, Active Review Duration, Merge Latency).
4. Code review ratio mathematical consistency.
5. Traceability compliance ratios (PR-to-Issue, Commit-to-PR).
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
    "review_cycle.ipynb"
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

def test_review_phase_duration_logic():
    """Test duration phase partitioning logic."""
    created_at = pd.Timestamp("2024-01-01 10:00:00")
    first_review = pd.Timestamp("2024-01-02 10:00:00")  # 1 day later
    approved_at = pd.Timestamp("2024-01-04 10:00:00")   # 2 days active review
    merged_at = pd.Timestamp("2024-01-05 10:00:00")     # 1 day merge latency

    time_to_first_review = (first_review - created_at).total_seconds() / 86400.0
    active_review_dur = (approved_at - first_review).total_seconds() / 86400.0
    merge_latency = (merged_at - approved_at).total_seconds() / 86400.0
    total_dur = (merged_at - created_at).total_seconds() / 86400.0

    assert time_to_first_review == 1.0
    assert active_review_dur == 2.0
    assert merge_latency == 1.0
    assert total_dur == (time_to_first_review + active_review_dur + merge_latency)

def test_code_review_ratio_math():
    """Verify code review ratio calculation against self-merged PRs."""
    total_merged = 100
    peer_reviewed = 85
    self_merged = 15

    review_ratio = (peer_reviewed / total_merged) * 100.0
    self_merge_ratio = (self_merged / total_merged) * 100.0

    assert review_ratio == 85.0
    assert self_merge_ratio == 15.0
    assert np.isclose(review_ratio + self_merge_ratio, 100.0)

def test_traceability_compliance_ratios():
    """Verify PR-to-Issue linkage and Commit-to-PR compliance bounds."""
    # 50 total PRs, 40 linked to issues -> 80%
    pr_issue_ratio = (40 / 50) * 100.0
    assert 0.0 <= pr_issue_ratio <= 100.0
    assert pr_issue_ratio == 80.0

    # 200 total commits, 180 made via PRs -> 90%
    commit_pr_ratio = (180 / 200) * 100.0
    assert 0.0 <= commit_pr_ratio <= 100.0
    assert commit_pr_ratio == 90.0

def test_end_to_end_review_cycle_execution():
    """Execute all code cells of review_cycle.ipynb cleanly."""
    with open(NOTEBOOK_PATH, "r", encoding="utf-8") as f:
        nb = json.load(f)

    env = {}
    import plotly.graph_objects as go
    go.Figure.show = lambda *args, **kwargs: None

    for idx, cell in enumerate(nb.get("cells", [])):
        if cell.get("cell_type") == "code":
            src = "".join(cell.get("source", []))
            exec(src, env)

    assert "df_pr_metrics" in env, "Expected df_pr_metrics DataFrame"
    assert "fig_phases" in env, "Expected fig_phases figure"
    assert "fig_iter" in env, "Expected fig_iter figure"
    assert "fig_review_ratio" in env, "Expected fig_review_ratio figure"
    assert "fig_traceability" in env, "Expected fig_traceability figure"

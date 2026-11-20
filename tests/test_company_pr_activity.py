import os
import json
import ast
import re
import pytest
import nbformat
import pandas as pd
import numpy as np

NOTEBOOK_PATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "collectoss-analysis", "8knot", "company_pr_activity.ipynb"
))

# ---------------------------------------------------------------------------
# Test 1: Notebook Schema and Structure
# ---------------------------------------------------------------------------
def test_notebook_schema_and_validity():
    """Verify that the notebook is valid JSON and complies with the nbformat 4 schema."""
    assert os.path.isfile(NOTEBOOK_PATH), f"Notebook file not found at: {NOTEBOOK_PATH}"
    with open(NOTEBOOK_PATH, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
    nbformat.validate(nb)
    assert len(nb.cells) >= 20, f"Expected at least 20 cells, got {len(nb.cells)}"

def test_notebook_has_rendered_outputs():
    """Verify that code cells have execution counts and pre-rendered outputs for ReviewNB."""
    with open(NOTEBOOK_PATH, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
    code_cells = [c for c in nb.cells if c.cell_type == "code"]
    cells_with_outputs = [c for c in code_cells if len(c.get("outputs", [])) > 0]
    assert len(cells_with_outputs) >= 10, f"Expected >= 10 cells with outputs, found {len(cells_with_outputs)}"

# ---------------------------------------------------------------------------
# Test 2: Normalization Logic
# ---------------------------------------------------------------------------
KNOWN_ORGS = {
    "red hat": "Red Hat", "redhat": "Red Hat",
    "google": "Google", "ibm": "IBM", "microsoft": "Microsoft",
    "intel": "Intel", "amazon": "Amazon", "cisco": "Cisco", "meta": "Meta"
}
DOMAIN_TO_ORG = {
    "redhat.com": "Red Hat", "google.com": "Google", "ibm.com": "IBM",
    "microsoft.com": "Microsoft", "intel.com": "Intel", "amazon.com": "Amazon"
}
GENERIC_DOMAINS = {"gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "users.noreply.github.com"}
UNAFFILIATED_PATTERNS = {"none", "self", "n/a", "independent", "student", "freelance", "individual", "personal"}

def clean_company_name(val):
    if not val or pd.isna(val):
        return ""
    s = str(val).strip()
    s = re.sub(r"^@", "", s).strip()
    s = re.sub(r"https?://\S+", "", s).strip()
    s = re.sub(r",?\s+(inc|llc|ltd|corp|corporation|gmbh|co|technologies|software)\.?$", "", s, flags=re.IGNORECASE).strip()
    return s

def normalize_company(raw_company, email_list):
    clean = clean_company_name(raw_company)
    clean_lower = clean.lower()

    if clean_lower in UNAFFILIATED_PATTERNS:
        return "Independent / Unaffiliated"

    if clean_lower:
        for pattern, canonical in KNOWN_ORGS.items():
            if pattern in clean_lower:
                return canonical
        if len(clean) > 1:
            return clean.title()

    if email_list and pd.notna(email_list):
        for email in str(email_list).split(","):
            email = email.strip()
            if "@" in email:
                domain = email.split("@")[-1].lower().strip()
                if domain in DOMAIN_TO_ORG:
                    return DOMAIN_TO_ORG[domain]
                if domain not in GENERIC_DOMAINS and "." in domain:
                    parts = domain.split(".")
                    corp_name = parts[0]
                    if corp_name in KNOWN_ORGS:
                        return KNOWN_ORGS[corp_name]
                    return corp_name.title()

    return "Independent / Unaffiliated"

@pytest.mark.parametrize("raw_company,email_list,expected", [
    ("Red Hat, Inc.", "dev@redhat.com", "Red Hat"),
    ("@redhat", None, "Red Hat"),
    ("Google LLC", None, "Google"),
    ("@google", "engineer@google.com", "Google"),
    ("IBM Corp.", None, "IBM"),
    ("Microsoft Corporation", None, "Microsoft"),
    ("none", None, "Independent / Unaffiliated"),
    ("Self", "freelance@gmail.com", "Independent / Unaffiliated"),
    ("student", None, "Independent / Unaffiliated"),
    (None, "dev@amazon.com", "Amazon"),
    (None, "user@gmail.com", "Independent / Unaffiliated"),
    (None, "contributor@users.noreply.github.com", "Independent / Unaffiliated"),
    ("Acme Technologies LLC", "eng@acme.com", "Acme Technologies")
])
def test_company_normalization(raw_company, email_list, expected):
    result = normalize_company(raw_company, email_list)
    assert result == expected

# ---------------------------------------------------------------------------
# Test 3: Aggregation and Market Share Mathematical Integrity
# ---------------------------------------------------------------------------
def test_market_share_and_hhi_calculations():
    data = pd.DataFrame([
        {"org": "Company A", "is_merged": True, "created_at": pd.Timestamp("2023-01-01"), "merged_at": pd.Timestamp("2023-01-05")},
        {"org": "Company A", "is_merged": True, "created_at": pd.Timestamp("2023-01-02"), "merged_at": pd.Timestamp("2023-01-04")},
        {"org": "Company A", "is_merged": False, "created_at": pd.Timestamp("2023-01-03"), "merged_at": pd.NaT},
        {"org": "Company B", "is_merged": True, "created_at": pd.Timestamp("2023-01-01"), "merged_at": pd.Timestamp("2023-01-10")},
        {"org": "Company B", "is_merged": False, "created_at": pd.Timestamp("2023-01-02"), "merged_at": pd.NaT},
    ])
    total_sub = len(data)  # 5
    total_mrg = data["is_merged"].sum()  # 3

    summary = data.groupby("org").agg(
        prs_submitted=("is_merged", "count"),
        prs_merged=("is_merged", "sum")
    ).reset_index()

    summary["share_of_sub"] = (summary["prs_submitted"] / total_sub) * 100
    summary["share_of_mrg"] = (summary["prs_merged"] / total_mrg) * 100
    summary["merge_rate"] = (summary["prs_merged"] / summary["prs_submitted"]) * 100

    # Total shares must sum to 100%
    assert round(summary["share_of_sub"].sum(), 2) == 100.0
    assert round(summary["share_of_mrg"].sum(), 2) == 100.0

    # Company A internal merge rate: 2/3 = 66.7%
    assert round(summary.loc[summary["org"] == "Company A", "merge_rate"].values[0], 1) == 66.7
    # Company A share of all merges: 2/3 = 66.7%
    assert round(summary.loc[summary["org"] == "Company A", "share_of_mrg"].values[0], 1) == 66.7
    # Company A share of all submissions: 3/5 = 60.0%
    assert round(summary.loc[summary["org"] == "Company A", "share_of_sub"].values[0], 1) == 60.0

    # HHI calculation
    hhi = np.sum(summary["share_of_mrg"] ** 2)
    assert hhi > 0

# ---------------------------------------------------------------------------
# Test 4: End-to-End Notebook Code Execution
# ---------------------------------------------------------------------------
def test_end_to_end_notebook_execution():
    """Verify that every single code cell in the notebook executes successfully."""
    import plotly.graph_objects as go
    go.Figure.show = lambda self, *args, **kwargs: None

    with open(NOTEBOOK_PATH, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    namespace = {}
    for i, cell in enumerate(nb.cells):
        if cell.cell_type != "code":
            continue
        try:
            tree = ast.parse(cell.source)
            code = compile(tree, f"<cell_{i}>", "exec")
            exec(code, namespace)
        except Exception as e:
            pytest.fail(f"Cell {i} failed with error: {e}")

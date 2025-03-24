
# 📊 Project Planning: Corporate Projects Moving to Foundations

This project investigates **what happens when corporate-owned open source projects transition into foundation governance**. It aims to explore measurable indicators of project health, community engagement, and governance efficiency before and after such transitions.

This project is led by the **CHAOSS Africa Researchers Team**. For more information, please contact **Tosan Okome**.

🔗 **Data Science WG Issue**: [chaoss/wg-data-science#90](https://github.com/chaoss/wg-data-science/issues/90)  
📚 **Publication Guidelines**: [CHAOSS Data Science WG Publication Guidelines](https://github.com/chaoss/wg-data-science/blob/main/publications/publication-guidelines.md)

---

## 🎯 Research Goals

- **Understand project health impacts** after a project moves from corporate to foundation ownership.
- Analyze the effects across **different foundations** (CNCF, Apache, Eclipse).
- Measure **corporate vs. community contribution ratios** pre- and post-migration.
- Evaluate **project governance changes** based on data like PR approval times and contributor growth.

---

## 🧩 How These Scripts Support the Research

### ✅ 1. `convert.py`
- **Purpose**: Pulls project metadata from the [Eclipse API](https://projects.eclipse.org/api/projects).
- **Usefulness**: This helps gather metadata for Eclipse projects, including when they were donated, by whom, and what their lifecycle looks like.
- **Next Step**: Integrate Eclipse-specific contributor data (if available) for health metrics.

### ✅ 2. `projectsJsonConvert.py`
- **Purpose**: Transforms a filtered CNCF `projects.json` into a structured CSV format.
- **Usefulness**: Helps us build a structured list of CNCF projects to identify when they were donated, who the original contributor was, and classify their project stage (sandbox, incubating, graduated).
- **Next Step**: Cross-reference with CNCF TOC GitHub issues for donation provenance and contributor metadata.

### ✅ 3. `yamlFile.py`
- **Purpose**: Parses the CNCF `landscape.yml` file and converts relevant project data into CSV.
- **Usefulness**: Extracts nested metadata for CNCF projects to identify project classification over time and build a timeline for analysis.
- **Next Step**: Enhance with project movement data (e.g., sandbox → graduated).

---

## 🧪 Phase 1: Scope

- Analyze **10 projects from each foundation** (CNCF, Apache, Eclipse).
- Focus on projects:
  - Donated by **corporations**.
  - Donated **1–5 years ago**.
  - Hosted on **GitHub**.
- Analyze pre- and post-migration **commit data**, **contributor diversity**, **PR latency**, etc.

---

## 📦 Current Dataset: `website_data_projects.csv`

The CSV file contains:
- Basic metadata for each project.
- Classification by foundation and project maturity level.
- Repo links and social indicators (Slack, Twitter, Blog, etc.).

This allows us to:
- Classify and sample from real-world project data.
- Use consistent formatting across foundations.
- Match with GitHub commit and contributor data for time-based metrics.

---

## 🔍 Next Steps

1. **Apache Dataset Expansion**  
   Pull and transform Apache’s JSON endpoints into structured project lists and add corporate donation metadata manually or via scripts.

2. **Contributor Analysis**
   - Pull GitHub contributor data (via Augur or custom GH API queries).
   - Integrate LF Research contributor affiliation data (when available).
   - Use this to measure corporate vs. community dominance.

3. **Time-Based Health Metrics**
   - Number of commits and PRs (monthly).
   - New contributor growth.
   - PR/issue merge time and churn rates.

4. **Automated Detection**
   - Create functions/scripts to detect and label projects that moved from corporate to foundation governance.
   - Automate classification of sandbox/incubating/graduated transitions.

5. **Prepare for Reporting**
   - Clean, merged dataset.
   - Statistical analysis (e.g., t-tests, regressions).
   - Drafts of visualizations and summary stats.

---

## 📘 Publication Plan

- Comparative charts across foundations.
- Narratives about contribution shifts and governance changes.
- Possibly a **network map** of contributor overlap or foundation collaborations.

Academic publication is optional but encouraged with shared authorship.

---

## ✉️ Contact

Project Lead: **Tosan Okome**  
Technical Assistant: **Sal Kimmich**
Organization: **CHAOSS Africa Researchers Team**  
For technical support with data scripts, contact the [CHAOSS Data Science Working Group](https://chaoss.community/working-groups/#data-science)


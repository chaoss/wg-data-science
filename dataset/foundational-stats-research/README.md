# Foundation Stats Project: Mapping Collaboration Pathways in Open Source Communities
## A CHAOSS-Aligned, Reproducible Assessment of Community Health

This project is part of the [CHAOSS Data Science Working Group](https://chaoss.community/inside-the-chaoss-data-science-working-group/) initiative to develop rigorous, evidence-based statistical frameworks for understanding collaboration patterns across major open source foundations.

## IMPORTANT INFO:
We are currently focused on manualy collecting the Apache metadata from individual websites. If you'd like to contribute to this effort, kindly use [this tracker](https://docs.google.com/spreadsheets/d/1rWW773oOudiM5xpfroIjEiQazOr42YNCfGWISnR0Tk4/edit?usp=sharing) to know what project you can document:
-  "In Progress" means a contributor has started working on the project but yet to send a PR or PR is yet to be merged.
- "Done" implies that the metadata for that Apache project has been done and merged to /data/raw/apache.json
- Empty or "To Do" means noone is currently working on the project. If you decide to work on it, please change the status to "In Progress" to avoid duplicating efforts from contributors. 

## 🎯 Project Overview

This research project conducts a comprehensive, reproducible assessment of community health across three major open source ecosystems: **Cloud Native Computing Foundation (CNCF)**, **Apache Software Foundation**, and **Eclipse Foundation**. 

Our goal is to map collaboration pathways by combining metadata analysis, engagement modeling, and predictive insights to understand what drives successful community participation in open source projects.

### Why This Matters

Open source foundations manage thousands of projects, but lack systematic approaches to:

- **Compare health metrics** across different governance models and ecosystems  
- **Predict engagement outcomes** based on project infrastructure and communication patterns
- **Identify at-risk projects** before they become inactive or lose contributors
- **Provide evidence-based guidance** to maintainers and foundation leadership

This research addresses these gaps through transparent, reproducible methodology aligned with CHAOSS metrics.

## 🔬 Research Methodology

Our analysis follows a six-section research design that builds from descriptive statistics to predictive modeling:

### 1. CHAOSS-Aligned Metadata Audit
- Field-level presence analysis across foundations
- Alignment with CHAOSS metric categories  
- Completeness benchmarking and structural gap identification

### 2. Foundation-Specific Narratives
- Programming language ecosystem analysis
- Communication infrastructure presence (chat, blogs)
- Contributor and repository distribution patterns

### 3. Cross-Foundation Outlier Analysis  
- Statistical outlier detection using z-scores and IQR methods
- Foundation-specific reporting gap analysis
- "Risk by absence" identification (high-activity projects missing key infrastructure)

### 4. Aggregate Landscape Summary
- Ecosystem-wide benchmarking across all three foundations
- Maturity stage distributions and technology trends
- Global summary metrics for stakeholder reference

### 5. Predictive and Stochastic Modeling
- **Communication state transition modeling** using Markov chains
- **Monte Carlo simulations** to estimate engagement pathways
- **Topic modeling** and content-based engagement prediction
- **Panel regression models** (Poisson, Zero-Inflated Poisson) for explanatory analysis

### 6. Actionable Insights and Recommendations
- Project classification into engagement tiers (Healthy, At-Risk, Inactive)
- Foundation-specific gap analysis and improvement recommendations
- Stakeholder-specific recommendation matrix

## 📁 Repository Structure

This project follows a structured approach to research documentation and reproducibility:

```
foundational-stats-research/
├── README.md                              # This file
├── Final_Research_Design_Report.md        # Complete research methodology & analysis plan
├── REPOSITORY_STRUCTURE_RECOMMENDATION.md # Organization guidelines
├── data/                                  # Research datasets (CNCF, Apache, Eclipse)
│   ├── raw/                              # Original foundation data exports  
│   ├── processed/                        # Cleaned and normalized datasets
│   └── external/                         # Chat logs, communication data
├── analysis/                              # Statistical analysis scripts
│   ├── metadata-audit/                   # Section 1: CHAOSS alignment analysis
│   ├── foundation-narratives/            # Section 2: Individual foundation analysis  
│   ├── outlier-analysis/                 # Section 3: Cross-foundation comparison
│   ├── landscape-summary/                # Section 4: Ecosystem-wide benchmarking
│   ├── predictive-modeling/              # Section 5: Engagement prediction models
│   └── insights-recommendations/         # Section 6: Actionable guidance generation
├── documentation/                         # Additional research documentation
│   ├── methodology-notes/                # Detailed methodological decisions
│   ├── risk-mitigation/                  # Risk assessment and mitigation strategies
│   └── chaoss-alignment/                 # CHAOSS metric mapping documentation
└── results/                              # Research findings and outputs
    ├── visualizations/                   # Charts, graphs, heatmaps
    ├── models/                          # Trained predictive models
    ├── project-health-cards/            # Prototype tooling outputs
    └── reports/                         # Final research reports and summaries
```

For detailed information about the recommended repository organization, see [`REPOSITORY_STRUCTURE_RECOMMENDATION.md`](./REPOSITORY_STRUCTURE_RECOMMENDATION.md).

## 🚀 Getting Started

### For Researchers and Data Scientists

1. **Review the research design**: Start with [`Final_Research_Design_Report.md`](./Final_Research_Design_Report.md) to understand our methodology
2. **Explore the data**: Check the `data/` directory for available datasets
3. **Examine existing analysis**: Look through `analysis/` for current statistical approaches
4. **Join the discussion**: Participate in [GitHub Issues](https://github.com/chaoss/wg-data-science/issues?q=is%3Aissue+is%3Aopen+label%3A%22foundational-stats%22) tagged with foundational-stats

### For Contributors

We welcome contributions from various backgrounds:

- **Statisticians**: Help refine our statistical methodologies
- **Data Scientists**: Contribute analysis scripts and validation approaches  
- **Open Source Practitioners**: Provide domain expertise and real-world validation
- **Researchers**: Contribute to literature review and theoretical frameworks
- **Students**: Great opportunity to work on meaningful research projects

## 🤝 How to Contribute

### Ways to Get Involved

1. **Metadata Analysis & CHAOSS Alignment**
   - Help audit and normalize foundation data structures
   - Map additional fields to CHAOSS metric categories
   - Improve completeness benchmarking methodologies

2. **Foundation Ecosystem Analysis**
   - Contribute domain expertise for Apache, CNCF, or Eclipse communities
   - Help interpret programming language and infrastructure patterns
   - Validate findings against real-world foundation experience

3. **Statistical Modeling & Prediction**
   - Implement advanced statistical models (Markov chains, Monte Carlo simulation)
   - Develop topic modeling approaches for communication analysis  
   - Create panel regression models for engagement prediction
   - Work with Independent Component Analysis (ICA) for dimensionality reduction

4. **Communication Pattern Analysis**
   - Process and analyze Slack, mailing list, or chat data (with appropriate privacy protections)
   - Develop transition matrices for communication state modeling
   - Create engagement flow simulations and visualizations

5. **Tooling & Dashboard Development**  
   - Build "Project Health Card" prototypes
   - Create visualization tools for foundation stakeholders
   - Develop monitoring and alerting systems for at-risk projects

6. **Documentation & Reproducibility**
   - Improve methodological documentation
   - Create tutorials for statistical approaches
   - Enhance risk mitigation and ethical considerations
   - Validate reproducibility across different computing environments

### Research Ethics and Data Privacy

This project adheres to strict ethical standards:

- **Privacy-first approach**: All communication data is anonymized before analysis
- **Consent protocols**: Community consent obtained before using conversational data  
- **Open science principles**: Transparent, reproducible research with public datasets
- **CHAOSS Code of Conduct**: Respectful collaboration and inclusive participation

## 🛠️ Technical Requirements

### Prerequisites

- **Statistical Software**: Python (recommended) or R with statistical libraries
- **Advanced Analytics**: Experience with Markov modeling or panel regression preferred but not required
- **Version Control**: Git knowledge for collaboration
- **Documentation**: Markdown for documentation, LaTeX for formal papers (optional)

### Recommended Tools

- **Python**: pandas, scipy, scikit-learn, gensim (for topic modeling), statsmodels
- **R**: tidyverse, ggplot2, Markov chain packages, ICA libraries
- **Communication Analysis**: Text processing libraries, network analysis tools
- **Documentation**: Jupyter notebooks, RMarkdown  
- **Reproducibility**: Docker (optional but encouraged), environment management tools

### Key Technical Skills (Helpful but not required)

- Panel data regression modeling (Poisson, Zero-Inflated Poisson)
- Natural Language Processing and topic modeling (LDA)
- Markov chain analysis and Monte Carlo simulation
- Independent Component Analysis (ICA) for dimensionality reduction
- Data visualization for statistical reporting

## 📊 Current Research Status

### Research Phases

**Phase 1: Foundation Data Collection & CHAOSS Alignment** ✅ *Design Complete*
- Metadata extraction from CNCF, Apache, and Eclipse foundations
- Field-level presence analysis and completeness benchmarking
- CHAOSS metric category mapping

#### **NOTE** : The [notebook](https://colab.research.google.com/drive/1DTOHZv0HOyT64GWrvBTyQprU6P08NyzZ?usp=sharing) and [datasets](https://huggingface.co/datasets/Ernesty/foundational-stats-datasets/tree/main) used are in colab and Hugging Face respectively. The notebooks demostrates:
          - An attempt to crawl apache projects metadata 
          - Extract the ⁠ blog ⁠,  ⁠ community ⁠ , ⁠ license ⁠  and other useful links for each apache projects
          - Save the extracts to Hugging Face
   The dataset contains bunch of html files for each apache projects, and a `apache_project_links_named.json ⁠` with an attempt to save the useful links.
   
**Phase 2: Foundation Narratives & Outlier Analysis** 🔄 *In Progress*  
- Foundation-specific descriptive analytics
- Cross-foundation outlier detection and risk identification
- Communication infrastructure analysis

**Phase 3: Predictive Modeling** 📋 *Design Phase*
- Communication state transition modeling
- Topic modeling and content-based engagement prediction
- Panel regression for engagement drivers

**Phase 4: Insights & Tooling** 📋 *Planning*
- Project health classification system
- Stakeholder recommendation frameworks  
- Prototype health dashboard development

Check our [project board](https://github.com/chaoss/wg-data-science/projects) and [issues](https://github.com/chaoss/wg-data-science/issues) for current research priorities and detailed progress updates.

## 📚 Resources and References

- [CHAOSS Metrics](https://chaoss.community/metrics/)
- [Data Science Working Group Documentation](https://github.com/chaoss/wg-data-science)
- [CHAOSS Practitioner Guides](https://chaoss.community/about-chaoss-practitioner-guides/)
- Research literature and references (see research documentation)

## 🗓️ Community Engagement

### Join Our Community

- **Slack**: Join #wg-data-science in the [CHAOSS Slack workspace](https://join.slack.com/t/chaoss-workspace/shared_invite/zt-r65szij9-QajX59hkZUct82b0uACA6g)
- **Meetings**: Come to the CHOASS Data Science Group Bi-Weekly Meeting [meeting calendar](https://chaoss.community/chaoss-calendar/) for schedule
- **Conferences**: Present and discuss research at CHAOSS events

### Recognition

Contributors to this research project will be acknowledged in:
- Research publications and reports
- CHAOSS community recognition programs  
- Conference presentations and papers
- Project documentation and credits

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/chaoss/wg-data-science/blob/main/LICENSE) file for details.

## 📞 Contact

- **Project Maintainers**: Ernest Owojori and Sal Kimmich (reach out on the CHAOSS Slack)
- **Working Group**: CHAOSS Data Science Working Group
- **General Questions**: Open an issue or reach out on Slack

---

*This project is part of the [CHAOSS](https://chaoss.community) initiative, hosted by the Linux Foundation. We're building a community around measuring open source project health using data science approaches.*

**Ready to contribute?** Start by exploring our [issues](https://github.com/chaoss/wg-data-science/issues) and join the conversation!

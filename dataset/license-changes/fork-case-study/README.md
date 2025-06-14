This folder is where we can collaborate on a research report that contains several case studies of open source projects that resulted in hard forks after the project relicensed.

* Elasticsearch -> OpenSearch
* Redis -> Valkey
* Terraform -> OpenTofu

If you just want an overview of the results so far, here are some summaries:
* [The New Stack: What Happens to Relicensed Open Source Projects and Their Forks?](https://thenewstack.io/what-happens-to-relicensed-open-source-projects-and-their-forks/)
* [State of Open Con 7 minute keynote video](https://www.youtube.com/watch?v=rphZFv9QbV0&list=PL0U2cL1JGPZdJTUooEjFMb_djIzreUxGM&index=4)
* Additional presentations: [FOSDEM Panel](https://fosdem.org/2025/schedule/event/fosdem-2025-5258-forked-communities-project-re-licensing-and-community-impact/), [State of Open Con Panel](https://www.youtube.com/watch?v=DSTiQil10GQ&list=PL0U2cL1JGPZdfn4ODuMVouXMh9lDsiPGh&index=4), [OpenUK Meetup](https://www.youtube.com/watch?v=wliDVF3FpI0)
* [Academic paper](https://github.com/chaoss/wg-data-science/tree/main/publications) with the results that were presented at the OpenForum Academy Symposium in November 2024.

The current WIP draft of the research report can be found in this [Google doc for the Report](https://docs.google.com/document/d/1sYlUn9UsY7ynmzc3MVJTtktNgaLFQDOZ8W9fhYarWNo/edit). At this point, it's mostly an outline that still needs a lot of work.

The [notebooks](notebooks) folder contains basic analysis of the organizational affiliation data for the contributors per open source project.

The [data-files](data-files) folder contains data files (pickled) for each project with commits for a specific time period being studied (e.g., 1 year before the relicense).

We still have a lot of work to do. Here are a few next steps that people can begin working on:
* **Writing**: Write more of the Introduction and Context sections for the report (see doc above) - No data science experience required, and the links in the "Helpful articles" section at the top of the doc should help someone get started with this work. Much of this can probably be taken from the [OFA paper](https://docs.google.com/document/d/1hdLqLhQjPGwOpwMgH5dpTFMioSTRRZEGdQ5-lEZ9o_Q/edit?usp=sharing) as a start, but it will need to be heavily edited so that it isn't in an academic style, since the final output will be a report that is more in the style of an LF report (see the report Google doc above for more on style).  
* **Collect Data & Metrics Analysis**: Select several project health metrics from the CHAOSS project (ideally based on research) that might be used to answer some of the research questions listed in the doc. Ideally, these metrics should be implemented in Augur / 8Knot and / or GrimoireLab so that we can use CHAOSS projects for the visualizations. Several people could work on this at the same time. We have a start on this that can be found in the Appendix / Notes section of the report doc, but it still needs quite a bit of work.
* **Validation**: Validate the data for the 6 projects by talking to people who are directly involved in those projects. @geekygirldawn has started this work and contacted people from the projects.


# Hackathon Project Details

The project is part of the CHAOSS Data Science Hackathon on June 26, 2025 in Denver Colorado.

**Project Mentors**: Chan Voong and Cali Dolfi. We're happy to answer questions or provide feedback!

We will explore pull requests data on open source project forks specifically those caused by relicensing. A Python script has been prepared and the tasks will be beginner friendly. Basic Python skills are required. 

**Impact/Why does this matter?**: Analyzing PR data before and after a relicense/fork event helps us understand open source developer and community behavior. 

**Pre-reading**: Please review the text above and read the related articles. You're also welcomed to explore other datasets in this case-study. 

**Tasks**: 
- Fetch PR data using GitHub’s GraphQL API. 
- Validate dataset accuracy by cross-referencing with actual repo activity
- Visualize trends using Jupyter notebooks and 8knot. Interpret and describe visualizations to draw meaningful conclusions in a Jupyter Notebook
- Identify interesting patterns or anomalies in PR behavior
- Explore whether additional data (e.g. contributor metadata) would enrich the analysis


## 📝 Step 1: Prepare Your Environment

1. **Clone or download this repo** to your local machine.
2. **Install Anaconda** (if you haven’t already). After opening Anaconda, launch Jupyter Notebook. Within Jupyter, go to the "Hackathon" folder in this repo which should include two files:  fetch_pr.py and pr_data_hackathon.ipynb. Follow instrcutions in the Notebook.
3. **Get a GitHub personal access token**
Go to GitHub Settings > Developer settings > Personal access tokens
Click "Generate new token" (classic), select repo scope, and copy the token.

Save your token in a file named gh_keys.txt in the same folder as the scripts. 
This folder is where we can collaborate on a research report that contains several case studies of open source projects that resulted in hard forks after the project relicensed.

* Elasticsearch -> OpenSearch
* Redis -> Valkey
* Terraform -> OpenTofu

The current WIP draft of the research report can be found in this [Google doc](https://docs.google.com/document/d/1sYlUn9UsY7ynmzc3MVJTtktNgaLFQDOZ8W9fhYarWNo/edit). At this point, it's mostly an outline that still needs a lot of work.

The [notebooks](notebooks) folder contains basic analysis of the organizational affiliation data for the contributors per open source project.

The [data-files](datafiles) folder contains data files (pickled) for each project with commits for a specific time period being studied (e.g., 1 year before the relicense).

We still have a lot of work to do. Here are a few next steps that people can begin working on:
* Move the data collection script (currently at https://github.com/geekygirldawn/project-api-metrics/blob/main/scripts/commits_people.py) - @geekygirldawn is doing this.
* Create Notebooks and basic analysis for Terraform & OpenTofu - @geekygirldawn is working on this now.
* Write more of the Introduction and Context sections for the report (see doc above) - No data science experience required, and the links in the "Helpful articles" section at the top of the doc should help someone get started with this work.
* Select several project health metrics from the CHAOSS project (ideally based on research) that might be used to answer some of the research questions listed in the doc. Ideally, these metrics should be implemented in Augur / 8Knot and / or GrimoireLab so that we can use CHAOSS projects for the visualizations. Several people could work on this at the same time.
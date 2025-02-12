This folder is where we can collaborate on a research report that contains several case studies of open source projects that resulted in hard forks after the project relicensed.

* Elasticsearch -> OpenSearch
* Redis -> Valkey
* Terraform -> OpenTofu

If you just want an overview of the results so far, here are some summaries:
* [The New Stack: What Happens to Relicensed Open Source Projects and Their Forks?](https://thenewstack.io/what-happens-to-relicensed-open-source-projects-and-their-forks/)
* [State of Open Con 7 minute keynote video](https://www.youtube.com/watch?v=rphZFv9QbV0&list=PL0U2cL1JGPZdJTUooEjFMb_djIzreUxGM&index=4)
* Additional presentations: [FOSDEM Panel}(https://fosdem.org/2025/schedule/event/fosdem-2025-5258-forked-communities-project-re-licensing-and-community-impact/), [State of Open Con Panel](https://www.youtube.com/watch?v=DSTiQil10GQ&list=PL0U2cL1JGPZdfn4ODuMVouXMh9lDsiPGh&index=4), [OpenUK Meetup](https://www.youtube.com/watch?v=wliDVF3FpI0)
* [Academic paper](https://github.com/chaoss/wg-data-science/tree/main/publications) with the results that were presented at the OpenForum Academy Symposium in November 2024.

The current WIP draft of the research report can be found in this [Google doc for the Report](https://docs.google.com/document/d/1sYlUn9UsY7ynmzc3MVJTtktNgaLFQDOZ8W9fhYarWNo/edit). At this point, it's mostly an outline that still needs a lot of work.

The [notebooks](notebooks) folder contains basic analysis of the organizational affiliation data for the contributors per open source project.

The [data-files](data-files) folder contains data files (pickled) for each project with commits for a specific time period being studied (e.g., 1 year before the relicense).

We still have a lot of work to do. Here are a few next steps that people can begin working on:
* **Writing**: Write more of the Introduction and Context sections for the report (see doc above) - No data science experience required, and the links in the "Helpful articles" section at the top of the doc should help someone get started with this work. Much of this can probably be taken from the [OFA paper](https://docs.google.com/document/d/1hdLqLhQjPGwOpwMgH5dpTFMioSTRRZEGdQ5-lEZ9o_Q/edit?usp=sharing) as a start, but it will need to be heavily edited so that it isn't in an academic style, since the final output will be a report that is more in the style of an LF report (see the report Google doc above for more on style).  
* **Collect Data & Metrics Analysis**: Select several project health metrics from the CHAOSS project (ideally based on research) that might be used to answer some of the research questions listed in the doc. Ideally, these metrics should be implemented in Augur / 8Knot and / or GrimoireLab so that we can use CHAOSS projects for the visualizations. Several people could work on this at the same time. We have a start on this that can be found in the Appendix / Notes section of the report doc, but it still needs quite a bit of work.
* **Validation**: Validate the data for the 6 projects by talking to people who are directly involved in those projects. @geekygirldawn has started this work and contacted people from the projects.

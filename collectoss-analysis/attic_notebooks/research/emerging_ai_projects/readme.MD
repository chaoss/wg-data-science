## EMERGING AI PROJECTS

This directory aims to identify emerging projects in AI/ML space by applying different techniques like social graph analysis, page rank etc., on the contribution and contributors' data obtained using the Augur DB for an initial set of known repositories called [`seed`](ai_repos.json) projects.

Let's see the overview of all the notebooks developed this project.

### [repo_analysis](repo_analysis.ipynb)
In this notebook, we fetch the contribution data like pull request, pull request review, commit, and issue and perform perform social graph analysis by representing 
- projects and contributors as nodes and identifies the influential repositories in each AI/ML category.
- projects as nodes and contributors as edges and highlight the interconnectedness among various open-source repositories and identify key repositories that serve as hubs of collaboration. 


### [networkx_to_plotly](networkx_to_plotly.ipynb)
In this notebook, we try to convert the networkx graph of shared contributors between the math repositories for pull request contribution type to a plotly graph for more interactivity as a proof of concept for the later work. 


### [common_contributors](common_contributors.ipynb)
In this notebook, we identify the number of common pull request contributors in each AI/ML category(math, nlp, llm, gen_ai, personal_assistants) and also across all the mentioned categories and draw some important conclusions.


### [project_discovery_iterations](./project_discovery_iterations/)
This directory contains a couple of notebooks that were previously built for WASM network analysis. In this iteration, we perform similar analysis for AI/ML repositories to find new and interesting projects in this space. Please refer to the [readme](./project_discovery_iterations/readme.MD) for more information.
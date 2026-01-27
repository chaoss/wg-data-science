## PROJECT DISCOVERY ITERATIONS

The notebooks in this directory are based on the previous notebooks contributed by James Kunstle in [project_discovery](../../project_discovery).

The main goal to iterate on the listed notebooks is to perform similar analysis on the AI/ML repositories to find new projects that are not present in our [seed repositories](../ai_repos.json) and rank them based on page rank algorithm.


### [top_pagerank_common_repos](top_pagerank_common_repos.ipynb)
- top_page_rank_common_repos in this folder is based on the notebook [project_discovery/top_page_rank_common_repos](../../project_discovery/pagerank_top_repos/top_pagerank_common_repos.ipynb).
- In this notebook, we read the pagerank_scores for different contributors from [ai_contributor_pagerank.csv](ai_contributor_pagerank.csv) and retreive the event stream for the top 10% pagrank_score-havers and find new repositories by fetching other repositories they have worked on.


### [repo_discovery](repo_discovery.ipynb)
- repo_discovery in this folder is based on the notebook [project_discovery/repo_discovery](../../project_discovery/repo_discovery/repo_discovery.ipynb).
- In this notebook, we perform event stream analysis for known(seed), and unknown(non seed) repositories and overall repositories in general. We also perform known vs Unknown contributor analysis and find out new set of contributors $\hat{P}$ who were not in our seed.
- In addition to this, we also implement alpha and beta metrics and sort the repositories by their values to rank them.
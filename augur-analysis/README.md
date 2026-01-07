# Augur Notebooks 

This directory holds notebooks designed to connect with an Augur instance. Any notebook created before 2026 was orignially a resource in the oss-aspen/Rappel repository that has now been archieved. 

To get a local instance of Augur running on your local machine, follow these [docs](https://oss-augur.readthedocs.io/en/main/getting-started/using-docker.html). 


Overview of notebook directories: 

    ├── 8knot         <- Visualization development for 8Knot
    ├── density_metrics        <- EDA 
    ├── graph_analysis        <- EDA for discovering important open source projects
    ├── old        <- archieve notebooks from beginning of projects
    ├── performance        <- EDA 
    ├── survival_analysis           <- EDA notebooks for dash app


    Example of config.json file:

```
{
    "connection_string": "sqlite:///:memory:",
    "database": "sandiegorh",
    "host": "chaoss.tv",
    "password": "<<Your Password>>",
    "port": 5432,
    "schema": "augur_data",
    "user": "<<Your Username>>",
    "user_type": "read_only"
}

```
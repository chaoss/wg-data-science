# CollectOSS Notebooks 

This directory holds notebooks designed to connect with an CollectOSS instance. Any notebook created before 2026 was orignially a resource in the oss-aspen/Rappel repository that has now been archieved. 

To get a local instance of CollectOSS running on your local machine, follow these [docs](https://docs.collectoss.org/en/latest/). 


Overview of notebook directories: 

    ├── 8knot         <- Visualization development for 8Knot
    ├── attic_notebooks        <- prior research, no longer maintained
    ├── chaoss_election        <- notebook for chaoss election eligibility 
    ├── survival_analysis      <- EDA notebooks for dash app


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
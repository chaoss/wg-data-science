# License Change Dataset

The idea behind this dataset is to use it as a starting point to see if we can we predict the likelihood of a license change for an open source project from an open source license to a non-open source or more restrictive license. The project itself is being tracked in this [Issue](https://github.com/chaoss/wg-data-science/issues/47). Note that we have a related dataset for forks (see below).

Because we want to do some analysis on the repositories, any project without a GitHub repository has been excluded from the dataset (see section below for more details).

## The Dataset

[license_changes.csv](license_changes.csv)

The dataset can be found in the license_changes.csv file. It contains the following fields:
* project: project name
* relicense_date: relicense date
* orig_license: original license name
* new_license: new license name or description
* org: GitHub organization where the project can be found
* repo: GitHub repository where the project can be found
* license_file: license filename in the GitHub repo

The starting point for this dataset came from this [Wikipedia List of formerly open source software](https://en.wikipedia.org/wiki/List_of_formerly_open-source_or_free_software) page. You can find this list converted to a csv file in this folder called [wikipedia_list.csv](wikipedia_list.csv). Because we want to analyze what happens in a repo both before and after a license change, projects where the repo couldn't be found or where there were other issues that made the data suspect were excluded from license_changes.csv. Those issues are documented in a file in this folder called [dataset_notes.md](dataset_notes.md). If you want to help improve the dataset in license_changes.csv, the dataset_notes.md file would be an excellent place to start.


[more_forks.csv](more_forks.csv)

This dataset includes some additional examples of forks that were not created due to relicensing but most often either a) the original got bought by an entity the community found suspicious and decided to fork, or b) the original became unmaintained and someone new picked it up. The fields of the CSV match the structure of the license_changes dataset above.

## Contributions

This dataset is still a bit rough and incomplete, so contributions are welcome to help us improve it. See details above for ideas about where to contribute, and please follow our [Contribution guidelines](https://github.com/chaoss/wg-data-science/blob/main/CONTRIBUTING.md) including DCO sign-off for all commits.

If you learn of new projects that have been relicensed or older ones that we've missed, please feel free to submit a PR against license_changes.csv with the data. If you don't have time to create the PR, please file an issue to let us know, and we can add it to the dataset.

## Next Steps

This is a very basic dataset that is meant to be the starting point to create more robust data sets. By keeping license_changes.csv simple and limited to the basic information required to know where / when a license change took place, we can easily build on it in so many ways. In particular, it would be interesting to put this data into Augur and GrimoireLab for further study. We can also use the GitHub API to gather additional data as in the example below in the Additional Data section.

## Additional Data

There are some additional files in this folder.

* [generate-license-data.py](generate-license-data.py) is a script that was used to make it easier to find the date of the commit where the license change occurred. It also serves as an example of how you might use this dataset as a starting point to gather more data that can be used to learn about a license change.
* [output.json](output.json) is an autogenerated file created by generate-license-data.py and should not be edited. This is the output that was used to learn more about each license change in license_changes.csv.
* wikipedia_list.csv is a convenience file where the data from the Wikipedia page was stored that was used as a starting point. This isn't used anywhere else and should not be updated, since it just contains historical data. Any updates should be make in license_changes.csv.

# Forks Dataset

[forks.csv](forks.csv)

We are just beginning work on a dataset containing forks of open source projects, so right now it is very incomplete, but contributions are welcome! Please follow our [Contribution guidelines](https://github.com/chaoss/wg-data-science/blob/main/CONTRIBUTING.md) including DCO sign-off for all commits. You can also file issues or let us know via other channels if you see a mistake and want to let us know, but don't plan to make the change yourself.

Many recent forks are a result of license changes, so we are keeping the dataset here to make it easy for people to find.

Category column definitions:
* acquisition: primarily the result of one company acquiring another
* relicense: relicensing of a project, usually to a more restrictive license
* feature: this generally refers to issues with getting contributions (features) included in the original project and could be a result of disagreements, governance issues, or other community dynamics.

We know that open source projects are complex, and many forks don't fit into a single category, so we've attempted to pick the primary category and add any additional details in the notes.

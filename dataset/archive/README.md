# Archival of Open Source Projects (aka Sudden Archival)

Archival is often used as an indicator that a project is no longer being maintained and will not be updated (including security updates). We know that a lot of projects are archived when they are abandoned and people stop working on them, but what about projects that are archived for other reasons?

**More Details about this project:**
* Tracked in [Issue #45](https://github.com/chaoss/wg-data-science/issues/45)
* [Project Planning document](https://docs.google.com/document/d/18audPynKQg_n7ZdspeUGtPSF7cMzc9O7CVcrEdJAhtk/edit?usp=sharing)
* [WIP datasets](https://github.com/chaoss/wg-data-science/tree/main/dataset/archive)
  * data-files/archive_repos.csv: contains ~730 repos - all GH repos with > 1000 stars and > 100 forks with an open source license. These projects were imported into a [spreadsheet](https://docs.google.com/spreadsheets/d/1Nzi9kFLDoZC2RX7LMqGas9nSfHNIWvYNUBpkYXi5_40/edit?usp=sharing) for categorization.
  * archived_projects.py: the script containing the GraphQL API query to generate data-files/archive_repos.csv

**Current status:**
* Initial [WIP datasets](https://github.com/chaoss/wg-data-science/tree/main/dataset/archive) gathered.
* We'll start this project in June during the [Data Science Hackathon](https://chaoss.community/chaoss-data-science-hackathon-2025/).

## Hackathon Project Details

The project is part of the [CHAOSS Data Science Hackathon](https://chaoss.community/chaoss-data-science-hackathon-2025/) on June 26, 2025 in Denver Colorado.

Project Mentors: Dawn Foster (in person) and Peculiar C. Umeh (remote). We're happy to answer questions or provide feedback!

We'll all be working together in a [spreadsheet](https://docs.google.com/spreadsheets/d/1Nzi9kFLDoZC2RX7LMqGas9nSfHNIWvYNUBpkYXi5_40/edit?usp=sharing) to categorize archived projects and describe how and why they were archived. 

Not all data science work is glamorous. Data scientists spend a lot of time doing manual tasks like cleaning up and classifying data. This project is one of those less glamorous, manual activities. Anyone can help out with this project; no special data science skills are required.

**Pre-reading for the hackathon:**
* The [Instructions tab in the spreadsheet](https://docs.google.com/spreadsheets/d/1Nzi9kFLDoZC2RX7LMqGas9nSfHNIWvYNUBpkYXi5_40/edit?gid=1289159234#gid=1289159234) has detailed instructions for how we will be working during the hackathon and how to categorize each project. Before the hackathon, please read these instructions.
* The [Archive Reason Categories tab](https://docs.google.com/spreadsheets/d/1Nzi9kFLDoZC2RX7LMqGas9nSfHNIWvYNUBpkYXi5_40/edit?gid=1048670093#gid=1048670093) has a definition for each category. It's important that you read and understand these categories before we start so that we are all using the categories in the same way.
* The [Archived Repo Data tab](https://docs.google.com/spreadsheets/d/1Nzi9kFLDoZC2RX7LMqGas9nSfHNIWvYNUBpkYXi5_40/edit?gid=1500607077#gid=1500607077) has the list of projects that we will be reviewing. Your mentors, Dawn and Peculiar, have already categorized several projects. Please look at how these have been categorized and use the notes in the "How Notes" column to get a feel for the level of detail expected and where to look for information about archival.
* There are also a few articles about archiving (also called Sunsetting) open source projects that might help you better understand the process before you start categorizing projects:
  * [Practitioner Guide: Getting Started with Sunsetting an Open Source Project](https://chaoss.community/practitioner-guide-sunset/)
  * [GitHub’s Do’s and Don'ts When Sunsetting Open Source Projects](https://github.blog/open-source/maintainers/dos-and-donts-when-sunsetting-open-source-projects/)
  * [TODO Group Guide: Shutting Down an Open Source Project](https://todogroup.org/resources/guides/shutting-down-an-open-source-project)

**Here are a few important things to keep in mind:**
* **DO NOT re-sort the spreadsheet, move or resize columns**, or do anything other than editing the fields described below. These actions take effect for EVEYRONE in the spreadsheet, not just you, so they are disruptive to the work of others.
* **Not all of the information you need is in the spreadsheet**. You will need to click the link to the repo to look at the README text, issues, PRs, and other details. You may also want to look at the website (if they have one) or search for the project to see if anyone posted more details elsewhere about the archival.
*  The goal is not to be as fast as possible, but to be **as complete as possible**, so leave as many notes as you can and take the time to investigate multiple areas.
# Copyright Dawn M. Foster
# SPDX-License-Identifier: MIT

"""This script collects data about the archived repositories on GitHub with the most
stars / forks using the GitHub GraphQL Search API. Results with no license or 
license = Other are discarded to store only results for open source repositories.  

Inputs via command line arguments - see below or use -h for a list:
* file containing a GitHub access token
* threshold for stars (any project with more than that number of stars) - default to 1000
* threshold for forks (any project with more than that number of forks) - default to 100

As of May 22, 2025, using the default thresholds collects data on 1001 repositories, 
and stores 733 repositories after filtering by license as described above.

Outputs:
* GitHub API response code (success is "<Response [200]>") - printed to the screen
* csv file with the data stored as data-files/archive_repos.csv
"""

import sys
import csv
import argparse
import requests
import json

# Read arguments and store from command line
parser = argparse.ArgumentParser()

parser.add_argument("-t", "--token", dest="api_token_file", help="Filename of a file containing a GitHub Personal Access Token")
parser.add_argument("-s", "-stars", dest="num_stars", help="Collect data on projects with more than this number of stars. Default is 1000",
                    default=1000)
parser.add_argument("-f", "--forks", dest="num_forks", help="Collect data on projects with more than this number of forks. Default is 100",
                    default=100)

args = parser.parse_args()

api_token_file = args.api_token_file
num_stars = args.num_stars
num_forks = args.num_forks

def make_query(after_cursor = None):
    """ This function contains the GraphQL query
    """
    return """
        query archived ($search_string: String!) { 
          search(
            type:REPOSITORY,
            query:$search_string,
            first: 50 after:AFTER) {
                pageInfo {
                    hasNextPage
                    endCursor
                    }
                repos: edges{
              repo:node{
                ... on Repository {
                  url
                  homepageUrl
                  shortDescriptionHTML
                  isFork
                  isInOrganization
                  createdAt
                  updatedAt
                  pushedAt
                  archivedAt
                  stargazerCount
                  forkCount
                  primaryLanguage{
                    name
                  }
                  latestRelease{
                    publishedAt
                  }
                  licenseInfo{
                    name
                  }
            }
          } 
        }
      }
    }""".replace(
        "AFTER", '"{}"'.format(after_cursor) if after_cursor else "null"
            )

# Read GitHub key from file 
try:
    with open(api_token_file, 'r') as kf:
        api_token = kf.readline().rstrip() # remove newline & trailing whitespace

except:
    print("Error reading GH Key. This script depends on the existence of a file containing your GitHub API token. Exiting")
    sys.exit()

# Set up the variables needed for the GraphQL query
url = 'https://api.github.com/graphql'
headers = {'Authorization': 'token %s' % api_token}
search_string = "archived:True stars:>" + str(num_stars) + " forks:>" + str(num_forks)

# Variable initialization
results = []
has_next_page = True
after_cursor = None

# Run the GraphQL query for each page of results from the API
while has_next_page:

    query = make_query(after_cursor)

    variables = {"search_string": search_string}

    r = requests.post(url=url, json={'query': query, 'variables': variables}, headers=headers)
    print(r) # This prints the response so that you can see if the query fails with an error
    
    json_data = json.loads(r.text)
    
    results.append(json_data)

    has_next_page = json_data['data']['search']["pageInfo"]["hasNextPage"]

    after_cursor = json_data['data']['search']["pageInfo"]["endCursor"]

# Create csv output file
with open("data-files/archive_repos.csv", "w", newline="") as f:

    w = csv.DictWriter(f, results[0]['data']['search']['repos'][0]['repo'].keys())
    w.writeheader()
    
    # Loops through the results list and writes the csv file by row.
    # This also unpacks the nested JSON structures to allow them to 
    # be more readable in the csv file.
    for element in results:
    
        for repo_dict in element['data']['search']['repos']:
            try:
                repo_dict['repo']['latestRelease'] = repo_dict['repo']['latestRelease']['publishedAt']
            except:
                repo_dict['repo']['latestRelease'] = None
            try:
                repo_dict['repo']['primaryLanguage'] = repo_dict['repo']['primaryLanguage']['name']
            except:
                repo_dict['repo']['primaryLanguage'] = None
            try:
                repo_dict['repo']['licenseInfo'] = repo_dict['repo']['licenseInfo']['name']
            except:
                repo_dict['repo']['licenseInfo'] = None

            if repo_dict['repo']['licenseInfo'] != None and repo_dict['repo']['licenseInfo'] != "Other":
                # this only writes repos with a specified license into the csv file
                w.writerow(repo_dict['repo']) 
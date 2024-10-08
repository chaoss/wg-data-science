# Copyright Dawn M. Foster
# SPDX-License-Identifier: MIT

"""Gets Commit Data 
This is aggregated per person for a repo between two specified dates.
I'm currently using this to better understand who contributes to a project
before and after a key time in the project (relicense / fork) with a focus on
understanding organizational diversity.

Output (files are stored in the data-files directory)
* GitHub API response code (should be "<Response [200]>")
* Commit data pickle file containing a dataframe
* Person pickle file containing a dictionary
"""

import sys
import pandas as pd
import argparse
import requests
import json

# Read arguments from command line
parser = argparse.ArgumentParser()

parser.add_argument("-t", "--token", dest = "gh_key", help="GitHub Personal Access Token")
parser.add_argument("-u", "--url", dest = "gh_url", help="URL for a GitHub repository")
parser.add_argument("-b", "--begin_date", dest = "begin_date", help="Date in the format YYYY-MM-DD - gather commits after this begin date")
parser.add_argument("-e", "--end_date", dest = "end_date", help="Date in the format YYYY-MM-DD - gather commits up until this end date")

args = parser.parse_args()

gh_url = args.gh_url
gh_key = args.gh_key
since_date = args.begin_date + "T00:00:00.000+00:00"
until_date = args.end_date + "T00:00:00.000+00:00"

url_parts = gh_url.strip('/').split('/')
org_name = url_parts[3]
repo_name = url_parts[4]

# Read GitHub key from file 
try:
    with open(gh_key, 'r') as kf:
        api_token = kf.readline().rstrip() # remove newline & trailing whitespace

except:
    print("Error reading GH Key. This script depends on the existence of a file called gh_key containing your GitHub API token. Exiting")
    sys.exit()

pickle_file = 'data-files/' + repo_name + str(since_date) + str(until_date) + '.pkl'

def make_query(after_cursor = None):
    return """query repo_commits($org_name: String!, $repo_name: String!, $since_date: GitTimestamp!, $until_date: GitTimestamp!){
               repository(owner: $org_name, name: $repo_name) {
  ... on Repository{
      defaultBranchRef{
          target{
              ... on Commit{
                  history(since: $since_date, until: $until_date, first: 100 after: AFTER){
                      pageInfo {
                         hasNextPage
                         endCursor
                      }
                      edges{
                          node{
                              ... on Commit{
                                committedDate
                                deletions
                                additions
                                oid
                                authors(first:100) {
                                  nodes {
                                    date
                                    email
                                    user {
                                      login
                                      company
                                      email
                                      name
                                      }
                                    }
                                  }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
  }
            }""".replace(
        "AFTER", '"{}"'.format(after_cursor) if after_cursor else "null"
            )

def get_data(api_token, org_name, repo_name, since_date, until_date):
    """Executes the GraphQL query to get data from one GitHub repo.

    Returns
    -------
    repo_info_df : pandas.core.frame.DataFrame
    """
    
    url = 'https://api.github.com/graphql'
    headers = {'Authorization': 'token %s' % api_token}
    
    repo_info_df = pd.DataFrame()
    
    has_next_page = True
    after_cursor = None

    while has_next_page:

        query = make_query(after_cursor)

        variables = {"org_name": org_name, "repo_name": repo_name, "since_date": since_date, "until_date": until_date}
        r = requests.post(url=url, json={'query': query, 'variables': variables}, headers=headers)
        print(r)
        json_data = json.loads(r.text)

        df_temp = pd.DataFrame(json_data['data']['repository']['defaultBranchRef']['target']['history']['edges'])

        repo_info_df = repo_info_df.append(df_temp, ignore_index=True)

        has_next_page = json_data['data']['repository']['defaultBranchRef']['target']['history']["pageInfo"]["hasNextPage"]

        after_cursor = json_data['data']['repository']['defaultBranchRef']['target']['history']["pageInfo"]["endCursor"]
        
    return repo_info_df

repo_info_df = get_data(api_token, org_name, repo_name, since_date, until_date)

def expand_commits(commits):
    if pd.isnull(commits):
        commits_list = [None, None, None, None, None]
    else:
        node = commits
        try:
            commit_date = node['committedDate']
        except:
            commit_date = None
        try:
            dels = node['deletions']
        except:
            dels = None
        try:
            adds = node['additions']
        except:
            adds = None
        try:
            oid = node['oid']
        except:
            oid = None
        try:
            author = node['authors']['nodes']
        except:
            author = None
        commits_list = [commit_date, dels, adds, oid, author]
    return commits_list

repo_info_df['commits_list'] = repo_info_df['node'].apply(expand_commits)
repo_info_df[['commit_date','deletions', 'additions','oid','author']] = pd.DataFrame(repo_info_df.commits_list.tolist(), index= repo_info_df.index)
#repo_info_df = repo_info_df.drop(columns=['commits_list'])
repo_info_df
repo_info_df.to_pickle(pickle_file)

def create_person_dict(pickle_file, repo_name, since_date, until_date):
    import collections
    import pickle

    repo_info_df = pd.read_pickle(pickle_file)

    output_pickle = 'data-files/' + repo_name + '_people_' + str(since_date) + str(until_date) + '.pkl'

    # Create a dictionary for each person with the key being the gh login
    # Create a dict for commits that aren't tied to a gh login (gh user = None)
    person_dict=collections.defaultdict(dict)
    fail_person_dict=collections.defaultdict(dict)

    for x in repo_info_df.iterrows():
        data = x[1]

        for y in data['author']:
            try:
                login = y['user']['login']
                company = y['user']['company']
                commit_email = y['email']
                login_email = y['user']['email']
                name = y['user']['name']

                if person_dict[login]:
                    person_dict[login]['commits'] = person_dict[login]['commits'] + 1
                    person_dict[login]['additions'] = person_dict[login]['additions'] + data['additions']
                    person_dict[login]['deletions'] = person_dict[login]['deletions'] + data['deletions']
                    if commit_email not in person_dict[login]['email']:
                        person_dict[login]['email'].append(commit_email)
                else:
                    person_dict[login]['company'] = company
                    person_dict[login]['name'] = name
                    person_dict[login]['commits'] = 1
                    person_dict[login]['additions'] = data['additions']
                    person_dict[login]['deletions'] = data['deletions']
                    if len(login_email) == 0:
                        person_dict[login]['email'] = [commit_email]
                    elif commit_email == login_email:
                        person_dict[login]['email'] = [commit_email]
                    else:
                        person_dict[login]['email'] = [commit_email,login_email]
            except:
                try:
                    if fail_person_dict[commit_email]:
                        fail_person_dict[commit_email]['commits'] = fail_person_dict[commit_email]['commits'] + 1
                        fail_person_dict[commit_email]['additions'] = fail_person_dict[commit_email]['additions'] + data['additions']
                        fail_person_dict[commit_email]['deletions'] = fail_person_dict[commit_email]['deletions'] + data['deletions']
                    else:
                        fail_person_dict[commit_email]['commits'] = 1
                        fail_person_dict[commit_email]['additions'] = data['additions']
                        fail_person_dict[commit_email]['deletions'] = data['deletions']
                except:
                    print("Unknown Exception on", y)

    # For every email that didn't have a GH login / user, search for that email in the
    # person_dict and if found, add the commits, additions, and deletions to the proper user
    # Print error message if not found (above items for testing of that case)
    for f_key, f_value in fail_person_dict.items():
        found = False
        for key, value in person_dict.items():
            if f_key in value['email']:
                person_dict[key]['commits'] = person_dict[key]['commits'] + f_value['commits']
                person_dict[key]['additions'] = person_dict[key]['additions'] + f_value['additions']
                person_dict[key]['deletions'] = person_dict[key]['deletions'] + f_value['deletions']
                found = True
        if found == False:
            print('Not found - no person with this email',f_key,f_value)

    with open(output_pickle, 'wb') as f:
        pickle.dump(person_dict, f)

    print('Commit data stored in', pickle_file)
    print('People Dictionary stored in', output_pickle)

create_person_dict(pickle_file, repo_name, since_date, until_date)

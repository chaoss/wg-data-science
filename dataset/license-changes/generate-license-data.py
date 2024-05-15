#SPDX-License-Identifier: MIT

# Note: License file must be in the same org/repo

def setup_validate():
    import argparse
    import os
    import csv
    import sys

    # Gather options from command line arguments and store them in variables

    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--configfile", required=False, dest="input_data_file", default="inputdata.csv", help="The full path to a csv input file see inputdata.csv example in this repo (defaults to inputdata.csv)")
    parser.add_argument("-t", "--tokenvar", required=False, dest="token_var", default="GITHUB_AUTH_TOKEN", help="The name of the environmental variable where your GitHub personal access token can be found (defaults to GITHUB_AUTH_TOKEN)")

    args = parser.parse_args()
    input_data_file = args.input_data_file
    token_var = args.token_var

    # Read GitHub personal access token from the GITHUB_AUTH_TOKEN environment variable

    try:
        gh_key = os.environ[token_var]

    except:
        print("You must have an environment variable with a GitHub personal access token to run this script")
        print("For Linux / MacOS: export GITHUB_AUTH_TOKEN=<your access token>")
        print("For Windows: set GITHUB_AUTH_TOKEN=<your access token>")
        print("Exiting ...")
        sys.exit(1)

    # Read input file with some minimal data validation and store data in a list

    try:
        input_data = []
        
        with open(input_data_file, 'r') as f:
            data = csv.reader(f)
            for row in data:
                # Skip blank lines
                if len(row) != 0:
                    input_data.append(row)

                    # Make sure the csv file has 3 values per row before continuing
                    if len(row) != 8:
                        print("Data errors detected in row containing:", row)
                        print("Each line in the csv must contain 8 values.")
                        sys.exit(1)

        # Check for empty file and exit
        if len(input_data) == 0:
            print(input_data_file, "appears to be empty.")
            sys.exit(1)

        print("Reading input data from", input_data_file)

        return input_data, gh_key

    except:
        print("Can't read file", input_data_file, "Exiting ...")
        sys.exit(1)
    
    

def make_query():
    return """query licenseData($org: String!, $repo: String!, $lic_file: String!){
        repository(owner: $org, name: $repo){
            defaultBranchRef {
                target {
                    ... on Commit {
                    history(path: $lic_file, first: 100) {
                        nodes {
                            committedDate
                            url
                            additions
                            deletions
                            message
                        }
                    }
                    }
                }
                }
            url
            nameWithOwner
        }
    }
"""

def get_license_data():

    import requests
    import json
    import sys

    input_data, api_token = setup_validate()
    #print(input_data, api_token)

    url = 'https://api.github.com/graphql'
    headers = {'Authorization': 'token %s' % api_token}

    json_list = []

    for row in input_data:
        project = row[0]
        orig_yr = row[1]
        relicense_yr = row[2]
        orig_lic = row[3]
        new_lic = row[4]
        org = row[5]
        repo = row[6]
        lic_file = row[7]

        try:
            query = make_query()

            variables = {"org": org, "repo": repo, "lic_file": lic_file}
            #variables = {"org": org, "repo": repo}
            r = requests.post(url=url, json={'query': query, 'variables': variables}, headers=headers)
            json_data = json.loads(r.text)['data']
            
            # Add data from csv file
            json_data['repository']['project'] = project
            json_data['repository']['orig_yr'] = orig_yr
            json_data['repository']['relicense_yr'] = relicense_yr
            json_data['repository']['orig_lic'] = orig_lic
            json_data['repository']['new_lic'] = new_lic
                                    
            json_list.append(json_data)
        
        except:
            print("Unknown error: Could not get data from GitHub")
            sys.exit(1)
    
    return json_list

import json

json_list = get_license_data()
print(json_list)

json_obj = json.dumps(json_list, indent=4)

with open('output.json', 'w') as output:
    output.write(json_obj)

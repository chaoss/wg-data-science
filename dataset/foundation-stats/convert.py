import requests
import json
import csv

# URL containing the JSON data
url = "https://projects.eclipse.org/api/projects"

# Fetch JSON data from the URL
response = requests.get(url)
data = response.json()  # Parse JSON data

# Prepare data for CSV
# csv_data = []
# for project, details in data.items():
#     # Extract common fields (e.g., name, maintainer)
    
#     maintainer = details.get("maintainer", [])
#     if isinstance(maintainer, list) and len(maintainer) > 0:
#         maintainer_name = maintainer[0].get("name", "")
#         maintainer_email = maintainer[0].get("mbox", "")
#     else:
#         maintainer_name = ""
#         maintainer_email = ""
    
#     common_fields = {
#         "project": project,
#         "name": details.get("name", ""),
#         "category": details.get("category", ""),
#         "description": details.get("description", ""),
#         "doap": details.get("doap", ""),
#         "download_page": details.get("download-page", ""),
#         "homepage": details.get("homepage", ""),
#         "license": details.get("license", ""),
#         "programming_language": details.get("programming-language", ""),
#         "mailing_list": details.get("mailing-list", ""),
#         "repository": details.get("repository", ""),
#         "bug_database": details.get("bug-database", ""),
#         "maintainer_name": maintainer_name,
#         "maintainer_email": maintainer_email,
#     }

#     # Iterate through releases and create a row for each release
#     for release in details.get("release", []):
#         row = common_fields.copy()  # Copy common fields
#         row.update({
#             "release_version": release.get("revision", ""),
#             "release_date": release.get("created", ""),
#         })
#         csv_data.append(row)

# # Write to CSV
# csv_columns = ["project", "name","category","description","doap","download_page","homepage","license","programming_language","mailing_list","repository","bug_database", "maintainer_name", "maintainer_email", "release_version", "release_date"]

# with open('foundation_projects.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
#     writer.writeheader()
#     for row in csv_data:
#         writer.writerow(row)

# print("CSV file created successfully: output.csv")

# csv_data = []
# for project, details in data.items():
#     row = {
#         "project": project,
#         "description": details.get("description", ""),
#         "homepage": details.get("homepage", ""),
#         "name": details.get("name", ""),
#         "pmc": details.get("pmc", ""),
#         "podling": details.get("podling", ""),
#         "started": details.get("started", "")
#     }
#     csv_data.append(row)

# # Write to CSV
# csv_columns = ["project", "description", "homepage", "name", "pmc", "podling", "started"]

# with open('foundation_podlings.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
#     writer.writeheader()
#     for row in csv_data:
#         writer.writerow(row)

# print("CSV file created successfully: output.csv")


# csv_data = []
# for project, details in data.items():
#     row = {
#         "project": project,
#         "description": details.get("description", ""),
#         "ended": details.get("ended", ""),
#         "homepage": details.get("homepage", ""),
#         "name": details.get("name", ""),
#         "started": details.get("started", ""),
#         "status": details.get("status", "")
#     }
#     csv_data.append(row)

# # Write to CSV
# csv_columns = ["project", "description", "ended", "homepage", "name", "started", "status"]

# with open('foundation_podlings_history.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
#     writer.writeheader()
#     for row in csv_data:
#         writer.writerow(row)

# print("CSV file created successfully: output.csv")

# csv_data = []
# for item in data:
#     row = {
#         "established": item.get("established", ""),
#         "homepage": item.get("homepage", ""),
#         "id": item.get("id", ""),
#         "name": item.get("name", ""),
#         "retired": item.get("retired", "")
#     }
#     csv_data.append(row)

# # Write to CSV
# csv_columns = ["established", "homepage", "id", "name", "retired"]

# with open('foundation_committees_retired.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
#     writer.writeheader()
#     for row in csv_data:
#         writer.writerow(row)

# print("CSV file created successfully: output.csv")

# csv_data = []
# for project, url in data.items():
#     row = {
#         "project": project,
#         "url": url
#     }
#     csv_data.append(row)

# # Write to CSV
# csv_columns = ["project", "url"]

# with open('foundation_repositories.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
#     writer.writeheader()
#     for row in csv_data:
#         writer.writerow(row)

# print("CSV file created successfully: output.csv")


csv_columns = [
    "project_id", "short_project_id", "name", "summary", "url", "website_url", 
    "logo", "state", "provisioned", "top_level_project", "dev_list_name", 
    "dev_list_email", "dev_list_url", "documentation_url", "gettingstarted_url", 
    "download_url", "scope", "github_repos", "contributors", "committers", "project_leads"
]

# Prepare data for CSV
csv_data = []
for project in data:
    # Extract GitHub repos as a comma-separated string
    github_repos = ", ".join([repo.get("url", "") for repo in project.get("github_repos", [])])

    # Extract contributors as a comma-separated string
    contributors = ", ".join([f"{contributor.get('username', '')} ({contributor.get('full_name', '')})" 
                              for contributor in project.get("contributors", [])])

    # Extract committers as a comma-separated string
    committers = ", ".join([f"{committer.get('username', '')} ({committer.get('full_name', '')})" 
                            for committer in project.get("committers", [])])

    # Extract project leads as a comma-separated string
    project_leads = ", ".join([f"{lead.get('username', '')} ({lead.get('full_name', '')})" 
                               for lead in project.get("project_leads", [])])

    row = {
        "project_id": project.get("project_id", ""),
        "short_project_id": project.get("short_project_id", ""),
        "name": project.get("name", ""),
        "summary": project.get("summary", ""),
        "url": project.get("url", ""),
        "website_url": project.get("website_url", ""),
        "logo": project.get("logo", ""),
        "state": project.get("state", ""),
        "provisioned": project.get("provisioned", ""),
        "top_level_project": project.get("top_level_project", ""),
        "dev_list_name": project.get("dev_list", {}).get("name", ""),
        "dev_list_email": project.get("dev_list", {}).get("email", ""),
        "dev_list_url": project.get("dev_list", {}).get("url", ""),
        "documentation_url": project.get("documentation_url", ""),
        "gettingstarted_url": project.get("gettingstarted_url", ""),
        "download_url": project.get("download_url", ""),
        "scope": project.get("scope", ""),
        "github_repos": github_repos,
        "contributors": contributors,
        "committers": committers,
        "project_leads": project_leads
    }
    csv_data.append(row)

# Write to CSV
with open('projects.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for row in csv_data:
        writer.writerow(row)

print("CSV file created successfully: output.csv")
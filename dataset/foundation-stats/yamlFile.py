import yaml  # Install PyYAML if not already installed: pip install pyyaml
import csv



with open('landscape.yml', 'r', encoding='utf-8') as yaml_file:
    data = yaml.safe_load(yaml_file)



# Define CSV columns
csv_columns = [
    "name", "homepage_url", "repo_url", "logo", "twitter", "crunchbase", 
    "project", "accepted", "annual_review_date", "annual_review_url", 
    "dev_stats_url", "blog_url", "artwork_url", "slack_url", "chat_channel", 
    "clomonitor_name"
]

# Prepare data for CSV
csv_data = []
for category in data["landscape"]:
    for subcategory in category["subcategories"]:
        for item in subcategory["items"]:
            # Check if "item" exists and is not None
            if item and "item" in item and item["item"] is not None:
                item_data = item["item"]
                row = {
                    "name": item_data.get("name", ""),
                    "homepage_url": item_data.get("homepage_url", ""),
                    "repo_url": item_data.get("repo_url", ""),
                    "logo": item_data.get("logo", ""),
                    "twitter": item_data.get("twitter", ""),
                    "crunchbase": item_data.get("crunchbase", ""),
                    "project": item_data.get("project", ""),
                    "accepted": item_data.get("extra", {}).get("accepted", ""),
                    "annual_review_date": item_data.get("extra", {}).get("annual_review_date", ""),
                    "annual_review_url": item_data.get("extra", {}).get("annual_review_url", ""),
                    "dev_stats_url": item_data.get("extra", {}).get("dev_stats_url", ""),
                    "blog_url": item_data.get("extra", {}).get("blog_url", ""),
                    "artwork_url": item_data.get("extra", {}).get("artwork_url", ""),
                    "slack_url": item_data.get("extra", {}).get("slack_url", ""),
                    "chat_channel": item_data.get("extra", {}).get("chat_channel", ""),
                    "clomonitor_name": item_data.get("extra", {}).get("clomonitor_name", "")
                }
                csv_data.append(row)

# Write to CSV
with open('landscapeYml.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for row in csv_data:
        writer.writerow(row)

print("CSV file created successfully: output.csv")
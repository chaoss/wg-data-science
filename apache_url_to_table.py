import os
import json
import pandas as pd
import requests
import argparse

# Define script directory and output files
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_CSV = os.path.join(SCRIPT_DIR, "structured_project_analysis.csv")
OUTPUT_JSON = os.path.join(SCRIPT_DIR, "structured_project_cleaned.json")

# Define all data source URLs
SOURCE_URLS = {
    "projects": "https://projects.apache.org/json/foundation/projects.json",
    "podlings": "https://projects.apache.org/json/foundation/podlings.json",
    "podlings-history": "https://projects.apache.org/json/foundation/podlings-history.json",
    "committees-retired": "https://projects.apache.org/json/foundation/committees-retired.json",
    "repositories": "https://projects.apache.org/json/foundation/repositories.json"
}

# Function to fetch data from a URL
def fetch_data_from_web(url, source_name):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        json_data = response.json()
        print(f"✔ Successfully fetched data from {source_name}")
        return json_data
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching data from {url}: {e}")
        return None
    except json.JSONDecodeError:
        print(f"❌ Error: Failed to decode JSON from {url}")
        return None

# Function to dynamically extract meaningful data
def extract_relevant_data(data, source_name):
    structured_list = []

    # Debugging for repositories
    if source_name == "repositories":
        # Save the raw data for inspection
        with open(os.path.join(SCRIPT_DIR, "raw_repositories.json"), "w") as f:
            json.dump(data, f, indent=2)

        if isinstance(data, dict):
            # Repositories structure is: {project_id: [{repository_info}, {repository_info}, ...]}
            for project_id, repo_list in data.items():
                if isinstance(repo_list, list):
                    for repo in repo_list:
                        if isinstance(repo, dict):
                            # Extract repository data using .get to handle missing fields safely
                            structured_list.append({
                                "Source": source_name,
                                "Project ID": project_id,
                                "Project Name": repo.get("name", project_id),
                                "Category": "Repository",
                                "Description": repo.get("description", "N/A"),
                                "Homepage URL": repo.get("url", "N/A"),
                                "PMC": project_id,
                                "Podling": False,
                                "Start Date": "Unknown",
                                "Status": "Active",
                                "Repository Type": repo.get("type", "Unknown"),
                                "Repository URL": repo.get("url", "N/A")
                            })
                        elif isinstance(repo, str):
                            # Sometimes it might just be a URL string
                            structured_list.append({
                                "Source": source_name,
                                "Project ID": project_id,
                                "Project Name": project_id,
                                "Category": "Repository",
                                "Description": "N/A",
                                "Homepage URL": repo,
                                "PMC": project_id,
                                "Podling": False,
                                "Start Date": "Unknown",
                                "Status": "Active",
                                "Repository Type": "Unknown",
                                "Repository URL": repo
                            })
                else:
                    print(f"⚠ Unexpected repository format for {project_id}: {type(repo_list)}")
                    # Try handling as a single dictionary if not a list
                    if isinstance(repo_list, dict):
                        structured_list.append({
                            "Source": source_name,
                            "Project ID": project_id,
                            "Project Name": repo_list.get("name", project_id),
                            "Category": "Repository",
                            "Description": repo_list.get("description", "N/A"),
                            "Homepage URL": repo_list.get("url", "N/A"),
                            "PMC": project_id,
                            "Podling": False,
                            "Start Date": "Unknown",
                            "Status": "Active",
                            "Repository Type": repo_list.get("type", "Unknown"),
                            "Repository URL": repo_list.get("url", "N/A")
                        })
        else:
            print(f"⚠ Unexpected repositories format: {type(data)}")

        print(f"✔ Extracted {len(structured_list)} repository records")
        return structured_list

    # Handle other data sources (projects, podlings, etc.)
    if isinstance(data, dict):
        # Look for common patterns in the data structure
        keys = list(data.keys())
        if "projects" in data:
            data = data["projects"]
        elif "podlings" in data:
            data = data["podlings"]
        elif "entries" in data:
            data = data["entries"]
        elif len(keys) == 1 and isinstance(data[keys[0]], list):
            data = data[keys[0]]

    if not isinstance(data, list):
        print(f"⚠ Unexpected data format from {source_name}: {type(data)}")
        # Try to extract data from dictionary values if possible
        if isinstance(data, dict):
            temp_data = []
            for k, v in data.items():
                if isinstance(v, dict):
                    v["id"] = v.get("id", k)
                    temp_data.append(v)
            data = temp_data

    if not isinstance(data, list):
        print(f"⚠ Could not convert {source_name} data to list")
        return []

    for item in data:
        if not isinstance(item, dict):
            print(f"⚠ Skipping non-dictionary item in {source_name}: {type(item)}")
            continue

        structured_list.append({
            "Source": source_name,
            "Project ID": item.get("id") or item.get("name") or "Unknown",
            "Project Name": item.get("name", "Unknown"),
            "Category": item.get("category") or item.get("type") or "Unknown",
            "Description": item.get("description") or item.get("summary") or "Unknown",
            "Homepage URL": item.get("homepage") or item.get("url") or "Unknown",
            "PMC": item.get("pmc", "Unknown"),
            "Podling": item.get("podling", False),
            "Start Date": item.get("start_date") or item.get("started") or item.get("created") or "Unknown",
            "Status": item.get("status") or item.get("phase") or "Unknown"
        })

    print(f"✔ Extracted {len(structured_list)} records from {source_name}")
    return structured_list

# Argument parser for force update
parser = argparse.ArgumentParser()
parser.add_argument("--force-update", action="store_true", help="Force update by fetching the latest data from the web")
parser.add_argument("--debug", action="store_true", help="Save raw JSON data for debugging")
args = parser.parse_args()

# Check if existing files should be used
if os.path.exists(OUTPUT_CSV) and os.path.exists(OUTPUT_JSON) and not args.force_update:
    print(f"Using existing files: {OUTPUT_CSV} and {OUTPUT_JSON}. Run with --force-update to refresh data.")
else:
    all_data = []

    print("🔍 Fetching the most up-to-date data from Apache sources...")
    for source_name, url in SOURCE_URLS.items():
        print(f"📡 Fetching data from: {url}")
        raw_data = fetch_data_from_web(url, source_name)

        if raw_data:
            # Save raw data if in debug mode
            if args.debug:
                debug_file = os.path.join(SCRIPT_DIR, f"raw_{source_name}.json")
                with open(debug_file, "w") as f:
                    json.dump(raw_data, f, indent=2)
                print(f"🔍 Debug data saved to {debug_file}")

            structured_data = extract_relevant_data(raw_data, source_name)
            all_data.extend(structured_data)
        else:
            print(f"⚠ Warning: No data fetched from {url}")

    # Convert to Pandas DataFrame and save
    df = pd.DataFrame(all_data)

    if not df.empty:
        # Print data summary
        print("\n📊 Data Summary:")
        print(f"  - Total Records: {len(df)}")
        print(f"  - Records by Source:")
        for source, count in df['Source'].value_counts().items():
            print(f"    - {source}: {count}")

        df.to_csv(OUTPUT_CSV, index=False)
        with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
            json.dump(all_data, f, indent=4)
        print(f"\n✔ Processing complete. Data saved to: {OUTPUT_CSV} and {OUTPUT_JSON}")
    else:
        print("❌ Error: No valid data retrieved. CSV and JSON will not be updated.")
import os
import json
import pandas as pd
import requests

# Step 1: Define script directory and output file names
# This ensures all files are stored in the same location as the script.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_CSV = os.path.join(SCRIPT_DIR, "structured_project_analysis.csv")  # Clearer purpose
OUTPUT_JSON = os.path.join(SCRIPT_DIR, "structured_project_cleaned.json")  # More descriptive

# Step 2: Define web scraping source URL
# This is the source URL where we will fetch the latest project data.
SOURCE_URL = "https://incubator.apache.org/projects.json"  # Example data source

# Step 3: Function to fetch data from the web
def fetch_data_from_web(url):
    """
    Fetch JSON data from a specified web URL.
    Handles errors related to network failures and invalid JSON responses.
    """
    try:
        response = requests.get(url, timeout=10)  # 10-second timeout
        response.raise_for_status()  # Raise error for HTTP issues
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from web response.")
        return []

# Step 4: Function to normalize and clean data
def normalize_data(data):
    """
    Standardizes JSON structure to ensure consistent fields across all records.
    """
    structured_list = []
    for item in data:
        structured_list.append({
            "Project ID": item.get("id", "Unknown"),
            "Project Name": item.get("name", "Unknown"),
            "Category": item.get("category", "Unknown"),
            "Description": item.get("description", "Unknown"),
            "Homepage URL": item.get("homepage", "Unknown"),
            "PMC": item.get("pmc", "Unknown"),
            "Podling": item.get("podling", False),
            "Start Date": item.get("started", "Unknown"),
            "Status": item.get("status", "Unknown")
        })
    return structured_list

# Step 5: Add user option to force update for most up-to-date data
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--force-update", action="store_true", help="Force update by fetching the latest data from the web")
args = parser.parse_args()

# Step 6: Check if the output files already exist
# If the files exist and --force-update is not set, we avoid re-downloading the data.
if os.path.exists(OUTPUT_CSV) and os.path.exists(OUTPUT_JSON) and not args.force_update:
    print(f"Using existing files: {OUTPUT_CSV} and {OUTPUT_JSON}. To force an update, run with --force-update.")
else:
    # Step 7: Confirm before overwriting existing files
    if args.force_update and os.path.exists(OUTPUT_CSV) and os.path.exists(OUTPUT_JSON):
        confirm = input("Warning: This will overwrite existing files. Do you want to proceed? (yes/no): ").strip().lower()
        if confirm != "yes":
            print("Update canceled. Using existing files.")
            exit()

    print("Fetching the most up-to-date data from the web.")
    # Fetch and process data
    data = fetch_data_from_web(SOURCE_URL)
    normalized_data = normalize_data(data)

    # Convert to Pandas DataFrame
    df = pd.DataFrame(normalized_data)

    # Save outputs
    df.to_csv(OUTPUT_CSV, index=False)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(normalized_data, f, indent=4)

    # Step 8: Notify user of successful completion
    print(f"Processing complete.\nSaved structured data to: {OUTPUT_CSV} and {OUTPUT_JSON}")

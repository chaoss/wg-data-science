# README: Apache URL to Table Data Processor

## **Overview**
The `apache_url_to_table.py` script fetches, processes, and normalizes 
Apache project data from multiple sources. The goal is to create a 
structured dataset that allows researchers to analyze the transition of 
corporate projects into open-source foundations.

## **Features**
- Pulls project data from **six different Apache Foundation sources**.
- Normalizes data for consistency across all projects.
- Saves structured data in **CSV and JSON** formats.
- Includes an optional **force update** mode to fetch the latest data.
- Prevents redundant downloads by using existing files when possible.

## **Data Sources**
This script retrieves data from the following sources:
- [Apache Projects Overview](https://projects.apache.org/)
- [Apache Projects 
JSON](https://projects.apache.org/json/foundation/projects.json)
- [Podlings 
JSON](https://projects.apache.org/json/foundation/podlings.json)
- [Podlings History 
JSON](https://projects.apache.org/json/foundation/podlings-history.json)
- [Retired Committees 
JSON](https://projects.apache.org/json/foundation/committees-retired.json)
- [Repositories 
JSON](https://projects.apache.org/json/foundation/repositories.json)

## **Installation**
Ensure Python is installed and install required dependencies:
```sh
pip install pandas requests
```

## **How to Run the Script**
### **Using Existing Data (if Available)**
If the script has been run before, it will use previously downloaded 
files:
```sh
python apache_url_to_table.py
```

### **Forcing an Update (Fetching the Latest Data)**
To ensure you get the most up-to-date project data, use:
```sh
python apache_url_to_table.py --force-update
```
- This will **overwrite existing files**.
- The script will **prompt you for confirmation** before replacing data.
  - Type **'y'** and press **Enter** to proceed.
  - Press **Enter** without typing anything to cancel the update.

## **Output Files**
- **`structured_project_analysis.csv`** → CSV file containing the 
processed project data.
- **`structured_project_cleaned.json`** → JSON file containing the 
structured project data.

## **Confirming the Data for Research**
This script provides **a foundational dataset** for analyzing how 
corporate-owned open-source projects evolve once moved into foundations. 
**You can confirm the script's success by:**
1. Checking if **`structured_project_analysis.csv`** contains structured 
data.
2. Opening **`structured_project_cleaned.json`** to see if all project 
details were captured.
3. Manually inspecting **Apache source URLs** in a browser to ensure they 
are still available.

## **What’s Missing & Next Steps**
This dataset **still requires human research** to be fully complete. 
Recommended steps include:

### **1. Verifying Company Contributions**
- Manually research which corporations originally contributed each 
project.
- Compare corporate vs. community contributions over time.

### **2. Analyzing Governance Changes**
- Investigate if project governance structures changed post-transition.

### **3. Improving Data Quality**
- Identify missing or inconsistent project data.
- Cross-reference project status with Apache’s live data.

---
This script provides **a structured and repeatable method** for collecting 
across foundations, and should be revised with that intent. Have fun - 
this is an initial script and your edits could make you an author on an 
invaluable script for Open Source! 

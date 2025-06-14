import os
import requests
import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
import matplotlib.pyplot as plt

# --- CONFIGURABLE INPUTS ---
REPO_OWNER = "redis"
REPO_NAME = "redis"
RELICENSE_DATE = "2024-03-20"  # YYYY-MM-DD
MONTHS_BEFORE = 12
MONTHS_AFTER = 12

# --- TOKEN LOADING ---
with open("gh_keys.txt", "r") as file:
    GITHUB_TOKEN = file.read().strip()

print("Token loaded:", GITHUB_TOKEN[:6] + "..." if GITHUB_TOKEN else "No token found")

HEADERS = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
GITHUB_API_URL = "https://api.github.com/graphql"

def safe_parse(dt):
    """Safely parse a datetime string, return None if invalid or missing."""
    try:
        if dt is None or pd.isna(dt):
            return None
        return pd.to_datetime(dt, utc=True)
    except Exception:
        return None

def fetch_prs(repo_owner, repo_name, start, end):
    prs = []
    after = None
    query = '''
    query($owner: String!, $name: String!, $after: String) {
      repository(owner: $owner, name: $name) {
        pullRequests(first: 100, orderBy: {field: CREATED_AT, direction: ASC}, after: $after) {
          pageInfo {
            hasNextPage
            endCursor
          }
          nodes {
            state
            createdAt
            closedAt
            mergedAt
            author {
              login
              ... on User {
                company
              }
            }
          }
        }
      }
    }
    '''
    while True:
        variables = {"owner": repo_owner, "name": repo_name, "after": after}
        response = requests.post(GITHUB_API_URL, json={"query": query, "variables": variables}, headers=HEADERS)
        try:
            response.raise_for_status()
            data = response.json()
        except Exception as e:
            print("Error fetching data:", e)
            print("Response text:", response.text)
            break
        if 'errors' in data:
            print(f"GraphQL error: {data['errors']}")
            break
        nodes = data.get('data', {}).get('repository', {}).get('pullRequests', {}).get('nodes', [])
        for pr in nodes:
            created_at = safe_parse(pr.get('createdAt'))
            if created_at is None:
                continue
            if start <= created_at < end:
                pr['createdAt'] = created_at
                pr['closedAt'] = safe_parse(pr.get('closedAt'))
                pr['mergedAt'] = safe_parse(pr.get('mergedAt'))
                # Add author and organization info
                author = pr.get('author', {})
                pr['author_login'] = author.get('login') if author else None
                pr['author_org'] = author.get('company') if author else None
                prs.append(pr)
            elif created_at >= end:
                return prs
        page_info = data.get('data', {}).get('repository', {}).get('pullRequests', {}).get('pageInfo', {})
        if not page_info.get('hasNextPage'):
            break
        after = page_info.get('endCursor')
    return prs

def aggregate_monthly(prs, start, end):
    df = pd.DataFrame(prs)
    df["createdAt"] = pd.to_datetime(df["createdAt"])
    df["closedAt"] = pd.to_datetime(df["closedAt"])
    df["mergedAt"] = pd.to_datetime(df["mergedAt"])
    months = pd.date_range(start=start, end=end, freq="MS")
    agg = pd.DataFrame(index=months, columns=["open", "closed", "merged"]).fillna(0).astype(int)
    for month in months:
        next_month = month + pd.DateOffset(months=1)
        opened = df[(df["createdAt"] >= month) & (df["createdAt"] < next_month)]
        closed = df[(df["closedAt"] >= month) & (df["closedAt"] < next_month)]
        merged = df[(df["mergedAt"] >= month) & (df["mergedAt"] < next_month)]
        agg.loc[month, "open"] = len(opened)
        agg.loc[month, "closed"] = len(closed)
        agg.loc[month, "merged"] = len(merged)
    return agg

def plot_agg(agg):
    plt.figure(figsize=(12,6))
    plt.plot(agg.index, agg["open"], label="Opened PRs", marker="o")
    plt.plot(agg.index, agg["closed"], label="Closed PRs", marker="o")
    plt.plot(agg.index, agg["merged"], label="Merged PRs", marker="o")
    plt.title(f"PRs for {REPO_OWNER}/{REPO_NAME} ({MONTHS_BEFORE} months before and {MONTHS_AFTER} months after {RELICENSE_DATE})")
    plt.xlabel("Month")
    plt.ylabel("Count")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    center = datetime.datetime.strptime(RELICENSE_DATE, "%Y-%m-%d").replace(tzinfo=datetime.timezone.utc)
    start = (center - relativedelta(months=MONTHS_BEFORE))
    end = (center + relativedelta(months=MONTHS_AFTER+1))
    print(f"Fetching PRs from {start.date()} to {end.date()} ...")
    prs = fetch_prs(REPO_OWNER, REPO_NAME, start, end)
    print(f"Fetched {len(prs)} PRs.")

# Convert list of DataFrame and save as CSV
    df = pd.DataFrame(prs)
    df.to_csv("pull_requests.csv", index=False)
    print("Saved pull_requests.csv")

    agg = aggregate_monthly(prs, start, end)
    print("\nMonthly PR counts:")
    agg.to_csv("monthly_counts.csv")
    print("Saved monthly_counts.csv")
    
    print(agg)
    plot_agg(agg)

if __name__ == "__main__":
    main()
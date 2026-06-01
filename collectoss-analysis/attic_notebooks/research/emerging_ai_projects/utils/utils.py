from sqlalchemy import text
import sqlalchemy as salc
import pandas as pd
import collections
import plotly.graph_objects as go
from scipy.interpolate import interp1d
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def get_melted_df(contrib_df):
    
    # Group by 'repo_name' and 'cntrb_id', count occurrences, and reshape with 'repo_name' as columns
    df = contrib_df.groupby(['repo_name', 'cntrb_id']).size().unstack(fill_value=0)
    
    df = df.reset_index()

    # Melt df_pr from wide to long format, using 'repo_name' as the identifier variable
    df_melted = df.melt(
        ['repo_name'],        # Columns to keep as identifier variables
        var_name='cntrb_id',  # Name for the variable column
        value_name='number'   # Name for the values column
    )
    
    # Filter df_melted_commit to keep only rows where the 'number' column is not equal to 0
    df_melted = df_melted[df_melted[df_melted.columns[2]] != 0]
    
    return df_melted
    
def get_contributor_graph(df_melted):
    # Initialize an empty dictionary to store the graph
    contributorGraph = {}

    # Iterate over each row in df_melted_pr
    for i, row in df_melted.iterrows():
        # If the 'cntrb_id' is not already a key in the dictionary, add it with an empty list
        if row['cntrb_id'] not in contributorGraph:
            contributorGraph[row['cntrb_id']] = []
        
        # Append the repository name to the list for this 'cntrb_id'
        contributorGraph[row['cntrb_id']].append(row['repo_name'])
        
    return contributorGraph


def get_common_contributors_count(contributorGraph):
    # Initialize a defaultdict to store the count of common contributors for each pair of repositories
    commonRepoContributorsCount = collections.defaultdict(int)

    # Iterate over each contributor in the contributorGraph
    for key in contributorGraph:
        # Skip contributors with less than 2 repositories in their list
        if len(contributorGraph[key]) <= 1:
            continue
        
        # Iterate through the list of repositories for the current contributor
        for repo1 in range(len(contributorGraph[key]) - 1):
            for repo2 in range(repo1 + 1, len(contributorGraph[key])):
                # Update the count of common contributors for the pair of repositories
                commonRepoContributorsCount[
                    (contributorGraph[key][repo1], contributorGraph[key][repo2])
                ] += 1

    return commonRepoContributorsCount

def get_repo_common_contributors(commonRepoContributorsCount):
    repo_common_contributors = []

    # Iterate over each key-value pair in commonRepoContributionsByContributor
    for key in commonRepoContributorsCount:
        # Convert the key (a tuple of repository names) to strings and append the corresponding value
        repo_common_contributors.append(
            tuple(str(k) for k in list(key)) + (commonRepoContributorsCount[key],)
        )
    return repo_common_contributors



########################## Queries ##########################

def fetch_repo_ids_and_names(engine, repo_git_set):
    repo_set = []
    repo_name_set = []

    # Iterating through the list of repository git URLs
    for repo_git in repo_git_set:
        # Creating a SQL query to fetch repository ID and name for each git URL
        repo_query = text(f"""
                        SET SCHEMA 'augur_data';
                        SELECT 
                            b.repo_id,
                            b.repo_name
                        FROM
                            repo_groups a,
                            repo b
                        WHERE
                            a.repo_group_id = b.repo_group_id AND
                            b.repo_git = '{repo_git}'
                """)

        # Using the connection to execute the query
        with engine.connect() as connection:
            t = connection.execute(repo_query)  # Executing the query
            results = t.mappings().all()  # Fetching all the results
            
            # Checking if results are found and extracting repo_id and repo_name
            if results:
                repo_id = results[0]['repo_id']
                repo_name = results[0]['repo_name']
            else:
                repo_id = None
                repo_name = None
            
            # Appending the fetched repository ID and name to the respective lists
            repo_set.append(repo_id)
            repo_name_set.append(repo_name)
            
    return repo_set, repo_name_set



def fetch_pr_contributors(engine, repo_id):
    # Creating a SQL query to fetch pull request contributions for each repository
    repo_query = salc.sql.text(f"""
                    SET SCHEMA 'augur_data';
                    SELECT 
                        r.repo_id,
                        r.repo_name,
                        r.repo_git,
                        pr.pr_augur_contributor_id,
                        pr.pull_request_id
                    FROM
                        repo r, pull_requests pr
                    WHERE
                        pr.repo_id = '{repo_id}' AND
                        pr.repo_id = r.repo_id
                """)
    
    # Executing the query and reading the results into a DataFrame
    df_current_repo = pd.read_sql(repo_query, con=engine)
    
    return df_current_repo


####################### GRAPHS AND VISUALIZATIONS #######################################

def plot_networkx_graph(repo_common_contributors, node_size_factor=None):
    # Create an empty undirected graph
    g = nx.Graph()

    # Add edges with weights to the graph from the 'repo_common_contributors' list
    # Each item in 'repo_common_contributors' should be a tuple in the format (node1, node2, weight)
    g.add_weighted_edges_from(repo_common_contributors)
    # Get positions for all nodes
    pos = nx.spring_layout(g)
    
    # Draw the nodes with sizes based on their degree
    if node_size_factor:
        node_sizes = [nx.degree(g, n) * node_size_factor for n in g.nodes()]
    else:
        node_sizes = [nx.degree(g, n) * 100 for n in g.nodes()]

    # Draw the edges with widths based on their weight
    edge_widths = [g[u][v]['weight'] / 25 for u, v in g.edges()]

    # Create a plot with the specified size
    fig, ax = plt.subplots(figsize=(20, 20))

    # Draw the nodes and edges with the specified attributes
    nx.draw_networkx_nodes(g, pos, node_size=node_sizes, ax=ax)
    nx.draw_networkx_edges(g, pos, width=edge_widths, ax=ax)

    # Draw the labels with a background box for readability
    nx.draw_networkx_labels(g, pos, font_size=14, ax=ax, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

    # Draw edge labels with the number of contributors
    edge_labels = {(u, v): g[u][v]['weight'] for u, v in g.edges()}
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, font_size=10, ax=ax)
    
    plt.show()
    

def get_plotly_graph(repo_common_contributors, node_size_factor=None):
    # Create a graph and add weighted edges
    g = nx.Graph()
    g.add_weighted_edges_from(repo_common_contributors)

    # Get positions for all nodes using the spring layout algorithm
    pos = nx.spring_layout(g)

    # Calculate node sizes based on their degree
    if node_size_factor:
        node_sizes = [nx.degree(g, n)/node_size_factor for n in g.nodes()]
    else:
        node_sizes = [nx.degree(g, n) for n in g.nodes()]

    # Extract the x and y coordinates of the nodes
    x_nodes = [pos[node][0] for node in g.nodes()]
    y_nodes = [pos[node][1] for node in g.nodes()]

    # Create the Plotly figure
    fig = go.Figure()

    # Iterate through edges to add them to the Plotly figure
    for edge in g.edges(data=True):
        x0, y0 = pos[edge[0]]  # Starting coordinates of the edge
        x1, y1 = pos[edge[1]]  # Ending coordinates of the edge
        x_edges = [x0, x1]  # x-coordinates for the edge
        y_edges = [y0, y1]  # y-coordinates for the edge

        # Generate interpolated points between the nodes for smoother edges
        num_points = 3
        interp_func_x = interp1d([0, 1], x_edges)
        interp_func_y = interp1d([0, 1], y_edges)
        x_interp = interp_func_x(np.linspace(0, 1, num_points))
        y_interp = interp_func_y(np.linspace(0, 1, num_points))

        # Add edges to the figure
        fig.add_trace(go.Scatter(
            x=x_interp, y=y_interp,
            mode='lines',  # Use lines for edges
            line=dict(width=edge[2]['weight'] / 25, color='blue'),  # Set line width and color
            hoverinfo='text',  # Enable hover information
            text=[f'Shared contributors ({edge[1]}, {edge[0]}): {edge[2]["weight"]}']*num_points,  # Hover text for each edge
            showlegend=False
        ))
    n = 0.25 if node_size_factor else 2
    # Add the nodes as a scatter plot
    fig.add_trace(go.Scatter(
        x=x_nodes, y=y_nodes,
        mode='markers',  # Use markers for nodes
        marker=dict(size=[size * n for size in node_sizes], color='black', line=dict(color='black', width=1)),  # Set marker properties
        textposition='top center',
        textfont=dict(size=14),
        hoverinfo='text'  # Enable hover information for nodes
    ))

    # Add annotations for the node labels
    annotations = []
    for node, (x, y) in pos.items():
        annotations.append(
            dict(
                x=x, y=y,
                text=str(node),  # Node label
                showarrow=False,  # Disable arrow
                xanchor='center',
                yanchor='top',
                font=dict(color='red', size=12),
                bgcolor='white',
                bordercolor='black',
                borderwidth=1,
                opacity=1.0  # Solid white background
            )
        )

    # Update the layout to include annotations and adjust figure size
    fig.update_layout(
        showlegend=False,  # Disable legend for edges
        annotations=annotations,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        plot_bgcolor='white',
        title='Repositories Network with Shared Contributors',
        height=800,  # Set the height of the figure
        width=1000,  # Set the width of the figure
        margin=dict(l=75, r=100, t=75, b=100)  # Adjust margins to make the figure look nicer
    )
    
    return fig

def get_repo_pairs_with_highest_common_contributors(repo_common_contributors):
    # Sort the list by common contributors count in descending order
    sorted_repos = sorted(repo_common_contributors, key=lambda x: x[2], reverse=True)

    # Limit to top 50 repository pairs
    sorted_repos = sorted_repos[:50]

    # Extract data for visualization
    repos_pairs = [f"{repo[0]} & {repo[1]}" for repo in sorted_repos]
    contributors_counts = [repo[2] for repo in sorted_repos]

    # Create a horizontal bar chart with Plotly
    fig = go.Figure(go.Bar(
        x=contributors_counts,
        y=repos_pairs,
        orientation='h',
        marker=dict(color='skyblue'),
        hoverinfo='x+y',  # Show the number of contributors and repo pair on hover
    ))

    # Update layout
    fig.update_layout(
        title='Top Repository Pairs with Highest Common Contributor Count',
        xaxis_title='Number of Common Contributors',
        yaxis_title='Repository Pairs',
        yaxis=dict(
            autorange='reversed',  # Invert y-axis to show the highest count on top
            automargin=True  # Automatically adjust margins to accommodate the labels
        ),
        height=1400,  # Adjust height for better readability
        width=1000,  # Increase width to give more space for labels
        margin=dict(l=300),  # Increase left margin to make space for long labels
    )

    return fig

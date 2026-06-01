import numpy as np
import plotly.express as px

# Function to calculate the log growth rate for any 6-month period
def calculate_log_monthly_growth(df):

    # Sort data to ensure chronological order
    df = df.sort_values(by=['year', 'month'])
    
    # Calculate month-to-month log growth rate
    df['log_growth_rate'] = (np.log(df['total_contributions']) - np.log(df['total_contributions'].shift(1))) * 100

    # Drop the first month, as its growth rate will be NaN
    df = df.dropna(subset=['log_growth_rate'])
    
    # Create a sequential 'x-axis' column (1, 2, 3, ..., months_to_consider)
    df['x_axis'] = np.arange(1, 7)

    return df


# Function to calculate the Z-Score which standardizes the log_growth_rate for each category
def calculate_z_score(df, column_name):
    
    # Calculate the mean
    mean = df[column_name].mean()
    
    # Calculate the standard deviation
    std = df[column_name].std()
    
    # Calculate the S-score
    df['z_score'] = (df[column_name] - mean) / std
    
    return df


# Function to plot the growth rate by category
def plot_growth_rate_by_category(df, category_name, title):
    
    # Filter by category
    category_df = df[df['category'] == category_name].copy()

    # Format the 'x_axis' to show month and year in a readable format, if not already done
    category_df['formatted_date'] = category_df['month'].astype(str) + '-' + category_df['year'].astype(str)
    
    # Customize hover information
    hover_template = (
        "<b>Repository:</b> %{fullData.name}<br>"  # Repository name as title
        "<b>Month-Year:</b> %{customdata[0]}<br>"  # formatted date
        "<b>Growth Rate:</b> %{y:.2f}"  # log growth rate with 2 decimal precision
        "<extra></extra>"  # Remove extra trace name from hover
    )

    # Create the line plot with custom hover data
    fig = px.line(
        category_df, 
        x='x_axis', 
        y='log_growth_rate', 
        color='repo_name', 
        title=f'{title} for {category_name} repositories', 
        markers=True,
        custom_data=['formatted_date']  
    )

    fig.update_traces(hovertemplate=hover_template)

    # Customize layout
    fig.update_layout(
        xaxis_title="Month", 
        yaxis_title="Growth Rate",
        xaxis=dict(tickvals=[1, 2, 3, 4, 5, 6], ticktext=[1, 2, 3, 4, 5, 6]),
        legend_title="Repository", 
        title_x=0.5
    )

    return fig


# Function to plot the standardized growth rate by category
def plot_standardized_growth_rate(df, category_name, title):
    
    # Filter by category
    category_df = df[df['category'] == category_name].copy()
    category_df = calculate_z_score(category_df, 'log_growth_rate')
    
    # Format the 'x_axis' to show month and year in a readable format, if not already done
    category_df['formatted_date'] = category_df['month'].astype(str) + '-' + category_df['year'].astype(str)
    
    # Customize hover information
    hover_template = (
        "<b>Repository:</b> %{fullData.name}<br>"  # Repository name as title
        "<b>Month-Year:</b> %{customdata[0]}<br>"  # formatted date
        "<b>Standardized Growth Rate (Z-score):</b> %{y:.2f}"  # log growth rate with 2 decimal precision
        "<extra></extra>"  # Remove extra trace name from hover
    )

    # Create the line plot with custom hover data
    fig = px.line(
        category_df, 
        x='x_axis', 
        y='z_score', 
        color='repo_name', 
        title=f'{title} for {category_name} repositories', 
        markers=True,
        custom_data=['formatted_date']  
    )

    fig.update_traces(hovertemplate=hover_template)

    # Customize layout
    fig.update_layout(
        xaxis_title="Month", 
        yaxis_title="Z-score",
        xaxis=dict(tickvals=[1, 2, 3, 4, 5, 6], ticktext=[1, 2, 3, 4, 5, 6]),
        legend_title="Repository", 
        title_x=0.5
    )

    return fig


# Function to plot the exponential decay by category
def plot_exponential_decay_by_category(df, category_name, title):
    
    # Filter by category
    category_df = df[df['category'] == category_name].copy()

    # Format the 'x_axis' to show month and year in a readable format, if not already done
    category_df['formatted_date'] = category_df['month'].astype(str) + '-' + category_df['year'].astype(str)
    
    # Customize hover information
    hover_template = (
        "<b>Repository:</b> %{fullData.name}<br>"  # Repository name as title
        "<b>Month-Year:</b> %{customdata[0]}<br>"  # formatted date
        "<b>Exponential Decay:</b> %{y:.2f}"  # log growth rate with 2 decimal precision
        "<extra></extra>"  # Remove extra trace name from hover
    )

    # Create the line plot with custom hover data
    fig = px.line(
        category_df, 
        x='x_axis', 
        y='weighted_decayed_activity', 
        color='repo_name', 
        title=f'{title} for {category_name} repositories', 
        markers=True,
        custom_data=['formatted_date']  
    )

    fig.update_traces(hovertemplate=hover_template)

    # Customize layout
    fig.update_layout(
        xaxis_title="Month", 
        yaxis_title="Exponential Decay",
        xaxis=dict(tickvals=[1, 2, 3, 4, 5, 6], ticktext=[1, 2, 3, 4, 5, 6]),
        legend_title="Repository", 
        title_x=0.5
    )

    return fig
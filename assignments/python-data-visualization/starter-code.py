"""
Python Data Visualization Starter Code

This template provides a foundation for creating static and interactive visualizations.
Complete the tasks outlined in the assignment to implement the required functionality.
"""

import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px


# TODO: Task 1 - Create Static Charts with Matplotlib
# Implement the following functions:


def plot_line_chart(data, title):
    """
    Create a line chart showing trends.
    
    Args:
        data (list): List of values
        title (str): Chart title
    """
    pass


def plot_bar_chart(categories, values, title):
    """
    Create a bar chart for categorical data.
    
    Args:
        categories (list): List of category labels
        values (list): List of values for each category
        title (str): Chart title
    """
    pass


def plot_histogram(data, bins, title):
    """
    Create a histogram showing data distribution.
    
    Args:
        data (list): List of numerical values
        bins (int): Number of bins
        title (str): Chart title
    """
    pass


def plot_scatter(x_data, y_data, title):
    """
    Create a scatter plot showing relationships.
    
    Args:
        x_data (list): X-axis values
        y_data (list): Y-axis values
        title (str): Chart title
    """
    pass


# TODO: Task 2 - Build Interactive Visualizations with Plotly
# Implement the following functions:


def create_interactive_line(data, title):
    """
    Create an interactive line chart.
    
    Args:
        data (list): List of values
        title (str): Chart title
        
    Returns:
        plotly figure: Interactive line chart
    """
    pass


def create_interactive_bar(categories, values, title):
    """
    Create an interactive bar chart.
    
    Args:
        categories (list): List of category labels
        values (list): List of values for each category
        title (str): Chart title
        
    Returns:
        plotly figure: Interactive bar chart
    """
    pass


def create_dashboard(datasets):
    """
    Create a dashboard combining multiple charts.
    
    Args:
        datasets (dict): Dictionary with chart data and configurations
        
    Returns:
        plotly figure: Combined dashboard with multiple subplots
    """
    pass


# TODO: Main program
# Test your visualization functions with sample data


if __name__ == "__main__":
    # Add your test code here
    pass

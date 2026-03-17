# 📘 Assignment: Python Data Visualization

## 🎯 Objective

Learn to create compelling visual representations of data using matplotlib and plotly. You will practice building various chart types, customizing visualizations, and creating interactive dashboards to communicate insights effectively.

## 📝 Tasks

### 🛠️ Create Static Charts with Matplotlib

#### Description
Write a program that uses matplotlib to generate different types of static charts from datasets, including line plots, bar charts, histograms, and scatter plots.

#### Requirements
Completed program should:

- Create a function `plot_line_chart(data, title)` that generates a line plot showing trends over time.
- Implement a function `plot_bar_chart(categories, values, title)` that creates a bar chart comparing categorical data.
- Write a function `plot_histogram(data, bins, title)` that displays the distribution of numerical data.
- Create a function `plot_scatter(x_data, y_data, title)` that visualizes the relationship between two variables.
- Customize all charts with proper labels, titles, legends, and grid lines.
- Save charts to image files (e.g., PNG format).
- Example usage:
  ```python
  plot_line_chart([1, 2, 3, 4, 5], "Sales Trend")
  plot_bar_chart(["A", "B", "C"], [10, 15, 12], "Category Comparison")
  plot_histogram([1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5], bins=5, title="Distribution")
  ```

### 🛠️ Build Interactive Visualizations with Plotly

#### Description
Create interactive and dynamic visualizations using plotly that enable users to explore data through hover information, zooming, and filtering.

#### Requirements
Completed program should:

- Build a function `create_interactive_line(data, title)` that generates an interactive line chart with hover tooltips.
- Implement a function `create_interactive_bar(categories, values, title)` that creates an interactive bar chart.
- Write a function `create_dashboard(datasets)` that combines multiple charts into a single dashboard view.
- Add interactivity features such as hover information, zoom capabilities, and legend toggling.
- Ensure charts are responsive and display well on different screen sizes.
- Example usage:
  ```python
  create_interactive_line([10, 15, 13, 17, 20], "Monthly Revenue")
  create_interactive_bar(["Q1", "Q2", "Q3", "Q4"], [100, 150, 120, 180], "Quarterly Sales")
  ```

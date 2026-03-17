# 📘 Assignment: Statistics with Python

## 🎯 Objective

Master statistical analysis and data manipulation using pandas and numpy. You will practice loading datasets, calculating descriptive statistics, performing data cleaning, and conducting exploratory data analysis to extract meaningful insights from real-world data.

## 📝 Tasks

### 🛠️ Data Loading and Descriptive Statistics

#### Description
Write functions that load datasets using pandas and compute fundamental statistical measures to understand data characteristics and distributions.

#### Requirements
Completed program should:

- Create a function `load_dataset(filepath)` that reads CSV files into pandas DataFrames.
- Implement a function `calculate_statistics(dataframe, column)` that returns mean, median, mode, standard deviation, and variance for a given column.
- Write a function `data_summary(dataframe)` that generates a comprehensive summary including data types, missing values, and basic statistics for all numerical columns.
- Create a function `correlation_analysis(dataframe)` that calculates the correlation matrix and identifies highly correlated variables.
- Example usage:
  ```python
  df = load_dataset("data.csv")
  stats = calculate_statistics(df, "age")  # Returns dict with mean, median, mode, std, var
  summary = data_summary(df)  # Returns comprehensive statistics
  correlations = correlation_analysis(df)  # Returns correlation matrix
  ```

### 🛠️ Data Cleaning and Exploratory Analysis

#### Description
Develop functions for data cleaning, handling missing values, and performing exploratory data analysis to prepare data for statistical modeling.

#### Requirements
Completed program should:

- Create a function `handle_missing_values(dataframe, method)` that handles missing data using strategies like dropping, forward-fill, or mean imputation.
- Implement a function `remove_outliers(dataframe, column, method)` that identifies and removes outliers using IQR or Z-score methods.
- Write a function `data_distribution(dataframe, column)` that calculates skewness and kurtosis to understand data shape.
- Create a function `group_and_aggregate(dataframe, group_by_column, agg_column, operation)` that groups data and performs aggregations (sum, mean, count, etc.).
- Example usage:
  ```python
  cleaned_df = handle_missing_values(df, "mean")
  filtered_df = remove_outliers(df, "salary", "iqr")
  distribution = data_distribution(df, "age")
  grouped = group_and_aggregate(df, "department", "salary", "mean")
  ```

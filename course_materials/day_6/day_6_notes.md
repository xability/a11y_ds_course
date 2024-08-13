
# Line Plots and Scatter Plots  Notes


## What is a Line Plot?

- A line plot is a type of chart that represents data points connected by straight line segments.
- Line plots are particularly useful for visualizing data trends over time or across a continuous variable.

## When to Use a Line Plot:

- Use when you want to show trends or changes over time (e.g., stock prices over a year).
- Use to compare the trends of multiple datasets (e.g., sales trends of different products over time).

## Best for:

- Time series data or continuous data.
- Showing trends or changes over time.
- Comparing trends between different datasets.

## Key Components:

- **X-axis (Continuous Variable)**: Often represents time or another continuous variable.
- **Y-axis (Values)**: Represents the data points associated with each value on
the X-axis.
- **Line**: Connects the data points to show the trend.

## Types of Line Plots:

- **Simple Line Plot**: A single line connecting data points.
- **Multiple Line Plots**: Multiple lines on the same axes, useful for comparing
    different data series. (Not yet accessible with Maidr)

## Using Seaborn to Create Line Plots:

- **Basic Syntax**:

  ```python
  import seaborn as sns
  sns.lineplot(x='time', y='value', data=data)
  ```
  - `x`: The continuous variable to be plotted on the X-axis.
  - `y`: The numerical variable to be plotted on the Y-axis.
  - `data`: The data frame containing the variables.
- **Customization**:
  - Adjust line styles, colors, and markers to highlight specific trends.  (Use maidr AI to visualizes these differences)
  - Overlay multiple line plots for comparison. (Not accessible with Maidr.  You
    might be able to get some of this info from an AI we should try.)

## Common Pitfalls:

- **Overlapping Lines**: Too many lines on one plot can make it difficult to distinguish between them.  (Especially with Tactiles)
- **Misleading Axes**: Ensure the X-axis represents time or another continuous variable accurately.
- **Over-smoothing**: Avoid over-smoothing lines to the point where important data fluctuations are hidden.   (You will fail a test ifyou do)

## What is a Scatter Plot?

- A scatter plot is a type of chart that represents individual data points plotted on two axes.
- Scatter plots are useful for showing the relationship between two variables and identifying correlations.

### When to Use a Scatter Plot:

- Use when you want to explore the relationship or correlation between two variables (e.g., height vs. weight).
- Use to identify patterns, clusters, or outliers in the data.

### Best for:

- Data with Two variables.
- Identifying relationships, correlations, or patterns.
- Detecting outliers or unusual observations.

## Key Components:

- **X-axis (Variable 1)**: One of the variables being compared.
- **Y-axis (Variable 2)**: The other variable being compared.
- **Points**: Each point represents an observation (row) with two variable values.

## Interpreting Scatter Plots:

- **Positive Correlation**: Points trend upward from left to right.
- **Negative Correlation**: Points trend downward from left to right.
- **No Correlation**: Points are scattered with no clear pattern.
- **Outliers**: Points that fall far from the main cluster, indicating potential anomalies.

## Using Seaborn to Create Scatter Plots:

- **Basic Syntax**:

  ```python
  import seaborn as sns
  sns.scatterplot(x='variable1', y='variable2', data=data)
  ```
  - `x`: The first variable to be plotted on the X-axis.
  - `y`: The second variable to be plotted on the Y-axis.
  - `data`: The data frame containing the variables.
- **Customization**:
  - Adjust point colors, sizes, and styles to emphasize specific data points or patterns.
  - Overlay regression lines to highlight trends.

## Common Pitfalls:

- **Overplotting**: Too many points can overlap, making it difficult to see the
    relationship. (especially with tactile graphics)
- **Misinterpreting Correlations**: Be cautious of assuming correlation implies causation.
- **Ignoring or not ignoring Outliers**: Outliers can provide valuable insights,
but they can also distort the overall interpretation.


# Bar Plots and Histogram Notes

##  Look at the resources

Read the resources on Seaborn I found it easier to search for the type of Graph
rather than to go to their main page.  Sometimes the words don't match the thing
your trying to do so searching on google worked better for me.  Ifyour a pure data scientist this may not be true.


## figure Size

### Factors to Consider When Setting figsize

#### Amount of Data

- Bar Plots: If you have many categories or sub-categories, you might want to make the figure wider to accommodate all the bars without them overlapping.
- Histograms: If you're dealing with a large number of bins, a wider figure can make it easier to see the distribution clearly.

#### Purpose of the Plot

If you're creating a plot for presentation purposes (e.g., slides), you might prefer a larger figure.
For publication or embedding in a document, you may need a smaller or more precise size.

#### Aspect Ratio

A common aspect ratio is 16:9, but 4:3 or 3:2 are also used depending on the context.
For bar plots, a more square-like aspect ratio (e.g., 10x8 or 8x6) might be more appropriate if you have many categories.
For histograms, you might prefer a wider figure to make the distribution more visible (e.g., 12x6 or 10x6).

### Personal Preference sighted help

The choice of figsize can also come down to personal preference or specific
requirements for the visual style of the plot.  Only practice can make this work
good for you.  I normally make a few and ask someone.  Most of the time the data
we work on is repeditive.

#### Example Recommendations

##### Standard Bar Plot or Histogram

figsize=(10, 6) is a good default as it provides a nice balance between width and height for most datasets.

##### Wide Data with Many Categories or Bins

You might choose a wider figure, such as figsize=(12, 6) or even figsize=(14, 7).

##### Tall Data with Fewer Categories

If you have fewer categories but want to emphasize them, you might go with something like figsize=(8, 10).



## What is a Bar Plot?

- A bar plot is a type of chart that represents categorical data with rectangular bars.
- Each bar's height (or length in the case of horizontal bar plots) is proportional to the value it represents.
- Bar plots are useful for comparing different categories or groups.

## Key Components:

- **X-axis (Categories)**: Represents the different categories or groups.
- **Y-axis (Values)**: Represents the values associated with each category.
- **Bars**: The height (or length) of the bars shows the magnitude of each category's value.

## Types of Bar Plots:

- **Vertical Bar Plots**: Bars are aligned vertically, with categories on the X-axis.
- **Horizontal Bar Plots**: Bars are aligned horizontally, with categories on the Y-axis.
- **Grouped Bar Plots**: Multiple bars grouped together for comparison across categories.
- **Stacked Bar Plots**: Bars are stacked on top of each other to show the composition of different groups within a category.

## Using Seaborn to Create Bar Plots:

- **Basic Syntax**:

  ```python
  import seaborn as sns
  sns.barplot(x='category', y='value', data=data)
  ```
  - `x`: The categorical variable to be plotted on the X-axis.
  - `y`: The numerical variable to be plotted on the Y-axis.
  - `data`: The data frame containing the variables.
- **Customization**:
  - Adjust colors and styles to highlight specific categories.
  - Overlay additional information using annotations or labels.

## Common Pitfalls:


- No labels without good labels maidr will not read good information.
- **Color Choice**: Poor color contrast can make it difficult to distinguish
    between categories. or some data will not be visible for low vision.  Bright
    colors will help on presentations.
- **Misleading Scales**: Ensure that the Y-axis scale is appropriate and not misleading.
- **Overcrowding**: Too many bars can make the plot hard to read.

## More info on Grouped and Stacked (I needed more info)

### Grouped Bar Plot

A grouped bar plot is used to compare different categories within multiple groups. Imagine a standard bar plot, where each category has a single bar representing its value. Now, instead of one bar for each category, you have multiple bars grouped together side by side, each representing a different sub-category within the main category.

#### Example Description

Imagine you're comparing the sales of three products (A, B, C) across four regions (North, South, East, West). In a grouped bar plot:

- For each region (North, South, East, West), you would have  three bars standing next to each other.
- Each bar represents the sales of one of the products (A, B, or C).
- The bars are grouped by region, so you can easily compare the sales of different products within the same region.

The main takeaway from a grouped bar plot is that it allows you to compare the
values within each group (e.g., comparing the sales of Product A to Product B
within the North region) and also compare the same sub-category across different
groups (e.g., comparing Product A's sales in the North region to its sales in
the South region).

### Stacked Bar Plot

A stacked bar plot is used to show the composition of different categories within a single bar, stacked on top of each other. Instead of grouping bars side by side, all the categories within a group are stacked on top of each other in a single bar.

#### Example Description

Using the same example of product sales across regions:

- For each region (North, South, East, West), there would be a single bar.
- This single bar is divided into segments, with each segment representing the sales of one of the products (A, B, or C).
- The total height of the bar represents the combined sales of all three products in that region.
- Each segment within the bar shows how much of the total sales is contributed by each product.

The main purpose of a stacked bar plot is to compare the total values across categories (e.g., total sales in each region) while also showing the contribution of each sub-category (e.g., how much each product contributes to the total sales in that region).

### Key Differences

- Grouped Bar Plot: Useful for comparing values within the same category across
    different sub-categories. It emphasizes the differences within groups.
- Stacked Bar Plot: Useful for showing the total value across categories and how
    much each sub-category contributes to that total. It emphasizes the composition
    of each group.

## What is a Histogram?

- A histogram is a type of bar chart that represents the distribution of a numeric variable.
- It shows how frequently each value occurs by dividing the data into intervals, called bins.
- The height of each bar in the histogram reflects the count or frequency of data points within that bin.

## Key Components:
- **X-axis (Number line)**: Represents the range of the data values.
- **Bins**: Equal-width intervals along the X-axis.
- **Y-axis (Frequency or Count)**: Represents how many data points fall into each bin.
- **Bars**: The height of the bars shows the number of data points in each bin.

## Interpreting Histograms:
- **Shape**:
  - **Symmetric**: Data is evenly distributed around the center, resembling a bell curve.
  - **Right-Skewed**: Data tails off to the right; mean > median.
  - **Left-Skewed**: Data tails off to the left; mean < median.
  - **Uniform**: All values have the same frequency.
  - **Bimodal/Multimodal**: Two or more peaks indicating multiple modes.
- **Center**: The midpoint of the data, often represented by the mean, median, or mode.
- **Spread**: The range of the data, showing how spread out the values are.
- **Outliers**: Unusual values that stand apart from the rest of the data.

## Using Seaborn to Create Histograms:
- **Basic Syntax**:
  ```python
  import seaborn as sns
  sns.histplot(data, bins=10, kde=False)
  ```
  - `data`: The data to be plotted.
  - `bins`: Number of bins (intervals).
  - `kde`: Whether to add a Kernel Density Estimate line (smooth curve).
- **Customization**:
  - Adjust bin size to highlight different data characteristics.
  - Overlay multiple histograms to compare distributions. (Ask Jooyoung aif this is possible)
  - Use color, labels, and titles for clarity and presentation. (Labels are a must for Accessibility)

## Common Pitfalls:

- **Bin Width**: Too narrow may overcomplicate; too wide may oversimplify.  ( (Not sure how to make these choices)
- **Axis Alignment**: Ensure consistent axes when comparing multiple histograms.
    (this is true even for a Tactile comparison)
- **Over-Interpretation**: Avoid drawing conclusions from small, insignificant peaks or valleys. (Ask Jooyoung how to do this Blind Maybe ask AI)


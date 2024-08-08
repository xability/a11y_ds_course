# Empowering Data Vision: Data Science Course 

## Day 4 Syllabus 

## Session 1: Applying Functions with DataFrame.apply

- Introduction to the `DataFrame.apply` method.
o- Using `apply` to apply functions along the axis of DataFrames.
- Examples:
  - Applying a lambda function to normalize GDP per capita.
  - Applying a custom function to categorize life expectancy.

### Code Example:

```python
# Apply a lambda function to normalize gdpPercap
# This method scales the data based on the mean and standard deviation. The formula is:
# normalized =  mean (percap ) / STD( percap)
# All this does is make it so the numbers are easier to compare without losing information.

df['normalized_gdpPercap'] = df['gdpPercap'].apply(lambda x: (x - df['gdpPercap'].mean()) / df['gdpPercap'].std())
print(df[['country', 'gdpPercap', 'normalized_gdpPercap']].head())

# Custom function to categorize life expectancy

def life_exp_category(lifeExp):
    if lifeExp < 50:
        return 'Low'
    elif lifeExp < 70:
        return 'Medium'
    else:
        return 'High'

df['lifeExp_category'] = df['lifeExp'].apply(life_exp_category)
print(df[['country', 'lifeExp', 'lifeExp_category']].head())
```


## Session 2: Aggregation with Series and DataFrame

- Introduction to aggregation operations in pandas.
- Using `Series.agg` and `DataFrame.agg` to perform a variety of aggregation functions.
- Examples:
  - Calculate the mean and standard deviation of life expectancy and GDP per capita.
  - Aggregating multiple statistics in one go.

### Code Example:

```python

samp_df  = pd.DataFrame({'a':[1,2,3,4],'b':[5,6,7,8]})

#single series
result = samp_df['a'].agg(['sum','mean'])
print(result)

#multi series multi functions
result = samp_df.agg({
    'A': ['sum', 'mean'],
    'B': ['min', 'max']
})
print(result)

#named agg
result = samp_df.agg(
    sum_A=('A', 'sum'),
    mean_B=('B', 'mean')
)
print(result)

# gapminder Aggregation example
agg_results = df[['lifeExp', 'gdpPercap']].agg(['mean', 'std'])
print(agg_results)
```


## Session 3: Transformation with DataFrame.transform

- Introduction to the `DataFrame.transform` method.
- Using `transform` to perform element-wise transformations.
- Examples:
  - Transforming the GDP per capita to log scale.
  - Centering life expectancy around its mean.

### Code Example:

```python
import numpy as np

# Transform gdpPercap to log scale

df['log_gdpPercap'] = df['gdpPercap'].transform(np.log)

# this would also work
# df['log_gdp'] = np.log(df['gdp'])

print(df[['country', 'gdpPercap', 'log_gdpPercap']].head())

# Center life expectancy around its mean

df['centered_lifeExp'] = df['lifeExp'].transform(lambda x: x - x.mean())

#Could also be done as
df['centered_lifeExp'] = df['lifeExp'].mean()

print(df[['country', 'lifeExp', 'centered_lifeExp']].head())

```

## Session 4: Grouping Data with DataFrame.groupby

- Introduction to the `DataFrame.groupby` method.
- Performing group-wise operations.
- Examples:
  - Grouping by continent and calculating the mean life expectancy and GDP per capita.
  - revisit transform.
  
  - Applying multiple aggregation functions to grouped data.
  
### Code Example:

```python
# Group by continent and calculate mean life expectancy and GDP per capita
grouped = df.groupby('continent')[['lifeExp', 'gdpPercap']].mean()
print(grouped)

# Multiple aggregation functions with groupby
multi_agg = df.groupby('continent')[['lifeExp', 'gdpPercap']].agg(['mean', 'median', 'std'])
print(multi_agg)

# Calculate GDP per capita
df['gdp_per_capita'] = df['gdp'] / df['population']

# Use groupby and transform to apply log transformation to GDP per capita within each country
df['log_gdp_per_capita'] = df.groupby('country')['gdp_per_capita'].transform(np.log)

print(df)

```

## Session 5: Merging DataFrames with DataFrame.merge

- Introduction to the `DataFrame.merge` method.
- Using `merge` to combine DataFrames on common columns or indices.
- Examples:

  - Merging the Gapminder dataset with the World Bank country classification dataset on the 'country' column.
  - Performing different types of merges (inner, outer, left, right).

### Code Example:

```python
import pandas as pd

# Load Gapminder dataset
gap_df = pd.read_csv('gapminder.csv')

# Load World Bank country classification dataset
world_df = pd.read_csv('world_data.csv')

# Merge DataFrames on the 'name' column from World Bank dataset and 'country' column from Gapminder dataset
merged_df = pd.merge(gap_df, world_df, left_on='country', right_on='Country Name')
print(merged_df.head())

# Merge DataFrames with different types of merges
inner_merge = pd.merge(gap_df, world_df, left_on='country', right_on='Country Name', how='inner')
outer_merge = pd.merge(gap_df, world_df, left_on='country', right_on='Country Name', how='outer')
left_merge = pd.merge(gap_df, world_df, left_on='country', right_on='Country Name', how='left')
right_merge = pd.merge(gap_df, world_df, left_on='country', right_on='Country Name', how='right')

print("Inner Merge:\n", inner_merge.head())
print("Outer Merge:\n", outer_merge.head())
print("Left Merge:\n", left_merge.head())
print("Right Merge:\n", right_merge.head())

```


## Session 6: Joining DataFrames with DataFrame.join

- Introduction to the DataFrame.join method.
- Using join to combine DataFrames on indices.
- Examples:
- Joining the Gapminder dataset with the World Bank country classification dataset on their indices.
- Performing different types of joins (inner, outer, left, right).

### Code Example:

```python

# Set index for both DataFrames
gap_df.set_index('country', inplace=True)
world_df.set_index('Country Name', inplace=True)

# Join DataFrames on their indices
joined_df = gapminder_df.join(world_df)
print(joined_df.head())

# Join DataFrames with different types of joins
inner_join = gap_df.join(world_df, how='inner')
outer_join = gap_df.join(world_df, how='outer')
left_join = gap_df.join(world_df, how='left')
right_join = gap_df.join(world_df, how='right')

print("Inner Join:\n", inner_join.head())
print("Outer Join:\n", outer_join.head())
print("Left Join:\n", left_join.head())
print("Right Join:\n", right_join.head())

```


## Session 7: Pivoting Data with DataFrame.pivot

- Introduction to the `DataFrame.pivot` method.
- Using `pivot` to reshape data.
- Examples:
  - Pivoting the Gapminder dataset to show GDP per capita for different continents across years.
  - Using `pivot_table` for aggregation.

### Code Example:

```python
import pandas as pd

# Load Gapminder dataset
df = pd.read_csv('gapminder.csv')

# Pivot the DataFrame to show GDP per capita for different continents across years
pivot_df = df.pivot(index='year', columns='continent', values='gdpPercap')
print("Pivoted DataFrame:")
print(pivot_df.head())

```

## Session 8: Melting Data with DataFrame.melt

- Introduction to the DataFrame.melt method.
- Using melt to transform data from wide format to long format.
- Examples:
  -Melting the pivoted Gapminder dataset to return to its original form.
    =    Customizing the id_vars and value_vars parameters.
    
## Code Example:
```python

import pandas as pd

# Load Gapminder dataset
df = pd.read_csv('gapminder.csv')

# Example pivoted DataFrame
pivot_df = df.pivot(index='year', columns='continent', values='gdpPercap')
print("Pivoted DataFrame:")
print(pivot_df.head())

# Melt the DataFrame to return it to its original long format
melted_df = pivot_df.reset_index().melt(id_vars='year', value_vars=pivot_df.columns, var_name='continent', value_name='gdpPercap')
print("Melted DataFrame:")
print(melted_df.head())

## Session 9: Resampling Data with DataFrame.resample

- Introduction to the `DataFrame.resample` method.
- Performing operations on resampled data.
- Examples:
  - Resampling data to a lower frequency and calculating statistics.
  - Resampling GDP per capita data annually and calculating the mean.

### Code Example:

```python
# Assuming a datetime index is available
df['year'] = pd.to_datetime(df['year'], format='%Y')
df.set_index('year', inplace=True)

# Resample to decade and calculate mean
decade_resample = df.resample('10AS').mean()
print(decade_resample[['lifeExp', 'gdpPercap']])
```

## Session 10: Window Operations with Rolling, Expanding, and EWM

- Introduction to rolling, expanding, and exponential moving window operations.
- Examples:
  - Rolling mean of life expectancy.
  - Expanding sum of GDP per capita.
  - Exponential weighted mean of population.

### Code Example:

```python
# Rolling mean of life expectancy
# Rolling operations calculate statistics over a fixed-size sliding window.
# This can be useful for analyzing trends in GDP per capita over time for each

df['rolling_lifeExp'] = df['lifeExp'].rolling(window=5).mean()
print(df[['country', 'year', 'lifeExp', 'rolling_lifeExp']].head(10))

# Expanding sum of GDP per capita
# Expanding operations calculate cumulative statistics from the start of the
# data up to the current point. This can be useful for analyzing cumulative trends
# in GDP per capita.

df['expanding_gdpPercap'] = df['gdpPercap'].expanding().sum()
print(df[['country', 'year', 'gdpPercap', 'expanding_gdpPercap']].head(10))

# Exponential weighted mean of population
# Exponentially Weighted Moving operations apply a weighted moving average where
# more recent observations have exponentially more weight. This can be useful for
# smoothing GDP per capita data while giving more importance to recent years.

df['ewm_pop'] = df['pop'].ewm(span=5).mean()
print(df[['country', 'year', 'pop', 'ewm_pop']].head(10))
```

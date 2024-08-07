# Day 3: Exercises and Solutions


## Exercise 1: Load the penguin dataset and display the first 5 rows.
```python
import pandas as pd

# Load the dataset
df = pd.read_csv('penguins.csv')

# Display the first 5 rows
print(df.head())
```

## Exercise 2: Display concise summary information about the DataFrame.
```python
# Display concise summary information
print(df.info())
```

## Exercise 3: Display the descriptive statistics for the dataset.
```python
# Display descriptive statistics
print(df.describe())
```

## Exercise 4: Access the 'species' column as a Series.
```python
# Access 'species' column
species_series = df['species']
print(species_series.head())
```

## Exercise 5: Access the 'species' and 'island' columns.
```python
# Access 'species' and 'island' columns
species_island_df = df[['species', 'island']]
print(species_island_df.head())
```

## Exercise 6: Access the first row of the DataFrame using `.loc` and `.iloc`.
```python
# Access the first row using .loc
first_row_loc = df.loc[0]
print(first_row_loc)

# Access the first row using .iloc
first_row_iloc = df.iloc[0]
print(first_row_iloc)
```

## Exercise 7: View the index, columns, and data types of the DataFrame.

```python
# View the index
print(df.index)

# View the columns
print(df.columns)

# View the data types
print(df.dtypes)
```

##  Exercise 8: Count non-null values in each column.

```python
# Count non-null values
print(df.count())
```

## Exercise 9: Filter rows where 'bill_length_mm' is greater than 45.

```python
# Filter rows where 'bill_length_mm' is greater than 45
filtered_df = df[df['bill_length_mm'] > 45]
print(filtered_df.head())
```


## Exercise 10: Filter rows where 'species' is 'Adelie' and 'island' is 'Torgersen'.

```python
# Filter rows with multiple conditions
filtered_df = df[(df['species'] == 'Adelie') & (df['island'] == 'Torgersen')]
print(filtered_df.head())
```

## Exercise 11: Create a new DataFrame with only 'species' and 'bill_length_mm' columns and reset the index.

```python
# Create new DataFrame and reset index
new_df = df[['species', 'bill_length_mm']].reset_index(drop=True)
print(new_df.head())
```

## Exercise 12: Calculate the sum of 'bill_length_mm' for each species.
```python
# Calculate the sum of 'bill_length_mm' for each species
species_sum = df.groupby('species')['bill_length_mm'].sum()
print(species_sum)
```

## Exercise 13: Calculate the total sum of 'bill_length_mm' and 'bill_depth_mm' in the dataset.
```python
# Calculate total sum of specific columns
total_sum = df[['bill_length_mm', 'bill_depth_mm']].sum()
print(total_sum)
```

## Exercise 14: Sort the DataFrame by 'bill_length_mm' in ascending order.

```python
# Sort DataFrame by 'bill_length_mm' in ascending order
sorted_df = df.sort_values(by='bill_length_mm')
print(sorted_df.head())
```

## Exercise 15: Sort the DataFrame by 'species' in ascending order and 'body_mass_g' in descending order.

```python
# Sort DataFrame by 'species' and 'body_mass_g'
sorted_df = df.sort_values(by=['species', 'body_mass_g'], ascending=[True, False])
print(sorted_df.head())
```

## Exercise 17: Filter the DataFrame for 'Adelie' species and then sort by 'flipper_length_mm' in descending order.

```python
# Filter for 'Adelie' species and sort by 'flipper_length_mm'
adelie_df = df[df['species'] == 'Adelie']
sorted_adelie_df = adelie_df.sort_values(by='flipper_length_mm', ascending=False)
print(sorted_adelie_df.head())
```

## Exercise 18: Create a new DataFrame with only 'species' and 'bill_depth_mm' columns, then sort it by 'bill_depth_mm' in ascending order.

```python
# Create new DataFrame and sort by 'bill_depth_mm'
new_df = df[['species', 'bill_depth_mm']].sort_values(by='bill_depth_mm')
print(new_df.head())
```

## Exercise 19: Calculate the sum of 'body_mass_g' for each island, then sort the result by the sum in descending order.

```python
# Calculate sum of 'body_mass_g' for each island and sort
island_sum = df.groupby('island')['body_mass_g'].sum().sort_values(ascending=False)
print(island_sum)
```

### Exercise 20: Filter rows where 'flipper_length_mm' is between 200 and 210.

```python
# Filter rows based on flipper_length_mm range
filtered_flipper = df[(df['flipper_length_mm'] >= 200) & (df['flipper_length_mm'] <= 210)]
print(filtered_flipper.head())
```

## Exercise 21: Create a new DataFrame containing only rows where 'species' is 'Chinstrap' and then calculate the average 'body_mass_g' for this new DataFrame.

```python
# Filter and calculate average body_mass_g
chinstrap_df = df[df['species'] == 'Chinstrap']
average_body_mass = chinstrap_df['body_mass_g'].mean()
print(average_body_mass)
```

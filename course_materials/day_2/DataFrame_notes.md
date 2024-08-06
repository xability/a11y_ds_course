
# pandas DataFrame Class Attributes and Methods Notes

## Creating DataFrames

### From Lists

#### Description: 

Creating a DataFrame from a list of lists.

#### Example:

```python
import pandas as pd

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
df = pd.DataFrame(data, columns=['A', 'B', 'C'])
print(df)
```

### From Dictionaries

#### Description: 

Creating a DataFrame from a dictionary.

#### Example:

```python
data = {'A': [1, 4, 7], 'B': [2, 5, 8], 'C': [3, 6, 9]}
df = pd.DataFrame(data)
print(df)
```

### From Series

#### Description: 

Creating a DataFrame from multiple Series.

#### Example:

```python
series1 = pd.Series([1, 4, 7])
series2 = pd.Series([2, 5, 8])
series3 = pd.Series([3, 6, 9])
df = pd.DataFrame({'A': series1, 'B': series2, 'C': series3})
print(df)
```

## Attributes

### index

#### Description: 

The index (row labels) of the DataFrame.

#### Example:

```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['a', 'b', 'c'])
print(df.index)
```

### columns

#### Description: 

The column labels of the DataFrame.

#### Example:

```python
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df.columns)
```

### values

#### Description: 

Return a Numpy representation of the DataFrame.

#### Example:

```python
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df.values)
```

### dtypes

#### Description: 

Return the dtypes in the DataFrame.

#### Example:

```python
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6.0]})
print(df.dtypes)
```

### shape

#### Description: 

Return a tuple representing the dimensionality of the DataFrame.

#### Example:

```python
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df.shape)
```

### size

#### Description: 

Return an int representing the number of elements in this object.

#### Example:

```python
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df.size)
```

### empty

#### Description: 

Indicator whether DataFrame is empty.

#### Example:

```python
df = pd.DataFrame({'A': [], 'B': []})
print(df.empty)
```

### nbytes

#### Description: 

Return the number of bytes consumed by the DataFrame.

#### Example:

```python
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df.nbytes)
```

### ndim

#### Description: 

Return the number of dimensions of the DataFrame.

#### Example:

```python
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df.ndim)
```

### T

#### Description: 

Transpose index and columns.

#### Example:

```python
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df.T)
```

## Methods

### Adding a Series to a DataFrame

#### Adding a Series as a Column

#### Description: 

Add a Series to the DataFrame as a new column.

#### Example:

```python
new_column = pd.Series([10, 11, 12])
df['D'] = new_column
print(df)
```

#### Adding a Series as a Row

#### Description: 

Add a Series to the DataFrame as a new row.

#### Example:

```python
new_row = pd.Series([10, 11, 12, 13], index=['A', 'B', 'C', 'D'])
df = df.append(new_row, ignore_index=True)
print(df)
```


### head(n=5)

#### Description: 

Return the first n rows.

#### Example:

```python
df = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6], 'B': [6, 5, 4, 3, 2, 1]})
print(df.head(3))
```

### tail(n=5)

#### Description: 

Return the last n rows.

#### Example:

```python
df = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6], 'B': [6, 5, 4, 3, 2, 1]})
print(df.tail(3))
```

### describe()

#### Description: 

Generate descriptive statistics.

#### Example:

```python
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]})
print(df.describe())
```

### sum()

#### Description: 

Return the sum of the values over the requested axis.

#### Example:

```python
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df.sum())
```

### mean()

#### Description: 

Return the mean of the values over the requested axis.

#### Example:

```python
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df.mean())
```

### median()

#### Description: 

Return the median of the values over the requested axis.

#### Example:

```python
df = pd.DataFrame({'A': [1, 3, 2], 'B': [4, 6, 5]})
print(df.median())
```


## Accessing Elements in DataFrames

### Using Brackets

#### Description:

Brackets are used for simple indexing, which is primarily for accessing columns.

#### Example:

```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# Accessing a single column
print(df['A'])

# Accessing multiple columns
print(df[['A', 'B']])
```

#### When to use:

- Use brackets when you need to select a subset of the data by column labels or a range of rows via slicing.
- Suitable for quick and straightforward access.

### Using `loc`

#### Description:

`loc` is label-based data selecting method which means that we have to pass the
name of the row or column which we want to select. This method includes the last
element of the range passed in it.

#### Example:

```python
# Accessing a single row by index label
print(df.loc[0])

# Accessing multiple rows and columns by labels
print(df.loc[0:2, 'A'])

# Conditional access
print(df.loc[df['A'] > 1])
```

#### When to use:

- Use `loc` when indexing by label(s) or a boolean array.
- Ideal for modifying or accessing specific rows/columns based on label.
- Useful for when you need a more complex querying of row and column labels, with conditions.

### Using `iloc`

#### Description:

`iloc` is integer index-based. So here, we have to specify rows and columns by their integer index.

#### Example:

```python
# Accessing a single element
print(df.iloc[0, 1])

# Accessing a sub-DataFrame
print(df.iloc[0:2, 0:2])
```

#### When to use:

- Use `iloc` when you need to access elements by their integer index regardless of the DataFrame index labels.
- Suitable for scenarios where the position of the element is important, or when working with DataFrames where the index label does not matter.


## Looping Through DataFrames

### Iterating Over Rows

#### Using `iterrows()`

#### Description: 

Iterate over DataFrame rows as (index, Series) pairs.

#### Example:

```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
for index, row in df.iterrows():
    print(f"Index: {index}, Row: {row.tolist()}")


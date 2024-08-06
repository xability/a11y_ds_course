
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


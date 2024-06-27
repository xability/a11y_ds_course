# pandas DataFrame Class Attributes and Methods Notes
## Attributes

### index

#### Description: 

The index (row labels) of the DataFrame.

#### Example:


>
> import pandas as pd
>
> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['a', 'b', 'c'])
>
> print(df.index)

### columns

#### Description: 

The column labels of the DataFrame.

#### Example:


>
> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
>
> print(df.columns)

### values

#### Description: 

Return a Numpy representation of the DataFrame.

#### Example:


>
> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
>
> print(df.values)

### dtypes

#### Description: 

Return the dtypes in the DataFrame.

#### Example:


>
> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6.0]})
>
> print(df.dtypes)

### shape

#### Description: 

Return a tuple representing the dimensionality of the DataFrame.

#### Example:


>
> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
>
> print(df.shape)

### size

#### Description: 

Return an int representing the number of elements in this object.

#### Example:


>
> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
>
> print(df.size)

### empty

#### Description: 

Indicator whether DataFrame is empty.

#### Example:


>
> df = pd.DataFrame({'A': [], 'B': []})
>
> print(df.empty)

### nbytes

#### Description: 

Return the number of bytes consumed by the DataFrame.

#### Example:


>
> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
>
> print(df.nbytes)

### ndim

#### Description: 

Return the number of dimensions of the DataFrame.

#### Example:


>
> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
>
> print(df.ndim)

### T

#### Description: 

Transpose index and columns.

#### Example:


>
> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
>
> print(df.T)

## Methods

### head(n=5)

#### Description: 

Return the first n rows.

#### Example:


>
> df = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6], 'B': [6, 5, 4, 3, 2, 1]})
>
> print(df.head(3))

### tail(n=5)

#### Description: 

Return the last n rows.

#### Example:


>
> df = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6], 'B': [6, 5, 4, 3, 2, 1]})
>
> print(df.tail(3))

### describe()

#### Description: 

Generate descriptive statistics.

#### Example:


>
> df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]})
>
> print(df.describe())

### sum()

#### Description: 

Return the sum of the values over the requested axis.

#### Example:


>
> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
>
> print(df.sum())

### mean()

#### Description: 

Return the mean of the values over the requested axis.

#### Example:


>
> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
>
> print(df.mean())

### median()

#### Description: 

Return the median of the values over the requested axis.

#### Example:


>
> df = pd.DataFrame({'A': [1, 3, 2], 'B': [4, 6, 5]})
>
> print(df.median())

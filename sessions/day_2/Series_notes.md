# pandas Series Class Attributes and Methods Notes
## Attributes

### index

#### Description: 

The index (axis labels) of the Series.

#### Example:


>
>
> import pandas as pd
>
> s = pd.Series(\[1, 2, 3\], index=\[\'a\', \'b\', \'c\'\])
>
> print(s.index)

###  values

#### Description: 

Return Series as ndarray or ndarray-like
        depending on the dtype.

#### Example:

>
>
> s = pd.Series(\[1, 2, 3\])
>
> print(s.values)

###   dtype

#### Description: 

Data type of the Series.

#### Example:

>
>
> s = pd.Series(\[1, 2, 3\])
>
> print(s.dtype)

###  name

#### Description: 

The name of the Series.

#### Example:

>
>
> s = pd.Series(\[1, 2, 3\], name=\'numbers\')
>
> print(s.name)

###  shape

#### Description: 

Return a tuple of the shape of the underlying
        data.

#### Example:

>
>
> s = pd.Series(\[1, 2, 3\])
>
> print(s.shape)

###  size

#### Description: 

Return the number of elements in the Series.

#### Example:

>
>
> s = pd.Series(\[1, 2, 3\])
>
> print(s.size)

###  empty

#### Description: 

Indicator whether Series is empty.

#### Example:

>
>
> s = pd.Series(\[\])
>
> print(s.empty)

###  nbytes

#### Description: 

Return the number of bytes in the underlying
        data.

#### Example:

>
>
> s = pd.Series(\[1, 2, 3\])
>
> print(s.nbytes)

###  ndim

#### Description: 

Return the number of dimensions of the
        underlying data, which is 1 for Series.

#### Example:

>
>
> s = pd.Series(\[1, 2, 3\])
>
> print(s.ndim)

### hasnans

#### Description: 

Return if Series has any NaNs.

#### Example:

>
>
> s = pd.Series(\[1, 2, None\])
>
> print(s.hasnans)

## Methods

###  head(n=5)

#### Description: 

Return the first n elements of the Series.

#### Example:

>
>
> s = pd.Series(\[1, 2, 3, 4, 5, 6\])
>
> print(s.head(3))

### tail(n=5)

#### Description: 

Return the last n elements of the Series.

#### Example:

>
>
> s = pd.Series(\[1, 2, 3, 4, 5, 6\])
>
> print(s.tail(3))

### describe()

#### Description: 

Generate descriptive statistics.

#### Example:

>
>
> s = pd.Series(\[1, 2, 3, 4, 5\])
>
> print(s.describe())

### sum()

#### Description: 

Return the sum of the Series.

#### Example:

>
>
> s = pd.Series(\[1, 2, 3\])
>
> print(s.sum())

### mean()

#### Description: 

Return the mean of the Series.

#### Example:

>
>
> s = pd.Series(\[1, 2, 3\])
>
> print(s.mean())

### median()

#### Description: 

Return the median of the Series.

#### Example:

>
>
> s = pd.Series(\[1, 3, 2\])
>
> print(s.median())

### std()

#### Description: 

Return the standard deviation of the Series.

#### Example:

>
>
> s = pd.Series(\[1, 2, 3\])
>
> print(s.std())

### min()

#### Description: 

Return the minimum value in the Series.

#### Example:

>
>
> s = pd.Series(\[1, 2, 3\])
>
> print(s.min())

###max()

#### Description: 

Return the maximum value in the Series.

#### Example:

>
>
> s = pd.Series(\[1, 2, 3\])
>
> print(s.max())

1### count()

#### Description: 

Return the number of non-NA/null observations
        in the Series.

#### Example:

>
>
> s = pd.Series(\[1, 2, None\])
>
> print(s.count())

### unique()

#### Description: 

Return unique values of Series object.

#### Example:

>
>
> s = pd.Series(\[1, 2, 2, 3\])
>
> print(s.unique())

### nunique()

#### Description: 

Return number of unique elements in the Series.

#### Example:

>
>
> s = pd.Series(\[1, 2, 2, 3\])
>
> print(s.nunique())

### value\_counts()

#### Description: 

Return a Series containing counts of unique
        values.

#### Example:

>
>
> s = pd.Series(\[1, 2, 2, 3\])
>
> print(s.value\_counts())

### sort\_values()

#### Description: 

Sort by the values along either axis.

#### Example:

>
>
> s = pd.Series(\[3, 1, 2\])
>
> print(s.sort\_values())

### sort\_index()

#### Description: 

Sort Series by its index.

#### Example:

>
>
> s = pd.Series(\[3, 1, 2\], index=\[\'c\', \'a\', \'b\'\])
>
> print(s.sort\_index())

### apply(func)

#### Description: 

Invoke function on values of Series.

#### Example:

>
>
> s = pd.Series(\[1, 2, 3\])
>
> print(s.apply(lambda x: x\*\*2))

### map(arg)

#### Description: 

Map values of Series using input
        correspondence.

#### Example:

>
>
> s = pd.Series(\[1, 2, 3\])
>
> print(s.map({1: \'one\', 2: \'two\', 3: \'three\'}))

### astype(dtype)

#### Description: 

Cast a pandas object to a specified dtype
        dtype.

#### Example:

>
>
> s = pd.Series(\[1, 2, 3\])
>
> print(s.astype(float))

### isna()

#### Description: 

Detect missing values.

#### Example:

>
>
> s = pd.Series(\[1, 2, None\])
>
> print(s.isna())

### dropna()

#### Description: 

Return Series without null values.

#### Example:

>
>
> s = pd.Series(\[1, 2, None\])
>
> print(s.dropna())

### fillna(value)

#### Description: 

Fill NA/NaN values using the specified method.

#### Example:

>
>
> s = pd.Series(\[1, 2, None\])
>
> print(s.fillna(0))

### copy()

#### Description: 

Make a copy of this object\'s indices and data.

#### Example:

>
>
> s = pd.Series(\[1, 2, 3\])
>
> s\_copy = s.copy()
>
> print(s\_copy)

### rename(name)

#### Description: 

Alter Series name.

#### Example:

>
>
> s = pd.Series(\[1, 2, 3\])
>
> s\_renamed = s.rename(\"new\_name\")
>
> print(s\_renamed)

### to\_list()

#### Description: 

Return a list of the values.

#### Example:

>
>
> s = pd.Series(\[1, 2, 3\])
>
> print(s.to\_list())

### to\_dict()

#### Description: 

Convert Series to {label -\> value} dict.

#### Example:

>
>
> s = pd.Series(\[1, 2, 3\], index=\[\'a\', \'b\', \'c\'\])
>
> print(s.to\_dict())

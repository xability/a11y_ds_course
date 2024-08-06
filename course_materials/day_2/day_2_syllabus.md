# Empowering Data Vision: Data Science Course 
## Day 2 Syllabus 

### 1. Introduction and Setup 
- **Topic**: Review installation and configuration of `.pythonrc.py` file
- Install  great_tables module
  - Ensure all have it installed and configured correctly if they want it.

### 2. Pandas Terminology vs. Excel Terminology 
- **Topic**: Introduce key pandas terminology
  - Compare and contrast with familiar Excel terms
  - Series vs. Column
  - DataFrame vs. Sheet/Table
  - Index vs. Row Labels
  - Columns in DataFrame vs. Column Headers

### 3. Pandas Data Types 
- **Topic**: Overview of common pandas data types
  - `int64`, `float64`, `object`, `datetime64`, `bool`
  - Importance of data types in pandas operations
  - Example: `pd.Series([1, 2, 3]).dtype`

### 4. Series Creation and Attributes 
#### Session 1: Creating Series 
- **Topic**: Different ways to create Series
  - From List
    - Example: `pd.Series([1, 2, 3, 4, 5])`
  - From List with Index
    - Example: `pd.Series([10, 20, 30], index=['x', 'y', 'z'])`
  - From List with Name
    - Example: `pd.Series([10, 20, 30], name='MySeries')`
  - From Dictionary
    - Example: `pd.Series({'a': 1, 'b': 2, 'c': 3})`

#### Session 2: Series Attributes 
- **Topic**: Understanding Series attributes
  - `index`
    - Example: `s.index`
  - `values`
    - Example: `s.values`
  - `dtype`
    - Example: `s.dtype`
  - `name`
    - Example: `s.name`
  - `shape`
    - Example: `s.shape`
  - `size`
    - Example: `s.size`
  - `empty`
    - Example: `s.empty`
  - `nbytes`
    - Example: `s.nbytes`
  - `ndim`
    - Example: `s.ndim`
  - `hasnans`
    - Example: `s.hasnans`

### 5. Series Methods 
#### Session 1: Basic Methods 
- **Topic**: Using basic methods in Series
  - `head(n=5)`
    - Example: `s.head(3)`
  - `tail(n=5)`
    - Example: `s.tail(3)`
  - `describe()`
    - Example: `s.describe()`

#### Session 2: Statistical Methods 
- **Topic**: Applying statistical methods to Series
  - `sum()`
    - Example: `s.sum()`
  - `mean()`
    - Example: `s.mean()`
  - `median()`
    - Example: `s.median()`
  - `std()`
    - Example: `s.std()`
  - `min()`
    - Example: `s.min()`
  - `max()`
    - Example: `s.max()`

### 6. DataFrame Creation and Attributes (
#### Session 1: Creating DataFrames 
- **Topic**: Different ways to create DataFrames
  - From Dictionary
    - Example: `pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['a', 'b', 'c'])`

#### Session 2: DataFrame Attributes 
- **Topic**: Understanding DataFrame attributes
  - `index`
    - Example: `df.index`
  - `columns`
    - Example: `df.columns`
  - `values`
    - Example: `df.values`
  - `dtypes`
    - Example: `df.dtypes`
  - `shape`
    - Example: `df.shape`
  - `size`
    - Example: `df.size`
  - `empty`
    - Example: `df.empty`
  - `nbytes`
    - Example: `df.nbytes`
    - Example: `df.T`

### 7. DataFrame Methods (
#### Session 1: Basic Methods 
- **Topic**: Using basic methods in DataFrames
  - `head(n=5)`
    - Example: `df.head(3)`
  - `tail(n=5)`
    - Example: `df.tail(3)`
  - `describe()`
    - Example: `df.describe()`

#### Session 2: Statistical Methods 
- **Topic**: Applying statistical methods to DataFrames
  - `sum()`
    - Example: `df.sum()`
  - `mean()`
    - Example: `df.mean()`
  - `median()`
    - Example: `df.median()`
  - `std()`
    - Example: `df.std()`
  - `min()`
    - Example: `df.min()`
  - `max()`
    - Example: `df.max()`

### 8. Recreating Excel Spreadsheet in Pandas 
- **Topic**: Practical exercise
  - Task: Reproduce the Excel spreadsheet using pandas DataFrame and Series

# Empowering Data Vision: Data Science Course 
## Day 3 Syllabus 

## Objective:
To introduce basic data exploration, filtering, and data cleaning techniques
using pandas with the Student created Excel sheet and penguin dataset.

---

## Session  1:  Opening and exploring the sample xlsx file.

Continuing Day two by exploring the sample dataset. DataFrame Attributes 
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

#### Session 2: Basic Methods 
- **Topic**: Using basic methods in DataFrames
  - `head(n=5)`
    - Example: `df.head(3)`
  - `tail(n=5)`
    - Example: `df.tail(3)`
  - `describe()`
    - Example: `df.describe()`

#### Session 3: Statistical Methods 
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

### Recreating Excel Spreadsheet in Pandas 

- **Topic**: Practical exercise
  - Task: Reproduce the Excel spreadsheet using pandas DataFrame and Series
  - Work for tomorrow or this weekend.  The earlier the more questions you will have.

## session 4: Accessing Data, DataFrame Attributes, and Data Cleaning

### Accessing Columns and Rows 
- Accessing columns as Series.
  - Syntax: `df['column_name']`, `df.column_name`
- Accessing multiple columns.
  - Syntax: `df[['column1', 'column2']]`
- Accessing rows using `.loc` and `.iloc`.
  - Syntax: `df.loc[index]`, `df.iloc[index]`

### DataFrame Attributes 

- Viewing DataFrame index, columns, and data types.
  - Syntax: `df.index`, `df.columns`, `df.dtypes`



## Session 5:  Opening and exploring the Penguin dataset

### Introduction to Penguin Dataset 

- Overview of the penguin dataset.
- Importing pandas and loading the penguin dataset.
  - Syntax: `import pandas as pd` and `df = pd.read_csv('penguins.csv')`

### Basic DataFrame Inspection 

- Viewing the first and last few rows of the dataset.
  - Syntax: `df.head()`, `df.tail()`
- Getting a concise summary of the DataFrame.
  - Syntax: `df.info()`
- Descriptive statistics of the DataFrame.
  - Syntax: `df.describe()`

### Hands-on Practice 


## Session 6: Accessing Data, DataFrame Attributes, and Data Cleaning

### 2.1. Accessing Columns and Rows 
- Accessing columns as Series.
  - Syntax: `df['column_name']`, `df.column_name`
- Accessing multiple columns.
  - Syntax: `df[['column1', 'column2']]`
- Accessing rows using `.loc` and `.iloc`.
  - Syntax: `df.loc[index]`, `df.iloc[index]`

### 2.2. DataFrame Attributes 

- Viewing DataFrame index, columns, and data types.
  - Syntax: `df.index`, `df.columns`, `df.dtypes`
- Counting non-null values.
  - Syntax: `df.count()`

### 2.3. Data Cleaning 
- Dropping specific columns.
  - Syntax: `df.drop(columns=['column_name'])`
- Dropping specific rows.
  - Syntax: `df.drop(index=[row_index])`
- Dropping columns with missing values.
  - Syntax: `df.dropna(axis=1)`
- Dropping rows with missing values.
  - Syntax: `df.dropna(axis=0)`

### Hands-on Practice 

---

## Hour 3: Filtering, Creating New DataFrames, and Sorting

### 3.1. Filtering Rows and Columns 
- Filtering rows based on conditions.
  - Syntax: `df[df['column'] > value]`, `df[df['column'] == 'value']`
- Filtering multiple conditions using `&` and `|`.
  - Syntax: `df[(df['column1'] > value1) & (df['column2'] < value2)]`

### 3.2. Creating New DataFrame                                      

es 
- Creating a new DataFrame from a subset of the original DataFrame.
  - Syntax: `new_df = df[['column1', 'column2']]`
- Resetting index of the new DataFrame.
  - Syntax: `new_df.reset_index(drop=True)`

### 3.3. Sorting Data 
- Sorting the DataFrame by a single column in ascending order.
  - Syntax: `df.sort_values(by='column')`
- Sorting the DataFrame by multiple columns with different sorting orders.
  - Syntax: `df.sort_values(by=['column1', 'column2'], ascending=[True, False])`

### 3.4. Summarizing Data 
- Calculating sum for numeric columns.
  - Syntax: `df.sum()`
- Aggregating data with groupby (brief introduction).
  - Syntax: `df.groupby('column').sum()`

### Hands-on Practice 



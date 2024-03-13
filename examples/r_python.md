---
title: "Data Science Cheat Sheet: R vs. Python"
author: JooYoung Seo
---

```{r, include=FALSE}
knitr::opts_chunk$set(echo = TRUE, eval = FALSE)
```

# Load required packages for basic data science work

## R

```{r}
library(tidyverse)
library(tidymodels)
```

## Python

```{python}
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import pydataset
```

# Import data

## R

```{r}
df <- read_csv("file.csv")
```

## Python

```{python}
df = pd.read_csv("file.csv")
```

# Filtering

## R

```{r}
df %>% 
  filter(var1 %in% c("a", "b") & var2 < 50)
```

## Python

```{python}
df.\
  query('var1 in ["a", "b"] & var2 < 50')
```

# New column

## R

### Basic

```{r}
df <- df %>% 
  mutate(
    total = math + english,
    mean = (math + english) / 2
  )
```

### Advanced

```{r}
df <- df %>% 
  mutate(
    total = math + english,
    mean = total / 2
  )
```

## Python

### Basic

```{python}
df = df.\
  assign(
    total = df["math"] + df["english"],
    mean = (df["math"] + df["english"]) / 2
  )
```

### Advance: lambda must be used when variables are interdependent

```{python}
df = df.\
  assign(
    total = lambda x: x["math"] + x["english"],
    mean = lambda x: x["total"] / 2
  )
```

# Count

## R

```{r}
df %>%
  count(var, sort = TRUE)
```

## Python

```{python}
# The following returns pd.Series instead of pd.DataFrame
df["var"].\
  value_counts()
```

```{python}
# The following returns pd.DataFrame
df.\
  groupby("chr_var", as_index = False).\
  agg(n = ("chr_var", "count"))
```


# Drop column

## R

```{r}
df <- df %>%
  select(-var)
```

## Python

```{python}
df = df.\
  drop(columns = "var")
```

# Group by and summarize

## R

```{r}
df %>% 
  group_by(chr_var) %>% 
  summarize(mean_var = mean(num_var))
```

## Python

```{python}
df.\
  groupby('chr_var', as_index = False).\
  agg(mean_var = ('num_var', 'mean'))
```

# Arrange and sort

## Ascending

### R

```{r}
df %>% 
  arrange(var)
```

### Python

```{python}
df.\
  sort_values("var")
```

## Descending

### R

```{r}
df %>% 
  arrange(desc(var))
```

### Python

```{python}
df.\
  sort_values("var", ascending = False)
```

# Select variables

## As data frame

### R

```{r}
df %>% 
  select(var1, var2, var3)

  # The above is the same as the following:
df[c("var1", "var2", "var3")]
```

```{r}
# Single variable as a data frame
df[c("var")]
```

### Python

```{python}
df.\
  filter(["var1", "var2", "var3"])

# The above is the same as the following:
df[["var1", "var2", "var3"]]
```

```{python}
# Single variable as a data frame
df[["var"]]
```


## As a vector

### R

```{r}
df$var

# The above is the same as the following:
df[["var"]]
```

### Python

```{python}
df["var"]
```


# ifelse

## R

```{r}
ifelse()
```

## Python

```{python}
np.where()
```

# Data dimension

## R

```{r}
df %>%
  dim()
```

## Python

```{python}
df.\
  shape
```

# Variable types (altogether)

## r

```{r}
df %>%
  str()
```

## Python

```{python}
df.\
  dtypes
```


# Variable types (individually)

## r

```{r}
df$var %>%
  typeof()

## The following is the same
df[["var"]] %>%
  typeof()
```

## Python

```{python}
df["var"].\
  dtype
```

# Take a glimpse of data

## R

```{r}
df %>%
  glimpse()
```

## Python

```{python}
df.\
  info()
```

# Summarize

## R

```{r}
df %>%
  summary()
```

## Python

```{python}
df.\
  describe()
```

# Data frame

## R

```{r}
df <- tibble(
  column_header = c()
)
```

```{r}
df <- tibble(
  name = c("park", "kim"),
  english = c(80.5, 90.7),
  math = c(10L, 20L),
  pass = c(TRUE, FALSE),
  gender = factor(c("m", "f")),
  grade = ordered(c("a", "b"))
)
```

## Python

```{python}
df = pd.DataFrame({
  "column_header" : pd.Series()
})
```

```{python}
df = pd.DataFrame({
  "name" : ["park", "kim"],
  "english" : [80.5, 90.7],
  "math" : [10, 20],
  "pass" : [True, False],
  "gender" : pd.Series(["m", "f"], dtype = "category"),
  "grade" : pd.Series(["a", "b"], dtype = "category")
})
```

# Vector

## R

```{r}
var <- c(1L, 2L, 3L)
```

## Python

```{python}
var = pd.Series([1, 2, 3])
```

# Extract vector from data frame

## r

```{r}
var <- df[["var"]]
# The following is the same
var <- df$var
```

## Python

```{python}
var = df["var"]
```


# Class name

## R

```{r}
class(df)
class(df$var)
class(df[["var"]])
```

## Python

```{python}
type(df)
type(df['var'])
```

# Data type

r == python

int == int32
dbl == float64
chr == object
lgl == bool
fct == category
ord == category

# NA

## R

```{r}
NA
```

## Python

```{python}
np.nan
```

# in

## R

```{r}
var %in% c()
```

## Python

```{python}
var in []
```

# Scatterplot

## R

```{r}
ggplot(mpg, aes(x = displ, y = hwy, color = drv)) +
  geom_point()
```

## Python

```{python}
sns.scatterplot(
  data = mpg,
  x = "displ",
  y = "hwy",
  hue = "drv"
)
```

# Barplot

## R

```{r}
ggplot(mpg, aes(x = class)) +
  geom_bar()
```

## Python

```{python}
sns.countplot(
  data = mpg,
  x = "class"
)
```

# Col plot

## R

```{r}
class_count <- mpg %>% 
  count(class)

ggplot(class_count, aes(x = class, y = n)) +
  geom_col()
```

## Python

```{python}
class_count = mpg.\
  groupby("class", as_index = False).\
    agg(n = ("class", "count"))

sns.barplot(
  data = class_count,
  x = "class",
  y = "n"
)
```

# Line plot

## R

```{r}
ggplot(economics, aes(x = date, y = unemploy)) +
  geom_line()
```

## Python

```{python}
sns.lineplot(
  data = economics,
  x = "date",
  y = "unemploy"
)
```

# Box plot

## R

```{r}
ggplot(mpg, aes(x = drv, y = hwy)) +
  geom_boxplot()
```

## Python

```{python}
sns.boxplot(
  data = mpg,
  x = "drv",
  y = "hwy"
)
```

# Analyze Object Structure

## R

```{r}
ls(object)
```

## Python

```{python}
vars(object)
```

# Elipsis

## R

```{r}
function(...)
```

## Python

```{python}
function(*args, **kwargs)
```

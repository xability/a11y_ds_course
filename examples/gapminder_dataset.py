# Load required packages
import pandas as pd
from gapminder import gapminder

# Load the data
data = gapminder

# Take a glimpse at the data
data.info()

# Save the data as a csv file
data.to_csv("data/gapminder.csv", index=False)

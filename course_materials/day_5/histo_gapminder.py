import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import maidr

# Load the Gapminder dataset
gapminder = pd.read_csv("../../data/gapminder.csv")

# Basic Histogram: Distribution of Life Expectancy
plt.figure(figsize=(10, 6))
hist_plot = sns.histplot(gapminder["lifeExp"], bins=30, kde=True)
plt.title("Distribution of Life Expectancy")
plt.xlabel("Life Expectancy")
plt.ylabel("Frequency")
plt.show()
maidr.show(hist_plot)

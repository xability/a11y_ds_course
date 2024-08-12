import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import maidr

# Load the Gapminder dataset
gapminder = pd.read_csv("../../data/gapminder.csv")

# Regular Bar Plot: Example - Average life expectancy per continent
plt.figure(figsize=(10, 6))
bar_plot = sns.barplot(x="continent", y="lifeExp", data=gapminder)
plt.title("Average Life Expectancy per Continent")
plt.xlabel("Continent")
plt.ylabel("Average Life Expectancy")
plt.show()
maidr.show(bar_plot)

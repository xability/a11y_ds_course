import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import maidr

# Load the Gapminder dataset
gapminder = pd.read_csv("../../data/gapminder.csv")

# Filter the dataset to include only the Americas continent
gapminder_americas = gapminder[gapminder["continent"] == "Americas"]

# Histogram with Multiple Categories: Life Expectancy by Continent (Americas only)
plt.figure(figsize=(10, 6))
hist_plot_multi = sns.histplot(
    data=gapminder_americas, x="lifeExp", hue="continent", multiple="stack", bins=30
)
plt.title("Life Expectancy in the Americas")
plt.xlabel("Life Expectancy")
plt.ylabel("Frequency")
plt.show()
maidr.show(hist_plot_multi)

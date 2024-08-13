import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import maidr
gapminder = pd.read_csv('../../../data/gapminder.csv')

# Line plot of GDP per capita over time for USA
plt.figure(figsize=(10, 6))
usa_plot = sns.lineplot(data=gapminder[gapminder['country'] == 'United States'], x="year", y="gdpPercap", marker="o")
plt.title("GDP per Capita Over Time in the United States")
plt.xlabel("Year")
plt.ylabel("GDP per Capita")
plt.show()
maidr.show(usa_plot)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import maidr

gapminder = pd.read_csv('../../../data/gapminder.csv')

# Scatter Plot of GDP per capita vs population
plt.figure(figsize=(10, 6))
gdp_pop_plot = sns.scatterplot(data=gapminder, x="pop", y="gdpPercap", hue="continent")
plt.title("GDP per Capita vs Population by Continent")
plt.xlabel("Population")
plt.ylabel("GDP per Capita")
plt.show()
maidr.show(gdp_pop_plot)

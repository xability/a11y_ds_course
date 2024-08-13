import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import maidr

# Scatter plot of life expectancy vs GDP per capita
plt.figure(figsize=(10, 6))
life = sns.scatterplot(data=gapminder, x="gdpPercap", y="lifeExp", hue="continent")
plt.title("Life Expectancy vs GDP per Capita by Continent")
plt.xlabel("GDP per Capita")
plt.ylabel("Life Expectancy")
plt.show()

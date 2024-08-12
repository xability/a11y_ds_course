import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import maidr

# Load the Gapminder dataset
gapminder = pd.read_csv("../../data/gapminder.csv")


# Bar Plot: Example - Average life expectancy per continent 
# Count Plot: Example - Count of countries per continent
plt.figure(figsize=(10, 6))
count_plot = sns.countplot(x="continent", data=gapminder)
plt.title("Count of Countries per Continent")
plt.xlabel("Continent")
plt.ylabel("Number of Countries")
plt.show()
maidr.show(count_plot)

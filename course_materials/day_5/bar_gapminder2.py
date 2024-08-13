import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import maidr

# Load the Gapminder dataset
gapminder = pd.read_csv("../../data/gapminder.csv")

un_df = gapminder[['continent', 'country']].drop_duplicates()

# Count Plot: Example - Count of countries per continent
plt.figure(figsize=(10, 6))
count_plot = sns.countplot(x="continent", data=un_df)
plt.title("Count of Countries per Continent")
plt.xlabel("Continent")
plt.ylabel("Number of Countries")
plt.show()
maidr.show(count_plot)

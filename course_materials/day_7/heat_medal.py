import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import maidr

medals = pd.read_csv('../../data/athlete_events.csv')
medals = medals[medals['Team'] != 'undefined']
medals = medals[medals['Year'] > 2000]

# Pivot the data to have teams as rows and years as columns and medal as values.
medal_pivot = medals.pivot_table(index='Team', columns='Year', values='Medal', aggfunc='count', fill_value=0)


plt.figure(figsize=(10, 6))
medals_plot  = sns.heatmap(
data= medal_pivot,
annot=True,
fmt=".2f",
cmap="YlGnBu"
)

# Set the title
plt.title("Medals by team per year")
#plt.show()
maidr.show(medals_plot)

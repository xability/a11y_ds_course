import pandas as pd
import matplotlib.pyplot as plt
import maidr
import seaborn as sns


# Load gapminder
gapminder = pd.read_csv('../../data/gapminder.csv')

# Create a Box plot
plt.figure(figsize=(10, 6))
box_plot = sns.boxplot(
# normal order
x='continent',
y='lifeExp',
data=gapminder

)

# Set the title and labels
plt.title("Life Expectancy by Continent")
plt.xlabel("Life Expectancy")
plt.ylabel("Continent")

# Show the plot
plt.show()
maidr.show(box_plot)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import maidr
diamonds = sns.load_dataset("diamonds")

# Scatter plot for Carat vs price in the diamonds dataset
plt.figure(figsize=(10, 6))
karrat = sns.scatterplot(data=diamonds, x="carat", y="price")
plt.title("Carat vs Price")
plt.xlabel("Carat")
plt.ylabel("Price")
plt.show()
maidr.show(karrat)

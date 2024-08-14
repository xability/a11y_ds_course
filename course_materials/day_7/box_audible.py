import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import maidr
# Load the dataset
books = pd.read_csv('../../data/Audible_Catlog.csv')

# Create 5 bins for the ratings
books['rating_bins'] = pd.cut(books['Rating'], bins=5, labels=['0-1', '1-2', '2-3', '3-4', '4-5'])

# Create a box plot with the rating bins on the x-axis and price on the y-axis
plt.figure(figsize=(10, 6))
rating_plot = sns.boxplot(x='rating_bins', y='Price', data=books)

# Set the title and labels
plt.title("Price Distribution by Ratings")
plt.xlabel("Ratings")
plt.ylabel("Price")

# Show the plot
# plt.show()
maidr.show(rating_plot)


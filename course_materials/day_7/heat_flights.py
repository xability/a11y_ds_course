import seaborn as sns
import matplotlib.pyplot as plt
import maidr

flights = sns.load_dataset("flights")

# Pivot the data to have years as rows and months as columns
flights_pivot = flights.pivot(index="year", columns="month", values="passengers")

plt.figure(figsize=(10, 8))
flights = sns.heatmap(
data= flights_pivot, 
annot=True, 
fmt="d",
#cmap="YlGnBu"
)

# Set the title
plt.title("Monthly Number of Passengers (1949 - 1960)")

# Show the plot
#plt.show()
maidr.show(flights)
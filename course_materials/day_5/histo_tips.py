import seaborn as sns
import matplotlib.pyplot as plt
import maidr

# Load the tips dataset from Seaborn
tips = sns.load_dataset("tips")

# Filter the dataset to include only data for Sunday
sunday_tips = tips[tips["day"] == "Sun"]

# Create a histogram of tips by time for Sunday
plt.figure(figsize=(10, 6))
histo_tips = sns.histplot(
    sunday_tips, x="tip", hue="time", multiple="stack", kde=False, bins=10
)

# Add labels and title
plt.title("Distribution of Tips by Time on Sunday")
plt.xlabel("Tip Amount")
plt.ylabel("Frequency")

# Show the plot
plt.show()
maidr.show(histo_tips)

# Load required packages
import seaborn as sns

# Load the data
data = sns.load_dataset("penguins")

# Take a glimpse at the data
data.info()

# Save the data as a csv file
data.to_csv("data/penguins.csv", index=False)

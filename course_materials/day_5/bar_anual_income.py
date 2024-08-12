import pandas as pd

import matplotlib.pyplot as plt
import maidr
import seaborn as sns

# Read the CSV data into a DataFrame
df = pd.read_csv(
    "../../data/Successful_Employment_for_Blind_Iowans_by_Federal_Fiscal_Year.csv"
)


# Create a bar plot using Seaborn
plt.figure(figsize=(8, 6))
gender_plot = sns.barplot(
    x="Gender",
    y="Annual Earnings",
    data=df,
    palette=["blue", "pink"],
)
plt.xlabel("Gender")
plt.ylabel("Average Annual Income")
plt.title("Average Annual Income by Gender")
plt.show()
maidr.show(gender_plot)

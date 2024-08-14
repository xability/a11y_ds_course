import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import maidr
tips = sns.load_dataset("tips")

# days on the x-axis and tip on the y-axis
plt.figure(figsize=(10, 6))
tip_box = sns.boxplot(
x='day', 
y='tip', 
data=tips
)

plt.title("Tips by Day")
plt.xlabel("Week day")
plt.ylabel("Tip Amount")

# plt.show()
maidr.show(tip_box)

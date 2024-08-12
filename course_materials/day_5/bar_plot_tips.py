import matplotlib.pyplot as plt
import seaborn as sns
import maidr

# Load dataset
tips = sns.load_dataset("tips")

# group by average tips per day
avg_tips = tips.groupby("day")["tip"].mean().reset_index()

# Create a bar plot of the average tips per day
plt.figure(figsize=(10, 6))
av_tips = sns.barplot(x="day", y="tip", data=avg_tips, ci=None, palette="muted")
plt.title("Average Tips by Day")
plt.xlabel("Day")
plt.ylabel("Average Tip")

plt.show()
maidr.show(av_tips)

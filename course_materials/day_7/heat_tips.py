import seaborn as sns
import matplotlib.pyplot as plt
import maidr

tips = sns.load_dataset("tips")

# Pivot the data to have days as rows and time (meal) as columns 
tips_pivot = tips.pivot_table(values='tip', index='day', columns='time', aggfunc='mean')

# get rid of the extra digits  (Ask Jooyoung about this. maybe maidr is speaking them.
#tips_pivot = tips_pivot.transform(lambda x: round( x,2))

#Change the Na to 0 because 0 sounds better and na affects maidr
#tips_pivot = tips_pivot.fillna(0)

plt.figure(figsize=(10, 8))
tips = sns.heatmap(
data= tips_pivot, 
annot=True, 
fmt=".2f",
cmap="YlGnBu"
)

# Set the title
plt.title("Meal  tip amount for the week")
#plt.show()
maidr.show(tips)
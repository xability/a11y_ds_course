import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import maidr
from matplotlib.ticker import FuncFormatter
car_crashes = sns.load_dataset("car_crashes")

car_crashes['ptotal'] = car_crashes['total'].apply(lambda x: round (x,2))
car_crashes['pspeeding'] = car_crashes['speeding'].apply(lambda x : round(x,2))
# line plot using two variables: speed and total number of crashes
plt.figure(figsize=(10, 6))

car = sns.lineplot(data=car_crashes, x="pspeeding", y="ptotal")
plt.title("Total Car Crashes vs Speeding")
plt.xlabel("Speeding (% of total)")
plt.ylabel("Total Number of Crashes")

# Format the x-axis and y-axis to show only two digits after the decimal
#plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x:.2f}'))
#plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y:.2f}'))

plt.show()
maidr.show(car)
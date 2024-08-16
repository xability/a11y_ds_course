import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import maidr


# Load the data
data = pd.read_csv("total_2023.csv")

# Convert the 'Date time' column to datetime
data["Date time"] = pd.to_datetime(data["Date time"])

# Create a 'Month' column
# months={1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",7:"Jul",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}
data["Month"] = data["Date time"].dt.month
# data['Month'] =  data['Month'].apply(lambda x : months[x])


# Calculate the average temperature per month
monthly_avg_temp = data.groupby("Month")["Temperature"].mean().reset_index()

plt.figure(figsize=(10, 6))
# Plot the bar plot
bar_temp_plot = sns.barplot(x="Month", y="Temperature", data=monthly_avg_temp)
plt.title("Average Temperature by Month")
plt.ylabel("Average Temperature")
plt.xlabel("Month")
# plt.show()
maidr.show(bar_temp_plot)
plt.close()

input("")
# Calculate the total precipitation per month
monthly_precip = data.groupby("Month")["Precipitation"].sum().reset_index()

plt.figure(figsize=(10, 6))
# Plot the bar plot
bar_prec_plot = sns.barplot(x="Month", y="Precipitation", data=monthly_precip)
plt.title("Total Precipitation by Month")
plt.ylabel("Total Precipitation (inches)")
plt.xlabel("Month")
# plt.show()
maidr.show(bar_prec_plot)
plt.close()
input("")

# Now to see how the temp changes through the year
# Create a line plot
# Calculate the daily average temperature
daily_avg_temp = data.groupby("Date time")["Temperature"].mean().reset_index()

plt.figure(figsize=(10, 6))
# Plot the line plot
line_temp_avg_plot = sns.lineplot(x="Date time", y="Temperature", data=daily_avg_temp)
plt.title("Average Temperature Over the Year")
plt.ylabel("Temperature (F)")
plt.xlabel("Date")
# plt.show()
maidr.show(line_temp_avg_plot)
plt.close()
input("")
# now lets see what the shape of the data is with a box plot
plt.figure(figsize=(10, 6))
# Plot the box plot
box_prec_plot = sns.boxplot(x="Month", y="Precipitation", data=data)
plt.title("Precipitation by Month")
plt.ylabel("Precipitation (inches)")
plt.xlabel("Month")
# plt.show()
maidr.show(box_prec_plot)

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Prepare the Dataset
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct",
              "Nov", "Dec"],
    "Revenue": [12000, 15000, 17000, 14000, 18000, 22000, 24000, 20000, 23000, 25000,
                27000, 30000],
    "Profit": [3000, 3500, 4000, 3200, 4500, 6000, 6500, 5800, 6200, 7000, 7500, 8000],
    "Region": ["North", "South", "East", "West", "North", "South", "East", "West",
               "North", "South", "East", "West"]
}
df = pd.DataFrame(data)
print(df.head())

# ----------------------------
# Step 2: Visualization Tasks
# ----------------------------

# 1. Line Chart - Revenue over Months
plt.figure(figsize=(8, 5))
plt.plot(df["Month"], df["Revenue"], marker='o')
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()

# 2. Bar Chart - Profit for each Month
plt.figure(figsize=(8, 5))
plt.bar(df["Month"], df["Profit"], color=['red', 'green', 'blue', 'orange', 'purple', 
                                          'cyan', 'pink', 'yellow', 'brown', 'grey', 
                                          'teal', 'magenta'])
plt.title("Monthly Profit")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()

# 3. Grouped Bar Chart - Revenue vs Profit per Month
import numpy as np
x = np.arange(len(df["Month"]))
width = 0.35

plt.figure(figsize=(10, 6))
plt.bar(x - width/2, df["Revenue"], width, label="Revenue")
plt.bar(x + width/2, df["Profit"], width, label="Profit")
plt.xticks(x, df["Month"])
plt.title("Revenue vs Profit per Month")
plt.xlabel("Month")
plt.ylabel("Values")
plt.legend()
plt.show()

# 4. Pie Chart - Total Revenue contribution by Region
region_revenue = df.groupby("Region")["Revenue"].sum()
plt.figure(figsize=(6, 6))
plt.pie(region_revenue, labels=region_revenue.index, autopct='%1.1f%%', startangle=90)
plt.title("Revenue Contribution by Region")
plt.show()

# 5. Scatter Plot - Revenue vs Profit
plt.figure(figsize=(7, 5))
plt.scatter(df["Revenue"], df["Profit"], c='blue', marker='o')
plt.title("Revenue vs Profit")
plt.xlabel("Revenue")
plt.ylabel("Profit")
plt.grid(True)
plt.show()

# 6. Histogram - Distribution of Revenue values
plt.figure(figsize=(8, 5))
plt.hist(df["Revenue"], bins=6, edgecolor='black')
plt.title("Distribution of Revenue")
plt.xlabel("Revenue")
plt.ylabel("Frequency")
plt.show()

# 7. Box Plot - Profit across Regions
plt.figure(figsize=(7, 5))
df.boxplot(column="Profit", by="Region")
plt.title("Profit Distribution across Regions")
plt.suptitle("")  # remove default title
plt.xlabel("Region")
plt.ylabel("Profit")
plt.show()

# week2_data_processing.py
import pandas as pd
import numpy as np

# Load orders and delivery data from CSV exports (from MySQL)
orders = pd.read_csv("orders.csv")
delivery = pd.read_csv("delivery_status.csv")

# Merge datasets
df = pd.merge(orders, delivery, on="order_id", how="left")

# Convert dates
df['order_date'] = pd.to_datetime(df['order_date'])
df['delivery_date'] = pd.to_datetime(df['delivery_date'], errors='coerce')
df['estimated_date'] = pd.to_datetime(df['estimated_date'], errors='coerce')

# Fill missing issues
df.fillna({"delivery_status": "Pending"}, inplace=True)

# Calculate delay in days (if delivery exists)
df['delay_days'] = (df['delivery_date'] - df['estimated_date']).dt.days
df['delay_days'] = df['delay_days'].fillna(0).astype(int)

# Delayed flag
df['delayed'] = np.where(df['delay_days'] > 0, 1, 0)

# Insights
print("\nTop 5 Delayed Customers:")
print(df.groupby('customer_id')['delayed'].sum().sort_values(ascending=False).head(5))

print("\nMost Common Delivery Issues:")
print(df['delivery_status'].value_counts().head(5))

# Save cleaned dataset
df.to_csv("cleaned_orders.csv", index=False)

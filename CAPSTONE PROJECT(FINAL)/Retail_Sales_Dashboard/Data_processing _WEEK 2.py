import pandas as pd
import numpy as np

# 1. Load sales & product data (from CSVs exported from SQL)
sales = pd.read_csv("sales.csv")
products = pd.read_csv("products.csv")
stores = pd.read_csv("stores.csv")

# 2. Data Cleaning
# Remove duplicates
sales.drop_duplicates(inplace=True)

# Handle missing values
sales.fillna({'discount': 0, 'customer_name': 'Unknown'}, inplace=True)

# Correct data types
sales['sale_date'] = pd.to_datetime(sales['sale_date'])
sales['quantity'] = sales['quantity'].astype(int)

# 3. Feature Engineering
sales['revenue'] = sales['quantity'] * sales['total_amount'] / sales['quantity']  # total_amount is already post-discount
sales['discount_percent'] = (sales['discount'] / (sales['total_amount'] + sales['discount'])) * 100
sales['profit'] = sales['revenue'] * 0.2   # assume 20% margin
sales['profit_margin'] = (sales['profit'] / sales['revenue']) * 100

# 4. Summaries
# Revenue & profit by store
store_summary = sales.groupby('store_id')[['revenue', 'profit']].sum()

# Revenue by product
product_summary = sales.groupby('product_id')[['revenue', 'profit']].sum()

# 5. Save outputs
sales.to_csv("cleaned_sales.csv", index=False)
store_summary.to_csv("store_summary.csv")
product_summary.to_csv("product_summary.csv")

print("✅ Data cleaned and summaries generated.")
print(store_summary.head())

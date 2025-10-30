import pandas as pd
import numpy as np

# 1. Data Collection & Loading (from CSV files)
# --------------------------------------------------------------------------------
df_sales = pd.read_csv('sales.csv')
df_products = pd.read_csv('products.csv')

# Join dataframes on product_id
df = pd.merge(df_sales, df_products, on='product_id', how='left')


# 2. Data Cleaning Using Pandas
# --------------------------------------------------------------------------------
# Correct data types
df['sale_date'] = pd.to_datetime(df['sale_date'])

# Clean missing values: Fill NaNs in discount_pct_raw with 0 [cite: 18]
df['discount_pct_raw'] = df['discount_pct_raw'].fillna(0)


# 3. Calculations Using NumPy (Feature Engineering)
# --------------------------------------------------------------------------------
# Calculate revenue [cite: 19]
df['total_cost'] = df['quantity'] * df['cost']
df['revenue'] = (df['quantity'] * df['unit_price']) * (1 - df['discount_pct_raw'])

# Calculate profit margins [cite: 19]
df['profit'] = df['revenue'] - df['total_cost']
df['profit_margin'] = np.divide(
    df['profit'], 
    df['revenue'], 
    out=np.zeros_like(df['profit']), 
    where=df['revenue'] != 0
)


# 4. Summary and Saving Deliverables
# --------------------------------------------------------------------------------

# Show summary of total revenue by product and store [cite: 19] (Week 2 Deliverable)
summary = df.groupby(['store_id', 'product_name'])[['revenue', 'profit']].sum().reset_index()
print("WEEK 2 SUMMARY (Revenue and Profit by Store and Product):\n", summary)

# SAVE THE CLEANED DATA (Needed for Week 3 and Week 4) [cite: 25, 44]
df.to_csv('cleaned_sales_with_metrics.csv', index=False)
print("\nFILE SAVED: 'cleaned_sales_with_metrics.csv' (Cleaned dataset with calculated fields)")

# SAVE THE SUMMARY METRICS (Week 2/5 Deliverable) [cite: 26, 49, 53]
summary.to_csv('weekly_sales_summary.csv', index=False)
print("FILE SAVED: 'weekly_sales_summary.csv'")

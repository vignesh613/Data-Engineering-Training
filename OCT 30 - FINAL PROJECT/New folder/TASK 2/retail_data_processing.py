import pandas as pd
import numpy as np

# --- 1. DATA LOADING (SIMULATION) ---
# NOTE: Replace with pd.read_csv('sales.csv') or API call in a real project.
sales_data = {
    'product_id': [101, 102, 101, 103, 102, 104, 101, 103, 102, 105],
    'product_name': ['Mouse', 'Coffee Maker', 'Mouse', 'Cable', 'Coffee Maker', 'Lamp', 'Mouse', 'Cable', 'Coffee Maker', 'Webcam'],
    'sale_date': ['2023-09-01', '2023-10-05', '2023-11-01', '2023-10-10', '2023-10-20', '2023-10-25', '2023-11-01', '2023-11-05', '2023-11-15', '2023-11-20'],
    'quantity_sold': [10, 15, 25, 20, 8, 3, 25, 30, 12, 5],
    'unit_price': [25.00, 55.00, 25.00, 5.00, 55.00, 30.00, 25.00, 5.00, 55.00, 40.00],
    'total_amount': [250.00, 825.00, 625.00, 100.00, 440.00, 90.00, 625.00, np.nan, 660.00, 200.00],
    'region': ['West', 'East', 'West', 'North', 'East', np.nan, 'West', 'North', 'East', 'South']
}
df_sales = pd.DataFrame(sales_data)

inventory_data = {
    'product_id': [101, 102, 103, 104, 105],
    'initial_stock': [100, 50, 60, 20, 10],
    'current_stock': [40, 25, 10, 17, 5],
    'reorder_point': [15, 10, 50, 5, 2],
    'cost_of_goods': [15.00, 30.00, 2.00, 18.00, 25.00]
}
df_inventory = pd.DataFrame(inventory_data)

# --- 2. DATA CLEANING AND FORMATTING ---
df_sales['sale_date'] = pd.to_datetime(df_sales['sale_date'])
df_sales['total_amount'] = df_sales['total_amount'].fillna(
    df_sales['quantity_sold'] * df_sales['unit_price']
)
df_sales['region'] = df_sales['region'].fillna('Unknown')

# --- 3. CALCULATE METRICS ---

# Monthly Sales (Pandas GroupBy + NumPy Sum)
df_sales['sale_month'] = df_sales['sale_date'].dt.to_period('M')
monthly_sales = df_sales.groupby('sale_month')['total_amount'].apply(np.sum).reset_index()

# Inventory Turnover (NumPy Divide)
df_sales_merged = pd.merge(df_sales, df_inventory[['product_id', 'cost_of_goods']], on='product_id', how='left')
total_cogs = (df_sales_merged['quantity_sold'] * df_sales_merged['cost_of_goods']).sum()
avg_inventory = ((df_inventory['initial_stock'] + df_inventory['current_stock']).sum() / 2) * df_inventory['cost_of_goods'].mean()
inventory_turnover = np.divide(total_cogs, avg_inventory).round(2)


# --- 4. GENERATE REPORTS AND FINAL DELIVERABLE ---

product_summary = df_sales.groupby(['product_id', 'product_name']).agg(
    Total_Revenue=('total_amount', 'sum'),
    Total_Units_Sold=('quantity_sold', 'sum')
).reset_index()

# Top-Selling and Underperforming Reports
top_selling_products = product_summary.sort_values(by='Total_Revenue', ascending=False).head(3)
underperforming_products = product_summary.sort_values(by='Total_Units_Sold', ascending=True).head(2)

# Final Processed Dataset (Deliverable 2)
df_processed = pd.merge(
    product_summary, 
    df_inventory[['product_id', 'current_stock', 'reorder_point']], 
    on='product_id', 
    how='left'
)

# Inventory Status Flag
df_processed['Inventory_Status'] = np.where(
    df_processed['current_stock'] <= df_processed['reorder_point'],
    'CRITICAL_LOW_STOCK',
    'IN_STOCK'
)

# Export the final processed dataset
df_processed.to_csv('processed_sales_performance_dataset.csv', index=False)
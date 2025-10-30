import pandas as pd
import numpy as np
from datetime import datetime
import sys

# --- Configuration ---
INPUT_FILE = 'orders.csv'
CLEANED_OUTPUT_FILE = 'cleaned_orders.csv'  # Deliverable for Week 4 (Databricks)
SUMMARY_LOG_FILE = 'delay_summary.txt'    # Deliverable for Week 5 (Azure DevOps Log)

# --- 1. Load Data (from CSV) ---
try:
    # Use Python to load customer order data from an API or CSV [cite: 15, 16]
    df = pd.read_csv(INPUT_FILE)
    print(f"Successfully loaded data from {INPUT_FILE}.")
except FileNotFoundError:
    print(f"ERROR: Input file '{INPUT_FILE}' not found. Please create it first.", file=sys.stderr)
    sys.exit(1) # Exit if the required file is missing

# --- 2. Clean Missing Fields and Convert Timestamps ---
# Clean missing fields [cite: 16]
df['delivery_issue'].fillna('None', inplace=True)

# Convert timestamps [cite: 16]
df['order_date'] = pd.to_datetime(df['order_date'])
df['expected_delivery_date'] = pd.to_datetime(df['expected_delivery_date'])
df['actual_delivery_date'] = pd.to_datetime(df['actual_delivery_date'])

# --- 3. Calculate Delivery Delays using NumPy ---
# Calculate delay days: actual delivery time minus expected delivery time
# Note: For orders still 'Shipped' (like Order 10), actual_delivery_date is NaT, resulting in NaN delay_days.
df['delay_days'] = (df['actual_delivery_date'] - df['expected_delivery_date']).dt.days

# Use NumPy to calculate delivery delays [cite: 17]
# Create 'delayed' flag: 1 if delayed (delay_days > 0), 0 otherwise.
df['delayed'] = np.where(df['delay_days'] > 0, 1, 0)

# --- 4. Generate Insights and Print Summary ---

# a) Show top delayed customers [cite: 18]
delay_summary_by_customer = df.groupby('customerid')['delayed'].sum().sort_values(ascending=False)

# b) Show most common delivery issues [cite: 18]
common_issues = df[df['delivery_issue'] != 'None']['delivery_issue'].value_counts().head(5)

# Print the required summary (Python script that prints delay summary by customer )
print("\n--- Top Delayed Customers (Total Delayed Orders) ---")
print(delay_summary_by_customer.to_string())
print("\n--- Most Common Delivery Issues (Excluding 'None') ---")
print(common_issues.to_string())

# --- 5. Deliverables: Saving Outputs ---

# a) Save Cleaned and Processed Dataset (Deliverable for Week 4)
# Save the cleaned and processed order dataset 
df.to_csv(CLEANED_OUTPUT_FILE, index=False)
print(f"\n✅ Cleaned dataset saved for Week 4 to: {CLEANED_OUTPUT_FILE}")

# b) Save Delay Summary Log (Deliverable for Week 5)
# Log delay summary to a file 
with open(SUMMARY_LOG_FILE, 'w') as f:
    f.write(f"Run Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    f.write("--- Top Delayed Customers (Total Delayed Orders) ---\n")
    f.write(delay_summary_by_customer.to_string())
    f.write("\n\n--- Most Common Delivery Issues (Excluding 'None') ---\n")
    f.write(common_issues.to_string())

# Send a basic success notification (print/log) [cite: 49]
print(f"✅ Delay summary log saved for Week 5 to: {SUMMARY_LOG_FILE}")
print("\nPython analysis completed successfully.")
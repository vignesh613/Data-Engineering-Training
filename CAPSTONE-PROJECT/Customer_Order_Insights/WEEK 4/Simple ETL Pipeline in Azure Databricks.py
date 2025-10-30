from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# --- 0. Configuration ---
# Input path remains the same
INPUT_PATH = "/FileStore/tables/cleaned_orders.csv"
# OUTPUT_PATH is now set to an accessible folder in FileStore for easy download
OUTPUT_PATH = "/FileStore/final_delivery_status_csv_output"

# SparkSession is typically pre-configured in Databricks

# --- 1. Load Data (Extract) ---
order_df = spark.read.csv(INPUT_PATH, header=True, inferSchema=True)
print(f"Loaded {order_df.count()} records from {INPUT_PATH}.")
order_df.createOrReplaceTempView("orders_staging")

# --- 2. Create ETL Pipeline (Transform) ---
# Logic remains the same: update latest delivery status
latest_status_df = spark.sql("""
    SELECT
        *,
        CASE
            WHEN delayed = 1 AND actual_delivery_date IS NULL THEN 'CRITICAL DELAY'
            WHEN delayed = 1 THEN 'RESOLVED DELAY'
            WHEN actual_delivery_date IS NOT NULL THEN 'DELIVERED'
            ELSE 'SHIPPED/PENDING'
        END AS latest_status
    FROM
        orders_staging
""")

# --- 3. Save Results (Load as CSV) ---
# Task: Save the results as CSV 
# coalesce(1) writes the entire DataFrame to a single CSV file inside the folder
latest_status_df.coalesce(1).write.mode("overwrite").csv(OUTPUT_PATH, header=True)
print(f"✅ ETL Pipeline completed. Results saved as a single CSV in folder: {OUTPUT_PATH}")

# --- 4. Optional: Run SQL Query ---
print("\n--- Top 5 Delayed Customers (using Spark SQL) ---")
spark.sql("""
    SELECT
        customerid,
        SUM(delayed) AS TotalDelayedOrders
    FROM
        orders_staging
    GROUP BY
        customerid
    ORDER BY
        TotalDelayedOrders DESC
    LIMIT 5
""").show()
from pyspark.sql import SparkSession
from pyspark.sql.functions import count, col

# --- 0. Setup ---
# Initialize Spark Session (if needed, e.g., on a local machine)
# In Azure Databricks, this step is often automatic.
spark = SparkSession.builder.appName("PySparkOrderAnalysis").getOrCreate()

# --- 1. Load Data ---
# Load cleaned order data into PySpark (using Week 2 output) [cite: 30]
orders_df = spark.read.csv("cleaned_orders.csv", header=True, inferSchema=True)

# Load customer data
customers_df = spark.read.csv("customers.csv", header=True, inferSchema=True)

# --- 2. Join and Filter ---
# Join orders and customer tables [cite: 31]
joined_df = orders_df.join(customers_df, "customerid", "inner")

# Filter for only delayed orders (where the 'delayed' flag is 1)
delayed_orders_df = joined_df.filter(col("delayed") == 1)

# --- 3. Group and Aggregate ---
# Group by region to count delays [cite: 32]
regional_delays_df = delayed_orders_df.groupBy("region").agg(
    count(col("orderid")).alias("TotalDelayedOrders")
).sort(col("TotalDelayedOrders").desc())

# --- 4. Save Results (Deliverable) ---
# Save results to a file (Output file showing delayed orders by region) [cite: 33, 35]
output_path = "delayed_orders_by_region_output"
# coalesce(1) is used to save output into a single CSV file inside the folder
regional_delays_df.coalesce(1).write.mode("overwrite").csv(
    output_path,
    header=True
)

# Optional: Show the result and confirmation
print("--- Delayed Orders by Region ---")
regional_delays_df.show()
print(f"✅ Output file showing delayed orders by region saved to: {output_path}")

# Stop Spark session
spark.stop()
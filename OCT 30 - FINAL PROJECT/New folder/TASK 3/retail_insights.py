from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, count
import pandas as pd

# 1. Initialize Spark Session
spark = SparkSession.builder \
    .appName("RetailInsightsPySpark") \
    .getOrCreate()

# 2. Load Data (Simulation)
sales_data_pd = pd.DataFrame({
    'product_id': [101, 102, 101, 103, 102, 104, 101, 103],
    'total_amount': [250.00, 275.00, 375.00, 100.00, 440.00, 90.00, 625.00, 150.00],
    'quantity_sold': [10, 5, 15, 20, 8, 3, 25, 30],
    'region': ['West', 'East', 'West', 'North', 'East', 'South', 'West', 'North'],
    'category': ['Electronics', 'Appliances', 'Electronics', 'Electronics', 'Appliances', 'Home Goods', 'Electronics', 'Electronics']
})
df_sales = spark.createDataFrame(sales_data_pd)

inventory_data_pd = pd.DataFrame({
    'product_id': [101, 102, 103, 104],
    'current_stock': [40, 25, 10, 17]
})
df_inventory = spark.createDataFrame(inventory_data_pd)


# 3. Join Data
df_joined = df_sales.join(
    df_inventory, 
    on='product_id', 
    how='left'
)

# 4. Aggregation and Analysis (Group by Category and Region)
df_aggregated = df_joined.groupBy(
    col("category"), 
    col("region")
).agg(
    sum("total_amount").alias("Total_Revenue"),
    sum("quantity_sold").alias("Total_Units_Sold"),
    count("*").alias("Number_of_Transactions")
).sort(
    col("Total_Revenue").desc()
)

# Show Results (Optional, for console output)
df_aggregated.show()

# 5. Export Deliverable
# NOTE: The output will be a directory with part files.
output_path = "category_sales_by_region.csv"
df_aggregated.write.csv(output_path, header=True, mode="overwrite")

# 6. Stop Spark Session
spark.stop()
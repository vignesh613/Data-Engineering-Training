from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, count

# Initialize Spark
spark = SparkSession.builder.appName("OrderAnalysis").getOrCreate()

# Load CSV exports (from Week 1 MySQL)
customers = spark.read.csv("customers.csv", header=True, inferSchema=True)
orders = spark.read.csv("orders.csv", header=True, inferSchema=True)
delivery = spark.read.csv("delivery_status.csv", header=True, inferSchema=True)

# Join orders with customers
orders_customers = orders.join(customers, on="customer_id", how="inner")

# Join with delivery status
full_data = orders_customers.join(delivery, on="order_id", how="left")

# Add delayed flag
full_data = full_data.withColumn(
    "delayed",
    when(col("delivery_date") > col("estimated_date"), 1).otherwise(0)
)

# Group by region (city, state) to count delays
delays_by_region = (
    full_data.groupBy("city", "state")
    .agg(count(when(col("delayed") == 1, True)).alias("delayed_orders"))
)

# Show results
delays_by_region.show(truncate=False)

# Save output
delays_by_region.coalesce(1).write.csv("delays_by_region_output", header=True, mode="overwrite")

spark.stop()

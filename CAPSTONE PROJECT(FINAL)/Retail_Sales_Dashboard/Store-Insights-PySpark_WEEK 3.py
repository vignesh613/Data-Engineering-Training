from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, avg, month

# 1. Start Spark
spark = SparkSession.builder.appName("RetailStoreInsights").getOrCreate()

# 2. Load cleaned sales data (from Week 2)
df = spark.read.csv("cleaned_sales.csv", header=True, inferSchema=True)

# 3. Identify underperforming products (low sales or high discounts)
underperforming = df.groupBy("product_id") \
    .agg(
        _sum("quantity").alias("total_quantity"),
        avg("discount_percent").alias("avg_discount")
    ) \
    .filter((col("total_quantity") < 5) | (col("avg_discount") > 10))

# 4. Store-level monthly revenue
monthly_store = df.withColumn("month", month("sale_date")) \
    .groupBy("store_id", "month") \
    .agg(
        avg("revenue").alias("avg_monthly_revenue")
    ) \
    .orderBy("store_id", "month")

# 5. Save outputs
underperforming.write.csv("underperforming_products.csv", header=True, mode="overwrite")
monthly_store.write.csv("monthly_store_revenue.csv", header=True, mode="overwrite")

print("✅ PySpark insights generated.")

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, month, year

# 1. Initialize Spark Session and Load Data
# --------------------------------------------------------------------------------
# Create the Spark Session
spark = SparkSession.builder.appName("RetailSalesInsights").getOrCreate()

# Load the cleaned CSV file from Week 2
# NOTE: File name must match the uploaded file.
sales_df = spark.read.csv("cleaned_sales_with_metrics.csv", header=True, inferSchema=True)

# Ensure sale_date is treated as a date for monthly grouping
sales_df = sales_df.withColumn("sale_date", col("sale_date").cast("date"))
sales_df = sales_df.withColumn("sale_month", month(col("sale_date")))
sales_df = sales_df.withColumn("sale_year", year(col("sale_date")))


# 2. Filter for Underperforming Products (Example Logic)
# --------------------------------------------------------------------------------
# Identify products with low revenue (e.g., less than $1000) AND negative margin

product_summary = sales_df.groupBy("product_name").agg(
    sum("revenue").alias("Total_Revenue"),
    avg("profit_margin").alias("Avg_Profit_Margin")
)

# Filter for underperformers
underperforming_list = product_summary.filter(
    (col("Total_Revenue") < 1000) & (col("Avg_Profit_Margin") < 0)
)
underperforming_list.show(truncate=False)


# 3. Group by Store and Calculate Average Monthly Revenue
# --------------------------------------------------------------------------------
# Calculate total monthly revenue per store
monthly_revenue = sales_df.groupBy("store_id", "sale_year", "sale_month").agg(
    sum("revenue").alias("Monthly_Revenue_Total")
)

# Calculate the average of the monthly revenue totals per store
store_avg_monthly_revenue = monthly_revenue.groupBy("store_id").agg(
    avg("Monthly_Revenue_Total").alias("Average_Monthly_Revenue")
).sort(col("Average_Monthly_Revenue").desc())

store_avg_monthly_revenue.show()


# 4. Deliverables: Save Output Files
# --------------------------------------------------------------------------------
# PySpark writes files into folders, not single CSVs.

# Save the PySpark script output for store summary (Week 3 Deliverable)
store_avg_monthly_revenue.coalesce(1).write.mode("overwrite").csv(
    "pyspark_store_summary", 
    header=True
)

# Save the underperforming products list
underperforming_list.coalesce(1).write.mode("overwrite").csv(
    "pyspark_underperforming_products", 
    header=True
)

# Stop the Spark session (Good practice in Colab)
spark.stop()

print("\nWEEK 3 COMPLETE. Output files are saved in the Colab file explorer under the 'pyspark_store_summary/' and 'pyspark_underperforming_products/' folders.")
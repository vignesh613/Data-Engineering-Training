from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, max, min, count, sum, desc

# Step 1: Create Spark Session
spark = SparkSession.builder.appName("DataFrame-Exercises").getOrCreate()

# Customers Data
customers_data = [
    (1, "Rahul Sharma", "Bangalore", 28),
    (2, "Priya Singh", "Delhi", 32),
    (3, "Aman Kumar", "Hyderabad", 25),
    (4, "Sneha Reddy", "Chennai", 35),
    (5, "Arjun Mehta", "Mumbai", 30),
    (6, "Divya Nair", "Delhi", 29)
]
customers_cols = ["customer_id", "name", "city", "age"]
customers_df = spark.createDataFrame(customers_data, customers_cols)

# Orders Data
orders_data = [
    (101, 1, "Laptop", 55000),
    (102, 2, "Mobile", 25000),
    (103, 1, "Headphones", 3000),
    (104, 3, "Chair", 5000),
    (105, 5, "Book", 700),
    (106, 2, "Tablet", 20000),
    (107, 6, "Shoes", 2500),
    (108, 7, "Camera", 30000)  # Order with non-existent customer
]
orders_cols = ["order_id", "customer_id", "product", "amount"]
orders_df = spark.createDataFrame(orders_data, orders_cols)

customers_df.show()
orders_df.show()

# ----------------------------
# Step 2: Exercises
# ----------------------------

# Basic Operations
# 1. Select only name and city
customers_df.select("name", "city").show()

# 2. Filter customers older than 30
customers_df.filter(col("age") > 30).show()

# 3. Count customers from Delhi
customers_df.filter(col("city") == "Delhi").count()

# 4. Find distinct cities
customers_df.select("city").distinct().show()

# Aggregations
# 5. Average age of customers
customers_df.agg(avg("age")).show()

# 6. Max & Min order amount
orders_df.agg(max("amount"), min("amount")).show()

# 7. Number of orders placed by each customer
orders_df.groupBy("customer_id").agg(count("order_id").alias("order_count")).show()

# 8. Total spending of each customer
orders_df.groupBy("customer_id").agg(sum("amount").alias("total_spend")).show()

# Joins
# 9. Inner join between customers & orders
customers_df.join(orders_df, "customer_id", "inner").show()

# 10. Left join (all customers, even without orders)
customers_df.join(orders_df, "customer_id", "left").show()

# 11. Customers who never placed an order
customers_df.join(orders_df, "customer_id", "left") \
    .filter(orders_df["order_id"].isNull()).show()

# 12. Orders with non-existent customers
orders_df.join(customers_df, "customer_id", "left") \
    .filter(customers_df["name"].isNull()).show()

# Sorting & Grouping
# 13. Customers ordered by age (descending)
customers_df.orderBy(col("age").desc()).show()

# 14. Top 3 highest order amounts
orders_df.orderBy(col("amount").desc()).limit(3).show()

# 15. Group customers by city and find average age
customers_df.groupBy("city").agg(avg("age").alias("avg_age")).show()

# 16. Group orders by product and find total sales
orders_df.groupBy("product").agg(sum("amount").alias("total_sales")).show()

# SQL Operations
# 17. Register DataFrames as temp views
customers_df.createOrReplaceTempView("customers")
orders_df.createOrReplaceTempView("orders")

# 18. SQL - Total revenue by city
spark.sql("""
    SELECT c.city, SUM(o.amount) AS total_revenue
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY c.city
""").show()

# 19. SQL - Top 2 customers by total spend
spark.sql("""
    SELECT c.name, SUM(o.amount) AS total_spend
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY c.name
    ORDER BY total_spend DESC
    LIMIT 2
""").show()

# 20. SQL - Customers who bought products worth more than 20,000
spark.sql("""
    SELECT c.name, SUM(o.amount) AS total_spend
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY c.name
    HAVING SUM(o.amount) > 20000
""").show()

import csv
import json
from collections import defaultdict
from product import Product
from order import Order
from customer import Customer


# ===== CSV Handling =====

def load_products(filename="products.csv"):
    products = {}
    with open(filename, mode="r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            product = Product(row["id"], row["name"], row["category"], row["price"], row["stock"])
            products[int(row["id"])] = product   # ✅ store with int key
    return products



def save_products(products, filename="products.csv"):
    with open(filename, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "category", "price", "stock"])
        for p in products.values():
            writer.writerow([p.id, p.name, p.category, p.price, p.stock])


# ===== JSON Handling =====

def load_orders(filename, products, customers):
    orders = []
    with open(filename, "r") as f:
        data = json.load(f)

    for o in data:
        customer_name = o["customer"]
        if customer_name not in customers:
            customers[customer_name] = Customer(customer_name)

        customer = customers[customer_name]
        order = Order(o["order_id"], customer)

        for item in o["items"]:
            product_id = int(item["product_id"])  # ✅ force int
            qty = int(item["qty"])

            if product_id not in products:
                print(f"⚠️ Warning: Product ID {product_id} not found in products.csv")
                continue

            product = products[product_id]
            order.add_item(product, qty)

        orders.append(order)
        customer.add_order(order)

    return orders



def save_orders(orders, filename="orders.json"):
    data = []
    for o in orders:
        order_data = {
            "order_id": o.order_id,
            "customer": o.customer.name,
            "items": [{"product_id": p.id, "qty": qty} for p, qty in o.items]
        }
        data.append(order_data)
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)


# ===== Reports =====

def generate_sales_report(customers):
    total_revenue = sum(c.total_spent() for c in customers.values())

    revenue_by_category = defaultdict(float)
    for c in customers.values():
        for o in c.orders:
            for p, qty in o.items:
                revenue_by_category[p.category] += p.price * qty

    top_customer = max(customers.values(), key=lambda c: c.total_spent())

    print("\n📊 Sales Report")
    print(f"Total Revenue: ₹{total_revenue}")
    print("Revenue by Category:")
    for cat, rev in revenue_by_category.items():
        print(f" - {cat}: ₹{rev}")
    print(f"Top Customer: {top_customer.name} (Spent ₹{top_customer.total_spent()})")


def generate_inventory_report(products):
    print("\n📦 Inventory Report")
    low_stock = [p for p in products.values() if p.stock < 5]
    if low_stock:
        print("Low Stock Products (<5):")
        for p in low_stock:
            print(f" - {p.name}: {p.stock} left")
    else:
        print("No low stock products.")

    avg_price = defaultdict(list)
    for p in products.values():
        avg_price[p.category].append(p.price)
    print("Average Price by Category:")
    for cat, prices in avg_price.items():
        print(f" - {cat}: ₹{sum(prices)/len(prices):.2f}")

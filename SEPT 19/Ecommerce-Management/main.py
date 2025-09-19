from utils import load_products, save_products, load_orders, save_orders, generate_sales_report, generate_inventory_report
from customer import Customer
from order import Order


def menu(products, customers, orders):
    while True:
        print("\n===== E-Commerce Menu =====")
        print("1. View Products")
        print("2. Place New Order")
        print("3. View All Orders")
        print("4. Generate Reports")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            print("\nAvailable Products:")
            for p in products.values():
                print(p)

        elif choice == "2":
            name = input("Enter customer name: ")
            customer = customers.get(name, Customer(name))
            customers[name] = customer

            order_id = max([o.order_id for o in orders], default=100) + 1
            order = Order(order_id, customer)

            while True:
                try:
                    pid = int(input("Enter product id (0 to finish): "))
                    if pid == 0:
                        break
                    qty = int(input("Enter quantity: "))
                    if pid in products:
                        order.add_item(products[pid], qty)
                except ValueError:
                    print("❌ Invalid input, try again.")

            if order.items:
                customer.add_order(order)
                orders.append(order)
                save_orders(orders)
                save_products(products)
                print(f"✅ Order placed! Total = ₹{order.get_total()}")

        elif choice == "3":
            print("\nAll Orders:")
            for o in orders:
                print(o)

        elif choice == "4":
            generate_sales_report(customers)
            generate_inventory_report(products)

        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    products = load_products("products.csv")
    customers = {}
    orders = load_orders("orders.json", products, customers)

    menu(products, customers, orders)

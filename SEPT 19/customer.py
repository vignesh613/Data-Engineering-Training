class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def total_spent(self):
        return sum(order.get_total() for order in self.orders)

    def __repr__(self):
        return f"Customer({self.name}, Orders={len(self.orders)})"

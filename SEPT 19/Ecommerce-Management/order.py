class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.items = []  # list of (Product, qty)

    def add_item(self, product, qty):
        if product.update_stock(qty):
            self.items.append((product, qty))

    def get_total(self):
        return sum(product.price * qty for product, qty in self.items)

    def __repr__(self):
        return f"Order({self.order_id}, Customer={self.customer.name}, Total=₹{self.get_total()})"

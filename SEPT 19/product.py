class Product:
    def __init__(self, product_id, name, category, price, stock):
        self.id = int(product_id)
        self.name = name
        self.category = category
        self.price = float(price)
        self.stock = int(stock)

    def update_stock(self, qty):
        if qty <= self.stock:
            self.stock -= qty
            return True
        else:
            print(f"❌ Not enough stock for {self.name}. Available: {self.stock}")
            return False

    def __repr__(self):
        return f"{self.id}. {self.name} ({self.category}) - ₹{self.price} | Stock: {self.stock}"

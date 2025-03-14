class Cart:
    def __init__(self):
        self.cart_items = []
    
    def add_to_cart(self, product):
        self.cart_items.append(product)
    
    def calculate_total(self):
        total = sum(item.price * item.quantity for item in self.cart_items)
        return total
    
    def display_cart(self):
        for item in self.cart_items:
            item.display_info()

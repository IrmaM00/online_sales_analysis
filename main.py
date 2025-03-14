from product import Product
from product_manager import ProductManager
from cart import Cart

# Kreirajte instancu ProductManager
manager = ProductManager()

# Dodajte proizvode
product1 = Product("Laptop", 1000, 5)
product2 = Product("Phone", 700, 10)
product3 = Product("Headphones", 150, 15)


manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)

# Prikaz proizvoda i ukupne vrednosti inventara

manager.display_products()
print("Total inventory value:", manager.total_inventory_value())

# Kreiranje instance za Cart
cart = Cart()

# Dodavanje proizvoda u korpu

cart.add_to_cart(manager.products[0])
cart.add_to_cart(manager.products[1])
cart.add_to_cart(manager.products[2])
cart.add_to_cart(manager.products[3])

# Prikaz korpe i ukupne vrednosti 

cart.display_cart()
print(f"Ukupna vrednost korpe: {cart.calculate_total()}")
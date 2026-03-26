# Step 1: Define Product class
class Product:
    def __init__(self, name, price):
        self.name = name # Name of the product
        self.price = price # Price of the product


# Step 2: Define ShoppingCart class
class ShoppingCart:
    def __init__(self):
        self.items = [] # List to store products added to cart

    # Method to add a product to cart
    def add_item(self, product):
        self.items.append(product)
        print(f"{product.name} added to cart")

    # Method to calculate total price and show cart items
    def show_cart(self):
        if not self.items:
            print("Cart is empty")
        return

        total = 0
        print("\nCart Items:")
    
        for item in self.items:
            print(f"{item.name} - ₹{item.price}")
            total += item.price
        print(f"Total Price = ₹{total}")


# Step 3: Main Program
# Create some products
p1 = Product("Laptop", 50000)
p2 = Product("Phone", 20000)
p3 = Product("Headphones", 2000)

# Create a shopping cart
cart = ShoppingCart()

# Add products to the cart
cart.add_item(p1) # Add Laptop
cart.add_item(p3) # Add Headphones

# Show cart contents and total
cart.show_cart()

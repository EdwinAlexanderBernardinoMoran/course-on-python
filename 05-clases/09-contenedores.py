class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}"
    
class Category:

    def __init__(self, name, products):
        self.name = name
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def print_products(self):
        for product in self.products:
            print(product)

football = Product("Football", 25.99)
basketball = Product("Basketball", 29.99)
tennis = Product("Tennis", 19.99)

sports = Category("Sports", [football, basketball])
sports.add_product(tennis)
sports.print_products()
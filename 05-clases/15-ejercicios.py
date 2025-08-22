# 1 Caja registradora

class CashRegister:

    def __init__(self):
        self.products = []

    def add_product(self, product, price):
        self.products.append({'name': product, 'price': price})

    def calculate_total(self):
        return sum(product['price'] for product in self.products)

    def calculate_change(self, payment):
        if payment < self.calculate_total():
            print("Insufficient payment.")
            return
        change = payment - self.calculate_total()
        self.products = []
        return change


    def get_list(self):
        # print(self.products)
        return self.products

# products = CashRegister()

# products.add_product("Manzana", 0.5)
# products.add_product("Pan", 1.0)

# products.get_list()

# products.calculate_change(2)
# products.get_list()

# 2 Caja registradora y cuentas.

class Accounts:

    def __init__(self):
        self.acounts = []

    def add_acount(self, cash_register):
        list_products = cash_register.get_list()
        total = cash_register.calculate_total()
        self.acounts.append({'products': list_products, 'total': total})

    def get_acounts(self):
        return sum(acount['total'] for acount in self.acounts)

    def average_ticket(self):
        if not self.acounts:
            return 0
        return self.get_acounts() / len(self.acounts)

    def get_list(self):
        return self.acounts
    
cash = CashRegister()
register_acount = Accounts()

# cash.add_product("Manzana", 0.5)
# print("Total: ", cash.calculate_total())
# cash.add_product("Pan", 1.0)
# print(cash.get_list())

# print("Total: ", cash.calculate_total())
# register_acount.add_acount(cash)
# print("Change: ", cash.calculate_change(2.0))
# print(cash.get_list())

# cash.add_product("Leche", 1.5)
# print("Total: ", cash.calculate_total())
# register_acount.add_acount(cash)
# print("Change: ", cash.calculate_change(3.0))
# print(cash.get_list())

# cash.add_product("Hueavos", 2.0)
# cash.add_product("Queso", 3.0)
# cash.add_product("Jamon", 4.0)
# cash.add_product("Pan", 1.0)
# print("Total: ", cash.calculate_total())
# register_acount.add_acount(cash)
# print("Change: ", cash.calculate_change(10.0))


# tickets = register_acount.average_ticket()
# cut_of_the_day = register_acount.get_acounts()
# counts = register_acount.get_list()

# print("Accounts of the day: ", counts)
# print(f"The average ticket for the day is: {tickets}")
# print(f"The total of sales for the day is: {cut_of_the_day}")


# 3 Jerarquia de clases para vehiculos

class Vehicle:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def description(self):
        return {"Marca": self.brand, "Modelo": self.model}
    
class Auto(Vehicle):
    def description(self):
        return f"Auto - {super().description()}";

class Moto(Vehicle):
    def description(self):
        return f"Moto - {super().description()}";

class Bicicleta(Vehicle):
    def description(self):
        return f"Bicicleta - {super().description()}";

auto = Auto("Toyota", "Corolla")
moto = Moto("Yamaha", "MT-07")
bicicleta = Bicicleta("Giant", "Escape 3")

print(auto.description())
print(moto.description())
print(bicicleta.description())
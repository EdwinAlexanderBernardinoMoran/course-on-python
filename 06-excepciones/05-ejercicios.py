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
            raise ValueError("Insufficient payment.")
        change = payment - self.calculate_total()
        self.products = []
        return change

    def get_list(self):
        # print(self.products)
        return self.products
    
# try:
#     products = CashRegister()
#     products.add_product("Manzana", 0.5)
#     products.add_product("Pan", 1.0)

#     print(products.get_list())
#     print("Cambio: ", products.calculate_change(1))
#     print(products.get_list())
# except ValueError as e:
#     print(e)

# ClASE DE CUENTA BANCARIA

class ErrorWithdrawal(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code

class BankAccount:
    def __init__(self, numberAccount, name, balance = 0):
        self.numberAccount = numberAccount
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ErrorWithdrawal("Deposit amount must be positive.", 400)
        self.balance += amount
        print("Deposit successful.")

    def showBalance(self):
        return self.balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ErrorWithdrawal("The amount to be withdrawn must be positive.", 400)

        if amount > self.balance:
            raise ErrorWithdrawal("Insufficient funds.", 403)
        self.balance -= amount
        print("Withdrawal successful.")
    
try:
    bankAccount = BankAccount("123456", "John Doe", 1000)
    bankAccount.deposit(500)
    print("Current Balance: ", bankAccount.showBalance())
    bankAccount.withdraw(-600)
    print("Current Balance: ", bankAccount.showBalance())
except ErrorWithdrawal as e:
    print(f"Error {e.code}: {e.message}")
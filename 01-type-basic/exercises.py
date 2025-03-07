# Ejercicio 1: Conversor de temperaturas
# Conversion de grados Celsius a grados Fahrenheit y Kelvin

number_celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Conversion a grados Fahrenheit
number_fahrenheit = (number_celsius * 9/5) + 32
print(f"{number_celsius} grados Celsius son {number_fahrenheit} grados Fahrenheit")

# Conversion a grados Kelvin
number_kelvin = number_celsius + 273.15
print(f"{number_celsius} grados Celsius son {number_kelvin} grados Kelvin")








# Ejercicio 2 : Conversor de monedas
money_local = float(input("Ingrese la cantidad de dinero en su moneda local: "))

dollar = money_local * 0.050
eur = money_local * 0.047
gbp = money_local * 0.039
jpy = money_local * 7.71

print(f"Usted tiene {dollar} dolares")
print(f"Usted tiene {eur} euros")
print(f"Usted tiene {gbp} libras esterlinas")
print(f"Usted tiene {jpy} yenes japoneses")








# Ejercicio 3: Calculadora de cambio
amount_of_money = float(input("Ingrese la cantidad de dinero entregada por el cliente: "))
price_of_product = float(input("Ingrese el precio del producto: "))

change = amount_of_money - price_of_product
print(f"El cambio que se le debe dar al cliente es de {change} pesos")








# Ejercicio 4: Formateador de nombres
firtName = input("Ingrese su primer nombre: ").strip().capitalize()
middleName = input("Ingrese su segundo nombre: ").strip().capitalize()
lastName = input("Ingrese su primer apellido: ").strip().capitalize()
secondSurname = input("Ingrese su segundo apellido: ").strip().capitalize()

print(f"Su nombre completo es: {firtName} {middleName} {lastName} {secondSurname}")

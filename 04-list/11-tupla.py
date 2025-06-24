numbers = (1, 2, 3) + (4, 5, 6)  # Concatenación de tuplas
print(numbers)

point = tuple([1, 2])  # Creación de una tupla a partir de una lista
print(point)

# Desempaquetado de tuplas
firt, second, *others = numbers
print(firt, second, others)

# Iteración de tuplas
for number in numbers:
    print(number)

# Conversión de tupla a lista
list_numbers = list(numbers)
list_numbers[0] = 'Developers'
print(list_numbers)
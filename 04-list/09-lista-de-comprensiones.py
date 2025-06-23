users = [
    ["John", 30],
    ["Jane", 25],
    ["Alice", 28],
    ["Bob", 22]
]

names = []

# TRANSFORMACIÓN DE LISTAS
# Forma 1: Using a for loop to extract names
for user in users:
    names.append(user[0])

print(names)

# Forma 2: Using list comprehension to extract names
namesTwo = [user[0] for user in users]
print(namesTwo)


# *******************************************************

# FILTRADO DE LISTAS
namesThree = [user for user in users if user[1] > 23]

# FILTRADO Y TRANSFORMACIÓN DE LISTAS
namesFour = [user[0] for user in users if user[1] > 23]

print(namesThree)
print(namesFour)
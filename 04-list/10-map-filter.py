users = [
    ["John", 30],
    ["Jane", 25],
    ["Alice", 28],
    ["Bob", 22]
]

names = []
names = list(map(lambda user: user[0], users))  # Using map to extract names

# Forma 2: Using list comprehension to extract names
namesTwo = [user[0] for user in users]


# *******************************************************


# FILTRADO DE LISTAS
namesThree = [user for user in users if user[1] > 23] # Retorna los usuarios con id mayor a 23
nameWithFilter = list(filter(lambda user: user[1] > 23, users))  # Si evalue en True devulve el elemento

# FILTRADO Y TRANSFORMACIÓN DE LISTAS
namesFour = [user[0] for user in users if user[1] > 23]


print(names)
print(nameWithFilter)
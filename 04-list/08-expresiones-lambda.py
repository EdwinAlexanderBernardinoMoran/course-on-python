users = [
    ["John", 30],
    ["Jane", 25],
    ["Alice", 28],
    ["Bob", 22]
]

users.sort(key=lambda element:element[1])  # Ordena por edad en orden descendente
print(users)
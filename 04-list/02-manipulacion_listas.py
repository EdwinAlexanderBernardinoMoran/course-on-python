mascotas = ['Wolfgan', 'Pelusa', 'Pulga', 'Copito']
print(mascotas[0])

mascotas[0] = 'Lobo'
print(mascotas)  # Loboc
print(mascotas[0:3])  # ['Lobo', 'Pelusa', 'Pulga']
print(mascotas[:3])  # ['Lobo', 'Pelusa', 'Pulga']
print(mascotas[2:]) # ['Pulga', 'Copito']
print(mascotas[-1])  # Copito
print(mascotas[::2])  # ['Lobo', 'Pulga']
print(mascotas[1::2])  # ['Pelusa', 'Copito']

numbers = list(range(21))
print(numbers)

# Numeros pares
print(numbers[::2])

# Numeros inpares
print(numbers[1::2])
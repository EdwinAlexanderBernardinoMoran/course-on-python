# Operador desempaquetador (*) de listas
lista = [1, 2, 3, 4, 5]

print(1, 2, 3, 4, 5)
print(*lista)

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

combinada = ["Example", *lista1, "python", *lista2]
print(combinada)

# Operador desempaquetador (**) de diccionarios
diccionario1 = {"a": 1, "b": 2}
diccionario2 = {"b": 3, "d": 4}

combinado = {**diccionario1, **diccionario2, "c": 5}
print(combinado)

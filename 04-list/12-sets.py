numbers = {1, 1, 2, 2, 3, 4}
print(numbers)  # Output: {1, 2, 3, 4}

# numbers.add(5)
# numbers.remove(1)
# print(numbers)  # Output: {2, 3, 4, 5}

lists = [3, 4, 5]
lists = set(lists)
print(lists)  # Output: {1, 2, 3, 4

# *****************************************************

# OPERADORES PARA LOS SETS

print( numbers | lists )  # Unión: {1, 2, 3, 4, 5}, Se encarga de hacer una unión entre dos sets y elimina los duplicados
print( numbers & lists )  # Intersección: {3, 4}, Se encarga de encontrar los elementos que están en ambos sets
print( numbers - lists )  # Diferencia: {1, 2}, Se encarga de encontrar los elementos que están en el primer set pero no en el segundo.
print( numbers ^ lists )  # Diferencia simétrica: {1, 2, 5}, Se encarga de encontrar los elementos que están en uno de los sets pero no en ambos
print( numbers == lists )  # Igualdad: False, Se encarga de comparar si los sets son iguales
print( numbers != lists )  # Desigualdad: True, Se encarga de comparar si los sets son diferentes


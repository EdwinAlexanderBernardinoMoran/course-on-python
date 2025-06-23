mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito Feliz"]

# Agregar elementos a una lista
mascotas.insert(2, "Gato con Botas")
mascotas.append("Firulais")
print(mascotas)  # ['Pelusa', 'Pulga', 'Gato con Botas', 'Felipe', 'Chanchito Feliz']

# Eliminar elementos de una lista
mascotas.remove("Pulga")
mascotas.pop(3)  # Elimina el elemento en la posición 3 si no recibe un argumento elimina el último
del mascotas[1]
mascotas.clear()  # Elimina todos los elementos de la lista
print(mascotas)  # ['Pelusa', 'Gato con Botas', 'Chanchito Feliz']
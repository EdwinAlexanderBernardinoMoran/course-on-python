animal = " ChanCHito Feliz "

# Los metodos son funciones que se encuentran dentro de un objeto

# upper() -> Convierte el texto a mayusculas
# lower() -> Convierte el texto a minusculas
# capitalize() -> Convierte la primera letra en mayuscula
# title() -> Convierte la primera letra de cada palabra en mayuscula
# strip() -> Elimina los espacios en blanco al inicio y al final
# lstrip() -> Elimina los espacios en blanco al inicio
# rstrip() -> Elimina los espacios en blanco al final
# find() -> Busca un texto dentro de otro y devuelve la posicion
# replace() -> Reemplaza un texto por otro
# in -> Devuelve True si el texto se encuentra en el otro
# not in -> Devuelve True si el texto no se encuentra en el otro

print(animal.upper())
print(animal.lower())
print(animal.strip().capitalize())
print(animal.title())
print(animal.strip())
print(animal.lstrip())
print(animal.rstrip())
print(animal.find("Feliz"))
print(animal.replace("nCH", "j"))
print("nCH" in animal)
print("nCH" not in animal)
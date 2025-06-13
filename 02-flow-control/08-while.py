numero = 1
while numero < 100:
    print("Número:", numero)
    numero *= 2

coman = ""

while coman.lower() != "salir":
    coman = input("Introduce un comando (o 'salir' para terminar): ")
    print("Comando introducido:", coman)
numero = 1
while numero < 100:
    print("Número:", numero)
    numero *= 2

coman = ""

while coman.lower() != "salir":
    coman = input("Introduce un comando (o 'salir' para terminar): ")
    print("Comando introducido:", coman)

# Loops Infinitos

while True:
    system = input("Cual es el sistema operativo rey de los servidores ? ")
    if system.lower() == "linux":
        print("Correcto, Linux es el rey de los servidores")
        break
    else:
        print("Incorrecto, intenta de nuevo")
    # Puedes agregar una condición de salida si es necesario
    # if alguna_condicion:
    #     break
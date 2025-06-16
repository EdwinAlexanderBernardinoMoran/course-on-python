print("Bienvenidos a la calculadora de la muerte")
print("Para salir escribe 'salir'")
print("Las operaciones disponibles son: suma, resta, multi y div")

result = ""

while True:

    if not result:
        numberOne = input("Introduce el primer número: ")
        if result.lower() == 'salir':
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break
        result = int(numberOne)

    operation = input("Introduce operación ")
    if operation.lower() == 'salir':
        print("Saliendo de la calculadora. ¡Hasta luego!")
        break

    numberTwo = input("Introduce el segundo número: ")
    if numberTwo.lower() == 'salir':
        print("Saliendo de la calculadora. ¡Hasta luego!")
        break
    numberOne = int(numberOne)

    if operation == "suma":
        result += int(numberTwo)
    elif operation == "resta":
        result -= int(numberTwo)
    elif operation == "multi":
        result *= int(numberTwo)
    elif operation == "div":
        if int(numberTwo) == 0:
            print("No se puede dividir por cero.")
            continue
        result /= int(numberTwo)
    else:
        print("Operación no válida. Por favor, elige entre suma, resta, multi o div.")
        continue

    print(f"El resultado es: {result}")
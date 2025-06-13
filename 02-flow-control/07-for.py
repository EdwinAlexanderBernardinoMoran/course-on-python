search = 10

for number in range(5):
    print("Número:", number)
    if number == search:
        print("Número encontrado:", number)
        break
else:
    print("Número no encontrado en el rango de 0 a 4")


for chart in "Python":
    print("Carácter:", chart)
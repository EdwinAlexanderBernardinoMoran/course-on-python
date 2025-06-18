saludo = "Hola, mundo global!"

def saludar():
    global saludo
    print(saludo)
    saludo = "Hola, mundo!"

def saludar_personalizado():
    saludo = "Hola, mundo personalizado!"
    print(saludo)

resultOne = saludo + 3
saludar()

resultTwo = saludo + 3
print(saludo)
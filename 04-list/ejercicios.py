from pprint import pprint

# 1. Eliminar los especios en blanco de un string y devolver una lista con los caracteres restantes.

def eliminar_espacios(texto):
    return [caracter for caracter in texto if caracter != " "]





# 2. Contar en un diccionario cuanto se repiten los carecteres de un string.

def contar_repeticiones(texto):
    contador = {}
    for caracter in texto:
        if caracter in contador:
            contador[caracter] += 1
        else:
            contador[caracter] = 1
    return contador



# 3. Ordenar las llaves de un diccionario por el valor que tienen y devolver una lista que contiene tuplas.

def ordenar_diccionario(diccionario):
    return sorted(diccionario.items(), key=lambda key: key[1], reverse=True)



# 4. De un listado de tuplas, devolver una tuplas que tenga el mayor valor.

def mayor_tupla(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta

def crea_mensage(diccionario):
    mensaje = "Los que mas se repiten son: \n"
    for clave, valor in diccionario.items():
        mensaje += f"- {clave}: con {valor} repeticiones \n"
    return mensaje


print("Eliminar espacios en blanco de un string:")
sin_espacios = eliminar_espacios("Hola mundo este es mi string")
print(sin_espacios)


print("Contar repeticiones de caracteres en un string:")
contados = contar_repeticiones(sin_espacios)
pprint(contados, width=1)


print("Ordenar llaves de un diccionario por valor:")
ordenados = ordenar_diccionario(contados)
print(ordenados)

print("Devolver tupla con el mayor valor de una lista de tuplas:")
mayores = mayor_tupla(ordenados)
print(mayores)

print("Crear mensaje con los caracteres que más se repiten:")
mensaje = crea_mensage(mayores)
print(mensaje)
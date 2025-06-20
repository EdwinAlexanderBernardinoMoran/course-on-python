import random
print("Calculo del total de una cuenta después de aplicar un descuento")


# Instrucciones:
# 1. De interés funciones:
#    o a_segundos: Convierte una cantidad y unidad dada a segundos.
#    o de_segundos: Convierte una cantidad en segundos a otra unidad deseada.
#    o convertir_tiempo: Usa las dos funciones anteriores para realizar una conversión completa entre dos unidades.
# 2. Considera las siguientes unidades:
#    - segundo
#    - minuto
#    - hora
#    - día
#    - mes (30 días)
#    - año (365 días)


# Ejercicio 0
def total_calculation_with_discount(total, discount):
    return total - (total * discount / 100)

# print(total_calculation_with_discount(1000, 100))


# Ejercicio 1
def a_segundos(cantidad, unidad):
    if unidad == 'segundo':
        return cantidad
    elif unidad == 'minuto':
        return cantidad * 60
    elif unidad == 'hora':
        return cantidad * 3600
    elif unidad == 'dia':
        return cantidad * 86400
    elif unidad == 'semana':
        return cantidad * 604800
    elif unidad == 'mes':
        return cantidad * 2592000
    elif unidad == 'año':
        return cantidad * 31536000
    else:
        return "Unidad no válida"
# print(a_segundos(5, 'año'))  # 60


# Ejercicio 2
def de_segundos(cantidad, unidad):
    if unidad == 'segundo':
        return cantidad
    elif unidad == 'minuto':
        return cantidad / 60
    elif unidad == 'hora':
        return cantidad / 3600
    elif unidad == 'dia':
        return cantidad / 86400
    elif unidad == 'semana':
        return cantidad / 604800
    elif unidad == 'mes':
        return cantidad / 2592000
    elif unidad == 'año':
        return cantidad / 31536000
    else:
        return "Unidad no válida"
# print(de_segundos(120, 'minuto'))  # 1.0


# Ejercicio 3
def convertir_tiempo(cantidad, unidad_origen, unidad_destino):
    cantidad_en_segundos = a_segundos(cantidad, unidad_origen)
    if cantidad_en_segundos == "Error":
        return "Unidad de tiempo no válida"
    cantidad_convertida = de_segundos(cantidad_en_segundos, unidad_destino)
    return f"{cantidad} {unidad_origen}(s) son {cantidad_convertida} {unidad_destino}(s)"

# print(convertir_tiempo(2, 'hora', 'minuto'))  # 60.0 meses

 
# Ejercicio 4
def cantidad_de_numeros(*numeros):

    resultado = 0
    cantidad_numeros = 0
    if not numeros:
        return 0
    for numero in numeros:
        resultado += numero
        cantidad_numeros += 1
    return resultado / cantidad_numeros
# print(cantidad_de_numeros(1, 2, 3, 4, 5))  # 6

def tirar_dados(veces):
    cara_1 = 0  
    cara_2 = 0   
    cara_3 = 0    
    cara_4 = 0    
    cara_5 = 0    
    cara_6 = 0    
    if veces == 1:        
        resultado = random.randint(1, 6)        
        return print(f"Salió la cara: {resultado}")    
    if veces <= 0:        
        return print("Error: El número de lanzamientos debe ser mayor a 0.")    
    for _ in range(veces):        
        resultado = random.randint(1, 6)        
        if resultado == 1:            
            cara_1 += 1        
        elif resultado == 2:            
            cara_2 += 1        
        elif resultado == 3:            
            cara_3 += 1        
        elif resultado == 4:           
            cara_4 += 1        
        elif resultado == 5:            
            cara_5 += 1        
        elif resultado == 6:            
            cara_6 += 1    
    cara_1 = (cara_1 / veces) * 100    
    cara_2 = (cara_2 / veces) * 100    
    cara_3 = (cara_3 / veces) * 100    
    cara_4 = (cara_4 / veces) * 100    
    cara_5 = (cara_5 / veces) * 100    
    cara_6 = (cara_6 / veces) * 100    

    print(f"Porcentaje de veces que salió la cara 1: {cara_1:.2f}%")    
    print(f"Porcentaje de veces que salió la cara 2: {cara_2:.2f}%")    
    print(f"Porcentaje de veces que salió la cara 3: {cara_3:.2f}%")    
    print(f"Porcentaje de veces que salió la cara 4: {cara_4:.2f}%")    
    print(f"Porcentaje de veces que salió la cara 5: {cara_5:.2f}%")    
    print(f"Porcentaje de veces que salió la cara 6: {cara_6:.2f}%")

tirar_dados(10000)


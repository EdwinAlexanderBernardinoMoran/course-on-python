name_course = "Ultimate Python"

description = """
Python is a high-level, interpreted, interactive and object-oriented scripting language. Python is designed to be highly readable. It uses English keywords frequently where as other languages use punctuation, and it has fewer syntactical constructions than other languages."""

# Obtiene la longitud de la cadena
print(len(name_course))

# Obtiene el primer caracter de la cadena
print(name_course[0])

# Obtiene los primeros 7 caracteres de la cadena
print(name_course[0:7])

# Obtiene los primeros 7 caracteres de la cadena, saltando de 2 en 2
print(name_course[0:7:2])

# Obtiene los últimos 7 caracteres de la cadena
print(name_course[9:])

# Obtiene los últimos 7 caracteres de la cadena
print(name_course[:8])

# Convierte todo el texto a mayúsculas
print(name_course.upper())

print(name_course, description)
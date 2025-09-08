from io import open

# Escritura
text = "Hello World"

# Si el archivo no existe, se crea.
# fileOne = open("09-files/test-file-one.txt", "w")
# fileOne.write(text)
# fileOne.close()

# Lectura
# fileTwo = open("09-files/test-file-one.txt", "r")
# content = fileTwo.read()
# fileTwo.close()
# print(content)

# with and seek
# with open("09-files/test-file-one.txt", "r") as file:
#     print(file.readlines())
#     file.seek(0)
#     for line in file:
#         print(line)

# Agregar
# file = open("09-files/hello-world.txt", "a+")
# file.write("Chao mundo :(")
# file.close()

# Lectura y escritura
# with open("09-files/hello-world.txt", "r+") as file:
#     text = file.readlines()
#     file.seek(0)
#     text[0] = "Curso de Python la"
#     file.writelines(text)
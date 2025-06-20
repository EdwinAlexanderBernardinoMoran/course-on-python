# def is_palindromo(palabra):

#     print("Palabra original:", palabra)
#     palabra = palabra.lower()
#     palabra = palabra.replace(" ", "")

#     return palabra == palabra[::-1]

# print(is_palindromo("Anita lava la tina"))

def no_space(text):
    new_text = ""

    for char in text:
        if char != " ":
            new_text += char
    return new_text

def reverse(text):
    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

def is_palindromo(text):

    text = no_space(text)
    text_reversed = reverse(text)
    
    return text.lower() == text_reversed.lower()

print(is_palindromo("Anita lava la tina"))
print(is_palindromo("Hola mundo"))
print(is_palindromo("Reconocer"))
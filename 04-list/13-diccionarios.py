punto = {
    "x": 10,
    "y": 20,
}

print(punto)
print(punto["x"])

punto["z"] = 30
if "newText" in punto:
    print(punto["newText"])

print(punto.get("newText", "No existe la clave 'newText'"))

# Forma de recorrer un diccionario
for clave in punto:
    print(f"{clave}: {punto[clave]}")

for clave in punto.items():
    print(clave)

for clave, valor in punto.items():
    print(f"{clave}: {valor}")

# Formas de eliminar elementos

del punto["y"]
del (punto["x"])

print(punto)

# Example

users = [
    {
        "id": 1,
        "name": "John",
        "age": 30,
        "email": "john@example.com"
    },
    {
        "id": 2,
        "name": "Jane",
        "age": 25,
        "email": "jane@example.com"
    },
    {
        "id": 3,
        "name": "Alice",
        "age": 28,
        "email": "alice@example.com"
    },
    {
        "id": 4,
        "name": "Bob",
        "age": 22,
        "email": "bob@example.com"
    }
]

for user in users:
    print(user["name"])
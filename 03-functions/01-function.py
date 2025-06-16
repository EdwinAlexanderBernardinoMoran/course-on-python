def green(name, lastname = "Bernardino"):
    print("Hello, " + name + " " + lastname + "! This is a green function.")

green("Alice", "Smith")
green("Edwin")

# Argumentos nombrados

# No importan el orden de los argumentos si se usan nombres python los utiliza normalmente
green(lastname="Doe", name="John")
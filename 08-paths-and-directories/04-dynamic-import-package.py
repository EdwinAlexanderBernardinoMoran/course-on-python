from pathlib import Path

# Importar todos los paquetes en el directorio actual

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]

dependencies = {
    "db": "database", # Simulando una instancia de base de datos
    "cache": "cache_system", # Simulando una instancia de sistema de caché
    "auth": "authentication", # Simulando una instancia de autenticación
}

def load(p):
    package = __import__(str(p).replace("/", "."))

    try:
        package.init(**dependencies)
    except AttributeError:
        print(f"The package {package} does not have an init function")

list(map(load, paths))
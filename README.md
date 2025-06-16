# Python y Django: Notas Rápidas

## PEP: Python Enhancement Proposals

- **Python** es un conjunto de reglas que define el lenguaje.
- Es un lenguaje de alto nivel.

## Implementaciones de Python

- **CPython**: Implementado en C
- **PyPy**: Implementado en Python
- **Jython**: Implementado en Java
- **IronPython**: Implementado en C#
- **Brython**: Para navegadores web, traduce a JavaScript

## Proceso de Ejecución

| Lenguaje | Compilador | ByteCode | Máquina Virtual | Lenguaje Máquina |
|----------|------------|----------|-----------------|------------------|
| Java     | ✔️         | ✔️       | JVM             | ✔️               |
| Python   | ✔️         | ✔️       | PVM             | ✔️               |

## Conceptos Básicos

- **Argumentos**: Valores que se pasan a una función.
- **Métodos**: Funciones dentro de un objeto.

---

## Django

- **Django**: Framework sobre Python.

### Instalación de Django

```bash
sudo apt install python3-django
django-admin --version
```

### Crear y Activar Entorno Virtual

```bash
python3 -m venv nombre_entorno
source nombre_entorno/bin/activate
```

### Dentro del Entorno Virtual

```bash
pip install django
django-admin startproject mysite .  # Crea el proyecto en el directorio actual
python3 manage.py startapp nombre_app
python3 manage.py runserver puerto  # Levanta el servidor
python3 manage.py --help
python3 manage.py makemigrations    # Después de editar models.py
python3 manage.py migrate           # Ejecuta todas las migraciones
```

- Crear una carpeta en Django = Crear un proyecto.
- Un proyecto Django se divide en aplicaciones.

### Uso de la Shell de Django

```python
python3 manage.py shell
from nombre_proyecto import ClaseModelo
variable = ClaseModelo(nombre="Aplicacion Movil")  # Inserción de datos
variable.save()                                   # Guardar datos
ClaseModelo.objects.all()                         # Listar datos
ClaseModelo.objects.get(id=1)                     # Buscar por campo
p.task_set.create(titulo="desarrollar login")     # Asignar tarea a proyecto
p.task_set.all()                                  # Todas las tareas del proyecto
p.task_set.get(id=1)                              # Filtrar por campo
ClaseModelo.objects.filter(nombre__startswith="aplicacion")  # Filtrar por nombre
```

### Panel Administrativo

```bash
python3 manage.py createsuperuser
```
- Permite usar el panel admin de Django (requiere usuario, contraseña y email).

### Plantillas y REST

- Django usa el motor de plantillas **Jinja2**.
- **Django Rest Framework**: Extiende Django para APIs REST.
    - Crear `serializers.py` para definir serializadores.
    - `ViewSet` controla el acceso a los serializadores.

---

## S3 - Control de Flujo

- Los operadores lógicos se evalúan de izquierda a derecha.
    - Con el operador `and` basta con que el valor izquiero sea `false` para ya no seguir evaluando lo demas
    - Con el operador `or` basta con que el primero sea `true` para ya no seguir evaluando lo demas.

- Operadores de comparacion

```py
# Forma normal
if edad >= 15 and edad <= 65:
    print("Puedes entrar a la piscina")

# Forma simplificada
if 15 <= edad <= 65:
    print("Puedes entrar a la piscina")
```

- Iterables son: Tuplas, Listas y Strings

## S4 - Funciones

**Parámetros**: Son variables que se definen en la declaración de una función y que reciben los valores (argumentos) que se pasan cuando la función es llamada. Permiten que la función trabaje con diferentes datos sin modificar su definición.Parametros

```py
def myFunction(parameterOne, parameterTwo):
    print(f"{parameterOne} {parameterTwo}")
```

- Para pasar multiples argumentos a una funcion es necesario utilizar `xargs` o el signo * y el nombre del parametro.

```py
def sum(*args):
    result = 0
    for arg in args:
        result += arg
    print(f"La suma de los argumentos es: {result}")
```
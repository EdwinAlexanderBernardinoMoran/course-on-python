# Python y Django: Notas Rápidas

## PEP: Python Enhancement Proposals

- **Python** es un conjunto de reglas que define el lenguaje.
- Es un lenguaje de alto nivel.

## Implementaciones de Python

- **CPython**: Implementado en C.
- **PyPy**: Implementado en Python.
- **Jython**: Implementado en Java.
- **IronPython**: Implementado en C#.
- **Brython**: Para navegadores web, traduce a JavaScript.

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
    - Con el operador `and` basta con que el valor izquierdo sea `false` para ya no seguir evaluando lo demás.
    - Con el operador `or` basta con que el primero sea `true` para ya no seguir evaluando lo demás.

- Operadores de comparación:

```python
# Forma normal
if edad >= 15 and edad <= 65:
    print("Puedes entrar a la piscina")

# Forma simplificada
if 15 <= edad <= 65:
    print("Puedes entrar a la piscina")
```

- Iterables son: Tuplas, Listas y Strings.

## S4 - Funciones

**Parámetros**: Son variables que se definen en la declaración de una función y que reciben los valores (argumentos) que se pasan cuando la función es llamada. Permiten que la función trabaje con diferentes datos sin modificar su definición.

```python
def myFunction(parameterOne, parameterTwo):
    print(f"{parameterOne} {parameterTwo}")
```

**`*args`**: Permite a una función recibir un número variable de argumentos posicionales. Dentro de la función, `args` es una tupla con todos los valores pasados como argumentos adicionales.

```python
def imprimir_argumentos(*args):
    for arg in args:
        print(arg)

imprimir_argumentos(1, 2, 3, "hola")
# Salida:
# 1
# 2
# 3
# hola
```

```python
def sum(*args):
    result = 0
    for arg in args:
        result += arg
    print(f"La suma de los argumentos es: {result}")
```

**`kwargs`**: Permite pasar un número variable de argumentos con nombre (clave-valor) a una función. Dentro de la función, `kwargs` es un diccionario con todos los argumentos nombrados.

```python
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=30, ciudad="Lima")
# Salida:
# nombre: Ana
# edad: 30
# ciudad: Lima
```

#### Alcance de las Variables en Python

El **alcance** (scope) de una variable en Python determina desde qué partes del código se puede acceder a esa variable. Los principales alcances son:

- **Local**: Definida dentro de una función, accesible solo ahí.
- **Global**: Definida fuera de cualquier función, accesible desde cualquier parte del archivo.
- **No local**: Usado en funciones anidadas, permite acceder a variables de la función envolvente.

#### ¿Por qué es mala práctica definir variables en el entorno global?

- **Dificultad para depurar**: Las variables globales pueden ser modificadas desde cualquier parte del código, dificultando rastrear errores.
- **Colisiones de nombres**: Es fácil sobrescribir accidentalmente una variable global.
- **Menor reutilización**: Reduce la modularidad y reutilización del código.
- **Dependencias ocultas**: Las funciones que dependen de variables globales no son independientes.

Se recomienda limitar el uso de variables globales y preferir variables locales dentro de funciones.

## 5 - Tipos avanzados

- Las listas en Python son estructuras de datos que permiten almacenar varios elementos en una sola variable. Son flexibles y pueden contener cualquier tipo de dato. Su tamaño puede cambiar dinámicamente.

- La función `enumerate` sirve para iterar sobre una colección y obtener el índice y el valor de cada elemento.

```python
mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito Feliz"]

for index, mascota in enumerate(mascotas):
    print(index, mascota)
```

#### Manipulando listas

- Buscando elementos:

```python
mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito Feliz"]

mascotas.index("Felipe")  # Devuelve el índice del primer elemento encontrado
mascotas.count("Felipe")  # Devuelve el número de veces que aparece el elemento
```

#### Métodos para agregar elementos a la lista

- **`insert(posición, elemento)`**: Inserta un elemento en una posición específica.
- **`append(elemento)`**: Agrega un elemento al final de la lista.

#### Métodos para eliminar elementos de la lista

- **`remove(elemento)`**: Elimina la primera aparición del elemento.
- **`pop([índice])`**: Elimina y retorna el último elemento o el de la posición dada.
- **`del lista[índice]`**: Elimina el elemento en la posición especificada.
- **`clear()`**: Elimina todos los elementos de la lista.

#### Métodos para ordenar listas

- **`sort()`**: Ordena la lista en el lugar.
- **`sorted()`**: Devuelve una nueva lista ordenada a partir de cualquier iterable.

#### Expresión lambda

- Forma concisa de crear funciones anónimas en una sola línea.

```python
users = [
    ["John", 30],
    ["Jane", 25],
    ["Alice", 28],
    ["Bob", 22]
]

users.sort(key=lambda user: user[1], reverse=True)  # Ordena por edad en orden descendente
print(users)
```

#### Listas de comprensión

- Forma concisa y eficiente de crear listas a partir de secuencias existentes.

```python
[expresión for elemento in iterable if condición]
```

```python
# Transformación (map)
users = [
    ["John", 30],
    ["Jane", 25],
    ["Alice", 28],
    ["Bob", 22]
]

namesTwo = [user[0] for user in users]
print(namesTwo)
```

```python
# Filtrado (filter)
users = [
    ["John", 30],
    ["Jane", 25],
    ["Alice", 28],
    ["Bob", 22]
]

namesThree = [user for user in users if user[1] > 23]
print(namesThree)
```

#### Tuplas

- Estructuras de datos inmutables que almacenan una colección ordenada de elementos. Se definen con paréntesis `()`.

```python
numbers = (1, 2, 3, 4, 5, 6)
```

#### Sets

- Colecciones no ordenadas de elementos únicos. Se definen con llaves `{}` o la función `set()`.

```python
# Crear un set
frutas = {"manzana", "banana", "naranja"}
print(frutas)

# Agregar un elemento
frutas.add("pera")

# Eliminar un elemento
frutas.remove("banana")

# Operaciones de conjuntos
numbers = {1, 1, 2, 2, 3, 4}

lists = [3, 4, 5]
lists = set(lists)

print(numbers | lists)  # Unión: {1, 2, 3, 4, 5}
print(numbers & lists)  # Intersección: {3, 4}
print(numbers - lists)  # Diferencia: {1, 2}
print(numbers ^ lists)  # Diferencia simétrica: {1, 2, 5}
print(numbers == lists)  # Igualdad: False
print(numbers != lists)  # Desigualdad: True
```

- Los sets no están ordenados y no se puede acceder a un elemento por índice.

#### Diccionarios

Los diccionarios en Python almacenan pares clave-valor. Son mutables, ordenados (desde Python 3.7+) y no permiten claves duplicadas.

- **Características principales**:
    - Mutables: Puedes agregar, modificar y eliminar elementos.
    - Ordenados: Mantienen el orden de inserción.
    - Claves únicas: No pueden existir claves duplicadas.
    - Acceso rápido: Búsqueda de elementos por clave en tiempo O(1) promedio.
    - Flexibles: Las claves deben ser inmutables (strings, números, tuplas), los valores pueden ser de cualquier tipo.

```python
# Crear un diccionario vacío
diccionario = {}
diccionario = dict()

# Crear un diccionario con datos
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "activo": True
}
```

- **Métodos útiles**:
    - keys(): Devuelve las claves
    - values(): Devuelve los valores
    - items(): Devuelve pares clave-valor
    - get(clave, default): Obtiene valor con valor por defecto si no existe
    - update(): Actualiza con otro diccionario

#### Operadores de desempaquetamiento

Los operadores de desempaquetamiento en Python son * y **.

Permiten "desempaquetar" (expandir) colecciones como listas, tuplas o diccionarios en argumentos individuales al llamar funciones.

- desempaqueta secuencias (listas, tuplas) en argumentos posicionales.
- desempaqueta diccionarios en argumentos nombrados (keyword arguments).


```python
# Desempaquetar una lista en argumentos de función
def suma(a, b, c):
    return a + b + c

numeros = [1, 2, 3]
resultado = suma(*numeros)  # Equivale a suma(1, 2, 3)

# Desempaquetar un diccionario en argumentos nombrados
def saluda(nombre, saludo):
    print(f"{saludo}, {nombre}!")

datos = {'nombre': 'Ana', 'saludo': 'Hola'}
saluda(**datos)  # Equivale a saluda(nombre='Ana', saludo='Hola')
```


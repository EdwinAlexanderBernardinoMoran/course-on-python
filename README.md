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

```python
# Forma normal
if edad >= 15 and edad <= 65:
    print("Puedes entrar a la piscina")

# Forma simplificada
if 15 <= edad <= 65:
    print("Puedes entrar a la piscina")
```

- Iterables son: Tuplas, Listas y Strings

## S4 - Funciones

**Parámetros**: Son variables que se definen en la declaración de una función y que reciben los valores (argumentos) que se pasan cuando la función es llamada. Permiten que la función trabaje con diferentes datos sin modificar su definición.

```python
def myFunction(parameterOne, parameterTwo):
    print(f"{parameterOne} {parameterTwo}")
```

**`*args`**: Es una convención en Python que permite a una función recibir un número variable de argumentos posicionales. Dentro de la función, `args` es una tupla que contiene todos los valores pasados como argumentos adicionales. Se utiliza anteponiendo un asterisco (`*`) al nombre del parámetro en la definición de la función.

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

**`kwargs`**: Es un mecanismo en Python que permite pasar un número variable de argumentos con nombre (clave-valor) a una función. Se define usando `**kwargs` en la declaración de la función. Dentro de la función, `kwargs` es un diccionario que contiene todos los argumentos nombrados que se pasaron.

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

- **Local**: La variable se define dentro de una función y solo es accesible dentro de esa función.
- **Global**: La variable se define fuera de cualquier función y es accesible desde cualquier parte del archivo.
- **No local**: Usado en funciones anidadas, permite acceder a variables de la función envolvente.

#### ¿Por qué es mala práctica definir variables en el entorno global?

Definir variables en el entorno global puede causar problemas como:

- **Dificultad para depurar**: Las variables globales pueden ser modificadas desde cualquier parte del código, lo que dificulta rastrear errores.
- **Colisiones de nombres**: Es fácil sobrescribir accidentalmente una variable global, causando comportamientos inesperados.
- **Menor reutilización**: El uso de variables globales reduce la modularidad y reutilización del código.
- **Dependencias ocultas**: Las funciones que dependen de variables globales no son independientes, lo que dificulta su comprensión y prueba.

Por estas razones, se recomienda limitar el uso de variables globales y preferir variables locales dentro de funciones.

## 5 - Tipos avanzados

- Las listas en Python son estructuras de datos que permiten almacenar varios elementos en una sola variable. Son muy flexibles porque pueden contener cualquier tipo de dato (números, cadenas, otras listas, etc.) y su tamaño puede cambiar dinámicamente (puedes agregar o quitar elementos).

- La función `enumerate` en Python sirve para iterar sobre una colección (como una lista, tupla, etc.) y, al mismo tiempo, obtener el índice y el valor de cada elemento.

En vez de solo obtener el valor, como en un ciclo for normal, `enumerate` te da una tupla con el índice (empezando por defecto en 0) y el elemento correspondiente.

```py
mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito Feliz"]

for index, mascota in enumerate(mascotas):
    print(index, mascota)
```

#### Manipulando listas

- Buscando elementos

```py
mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito Feliz"]

mascotas.index("Felipe")  # Devuelve el índice del primer elemento encontrado
mascotas.count("Felipe")  # Devuelve el número de veces que aparece el elemento

```

#### Métodos para agregar elementos a la lista

- **`insert(posición, elemento)`**: Inserta un elemento en una posición específica de la lista. Recibe dos argumentos: la posición donde se insertará el elemento y el valor del elemento a insertar.
- **`append(elemento)`**: Agrega un elemento al final de la lista. Solo recibe el elemento a agregar como argumento.

#### Métodos para eliminar elementos de la lista

- **`remove(elemento)`**: Elimina la primera aparición del elemento especificado en la lista. Si el elemento no existe, lanza una excepción.
- **`pop([índice])`**: Elimina y retorna el último elemento de la lista. Si se proporciona un índice, elimina y retorna el elemento en esa posición.
- **`del lista[índice]`**: Elimina el elemento en la posición especificada de la lista usando su índice.
- **`clear()`**: Elimina todos los elementos de la lista, dejándola vacía.

#### Metodos para ordenar listas

- **`sort()`**: Ordena los elementos de la lista en el lugar (modifica la lista original). Por defecto, ordena de menor a mayor, pero se puede personalizar usando los argumentos `key` y `reverse`.
- **`sorted()`**: Devuelve una nueva lista ordenada a partir de cualquier iterable (lista, tupla, etc.) sin modificar el original. También acepta los argumentos `key` y `reverse`.

#### Expresion lambda

- Es una forma concisa de crear funciones anónimas (sin nombre) en una sola línea. Se usa principalmente para funciones simples y de corta duración.

```py
users = [
    ["John", 30],
    ["Jane", 25],
    ["Alice", 28],
    ["Bob", 22]
]

users.sort(key=lambda parameter:returnValue)  # Ordena por edad en orden descendente
print(users)
```

#### Listas de comprension

- Las listas de comprensión en Python son una forma concisa y eficiente de crear listas a partir de secuencias existentes (como listas, rangos o cualquier iterable), aplicando una expresión y, opcionalmente, una condición.

```py
[expresión for elemento in iterable if condición]
```

```py
# Este ejemplo se le conoce como transformacion (map)
users = [
    ["John", 30],
    ["Jane", 25],
    ["Alice", 28],
    ["Bob", 22]
]

namesTwo = [user[0] for user in users]
print(namesTwo)
```

```py
# Este ejemplo se le conoce como filtrado (filter)
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

- Las tuplas en Python son estructuras de datos inmutables que permiten almacenar una colección ordenada de elementos. A diferencia de las listas, las tuplas no pueden ser modificadas después de su creación, lo que significa que no se pueden agregar, eliminar ni cambiar sus elementos. Se definen utilizando paréntesis () y pueden contener elementos de diferentes tipos de datos. Las tuplas son útiles para representar datos que no deben cambiar a lo largo del tiempo y pueden ser utilizadas como claves en diccionarios debido a su inmutabilidad.

```py
# Ejemplo de como luce una tupla
numbers = (1, 2, 3, 4, 5, 6)
```

#### Sets

- **Sets** en Python son colecciones no ordenadas de elementos únicos, es decir, no permiten elementos duplicados. Se definen usando llaves `{}` o la función `set()`. Los sets son útiles para operaciones de conjuntos como unión, intersección y diferencia.

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

print( numbers | lists )  # Unión: {1, 2, 3, 4, 5}, Se encarga de hacer una unión entre dos sets y elimina los duplicados
print( numbers & lists )  # Intersección: {3, 4}, Se encarga de encontrar los elementos que están en ambos sets
print( numbers - lists )  # Diferencia: {1, 2}, Se encarga de encontrar los elementos que están en el primer set pero no en el segundo.
print( numbers ^ lists )  # Diferencia simétrica: {1, 2, 5}, Se encarga de encontrar los elementos que están en uno de los sets pero no en ambos
print( numbers == lists )  # Igualdad: False, Se encarga de comparar si los sets son iguales
print( numbers != lists )  # Desigualdad: True, Se encarga de comparar si los sets son diferentes
```

- Los `Sets` no se encuentran ordenados y no podemos acceder a aun elemento de ellos.
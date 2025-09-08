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
pip freeze > requirements.txt # 
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

Existen tipos de variables:
    - Normal
    - Privada
    - Constantes


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


## 6 - Clases

Las clases en Python son plantillas o moldes que permiten crear objetos. Definen atributos (datos) y métodos (funciones) que describen el comportamiento y las características de esos objetos.

- **Conceptos clave**:

- Una clase es como un plano; un objeto es una instancia concreta de ese plano.
- Se definen usando la palabra clave class.
- Permiten organizar y reutilizar código.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

persona1 = Persona("Ana", 30)
persona1.saludar()  # Salida: Hola, mi nombre es Ana y tengo 30 años.

```

Puntos importantes:

- __init__ es el método constructor, se llama al crear un objeto.
- self se refiere a la instancia actual de la clase.
- a self se le puede asignar una propiedad ( viene siendo una variable que se encuentra asociada a una instancia de una clase )


#### Propiedades de clase

- Propiedad = Atributo

- Las propiedades de clase en Python son atributos que se definen directamente dentro de la clase, pero fuera de cualquier método. Estas propiedades son compartidas por todas las instancias de la clase, es decir, todas las instancias ven el mismo valor a menos que se sobrescriba en una instancia específica.

- **Puntos clave**:

    - Se accede a ellas usando Clase.propiedad o instancia.propiedad.
    - Cambiar el valor en la clase afecta a todas las instancias que no hayan sobrescrito ese atributo.
    - Son útiles para valores que deben ser iguales para todas las instancias (por ejemplo, número de patas en perro)



```python
class Dog:
    paws = 4  # Class property (attribute)

    def __init__(self, name, age = 0):
        self.name = name # Property instance
        self.age = age # Property instance
```

- Cuando creamos propiedades de instancia utilizamos la palabra reservada de `self` seguido de un punto y el nombre de la propiedad. Las propieades de clase se crean despues de definir las clases y para todas las instancias creadas de la clase deben tener el mismo valor para todas.

#### Métodos de clase

En Python, los **métodos de clase** son funciones definidas dentro de una clase que reciben la propia clase como primer argumento, en lugar de una instancia. Se definen usando el decorador `@classmethod`.

- El primer parámetro de un método de clase es convencionalmente llamado `cls`.
- Se utilizan para operar sobre la clase en sí, no sobre instancias específicas.
- Permiten modificar el estado de la clase o crear instancias de formas alternativas.

```python
class MiClase:
    contador = 0

    @classmethod
    def incrementar_contador(cls):
        cls.contador += 1

MiClase.incrementar_contador()
print(MiClase.contador)  # Imprime 1
```

- **Diferencia clave**:

- Los métodos de instancia usan self y afectan a una instancia.
- Los métodos de clase usan cls y afectan a la clase entera.


## 8 - Modulos

Los módulos en Python son archivos que contienen código Python (funciones, clases, variables) que puedes reutilizar en otros programas. Permiten organizar el código en partes más pequeñas y manejables.

**Conceptos clave:**

- Un módulo es simplemente un archivo `.py`.
- Puedes importar módulos usando la palabra clave `import`.
- Python tiene módulos estándar (como `math`, `os`) y puedes crear los tuyos propios.
- Los módulos ayudan a mantener el código organizado y reutilizable.

#### Modulos compilados

Cuando nosotros importamos un modulo python compila este modulo a bitecode

- Mejora el rendimiento de carga de modulos( El codigo nose vuelve efeciente, unicamente python ya no compila cuando se carga el modulo por segunda vez)
- El nombre de estos archivos se conforman por lo siguiente, la implementacion que utilizamos de python, la version de python y la extencion (.pyc, python y cache)
- Esto ahorra tiempo de carga, pero no hace que el programa corra más rápido en ejecución, porque la máquina virtual igual interpreta el bytecode.

#### Paquetes

- **Modulo**: Apunta a archivos
- **Paquetes**: Apuntan a Carpetas

Formas de importar modulos dentro de paquetes:

```py
from users.actions import save, payTaxes
import users.actions # Referenciaremos a todas la funciones que queramos acceder dentro de acciones de la siguiente manera

users.actions.save()
users.actions.payTaxes()

from users import actions

actions.save()
actions.payTaxes()
```

#### SubPaquetes

Los **subpaquetes** en Python son paquetes que están contenidos dentro de otros paquetes. Permiten organizar el código en una jerarquía de carpetas más profunda y estructurada. Un subpaquete es simplemente una carpeta dentro de un paquete principal que también contiene un archivo `__init__.py` (puede estar vacío).

Por ejemplo, si tienes la siguiente estructura de directorios:

```
mi_paquete/
    __init__.py
    modulo1.py
    subpaquete/
        __init__.py
        modulo2.py
```

- `mi_paquete` es un paquete.
- `subpaquete` es un subpaquete dentro de `mi_paquete`.


#### Referenciando paquetes

Puedes importar módulos de subpaquetes así:

```python
from mi_paquete.subpaquete import modulo2
```

Esto ayuda a mantener proyectos grandes organizados y facilita la reutilización de código.


#### dir

La función dir() en Python se utiliza para listar los nombres de los atributos y métodos de un objeto, módulo o del entorno actual si no se le pasa ningún argumento. Es útil para explorar qué propiedades y funciones están disponibles para un objeto.

#### Paquetes con nombres dinamicos

Dependiendo de donde se esten ejecutando es el nombre que van a tener, si lo ejecutamos de manera directa se muestra algo como (__main__), en caso lo ejecutemos desde otro archivo lo que muestra es la ruta de donde se encuentra (users.taxes.utilities)

#### Import condicionados

Esto funciona en caso queramos imprimir o utilizar directamente el archivo desde el nombre en caso sea asi se utiliza lo siguiente.

```python
if __name__ != "__main__":
    from ..management.management import save

    print(__name__)

    def payTaxes():
        print("User taxes paid")
        save()

if __name__ == "__main__":
    print("Task executed")
```

## 9 - Rutas y Directorios

#### Rutas

La función Path() en Python pertenece al módulo pathlib. Sirve para trabajar con rutas de archivos y directorios de forma orientada a objetos, facilitando la manipulación, comprobación y construcción de rutas de manera más intuitiva que usando cadenas de texto.

Ejemplo básico:

```python
from pathlib import Path

# Crear una ruta
ruta = Path('mi_carpeta/archivo.txt')

ruta.exists() # Comprobar si existe
ruta.is_file() # Si es un archivo
ruta.is_dir() # Si es un directorio

ruta.name, # Devuelve el nombre del archivo con su extencion.
ruta.stem, # Devuelve el nombre del archivo sin su extencion.
ruta.suffix, # Devuelve la extencion del archivo.
ruta.parent, # Directorio padre
ruta.absolute() # Devuelve la ruta completa de donde se encuentran.

ruta.with_name("file.txt"), # Cambia el nombre del archivo incluyendo su extencion.
ruta.with_suffix(".py"), # Cambia la extencion del archivo
ruta.with_stem("fileTwo"), # Cambia el nombre del archivo sin su extencion


# Obtener el directorio padre
padre = ruta.parent

# Unir rutas fácilmente
nueva_ruta = padre / 'otro_archivo.txt'

```

**Ventajas**:

- Más legible y seguro que manipular rutas como strings.
- Funciona en Windows, Linux y macOS sin preocuparse por los separadores de ruta.
- Permite operaciones como crear, borrar, listar archivos y carpetas.

#### Directorios

```py
# Metodos para directorios

path.mkdir()
path.rmdir()
path.rename("new_directory")
path.exists()
```

## - 10 Gestino de Archivos

#### Archivos

Un archivo es un recurso de almacenamiento en tu sistema operativo donde puedes guardar datos, como texto, imágenes, código, etc. Los archivos permiten guardar información de manera persistente, es decir, que no se pierde cuando cierras el programa.

```py
from pathlib import Path

file = Path("09-files/test-file.txt")
# file.exists()
# file.rename()
# file.unlink()

print(file.stat())

```

- **`file.exists()`**  
  Verifica si el archivo realmente existe en esa ruta.  
  Devuelve `True` o `False`.

- **`file.rename()`**  
  Cambia el nombre o mueve el archivo a otra ubicación.

- **`file.unlink()`**  
  Elimina (borra) el archivo.

- **`file.stat()`**  
  Devuelve información detallada sobre el archivo, como tamaño, fecha de creación, permisos, etc.

#### Lectura y Escritura

```py
from pathlib import Path

file = Path("09-files/test-file.txt")

text = file.read_text() # Lectura del contenido como texto
textTwo = file.read_text("utf-8").split("\n") # Lectura con codificación y separación por líneas

# Podemos modificar y trabajar con el listado que ya tenemos.
textTwo.insert(0, "New line added") # Modificar la lista de líneas

file.write_text("\n".join(textTwo), "utf-8") # Sobrescribir el archivo
```
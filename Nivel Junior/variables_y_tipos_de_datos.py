"""
1. Variables y tipos de datos en Python.

- Que son las variables?

Son espacios reservados en la memoria de nuestra computadora
que permite consulta posteriomente los valores y trabajar con ellos


- Que son los tipos de datos?

Los tipos de datos son la clasificacion que definen los valores que son almacenados en
variables.

Hay tipos de datos simples y compuestos en Python.

Los tipos de datos simples son aquellos valores que no representan una estructura de datos. Podemos
definir como simples los siguientes tipos:

- Numeros
    - Enteros
    - Decimales
    - Complejos
- Logicos
    - Falso
    - Verdadero
- Caracteres
    - Cadenas

Por otra parte los tipos de datos compuestos, son aquellos que se conforman por una estructura compleja, dicha estructura permite almacenar mas de 1 tipo de dato simple en su contenido y acceder
a ellos cuando se requieran, entre los que podemos encontrar

- Listas
- Tuplas
- Conjuntos
- Diccionarios


Dicho esto, comencemos a picar codigo!!!
"""


""" *** Valores Numericos ***

Referencia: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
"""
numero_entero: int = 10
numero_decimal: float = 10.0
numero_complejo: complex = 2j

""" *** Valores Logicos ***

"""
es_hora_de_irse_a_dormir: bool = True
listo_para_rendirse = False

""" *** Valores De Caracteres ***

Referencia: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
"""
nombre_completo: str = "Calamardo Tentaculos"
inicial_de_python = 'P'


""" *** Listas ***

Listas o Arrays. Son una coleccion de cualquier tipo de dato, tanto simple como compuesto.
Con las lista podemos agregar, eliminar o modificar cualquier parte del contenido y esto gracias
a los indices. Los indices son la posicion de cada valor almacenado en el contenido.

Referencia: https://docs.python.org/3/library/stdtypes.html#lists
"""
nombres: list = ["Angel", "Raul", "Karla", "Abigail"]
edades: list[str] = [20, 22, 30, 56]
nombres_y_edades = [nombres, edades]

""" *** Tuplas ***
Las Tuplas son similares que las listas, con una gran diferencia: Son "Inmutables", es decir,
una vez creada la tupla ya no podemos ni modificar, agregar o eliminar valores del contenido.

Referencia: https://docs.python.org/3/library/stdtypes.html#tuples
"""
dias_de_la_semana: tuple[str] = (
    "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"
)

""" *** Conjuntos ***
Los conjutos igual son una coleccion de datos, podemos agregar, modificar y eliminar valores,
sin embargo, este tipo de dato no permite almacenar otros tipos de datos compuestos, por ejemplo:
podemos agregar cadenas pero no podemos agregar listas, tuplas, diccionarios o conjuntos.

Los conjuntos tampoco almacena valores duplicados.

Referencia: https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
"""
participantes: set[str] = {"Alberto", "Javier", "Karla", "Adriana"}

""" *** Diccionarios ***
Los diccionarios al igual que los tipos de datos anteriores son colecciones de datos.
Los diccionarios tiene una caracteristica que distingue de las demas, que es que cada indice
del diccionario tiene un id o una clave con la que podremos acceder al valor, la clave solo puede ser
todos numericos, todos cadenas de caracteres o inclusive booleanos. el valor al que podremos acceder
por el id puede ser cualquier tipo de dato.

Referencia: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
"""
costo_frutas: dict[str] = {
    "manzana": 25,
    "pera": 15,
    "sandia": 16
}


"""Conclusiones

Notaste que al definir una variables colocaba ': tipo_de_variable'?

En Python podemos especificar el tipo de valor de una variable, aunque esto no es
necesario ya que Python es dinamico, pero esto nos permite agregar especifidad a cada
definicion (considerando esto poco necesario ya que con un buen naming seria suficiente)

Por ultimo, notaste tambien que cada variable que se creo estaba en minusculas y separadas las
palabras por '_'? A eso se le llama snake case y es la forma sugerida por Python para definir variables, funciones, etc.

Puedes encontrar mas informacion sobre naming convention y buenas practicas al escribir codigo en los siguientes enlaces oficiales:

- https://peps.python.org/pep-0008/
- https://visualgit.readthedocs.io/en/latest/index.html
- https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html
"""

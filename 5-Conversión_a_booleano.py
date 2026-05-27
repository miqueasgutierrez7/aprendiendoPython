#Conversión a booleano

"""  
Ya sabes que todos los objetos en Python se pueden interpretar como valores booleanos . Los objetos evaluados como True" truety" y " falsy" Falseson " falsy" . Los siguientes valores son "falsy":

algunas constantes: Noney False,
cero: 0, 0.0, 0j,
contenedores vacíos como una cadena "", una lista []y otros.
Todos los demás objetos se evalúan como True.

Esto nos permite usar objetos de cualquier tipo en expresiones booleanas . En este tema, aprenderemos cuándo puede ser útil y cuándo se deben convertir explícitamente objetos en valores booleanos.

Prueba de veracidad
Dado que en Python hay pocos objetos que se evalúan como False, no son frecuentes los casos en que se usen valores no booleanos en expresiones lógicas. El más común es comprobar si el contenedor dado está vacío. Escribamos una función que imprima una lista si no está vacía y la cadena "empty list"si lo está.
"""

def print_list(lst):
    if lst:
        print(lst)
    else:
        print('empty list')


print_list([2, 3, 4])  # [2, 3, 4]
print_list([])         # empty list
"""
Según PEP8, es preferible escribir if lsten lugar de if len(lst) > 0, pero es importante comprender bien qué objetos se pueden pasar a la función. En este ejemplo, si el argumento pasado lstresulta ser None, la función imprime "empty list".


Aquí y más adelante en este tema, todos los ejemplos utilizan listas, pero todo esto se puede aplicar a otros contenedores de la misma manera.

Hay una forma más compacta de implementar la misma función, pero requiere una comprensión profunda de cómo los operadores andy orfuncionan con valores no booleanos.

Operaciones lógicas con valores no booleanos
Ya sabes que, dados dos valores booleanos, anddevuelve Truesi ambos operandos son iguales, Truemientras que ordevuelve Truesi al menos un operando es igual a True. Cuando los operandos son de tipo arbitrario, Python puede aplicarles los operadores ``` andy or``, pero el resultado será uno de los operandos en lugar de los valores booleanos Trueo ` False``.

Las tablas a continuación muestran lo que andlos operadores ory notdevuelven dependiendo de si sus operandos son verdaderos o falsos.

"""
def print_list(lst):
    print(lst or 'empty list')


print_list([2, 3, 4])  # [2, 3, 4]
print_list([])         # empty list

"""
Según la segunda tabla, cuando lstno está vacío, por lo que es verdadero, el oroperador devuelve el primer operando (la lista misma); cuando lstestá vacío, por lo que es falso, el oroperador devuelve el segundo operando (la cadena en nuestro caso).

Otro aspecto a tener en cuenta es que cuando el primer operando determina de forma única el resultado de la operación, lo cual ocurre cuando el primer operando de la andoperación es falso o cuando el primer operando de la oroperación es verdadero, Python no considera el segundo operando en absoluto. Por ejemplo, si queremos comprobar si la lista dada lstno está vacía y su primer elemento es positivo, podemos escribir lo siguiente:

"""
if lst and lst[0] > 0:
    ...
"""
Si lstestá vacío, la lst[0] > 0expresión no es válida, pero no provoca una excepción porque nunca se evalúa.

función bool()
Aunque podemos usar cualquier objeto en expresiones booleanas, hay casos en los que debemos convertir explícitamente objetos en valores booleanos reales. Esto se puede hacer con la bool()función. La bool()función devuelve Truesi el argumento pasado es verdadero o Falsefalso.
"""

print(bool(True), bool(False))    # True False
print(bool(None))                 # False
print(bool([]), bool([2, 3, 9]))  # False True

"""
Esta función no es muy común, pero hay casos especiales en los que puede ser útil.

¿Cuándo utilizar la función bool()?
A veces es necesario almacenar el resultado de una expresión lógica o incluso escribirlo en un archivo. En este caso, se desea obtener Trueo False, no un objeto verdadero o falso.

Veamos el ejemplo. Tienes una lista de listas con valores enteros. Quieres comprobar si esta lista no está vacía y si su primer elemento no es cero en cada lista interna. La solución es el siguiente código:
"""
def check_list(lst):
    return lst and lst[0]


lists = [[5, 9], [0, 0], []]
result = []
for lst in lists:
    result.append(check_list(lst))

print(result)  # [5, 0, []]

Aunque 5es un valor verdadero y 0y []son valores falsos, probablemente prefiera obtener una lista de valores booleanos reales: result = [True, False, False]. Por lo tanto, debería convertir explícitamente el resultado de la función en un valor booleano.

def check_list(lst):
    return bool(lst and lst[0])


lists = [[5, 9], [0, 0], []]
result = []
for lst in lists:
    result.append(check_list(lst))

print(result)  # [True, False, False]

"""
Cuando no es necesario almacenar el resultado de una expresión lógica, no es necesario encerrar la expresión en la bool()función. Por ejemplo, if lstes más legible que if bool(lst).

Resumen
Todos los objetos en Python pueden interpretarse como valores booleanos.
Algunos operadores booleanos, como andy or, devuelven uno de los operandos como resultado; not, por el contrario, siempre devuelve un valor booleano.
Está bien utilizar la prueba de veracidad para verificar si el contenedor está vacío, pero hágalo con cuidado.
Cuando desee almacenar el resultado de una operación lógica, no solo verificar si es verdadero o falso, debe convertirlo explícitamente en un valor booleano usando la bool()función.
"""


#Practicando

#1

def print_list(lst):
    if lst:
        print(lst)
    else:
        print('empty list')


print_list([2, 3, 4])  # [2, 3, 4]
print_list([])  


print([1] and "hola")  

print("1 and '0' =>", 1 and '0')

xpresión	Resultado	Por qué
1 and '0'	'0'	1 es verdadero, devuelve el segundo valor '0'
[] or 0j	0j	[] es falso, devuelve el segundo valor 0j
[] and '0'	[]	[] es falso, devuelve el primer valor []
1 or 0j	1	1 es verdadero, devuelve el primer valor 1


config_usuario = None
config_default = {"tema": "claro"}

config = config_usuario or config_default
print(config)


¡Claro! Aquí te va una versión bien simple, como si fuera una nota rápida para estudiantes:

---

# Cómo funcionan `and` y `or` con valores que no son solo `True` o `False`

### 1. Valores “verdaderos” y “falsos” en Python

* Python considera que algunos valores son **falsos**: `0`, `0j`, `''` (cadena vacía), `[]` (lista vacía), `None`.
* Todo lo demás se considera **verdadero**.

---

### 2. Operador `and`

* Mira el primer valor.
* Si es **falso**, devuelve ese valor y ya.
* Si es **verdadero**, devuelve el segundo valor.

**Ejemplos:**

* `1 and '0'`
  El primero (1) es verdadero, entonces devuelve `'0'`.

* `[] and '0'`
  El primero (`[]`) es falso, entonces devuelve `[]`.

---

### 3. Operador `or`

* Mira el primer valor.
* Si es **verdadero**, devuelve ese valor y ya.
* Si es **falso**, devuelve el segundo valor.

**Ejemplos:**

* `[] or 0j`
  El primero (`[]`) es falso, entonces devuelve `0j`.

* `1 or 0j`
  El primero (1) es verdadero, entonces devuelve `1`.

---

### Resumen con tus ejemplos

| Expresión    | Resultado | Por qué                                         |
| ------------ | --------- | ----------------------------------------------- |
| `1 and '0'`  | `'0'`     | 1 es verdadero, devuelve el segundo valor `'0'` |
| `[] or 0j`   | `0j`      | `[]` es falso, devuelve el segundo valor `0j`   |
| `[] and '0'` | `[]`      | `[]` es falso, devuelve el primer valor `[]`    |
| `1 or 0j`    | `1`       | 1 es verdadero, devuelve el primer valor `1`    |

---

¿Quieres que te lo explique con ejemplos más fáciles o con dibujos?





def say_hello(name):
    if name:
    print('Hello, 'name'!)
    else:
    print('Hello, Anonymous!')

    def say_hello(name):
    if name:
        print('Hello, ' + name + '!')
    else:
        print('Hello, Anonymous!')


#4

def compare(numerator, denominator):
    return denominator and numerator / denominator == 0.5

a = 5
b = 10



return a and b / denominator == 0.5


print(compare(a, b))



def print_list(lst):
    if lst:
        print(lst)
    else:
        print('empty list')

print_list(0)


print(bool([1] and not [0]))

#5


def merge_arrays(a, b):
    # "c" will contain the result of merging arrays "a" and "b"
    c = []
    # CHECK that "a" or "b" are not empty
    while a or b:
        # CHECK that "b" is empty, or that "a" and "b" are not empty and compare the elements
        if not b or (a and a[0] < b[0]):
            # removing the first element from "a" and adding it to "c"
            c.append(a[0])
            a.pop(0)
        else:
            # removing the first element from "b" and adding it to "c"
            c.append(b[0])
            b.pop(0)
    return c

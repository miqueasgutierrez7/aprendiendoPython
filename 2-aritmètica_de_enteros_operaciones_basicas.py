"""
Aritmética de enteros: operaciones básicas
En la vida real, solemos realizar operaciones aritméticas . Nos ayudan a calcular el cambio de una compra, determinar el área de una habitación, contar el número de personas en una fila, etc. Estas mismas operaciones se utilizan en los programas.

Operaciones básicas
Python admite operaciones aritméticas básicas:

suma+

sustracción-

multiplicación*

división/

división de enteros//

Los ejemplos a continuación muestran cómo funciona con números enteros.
"""

print(10 + 10)  # 20
print(100 - 10)  # 90
print(10 * 10)  # 100
print(77 / 10)  # 7.7
print(77 // 10)  # 7

"""
Existe una diferencia entre la división /y la división de enteros //. La primera produce un número de punto flotante (como 7.7), mientras que la segunda produce un valor entero (como 7) ignorando la parte decimal.

Python genera un error si intenta dividir por cero.

ZeroDivisionError: division by zero

Escribir expresiones complejas
Las operaciones aritméticas se pueden combinar para escribir expresiones más complejas:
"""
print(2 + 2 * 2)  # 6

"""

El orden de cálculo coincide con las reglas de las operaciones aritméticas. La multiplicación tiene mayor prioridad que la suma y la resta, por lo que 2 * 2se calcula primero.

Para especificar un orden de ejecución, puede utilizar paréntesis, como en el siguiente ejemplo:
"""

print((2 + 2) * 2)  # 8

"""
Al igual que en aritmética, los paréntesis se pueden anidar. También se pueden usar para mayor claridad.

El operador menos tiene una forma unaria que niega el valor o la expresión. Un número positivo se vuelve negativo y un número negativo se vuelve positivo.
"""
print(-10)  # -10
print(-(100 + 200))  # -300
print(-(-20))  # 20
"""
Otras operaciones
El resto de una división. El operador módulo de Python %se usa para obtener el resto de una división. Puede ser útil para comprobar si un número es par. Al aplicarlo a un número y 2, devuelve 1si el número es impar y 0si es par.

"""

print(7 % 2)  # 1, because 7 is an odd number
print(8 % 2)  # 0, because 8 is an even number

"""

A continuación se muestran algunos ejemplos más:
"""
# Divide the number by itself
print(4 % 4)  # 0
# At least one number is a float
print(11 % 6.0)  # 5.0
# The first number is less than the divisor
print(55 % 77)  # 55
# With negative numbers, it preserves the divisor sign
print(-11 % 5)  # 4
print(11 % -5)  # -4

"""
Tomando el resto de la división por 0también obtenemos ZeroDivisionError.

El comportamiento de la función módulo cuando dos números tienen signos diferentes puede parecer inesperado a primera vista. Compare 11 % 5 = 1y -11 % -5 = -1(tanto el dividendo como el divisor tienen los mismos signos) con 11 % -5 = -4y -11 % 5 = 4(signos diferentes).

Para entender por qué funciona así, debemos analizarlo a fondo. En Python, el resto siempre tiene el mismo signo que el divisor, y el operador módulo ( %) y la división entera ( //) están conectados internamente mediante la siguiente expresión:

x == (x // y) * y + (x % y)

Podemos reescribirlo para obtener la "fórmula" para la división módulo:

(x % y) == x - (x // y) * y

Ahora, apliquémoslo a nuestros ejemplos. Queremos calcular 11 % -5. Primero, calculamos 11 // -5y el resultado es -3. Luego, aplicamos esto a nuestra fórmula y obtenemos 11 % -5 == 11 - (-3) * (-5) == 11 - 15 == -4.

Porque -11 % 5eso parece -11 % 5 == -11 - (-3) * 5que es igual a 4.

Si quieres comprender más a fondo esta operación, puedes consultar el tema "División módulo con números negativos" de la sección de Matemáticas.

Exponenciación. Aquí tienes una forma de elevar un número a una potencia:
"""
print(10**2)  # 100
"""
Esta operación tiene mayor prioridad que la multiplicación.

Prioridad de operación
En resumen, hay una lista de prioridades para todas las operaciones consideradas:

fuerza

unario menos

multiplicación, división y resto

suma y resta

Como se mencionó anteriormente, el signo menos unario cambia el signo de su argumento.

A veces las operaciones tienen la misma prioridad:
"""
print(10 / 5 / 2)  # 1.0
print(8 / 2 * 5)  # 20.0
"""
Las expresiones anteriores pueden parecerle ambiguas, ya que tienen soluciones alternativas según el orden de las operaciones: o bien 1.0o bien 4.0en el primer ejemplo, y o bien 20.0o bien 0.8en el segundo. En estos casos, Python sigue la convención matemática de operaciones de izquierda a derecha. Es bueno saberlo, así que trate de tenerlo en cuenta también.

¡Hora de PEP!
Hay algunas cosas que mencionar sobre el uso de operadores binarios (es decir, los operadores que influyen en ambos operandos). Como sabes, la legibilidad es importante en Python. Así que primero, recuerda rodear cada operador binario con un solo espacio a ambos lados:
"""
number = 30 + 12  # No!

number = 30 + 12  # It's better this way
"""
Los operadores son símbolos especiales que indican la operación a realizar. Los operandos son valores sobre los que se realiza la operación. Consideremos nuestro ejemplo: 30 + 12. Aquí +hay un operador y 30y 12son operandos.

Además, a veces se usa el salto después de los operadores binarios. Sin embargo, esto puede perjudicar la legibilidad de dos maneras:

los operadores no están en una columna,

cada operador se ha alejado de su operando y ha pasado a la línea anterior:
"""
# No: operators sit far away from their operands
income = (
    gross_wages
    + taxable_interest
    + (dividends - qualified_dividends)
    - ira_deduction
    - student_loan_interest
)
"""
Los matemáticos y sus editores siguen la convención opuesta para resolver el problema de legibilidad. Donald Knuth lo explica en su serie "Computadoras y Composición Tipográfica ": «Aunque las fórmulas dentro de un párrafo siempre se dividen después de las operaciones y relaciones binarias, las fórmulas mostradas siempre se dividen antes de las operaciones binarias». Seguir esta tradición hace que el código sea más legible:
"""
# Yes: easy to match operators with operands
income = (
    gross_wages
    + taxable_interest
    + (dividends - qualified_dividends)
    - ira_deduction
    - student_loan_interest
)
"""
En código Python, se permite la interrupción antes o después de un operador binario, siempre que la convención sea consistente localmente. Para código nuevo, se recomienda el estilo de Knuth , según PEP 8.

Resumen
Muy bien, ahora repasemos rápidamente lo que hemos aprendido en este tema:

Qué operaciones aritméticas básicas admite Python y cómo combinarlas en expresiones más complejas;

un par de otras operaciones útiles como el cálculo del resto de una división y la exponenciación;

prioridad de operación en Python;

Cómo escribir expresiones según PEP 8.
"""
# Ejercicios

# 1
a = int(input())
b = int(input())
c = int(input())
print((a * b) - c)

# 2

print(pow(31, 331, 20))
print(31**331 % 20)

# 3

print(2**179)

# 4

print(((3 + 5) // 2 * 2**3) % 7)

# 5

a = int(input())
b = int(input())
print(a + b)

# 6

n = 8

print((((n + n) * n) - n) // n)

# 7

print((1234567890 * 987654321) + 67890)

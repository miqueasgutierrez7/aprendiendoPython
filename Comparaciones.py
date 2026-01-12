# comparaciones
"""
Escribir código sin comparar valores solo te llevará hasta cierto punto. Ahora es el momento de dominar esta habilidad.

Operadores de comparación
Las operaciones de comparación o relación permiten comparar dos valores y determinar la relación entre ellos. En Python existen diez operadores de comparación :

<estrictamente menos que

<=menor o igual que

>estrictamente mayor que

>=mayor o igual que

==igual

!=no es igual

isidentidad del objeto

is notidentidad de objeto negada

inafiliación

not inmembresía negada.

El resultado de aplicar estos operadores siempre es verdadero bool. Las siguientes secciones se centran en los seis primeros operadores ( <, <=, >, >=, ==, !=), pero encontrará más detalles sobre las pruebas de identidad y pertenencia en los siguientes temas. Además, tenga en cuenta que los operadores mayor o igual que (<) y menor o igual que (<=), deben escribirse en el mismo orden en que se pronuncian sus nombres: <=menor o igual que, >=mayor o igual que.

Comparación de números enteros
En este tema, solo trataremos la comparación de números enteros.

"""
a = 5
b = -10
c = 15

result_1 = a < b  # False

result_2 = a == a  # True
result_3 = a != b  # True
result_4 = b >= c  # False

"""

Cualquier expresión que devuelva un número entero también es un operando de comparación válido:

"""
calculated_result = a == b + c  # True

"""
Dadas las variables definidas a, by c, básicamente comprobamos si 5es igual a -10 + 15, lo cual es cierto.

Encadenamiento de comparación
Dado que las operaciones de comparación devuelven valores booleanos , se pueden combinar mediante operadores lógicos . En este caso, es importante conocer su prioridad, es decir, cuál se ejecuta primero. Todas las operaciones de comparación tienen la misma prioridad, y esta es menor que la de cualquier operación aritmética, de desplazamiento o bit a bit (estas dos últimas se utilizan para operaciones con bytes).

"""

x = -5
y = 10
z = 12

result = x < y and y <= z  # True


"""
En Python, existe una forma más elegante de escribir comparaciones complejas. Se llama encadenamiento . Por ejemplo, `(x, y)` x < y <= zes casi equivalente a la expresión que viste en el ejemplo anterior. La diferencia radica en que `(x, y)` yse evalúa solo una vez.

result = 10 < (100 * 100) <= 10000  # True, the multiplication is evaluated once

Tenga en cuenta que las herramientas para el análisis de la calidad del código a menudo recomiendan encadenar las comparaciones en lugar de unirlas .

Sin embargo, conviene usar con precaución el encadenamiento de comparaciones , ya que a veces las expresiones pueden resultar complejas, por lo que el resultado dependerá del orden de los operadores y de cómo se coloquen los paréntesis. Considere este ejemplo:


"""

a = 1
b = 2
c = 3
e = 4
f = 5
g = 6

print(b + c <= e or f + g >= e == f == 5)  # False
print((b + c <= e or f + g >= e) == (f == 5))  # True


"""
La primera expresión Falsese evalúa de la siguiente manera: orel operador tiene la menor prioridad, por lo que se evalúa al final. El primer argumento ( b + c <= e) es False. El segundo argumento es el más largo: f + g >= e == f == 5, y se evaluará consecutivamente, así que analicémoslo: esta expresión es equivalente a (f + g >= e) and (e == f) and (f == 5), que se evalúa como False. Finalmente, calculamos el valor de toda la expresión: False or Falsees False. En el segundo caso, tenemos Trueen el paréntesis izquierdo y Trueen el derecho, por lo que Truees igual a Truey la expresión final también es True.

Lógica y aritmética
Veamos otro caso interesante. Al principio del tema, aprendimos que el resultado de aplicar operadores de comparación siempre es bool. Sin embargo, si una expresión contiene una parte lógica y otra aritmética, podríamos observar un comportamiento inusual debido a que los operadores lógicos en Python se evalúan de forma perezosa o mediante cortocircuito .


"""
a = 1
b = 2
c = 3
e = 4
f = 5
g = 6


# True and-expressions return the result of the last operation:
print(b + c * f >= e and (f + g) * c)  # (17 >= 4 is True) and 33 -> 33
print((f + g) * c and b + c * f >= e)  # 33 and (17 >= 4 is True) -- > True

# False and-expressions return a boolean False value:
print(b + c * f <= e and (f + g) * c)  # (17 <= 4 is False) and 33 --> False
print((f + g) * c and b + c * f <= e)  # 33 and (17 <= 4 is False) --> False

# True or-expressions return the result of the first operation:
print(b + c * f >= e or (f + g) * c)  # (17 >= 4 is True) or 33 --> True
print((f + g) * c or b + c * f >= e)  # 33 or (17 >= 4 is True) --> 33

# True-False or-expressions return the True part:
print((f + g) * c or b + c * f <= e)  # 33 or (17 <= 4 is False) --> 33
print(b + c * f <= e or (f + g) * c)  # (17 <= 4 is False) or 33 --> 33

"""
Puede parecer confuso a primera vista, pero si lo piensas bien, cada valor impreso es perfectamente legal y cumple con la lógica matemática común.

Resumen
En este tema, nos familiarizamos con los operadores de comparación de Python, aprendimos a comparar enteros y a usar el encadenamiento de comparaciones. ¡Estos operadores básicos sin duda te serán de gran ayuda en el futuro!
"""


# Practicas

# 1


def should_enroll(
    average_grade,
    recommended_by_tutor,
    finished_introductory_course,
    introductory_course_grade,
):
    return (average_grade >= 40 and recommended_by_tutor) or (
        finished_introductory_course and introductory_course_grade > 85
    )


# Ana

print("Respuesta:", should_enroll(33, False, True, 51))


# 2

andy_height = 6
ben_height = 3

print(andy_height > ben_height)

# 3

num1 = int(input())
num2 = int(input())

# Comprobar si el producto es igual al número secreto
print(num1 * num2 == set_number)

# 1:44- 2:14# 4
a = int(input().strip)
print(a > 0)

# 5
a = int(input().strip())
print(a < 10 or a > 250)

print("hola mundo")

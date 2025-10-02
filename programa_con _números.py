# Programa con números
"""
Los programas sin cálculos son bastante raros. Por lo tanto, aprender a programar con números nunca está de más. Una habilidad aún más valiosa que vamos a aprender es el procesamiento de datos de usuario. Con su ayuda, puedes crear aplicaciones interactivas y mucho más flexibles. ¡Comencemos!

Lectura de números a partir de la entrada del usuario
Dado que ya se ha familiarizado con la input()función en Python, no es ninguna novedad que cualquier dato pasado a esta función se trate como una cadena . Pero ¿cómo debemos tratar los valores numéricos? Por regla general, se convierten explícitamente a los tipos numéricos correspondientes :
"""

integer = int(input())
floating_point = float(input())

"""
Preste atención a las mejores prácticas actuales: es crucial no nombrar sus variables como tipos predefinidos (por ejemplo, float o int ). Además, debemos tener en cuenta los errores del usuario: si un usuario escribe una entrada incorrecta, por ejemplo, una cadena 'dos' en lugar de un número2, ValueErrorse producirá un error. Por ahora, no nos centraremos en ello; pero no se preocupen, encontrarán más información sobre errores en un tema específico. Ahora, consideren un ejemplo más detallado y pragmático del manejo de entradas numéricas.

millas aéreas gratis
Imagina que tienes una tarjeta de crédito con un programa de millas aéreas gratis (o quizás ya tienes uno). Como usuario, debes ingresar la cantidad promedio de dinero que gastas con esta tarjeta al mes. Supongamos que el programa de millas aéreas gratis te da 2 millas aéreas gratis por cada dólar que gastas. Aquí tienes un programa sencillo para calcular cuándo puedes viajar gratis:
"""

# the average amount of money per month
money = int(input("How much money do you spend per month: "))

# the number of miles per unit of money
n_miles = 2

# earned miles
miles_per_month = money * n_miles

# the distance between London and Paris
distance = 215

# how many months do you need to get
# a free trip from London to Paris and back
print(distance * 2 / miles_per_month)

"""
Este programa calculará cuántos meses se necesitan para recorrer la distancia seleccionada y regresar.

Aunque se recomienda escribir mensajes para los usuarios en la input()función, evítelos en nuestros desafíos de programación educativa, de lo contrario, su código podría no pasar nuestras pruebas.
Formas avanzadas de asignación
Al usar el signo igual =, se asigna un valor a una variable. Por ello, =se le suele llamar operador de asignación . Existen otros operadores de asignación que se pueden usar en Python. También se denominan operadores de asignación compuestos , ya que realizan una operación aritmética y una asignación en un solo paso. Vea el siguiente fragmento de código:
"""

# simple assignment
number = 10
number = number + 1  # 11

# compound assignment
number = 10
number += 1  # 11

"""
En el ejemplo se puede ver claramente que el segundo fragmento de código es más conciso (ya que no repite el nombre de la variable).

Naturalmente, existen formas de asignación similares para el resto de las operaciones aritméticas: -=, *=, /=, //=, %=, **=. Si tiene la oportunidad, úselas para ahorrar tiempo y esfuerzo.

A continuación se presenta una posible aplicación de la asignación compuesta.


Variable de contador
En programación, existe un concepto llamado bucle . Se utiliza para repetir un bloque de código un número determinado de veces. Suelen incluir variables especiales llamadas contadores . Un contador , como su nombre indica, cuenta algo: cuántas veces se cumple una condición, cuántos elementos hay en la secuencia , etc. Por lo tanto, los contadores deberían ser enteros. Ahora vamos al grano: puedes usar los operadores +=y -=para aumentar o disminuir el contador, respectivamente.

Considere este ejemplo donde un usuario determina el valor en el que se incrementa el contador:

"""

counter = 1
step = 5 # let it be 3
counter += step
print(counter)  # it should be 4

"""
Si solo necesita números enteros no negativos del usuario (¡después de todo, estamos incrementando el contador!), puede evitar entradas incorrectas usando la abs()función. Es una función integrada de Python que devuelve el valor absoluto de un número (es decir, el valor independientemente de su signo). Reajustemos un poco nuestro último programa:
"""
counter = 1
step = abs(int(input()))  # user types -3
counter += step
print(counter)  # it's still 4

"""
Como puedes ver, gracias a la abs()función obtuvimos un número positivo.

Por ahora, no importa si no conoces mucho sobre los detalles mencionados de errores , bucles y funciones integradas en Python. Nos pondremos al día y nos aseguraremos de que conozcas estos temas a fondo. ¡Sigue aprendiendo!


Resumen
Así, hemos aclarado nuevos detalles sobre la aritmética de enteros y el procesamiento de entradas numéricas en Python. Siéntete libre de usarlos en tus proyectos futuros. En este tema, abordamos:

Cómo leer números desde la entrada del usuario;
cómo asignar números a variables y utilizar operadores aritméticos para asignar el resultado del cálculo;
Qué son los contadores y cuándo se utilizan.
"""

number = 10
number += 2
print(number)


# Ejercicios

# 1

# the number of free miles per dollar
n_miles = 0.01

# money spent per month (in dollars)
money = 2000

# number of miles earned each month
miles_per_month = money * n_miles

# distance from London to Paris and back (in miles)
total_distance = 215 * 2

print(total_distance / miles_per_month)


# 3

squirrel = int(input())
nuts = int(input())
result = nuts % squirrel

print(sobran)
"""
| Operador | Significado              | Ejemplo   | Equivale a   |
| -------- | ------------------------ | --------- | ------------ |
| `+=`     | Suma y asigna            | `x += 3`  | `x = x + 3`  |
| `-=`     | Resta y asigna           | `x -= 2`  | `x = x - 2`  |
| `*=`     | Multiplica y asigna      | `x *= 4`  | `x = x * 4`  |
| `/=`     | Divide y asigna (float)  | `x /= 5`  | `x = x / 5`  |
| `//=`    | División entera y asigna | `x //= 3` | `x = x // 3` |
| `%=`     | Módulo y asigna          | `x %= 2`  | `x = x % 2`  |
| `**=`    | Potencia y asigna        | `x **= 2` | `x = x ** 2` |
"""

#4

a = 5
b = 10
c = 15
print("sum_lengths:", 4 * (a + b + c))
print("surface:", 2 * (a * b + b * c + a * c))
print("volume:", a * b * c)

#5

squirrels= 3
nuts= 14
print(nuts // squirrels)

#6

amount = 1000
interest_rate = 5
years = 1
# change the next line
income = amount * interest_rate * years / 100 

print(income)

#7

n = 3
print(((n + 1) * n + 2) * n + 3)

#8

n = int(input())  # Leer un número entero
print(n % 10)  
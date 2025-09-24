"""
Tipos de datos básicos

Cada objeto de datos (una variable o una constante ) tiene un tipo que describe cómo mantenerlo en la memoria, qué operaciones se pueden aplicar a este objeto y cómo ejecutar estas operaciones.

Una analogía de tipos en el mundo real se da mediante especies biológicas o cualquier otro atributo abstracto compartido entre objetos específicos. Por ejemplo, todos los perros que has visto tienen el tipo perro , pero cada uno es un objeto individual. Al considerar un perro como un tipo, puedes asumir que algunas operaciones están disponibles. Por ejemplo, un perro puede ladrar.

En este tema, consideraremos algunos de los tipos de datos más simples que se utilizan comúnmente en la práctica de programación.

Instrumentos de cuerda
Siempre que desee usar información textual en su programa, deberá trabajar con cadenas . En Python, el tipo de cadena se llama str. Las cadenas son extremadamente comunes y útiles. Como se mencionó, los literales de cadena pueden delimitarse mediante comillas simples o dobles.

Ejemplos de cadenas entre comillas dobles:
"""

print("")               # an empty string
print("string")         # one word
print("Hello, world!")  # a sentence

#Ejemplos de cadenas entre comillas simples:

print('a')                   # a single character
print('1234')                # a sequence of digits
print('Bonjour, le monde!')  # a sentence

#En un programa real, una cadena puede representar el correo electrónico de una persona o una organización.

print('hello@hyperskill.org')  # print an email

"""
¡Como puedes ver, las cuerdas son muy fáciles de usar!

""
Tipos numéricos
Los números son esenciales para cualquier programador. Es difícil escribir un programa sin ellos, así que analicemos algunos tipos numéricos básicos :
"""
int( enteros con signo ) . Llamados enteros o ints, son números (positivos, negativos o cero) que no tienen punto decimal.

float( números de punto flotante ) . Llamados flotantes, representan números reales y tienen un punto decimal.

#Puedes comenzar a trabajar con un número simplemente imprimiéndolo.

print(11)    # prints 11
print(11.0)  # prints 11.0

"""
Aunque 11y 11.0son el mismo número, el primero es un entero y el segundo es un punto decimal. La forma más sencilla de distinguirlos es mediante la coma decimal. Los puntos decimales tienen coma decimal , mientras que los enteros no. ¡Presta atención!

También puedes utilizar números negativos y ceros:
"""
print(0)      # prints 0
print(-5)     # prints -5
print(-1.03)  # prints -1.03

"""
Los números enteros pueden contar cosas en el mundo real, mientras que los números de punto flotante son una buena opción para cálculos estadísticos y científicos.

Tipos de impresión
También tenemos una forma de demostrar los tipos de diferentes objetos: usar la type()función , que es parte de Python.
"""
print(type('hello'))  # <class 'str'>
print(type("world"))  # <class 'str'>

print(type(100))      # <class 'int'>
print(type(-50))      # <class 'int'>

print(type(3.14))     # <class 'float'>
print(type(-0.5))     # <class 'float'>

"""
Como puede ver en los ejemplos anteriores, la type()función indica el tipo de datos de un valor pasado después de la palabra class .

Resumen
Esperamos que ahora tenga una idea general de los tipos de datos . Debe recordar los tipos más simples, stry int, floaty cómo escribir sus literales. En los siguientes temas, aprenderemos las características específicas de cada tipo. Si necesita saber el tipo de un objeto, imprímalo usando la type()función.
"""

#Ejercicios practicos

#1

print('1 2 3 4 5 6 7 8 9 10')

#2

#Integer

age = 26
print('Age:', age)

#Float 
height = 1.87
print('Height:', height)

#String
name = 'Jhon'
print('Name:', name)

#3

print('Supercalifragilisticexpialidocious')

#4

print(type("3.1415"))

#5
data = "Hello, world!"
data_type = type(data)
print(data_type)

#6
data = 42 
data_type = type(data)
print("El tipo de dato es:", data_type)

data = 3.14
data_type = type(data)
print("El tipo de dato es:", data_type)

#3

print(type("int"))
print(type(394))
print(type(2.12))

#4

print(10)

#5

var1 = 105
var2 = 'Hello'
var3 = 3.2

print(var1, type(var1))
print(var2, type(var2))
print(var3, type(var3))

#6

print(1.0000000000000001)

#7
celsius = float(input())
fahrenheit = celsius * 9/5 + 32
print(fahrenheit)


code3 = "Python\'s core and more"
print(code3)
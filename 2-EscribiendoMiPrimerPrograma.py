#Escribiendo el primer programa

"""
En este tema, aprenderás a desarrollar tus primeros programas en Python. Aunque son bastante simples, son sintácticamente correctos y demuestran que programar en Python es un placer.

El programa Hola Mundo
Nuestro primer ejemplo será "¡Hola Mundo!". Se usa tradicionalmente para introducir a los principiantes a un nuevo lenguaje de programación.
"""
print("Hello, World!")
"""
Como puede ver, este programa consta de una sola línea. Imprime la cadena pasada entre paréntesis, pero sin comillas. Puede ejecutar este código en línea. Para ello, copie el código a este sitio web y haga clic en el triángulo. También puede seguir estos consejos de instalación . Debería obtener este resultado:

Hello, World!

Aunque este código es muy simple, lo revisaremos a fondo.

Breve explicación
print es el nombre de una función. Una función es un bloque de código que realiza una función útil, por ejemplo, imprimir texto. En cierto sentido, una función es un subprograma que puede reutilizarse en los programas. Cuando el nombre de una función va seguido de paréntesis, significa que se llamó a la función para obtener el resultado.

Profundicemos: "Hello, World!"es una cadena de Python. Todas las cadenas se escriben entre comillas simples o dobles'Hello, World!' , por lo que también es una cadena válida. Puedes reemplazar esta cadena por otra y el programa la imprimirá. Por ejemplo:

print('Python 3.x')

Como puedes imaginar, este programa imprimirá lo siguiente:

Python 3.x

Cotizaciones de impresión
Imagine que la cadena que desea imprimir ya contiene comillas. Si desea incluirlas en una cadena, enciérrela entre comillas de otro tipo, por ejemplo:
"""
print("Yes, I'm ready to learn Python.")

"""
La parte de la cadena con I'mse imprime correctamente porque utilizó comillas dobles "..."para encerrar toda la cadena:

Yes, I'm ready to learn Python.

Escribir lo siguiente es incorrecto :
"""
print('Yes, I'm ready to learn Python.')

"""
Su programa no sabrá dónde comienza y termina la cadena.

Puedes ejecutar todos los ejemplos usando el sitio web proporcionado anteriormente. Esto te ayudará a familiarizarte con Python.

Posibles errores
Incluso las líneas de código más simples pueden contener errores. Los más comunes son:

Poner sangría adicional

"""
   print("Hello, World!")

"""
Esta afirmación no funciona debido a espacios adicionales antes de print.

Llamar a una función con el nombre incorrecto

"""
pint("Hello, World!")

""" 
Esta línea contiene pinten lugar de print. Asegúrese de referirse a cada función por su nombre apropiado.

Escribir nombres con mayúsculas y minúsculas incorrectas
"""
PRINT("All caps")
"""
Print, printy PRINTno son lo mismo. Los nombres distinguen entre mayúsculas y minúsculas en Python.

Falta una o ambas comillas en una cadena
"""
print("Python)
"""
Esta afirmación no funciona debido a que faltan comillas de cierre.

Faltan uno o más paréntesis
"""
print("I have no end"
"""
Tenga cuidado con los paréntesis, especialmente al llamar a una función.

Con la información anterior, no debería tener ningún problema grave con dichos programas.

Resumen
En este tema, escribimos nuestro primer programa en Python. Lo desglosamos, imprimimos algunas cadenas y analizamos los errores más comunes que puedes encontrar al principio.

"""
#Practicas

#1

print("Hollo,how's your day")

#2

fav_lang = "python"

print(fav_lang)

#3

print("Alice's adventure in wonderland")

#4

print("We love Python!")

#5

print("Hello, what is your name?")
user = input()
reply = "Nice to meet you, "+ user + "!"
print(reply)

#6

print("My name is Miqueas")

#7
print("2 + 2 = 4")
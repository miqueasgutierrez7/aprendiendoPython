"""
Tomando la entrada del usuario
A veces, los programas necesitan interactuar con los usuarios, ya sea para recibir datos o para entregar algún resultado. Y ahí es cuando la input() función cobra protagonismo.

Leyendo la entrada de un usuario
Los datos de entrada que queremos obtener son simplemente un valor introducido por el usuario. La input()función lee este valor y lo devuelve en un programa como una cadena. Por ejemplo, el siguiente programa lee el nombre de usuario e imprime un saludo.
"""
user_name = input()
print('Hello, ' + user_name)
"""
En la primera línea, el programa esperará a que el usuario introduzca una entrada. Asignaremos esta entrada a una variable para guardarla. En la segunda línea, el programa añade el nombre introducido al final de la 'Hello, 'cadena e imprime la frase completa como resultado.

Si un usuario ingresa Sauron, este programa imprime:

Hello, Sauron

Entonces, su programa imprime un resultado que depende de la entrada del usuario (nombre).

Mensajes claros
Es muy recomendable indicar claramente qué tipo de entrada esperamos de nuestros usuarios. Para ello, la input()función puede aceptar un argumento opcional, es decir, un mensaje:
"""
user_name = input('Please, enter your name: ')
print('Hello, ' + user_name)
"""
El programa se inicia, el usuario ve el mensaje, ingresa su nombre y obtiene el siguiente resultado:

Please, enter your name: Sauron
Hello, Sauron

Otra forma de hacerlo es imprimir el mensaje por separado:
"""
print('Enter your name: ')
user_name = input()
print('Hello, ' + user_name)
"""
En realidad, no hay mucha diferencia: en el ejemplo anterior, la entrada se imprimirá en la misma línea que el mensaje, mientras que en este caso se ingresará en la línea siguiente. Así que puedes elegir lo que prefieras.

Aunque se recomienda imprimir mensajes para los usuarios, evítelos en nuestros desafíos de programación educativa, de lo contrario, su código podría no pasar nuestras pruebas.

Detalles importantes
Profundicemos en algunos detalles.

En primer lugar, ¿cuánto tiempo puede durar la entrada del usuario y cómo entiende el programa que el usuario ha introducido todo lo que quería? Un detalle sobre la input()función: en cuanto el programa empieza a ejecutarla, se detiene y espera a que el usuario introduzca un valor y pulse Intro . Esto también significa que, si el usuario no introduce nada, el programa no se ejecutará.

¿Qué más debes recordar? Bueno, esto: cualquier valor que introduzcas, la función lo interpretará como una cadena . No importa si introduces dígitos o letras, la entrada se convertirá en una cadena.

Si quieres que una entrada sea un número , debes escribirlo explícitamente:
"""
print("What's your favorite number?")
value = int(input())  # now value keeps an integer number
"""
Sin embargo, tenga cuidado: en estas circunstancias, si un usuario ingresa un valor no entero, Erroraparecerá un .

Para leer varias entradas, debes llamar a la función más de una vez:
"""
day = int(input())  # 4
month = input()     # October
"""
¡Genial! ¿Por qué esta fecha? Es muy sencillo:
"""
print('Cinnamon roll day is celebrated on', month, day)
# Cinnamon roll day is celebrated on October 4
"""
Conclusión
¡Felicidades! Ahora ya sabes cómo trabajar con input()una función que te ayuda a interactuar con el usuario. Créenos, esto es algo que sin duda apreciarás al programar. Esto es lo que has aprendido:

no hay límite para la longitud de los datos de entrada, la función esperará hasta que el usuario presione Enter;

Puede agregar un mensaje al usuario junto con la solicitud de entrada;

La función interpreta cualquier valor ingresado como una cadena;

Los datos de entrada se pueden convertir posteriormente al tipo de datos que necesite.

"""

#Ejercicios

#1

# Take the user's current age as input
current_age = 1992

# Current year
current_year = 2025

# Calculate the birth year

# Print the birth year
print(current_year - current_age)

#2

print("Enter a number: ")
user_num = 10
# user enters 10
print(user_num + user_num)

#3

a = int(input())
b = int(input())
c = int(input())

print(a + b + c)


#4

a = float(input())
b = float(input())
print(a + b)

#5
nombre = "Sauron"
print("Hola, " + nombre)

#Bucle for
#Las computadoras son conocidas por su capacidad para realizar tareas que la gente considera aburridas y que consumen mucha energía. Por ejemplo, repetir tareas idénticas sin errores es una de ellas. En este tema, aprenderemos qué herramienta de Python puede ayudarte con esto, cómo implementarla y qué funciones puedes usar junto con ella.


for variable in iterable:
    statement


oceans = ['Atlantic', 'Pacific', 'Indian', 'Southern', 'Arctic']
for ocean in oceans:
    print(ocean)


#Las cadenas también son iterables, por lo que puedes deletrear una palabra, por ejemplo:

for char in 'magic':
    print(char)

#Función de rango Esta range() función permite especificar el número de iteraciones. Devuelve una secuencia de números que comienza en 0 (por defecto) y finaliza en un número determinado. Atención: el último número no aparecerá en la salida, ya que el proceso se inició desde 0.

for i in range(5):
    print(i)

#Puedes cambiar el valor inicial si no estás satisfecho con 0; además, puedes configurar el valor de incremento (paso) añadiendo un tercer parámetro:

for i in range(5, 45, 10):
    print(i)

#Si no vas a usar la variable contador en tu bucle, puedes mostrarla reemplazando su nombre con el símbolo de guion bajo:

for _ in range(100):
    do_smth()

#En el ejemplo anterior, no necesitamos la variable contador de ninguna manera; simplemente usamos el bucle para repetir la do_smth()función un número determinado de veces.

#Procesamiento de datos de entrada
#También puedes usar la input()función que permite al usuario asignar un valor a una variable y trabajar con él. De esta forma, obtendrás el mismo resultado que con el fragmento de código anterior:

word = input()
for char in word:
    print(char)


#¡Oh, mira! Puedes escribir un fragmento de código con un propósito práctico:

times = int(input('How many times should I say "Hello"?'))
for i in range(times):
    print('Hello!')

#Bucle anidado
#En Python, es fácil colocar un bucle dentro de otro: un bucle anidado . El tipo de bucle interno y externo no importa; primero se ejecuta el bucle externo, y luego el interno.

names = ['Rose', 'Daniel']
surnames = ['Miller', 'Smith']
for name in names:
    for surname in surnames:
         print(name, surname)


#Conclusión
#En resumen, forlos bucles son una forma eficiente de automatizar algunas acciones repetitivas. Puedes añadir variables y operaciones para crear bucles anidados. Además, puedes controlar el número de iteraciones con la ayuda de una range()función. ¡Ten cuidado con la sintaxis: una sangría extra o la falta de dos puntos pueden provocar un error!

#Para obtener más información sobre este tema, consulte la función range de Python y sus métodos en el blog de Hyperskill.

#Practica 1

for x in range(1, 3):
    for y in range(-2, 0):
        print(x * y)

#Practica 2

#FizzBuzz es un famoso desafío de programación que se utiliza en entrevistas para evaluar las habilidades básicas de programación. Es hora de que escribas tu propia implementación.
#Imprime los números del 1 al 100, ambos inclusive, siguiendo estas instrucciones:
#Si un número es múltiplo de 3, imprime "Fizz"en lugar de este número.
#Si un número es múltiplo de 5, imprime "Buzz"en lugar de este número.
#Para números que sean múltiplos de 3 y 5, imprime"FizzBuzz"
#Imprime el resto de los números sin cambios.


for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    else:
        print(x)





#Indices

#En Python, existen varios tipos de colecciones para almacenar datos. Las colecciones de elementos ordenados posicionalmente se denominan secuencias , y tanto las listas como las cadenas pertenecen a ellas. Cada elemento de una lista, así como cada carácter de una cadena, tiene un índice que corresponde a su posición. Los índices se utilizan para acceder a los elementos dentro de una secuencia. La indexación se basa en cero , así que si ves a alguien que cuenta desde cero, seguramente te has encontrado con un programador.

#Índices de elementos

#Para acceder a un elemento de una lista mediante su índice, debes usar corchetes. Agrega los corchetes después de la lista y, entre ellos, escribe el índice del elemento que deseas obtener.

#No olvides que los índices comienzan en 0, por lo que el índice del primer elemento es 0. El índice del último elemento es igual a len(list) - 1.

#Veamos el siguiente ejemplo:

colors = ['red', ''green', 'blue', 'yellow']

first_elem = colors[0]
second_elem = colors[1]
third_elem = colors[2]

#Las cadenas funcionan de la misma manera:

pet = "cat"

first_char = pet[0]   # 'c'
second_char = pet[1]  # 'a'
third_char = pet[2]   # 't'

#Posibles inconvenientes
#Al usar índices, es importante mantenerse dentro del rango de la secuencia: ¡obtendrá un error (llamado IndexError) si intenta acceder a un elemento con un índice inexistente!

colors = ['red', 'green', 'blue']
pet = "cat"

print(colors[2])
print(pet[2])

#Hay un obstáculo más en tu camino. Imagina que quieres cambiar uno de los elementos de una lista. Se puede hacer fácilmente:

colors = ['red', 'green', 'blue']

colors[1] = 'white'
print(colors)  # ['red', 'white', 'blue']

#Sin embargo, cuando se trata de cadenas de caracteres, dicha reasignación es imposible. Las cadenas, a diferencia de las listas, son inmutables, por lo que no se puede modificar su contenido con índices:

pet = "cat"

pet[0] = "b"
# TypeError: 'str' object does not support item assignment

#Índices negativos

#La forma más sencilla de acceder a los elementos al final de una lista o cadena es usar índices negativos : el signo menos antes del número cambia la perspectiva y permite ver la secuencia desde el final. Así, el último elemento de la lista, en este caso, tiene el índice -1 , y el primer elemento tiene el índice -len(list)(la longitud de la lista).

#Por ejemplo:

colors = ['red', 'green', 'blue']

last_elem = colors[-2]

print(last_elem)

second_elem = colors[-2]  # 'green'
first_elem = colors[-3]   # 'red'

pet = "cat"

last_char = pet[-1]    # 't'
second_char = pet[-2]  # 'a'
first_char = pet[-3]   # 'c'

Como puedes ver, funciona igual para listas y cadenas de texto.


Si escribes un índice negativo inexistente, también obtendrás un error IndexError. Ten cuidado con los índices para evitar errores de índices incorrectos en tu código.

La siguiente imagen muestra el concepto general de índices en una lista:

Índice de Python


#Resumen

#En este tema, hemos aprendido qué son los índices positivos y negativos en Python, cómo encontrar elementos en una lista mediante sus índices y qué errores pueden ocurrir al usarlos. Ahora que has aprendido el concepto de índices, ¡esperamos que de ahora en adelante no tengas ninguna dificultad al utilizarlos!

#Practicando

#Ejercicio 1

prices = input().split()

print(prices)


#Ejercicio 2

#imprimir la decimoquinta letra de esta cadena.

alphabet = input()
print(alphabet[14])

#Ejercicio 3

#acceder al último cálculo, pero no sabes cuántos cálculos se realizaron en total.
#Trabaja con la calculationsvariable e imprime el último cálculo.

# please, don't modify this variable
calculations = input().split()

# complete the code
print(calculationes[-1])

#Ejercicio 4

planets[4] = 'Jupiter'

#Ejercicio 5

#Los boletos de lotería son una especie de entretenimiento matemático. Un boleto se considera afortunado si la suma de sus tres primeros dígitos es igual a la suma de los tres últimos dígitos del número del boleto .

#Debes escribir un programa que compruebe si las dos sumas son iguales. El siguiente fragmento de código muestra "Lucky"si lo son y "Ordinary"si no lo son.


# Guardamos la entrada en la variable.

ticket = input()

# Sumamos los digitos de cada mitad.abs

half1 = int(ticket[0])+int(ticket[1])+int(ticket[2])
half2 = int(ticket[3])+int(ticket[4])+int(ticket[5])

# Gracia a ti este codigo funcionara

if half1 == half2:
   print("Lucky")
else:
   print("Ordinary")


#Ejercicio 6

# the following line reads the name from the input, do not modify it, please
name = input()

# your code here
print(name[0])


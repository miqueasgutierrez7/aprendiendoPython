#Invocar funciones

#Aunque invocar funciones en Python no es como lanzar un hechizo, a veces resulta de gran utilidad. Empecemos por el concepto. Una función es un fragmento de código estructurado que podemos usar en más de un lugar y en más de una ocasión. Además, las funciones nos permiten leer nuestro código y el de otros mucho mejor. ¿Acaso no se han convertido ya en tus herramientas favoritas?

#Aquí tienes una llamada a una función sencilla:

multiply(1,7)

#Aquí multiplyestá el nombre de la función, y los números entre paréntesis (1, 7)son sus argumentos . ¿Qué es un argumento? Bueno, es simplemente un valor que se utilizará dentro del cuerpo de la función. ¡Veamos esto con más detalle!

#Invocando print()

#Para llamar o invocar una función en tu programa, simplemente escribe su nombre y añade paréntesis después. ¡Eso es todo! Dato curioso: si alguna vez has escrito una expresión como esta , print("Hello, world!")ya sabes algo sobre funciones. En este pequeño ejemplo, sin embargo, vemos el mensaje "¡Hola, mundo!" entre paréntesis después del nombre de la printfunción. ¿Qué significa? Esta cadena es solo un argumento. Y, por lo general, las funciones tienen argumentos. En cuanto a la printfunción, podemos usarla sin ningún argumento o incluso con varios argumentos:

print("Hello, world!")
print()

#Y aquí está el resultado:

Hello, world!
Bye, then!

#Así pues, la primera llamada imprime una cadena, la segunda, printsin argumentos, imprime una línea vacía, y la última muestra nuestros dos mensajes como una sola expresión. ¿Te sorprenden estos resultados? Entonces puedes consultar la documentaciónprint para obtener más información sobre el funcionamiento de la función . La documentación de Python contiene todo tipo de información sobre la función que te interese, por ejemplo, qué argumentos espera.


#Funciones integradas

#Las funciones pueden facilitarnos la vida, siempre que conozcamos su existencia. Muchos algoritmos ya están escritos, por lo que no es necesario reinventarlos, salvo quizás con fines educativos. El intérprete de Python incluye varias funciones y tipos integrados , por lo que siempre están disponibles. Actualmente, el número de funciones integradas asciende a 71 (en la versión Python 3.13 ). Algunas se utilizan para convertir el tipo de objeto ; por ejemplo, str()devuelve una cadena, int()devuelve un entero y float()devuelve un número de coma flotante . Otras trabajan con números : se pueden round()usar sum()para calcular el mínimo min()o el máximo max(). Otras, en cambio, nos proporcionan información sobre el objeto: su type()tamaño o longitud len(). ¡Veamos cómo funcionan!

#En el siguiente ejemplo, len()se cuenta el número de caracteres en la cadena (lo mismo se aplica a cualquier secuencia , es decir, lista, tupla, rango, secuencias de bytes, matrices de bytes).

number = "111"

# finding the length of an object
print(len(number))  # 3


#Luego declaramos las variables integery float_number, convertimos nuestra cadena a los tipos correspondientes y escribimos su suma en my_sum. Por cierto, la sum()función trabaja con objetos iterables , por eso usamos paréntesis dobles.

# converting types
integer = int(number)  # 111
float_number = float(number)  # 111.0

# adding numbers
my_sum = sum((integer, float_number))

# El resultado es un número de punto flotante, lo cual se hace evidente después de imprimirlo my_sum

print(my_sum)  # 222.0
print(round(my_sum))  # 222

#Además, puedes ver cómo encontrar los valores mínimo y máximo: en este ejemplo, el número más pequeño es 3 y el número más grande 8.4 (la suma de 3 y 5.4) pertenece a los números de coma flotante.

# finding the minimum and the maximum
integer = 3
float_number = 5.4
my_sum = sum((integer, float_number))

print(min(integer, float_number))  # 3
print(type(max(integer, float_number, my_sum)))

help(len)

#Practicando

#Ejercicio 1

#Lee el texto tres veces. Cada entrada contiene la edad de una persona: Jack, Alex y Lana. Encuentra a la persona más joven y imprime su edad

jack_age = 22
alex_age = 42
lana_age = 34

print(max(jack_age, alex_age, lana_age))



#Declaración de funciones

#Con frecuencia, las funciones integradas no son suficientes ni siquiera para principiantes. En tal caso, no queda más remedio que crear una función propia. Veamos cómo hacerlo.

#Def para Definir
#Puedes crear tu propia función usando la palabra clave def(correctamente, derivada de define ). Veamos la sintaxis:

def function_name(parameter1, parameter2, ...):
    # function's body
    ...
    return "return value"


#Después def, escribimos el nombre de nuestra función (para invocarla posteriormente) y los nombres de los parámetros que nuestra función puede aceptar, entre paréntesis. No olvides los dos puntos al final de la línea. Los nombres de una función y sus parámetros siguen la misma convención que los nombres de las variables , es decir, deben escribirse en minúsculas con guiones bajos entre las palabras .

#Una sangría de 4 espacios indica al intérprete dónde comienza y dónde termina el cuerpo de la función. Todas las instrucciones dentro del cuerpo de la función deben estar sangradas. Se pueden realizar cálculos dentro de la función y usar la returnpalabra clave para devolver el resultado. La definición de la función solo finaliza cuando no hay sangría.

#Posteriormente, los parámetros toman los valores que se pasan en una llamada a la función . Estos valores que pasamos a una función se conocen como argumentos . La única diferencia entre parámetros y argumentos es que introducimos los parámetros en la definición de la función y proporcionamos argumentos (valores específicos) en la llamada a la función. He aquí un ejemplo menos abstracto de una función:

# Function definition
def multiply(x, y):
    return x * y


# Function calls
a = multiply(3, 5)   # 15
b = multiply(a, 10)  # 150

#En caso de que no desee pasar ningún argumento, los paréntesis permanecen vacíos:

def welcome():
    print("Hello, people!")

También puedes declarar una especie de función vacía con la passinstrucción:

# This function does nothing (yet)
def lazy_func(param):
    pass

#Si eliges llamar a la función lazy_func()con un valor arbitrario como argumento, no sucederá nada. Por lo tanto, passes solo un marcador de posición, pero al menos tu código será válido con él.

#Parámetros vs argumentos
#Ahora mismo no está del todo claro qué son los parámetros, ¿verdad? De hecho, los parámetros son simplemente alias de valores que se pueden pasar a una función. Consideremos el siguiente ejemplo:

def send_postcard(address, message):
    print("Sending a postcard to", address)
    print("With the message:", message)


send_postcard("Hilton, 97", "Hello, bro!")
# Sending a postcard to Hilton, 97
# With the message: Hello, bro!

send_postcard("Piccadilly, London", "Hi, London!")
# Sending a postcard to Piccadilly, London
# With the message: Hi, London!


#Como puede observar, esta función es un fragmento de código reutilizable que puede ejecutarse con diferentes argumentos, es decir, con diferentes valores. Aquí, addressy messageson simplemente alias, bajo los cuales la función recibe valores y luego los procesa en su cuerpo.

#Esta función requiere exactamente 2 argumentos, por lo que no podrá ejecutarla con más o menos de 2 argumentos:

send_postcard("Big Ben, London")

TypeError: send_postcard() missing 1 required positional argument: 'message'

#Ejecución y retorno

#Nuestra función anterior solo realizaba algunas acciones, pero no devolvía ningún valor . Sin embargo, es posible que desees calcular algo dentro de una función y devolver el resultado en algún momento. Consulta el siguiente ejemplo:

def celsius_to_fahrenheit(temps_c):
    temps_f = temps_c * 9 / 5 + 32
    return round(temps_f, 2)


# Convert the boiling point of water
water_bp = celsius_to_fahrenheit(100)
print(water_bp)  # 212.0

#La palabra clave returnse usa para indicar los valores que devuelve la función. Básicamente, es el resultado de la llamada a la función. Así, en el ejemplo anterior, hemos almacenado el valor devuelto por nuestra función en la variable water_bp. Para asegurarnos, imprimimos el resultado.

#Otro punto a mencionar es que las funciones no necesariamente devuelven valores. De hecho, la conocida print()función no devuelve nada. Examine el siguiente código:

chant = print("We Will Rock You")
print(chant)
print(chant + "!")

Y su resultado:

We Will Rock You
None
Traceback (most recent call last):
  ...
TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'

#Declaramos la variable chante invocamos print(). Obviamente, la función se ejecutó. Pero la variable en sí resultó ser el Noneobjeto, lo que significa que la función llamada no tenía nada que devolver. El valor de chantes None.

#Por eso falla la última línea. Python intenta agregar "!"a chant, pero Noneno se puede agregar a una cadena. El mensaje de error lo indica: el operando izquierdo es de tipo NoneType, el derecho es de tipo str.



Resumen
Así pues, hemos aprendido la sintaxis para declarar funciones. Ahora también sabes que:

#Los parámetros de una función son simplemente alias o marcadores de posición para los valores que se les pasarán. Los parámetros se reinicializan cada vez que se llama a la función. Dentro de la función, se tiene acceso a estos valores, lo que significa que se pueden realizar cálculos con ellos.

#Una función puede simplemente realizar una acción sin devolver nada o devolver un resultado específico. Si su función no devuelve nada, asignar su resultado a una variable o imprimirlo le dará None.

#Declarar tus propias funciones hace que tu código sea más estructurado y reutilizable. Siempre que uses el mismo fragmento de código más de una vez, ¡intenta crear una función para él!
#Fundición de tipos

#La informática, como cualquier otra ciencia, tiene una base teórica sólida. Siempre es útil conocer algunos fundamentos teóricos del lenguaje de programación que se está aprendiendo o utilizando. Esto puede ayudar a comprender mejor el lenguaje o las diferencias entre varios. En este tema, aprenderemos teoría sobre tipos en Python y veremos cómo funciona en la práctica.

#Tipado dinámico frente a tipado estático
#Python es un lenguaje de tipado dinámico y fuertemente tipado . El tipado dinámico implica que solo los objetos en tiempo de ejecución (valores) tienen un tipo, pero no las variables que los almacenan. Es posible almacenar varios valores de diferentes tipos en una sola variable durante la ejecución del código sin que se produzcan errores.

#El siguiente código es totalmente válido:


v = 10  # variable v stores an integer value

v = 'hello'  # v now stores a string

#Tipificación fuerte vs. débil

El tipado fuerte significa que no se producen conversiones de tipo implícitas.
Por ejemplo, aunque"125"consta solo de dígitos, es una cadena. Para usarla en operaciones aritméticas, es necesario cambiar su tipo a un entero u otro tipo numérico .
Intentar usarla tal cual conduce a un errorTypeError.

>>> "125" + 10
...
TypeError: can only concatenate str (not "int") to str
#Si Python tuviera un sistema de tipos débil , dicho valor podría interpretarse como un entero para realizar la operación correctamente. Este comportamiento, en el que uno de los operandos se convierte implícitamente al tipo de otro operando, se denomina coerción de tipos .

Dado que en Python no existe la conversión de tipos, el mismo operando puede dar resultados diferentes según los tipos de los argumentos proporcionados. Por ejemplo, se pueden sumar dos cadenas para obtener una concatenación . También es posible multiplicar una cadena por un número entero.

print(125 + 125)  #  250

print("125" + "125")  # "125125"

print(125 * 4)  # 500

print("125" * 4)  # "125125125125"

print("This is a number:", 125)  # "This is a number: 125"

El ejemplo también muestra que se pueden imprimir valores de diferentes tipos separándolos con comas entre paréntesis.
La print()función imprimirá todos los argumentos separados por un espacio.


Conversión de tipos explícita
El proceso de convertir un valor a otro tipo también se denomina conversión de tipos . Si bien la conversión implícita de tipos casi no está permitida en Python, a menudo necesitarás definir una conversión de tipo explícita en tu código. Esto sucede con frecuencia al trabajar con la entrada del usuario.

Imagina que estás sumando dos números, uno de los cuales es intde tipo y el otro es de floattipo . En este caso, durante la operación de suma, intel tipo se convertirá a float, pero la variable en sí no cambiará de tipo. Este ejemplo se muestra en el código a continuación.

a = 5
print(type(a))  # <class 'int'>

b = 0.7
print(type(b)) # <class 'float'>

c = a + b
print(type(c)) # <class 'float'>

print(a, type(a)) # 5 <class 'int'>

a = 5
print(type(a))  # <class 'int'>

b = 0.7
print(type(b)) # <class 'float'>

c = a + b
print(type(c)) # <class 'float'>

print(a, type(a)) # 5 <class 'int'>

Imagina que le pides a un usuario que proporcione una edad que luego usarás en algunos cálculos. Para convertir una cadena a un tipo entero, puedes usar la función integrada int(). Este es un ejemplo de conversión de tipo explícita .

raw_age = "22"
print(type(raw_age))  # <class 'str'>

age = int(raw_age)
print(type(age))  # <class 'int'>

Esta typefunción se utiliza para determinar el tipo de valor proporcionado.

Para convertir un entero al tipo cadena, utilice la str()función:
age = 22
print(type(age))  # <class 'int'>

string_age = str(age)
print(type(string_age))  # <class 'str'>

Como habrás notado, para convertir un valor a un tipo específico, usamos la función del mismo nombre. Si no se permite la conversión entre dos tipos, verás un error. Además de las str()funciones int()que vimos anteriormente float(), también existe una función que convierte un valor dado al tipo float.

Aquí hay algunos ejemplos más de conversión entre diferentes tipos:

f = 3.14  # the type is float
print(type(f))  # <class 'float'>

s = str(f)  # converting float to string
print(type(s))  # <class 'str'>

i = int(f)  # while converting a float value to an integer its fractional part is discarded
print(i)  # 3
print(type(i))  # <class 'int'>

f = float(i)
print(f)  # 3.0
print(type(f))  # <class 'float'>

#Resumen
#Este tema explora la naturaleza del sistema de tipos de Python, destacando que es tanto de tipado dinámico como de tipado fuerte. El tipado dinámico implica que las variables no tienen tipos fijos y pueden cambiar de tipo en tiempo de ejecución, a diferencia del tipado estático, donde los tipos se verifican en tiempo de compilación. El tipado fuerte garantiza que las operaciones con tipos incompatibles generen errores, evitando la conversión de tipos no deseada, en contraposición al tipado débil, que permite conversiones de tipo implícitas . Python también admite la conversión explícita de tipos, lo que permite a los desarrolladores convertir manualmente los tipos de datos para garantizar la compatibilidad y el comportamiento deseados.


#ejemplo1
word = input()

# Change the next line
print(word+word)


a = int("10.3")

print(a)

#Ejemplo2

n = 2.777
print(str(float(int(n))))

#Ejemplo3

try:
    dollar_amount = input("Enter the amount in dollars: ")
    dollar_float = float(dollar_amount)
    euro_amount = round(dollar_float * 0.85, 2)
    print(euro_amount)

except ValueError:
    print("Invalid input. Please enter a valid number.")

print(1.0 * 2)


#Ejemplo4

n = 12345
# put your python code here
print(str(n)*100)
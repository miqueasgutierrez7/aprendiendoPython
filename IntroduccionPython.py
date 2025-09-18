"""
¿Hablas Python?
Dado el énfasis de Python en la simplicidad, ya estás equipado para comprender y recrear programas básicos con facilidad.
Creemos el clásico programa "¡Hola, mundo!", un saludo amistoso desde tu computadora:
"""

print("Hello, world!")

"""
¡Puedes reemplazar la frase dentro de los paréntesis para crear tu propio programa Python!
Las funciones y métodos integrados de Python tienen nombres intuitivos, lo que facilita su comprensión. A continuación, se explica cómo usarlos input()para solicitar datos de usuario:
""" 

age = input("How old are you? ")
print("I know, that you're " + age + " years old")


#El uso de la sangría en Python para la estructura, a diferencia de las {}llaves o el punto y coma en muchos otros lenguajes, es otra característica que te resultará sencilla. Observa cómo la sangría ayuda a delinear los elementos de la sentencia if-else :


age = input("How old are you? ")
if age > 18:
    print("You're adult")
else:
    print("You're minor")


#Para mejorar la comprensión del código, también podemos usar #comments. Estas líneas no se ejecutan y describen el objetivo del código:

# Define a function that acts like a parrot
# Which repeats the things you say back to you

def parrot():
    answer = input()
    print(answer)



"""
 Call the parrot function
parrot()
Por ahora, no necesitas entender cómo funcionan todas estas líneas de código: aprecia su hermosa sintaxis, que no se aleja demasiado del inglés cotidiano. No tengas miedo de experimentar y equivocarte: ¡así se aprende!
"""

#Ejercicios practicos
#1 
#programa pregunta al usuario si el día es su cumpleaños e imprime un mensaje de cumpleaños si lo es. 

user_birthday = input("Is it your birthday today? ")
if  user_birthday== "yes":
    print("Happy birthday!")

#2
"""
Creando una función para sumar dos números enteros
Reportar un error tipográfico
De vez en cuando, puede que necesites ajustar el código de otra persona para un propósito diferente. Aquí es cuando leer código resulta útil. ¡Hagámoslo!
Escanea #commentsel código a continuación y luego complétalo rellenando los espacios en blanco. Puede que aún no entiendas todas las líneas de código, pero sin duda puedes usarlo, ¡con tu intuición para el lenguaje!
"""

#3


# Define a function that adds two numbers
def add_numbers(num1, num2):
    return num1 + num2  # ✅ Bien indentado
result = add_numbers(3, 4)

# Print the result

print("The sum of the numbers is " + str(result)) 
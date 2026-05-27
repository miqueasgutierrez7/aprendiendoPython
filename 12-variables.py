"""
Variables

Puedes usar un lenguaje de programación como Python para realizar cálculos o trabajar con valores constantes como cadenas. ¿Te basta con esto? Al escribir programas reales, normalmente necesitas almacenar valores o resultados de evaluación en la memoria del ordenador.

¿Qué es una variable?
Una variable es un lugar con nombre donde se puede almacenar un valor para acceder a él más tarde. Imagina una caja donde guardas algo. Eso es una variable.

Por ejemplo, si calcula un resultado y desea reutilizarlo en otro lugar, puede usar este cuadro para ahorrar tiempo.

En general, es una buena práctica darle a una variable un nombre que describa su contenido.

Definir una variable y asignarle valores
Se puede conservar prácticamente cualquier valor en variables asignando un valor a una variable con nombre mediante un signo igual. Según PEP 8 , se recomienda dejar un espacio antes y después del signo de asignación.
"""
day_of_week = "Monday"
"""
Ahora tienes un valor de cadena "Monday"almacenado en la memoria de la computadora. Puedes recuperarlo llamando a la variable `name` .
"""
print(day_of_week)  # Monday

#day_of_weekalmacena un valor del strtipo.

print(type(day_of_week))  # <class 'str'>

#Siempre puedes asignar un nuevo valor a una variable definida.

day_of_week = "Tuesday"

#Ahora, recuperarás otro valor:

print(day_of_week)  # Tuesday

#Es posible asignar el valor de una variable a otra variable:

a = 10
b = a  # b is 10

#Si no ha definido una variable dentro del alcance de su código, verá un error cuando intente usarla:

print(month_name)  # NameError: name 'month_name' is not defined

#Python permite asignar valores de diferentes tipos a la misma variable. Asignemos la cadena de un mes a una variable e imprimamos su tipo.

month = "December"
print(type(month)) # <class 'str'>

#Ahora, asignemos el número de este mes a la variable e imprimamos nuevamente su tipo.

month = 12
print(type(month))  # <class 'int'>
"""
Esta tarea funciona porque Python es un lenguaje con tipado dinámico .

¡Por favor, no abuses del tipado dinámico! Si tu código es largo, podrías olvidar que cambiaste el tipo de una variable. ¡Esta es una causa común de errores!

Reglas de nomenclatura
Como se mencionó anteriormente, cada variable tiene un nombre que la distingue de las demás. Existen algunas reglas para nombrar variables que se deben seguir:

Los nombres distinguen entre mayúsculas y minúsculas ( monthno es lo mismo que Month).

Un nombre comienza con una letra o un guion bajo, seguido de letras, dígitos o guiones bajos (por ejemplo, user_name, score1, _count).

Un nombre no puede comenzar con un dígito (por ejemplo, 2qno es válido).

Un nombre no debe ser una palabra clave.

No rompa estas reglas; de lo contrario, su programa no funcionará.

Conclusión

"""

#Ejercicios Practicos

#1

holiday = "Cinnamon Roll Day"

print(holiday)

#2

name = "Jhon"
age = 20
gpa = 3.9
is_student = True

print("Name:" + name)
print("Age:"+ str(age))
print("GPA:"+ str(gpa))
print("Is student:" + str(is_student))

#3
name = 'Harry'
print(type(name))

#4 
number = 10

#5

name = "John Doe"
age = 25
is_graduated = True
print("Name:"+ name)
print("Age:"+ str(age))
print("Graduated:" + str(is_graduated))

#6
a = "Trues"
b = 10
a = b
b = a
print(b)

print(type(b))

#7
a = 10
b = 20
c = 30
a = c
b = a
d = c
c = a


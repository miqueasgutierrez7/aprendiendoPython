#Tipos booleanos y operaciones. Verdadero y falso.
"""
En los lenguajes de programación, el tipo booleano, o lógico, es una forma común de representar algo que solo tiene dos estados opuestos, como " on " o "off" , "yes" o "no" , etc. Es un tipo muy útil que comprobarás rápidamente al empezar a trabajar en tus proyectos o incluso al escribir pequeños programas. En este tema, analizaremos el tipo booleano en Python y aprenderemos a usarlo.

tipo booleano
El tipo booleano , o simplemente bool, es un tipo de dato especial que solo tiene dos valores posibles: Truey False. En Python, los nombres de los valores booleanos empiezan con mayúscula.

Si está escribiendo una aplicación que realiza un seguimiento de las aperturas de puertas, le resultará natural utilizar boolpara almacenar el estado actual de la puerta.
"""
is_open = True
is_closed = False

print(is_open)    # True
print(is_closed)  # False
"""
Operaciones booleanas
Hay tres operadores booleanos integrados en Python: and, ory not. Los dos primeros son operadores binarios , lo que significa que requieren dos operandos. notComo es un operador unario , siempre se aplica a un solo operando. Primero, veamos cómo estos operadores se aplican a los valores booleanos.

y es un operador binario, toma dos argumentos y devuelve Truesi ambos argumentos son verdaderos, de lo contrario, devuelve False.
"""
a = True and True    # True
b = True and False   # False
c = False and False  # False
d = False and True   # False

#o es un operador binario, retorna Truesi al menos un argumento es verdadero, de lo contrario, retorna False.

a = True or True    # True
b = True or False   # True
c = False or False  # False
d = False or True   # True

#not es un operador unario, invierte el valor booleano de su argumento.

to_be = True           # to_be is True
not_to_be = not to_be  # not_to_be is False
"""
La precedencia de las operaciones booleanas
Los operadores lógicos tienen una prioridad diferente, lo que afecta el orden de evaluación. A continuación, se muestran los operadores en orden de prioridad:

1.not

2.and

3.or

Entonces, notse considera primero, luego and, finalmente or. Teniendo esto en cuenta, considere la siguiente expresión:

print(False or not False)  # True

Primero, se evalúa la pieza not Falsey, tras la evaluación, obtenemos False or True. Esto da como resultado True, si recuerda la sección anterior.

Aunque tratar únicamente con valores booleanos puede parecer obvio, será muy importante recordar la precedencia de las operaciones lógicas cuando comience a trabajar con los llamados valores verdaderos y falsos .

Valores de verdad y falsedad
Aunque Python tiene el tipo de dato booleano, a menudo queremos usar valores no booleanos en un contexto lógico. Python permite comprobar la veracidad de casi cualquier objeto. Cuando se usan con operadores lógicos, los valores de tipos no booleanos, como enteros o cadenas, se denominan truey o falsy . Depende de si se interpretan como Trueo False.

Los siguientes valores se evalúan Falseen Python:

constantes definidas como falsas: None, False,

cero de cualquier tipo numérico: 0, 0.0,

secuencias y contenedores vacíos : "", [], {}.

Cualquier otra cosa generalmente se evalúa como True. Aquí hay un par de ejemplos:
"""
print(0.0 or False)  # False
print("True" and True)  # True
print("" or False)  # False

"""

En términos generales, andpodría ortomar cualquier argumento que pueda probarse para obtener un valor booleano.

Ahora podemos demostrar más claramente la diferencia en la precedencia de operadores:
"""
# `and` has a higher priority than `or`
truthy_integer = False or 5 and 100  # 100
"""
Nuevamente, descompongamos la expresión anterior en partes. Dado que el operador andtiene mayor prioridad que or, debemos analizar la 5 and 100parte. Tanto 100como 5son valores verdaderos, por lo que esta operación devolverá 100. Nunca antes se ha visto esto, así que es natural preguntarse por qué tenemos un número en lugar del Truevalor. La explicación es la siguiente:

Los operadores ory anddevuelven uno de sus operandos, no necesariamente de tipo booleano (ver detalles a continuación). Sin embargo, notsiempre devuelve un valor booleano.

anddevuelve el primer valor si se evalúa como False, de lo contrario, devuelve el segundo valor.
"""
>>> False and True
False
>>> True and True
True
>>> True and False
False
"""
ordevuelve el primer valor si se evalúa como True, de lo contrario, devuelve el segundo valor.
"""
>>> True or False
True
>>> False or True
True
>>> True or True
True
>>> False or False
False
"""
Volviendo a la expresión original, puedes ver que la última parte False or 100hace exactamente lo mismo, retorna 100en lugar de True.

Otro ejemplo complicado es el siguiente:
"""
tricky = not (False or '')  # True
"""
Un par de paréntesis permite especificar el orden en que se realizan las operaciones. Por lo tanto, primero evaluamos esta parte de la expresión: False or ''. Este operando ''se evalúa Falsey ordevuelve esta cadena vacía. Dado que el resultado de la expresión encerrada se niega, obtenemos True: not ''es igual a True. ¿Por qué no obtuvimos, por ejemplo, una cadena no vacía? El notoperador crea un nuevo valor, que por defecto es de tipo booleano. Por lo tanto, como se mencionó anteriormente, el operador unario siempre devuelve un valor lógico.

Evaluación de cortocircuito
Finalmente, cabe mencionar que los operadores lógicos en Python se acortan . Por eso también se denominan perezosos . Esto significa que el segundo operando de dicha expresión solo se evalúa si el primero no es suficiente para evaluar toda la expresión.

x and ydevuelve x si x es falso; de lo contrario, evalúa y devuelve y.

x or ydevuelve x si x es verdadero; de lo contrario, evalúa y devuelve y.

Por ejemplo:
"""
# division is never evaluated, because the first argument is True
lazy_or = True or (1 / 0)  # True

# division is never evaluated, because the first argument is False
lazy_and = False and (1 / 0)  # False
"""
Resumen
En este tema, aprendimos sobre un tipo booleano en Python, qué operaciones booleanas tiene ( not, and, or) y su prioridad. También nos familiarizamos con el concepto de valores verdaderos y falsos y por qué los operadores lógicos en Python se denominan cortocircuitados. Estos fueron los fundamentos de los valores booleanos y las operaciones lógicas en Python. ¡Es muy útil conocerlos desde el principio!
"""

llueve = False

if llueve:
    print("Lleva paraguas")
else:
    print("No necesitas paraguas")

a = 10
b = 5

print(a > b)    # True
print(a == b)  
print(5 and 0 and 12)
print(5 or " ")

x = False
y = True
z = x and y
result = "The result of 'True and False' is " + str(z)
print(result)

b = False
a = True

resultado = a or b
print(resultado)


suario_activo = False
tiene_permisos = True

if usuario_activo and tiene_permisos:
    print("Acceso permitido")
else:
    print("Acceso denegado")



    nombre = ""  # Usuario no ingresó nada

saludo = nombre or "Invitado"
print(f"Hola, {saludo}")

#3

is_raining = True
is_sunny = False

print(not is_raining and is_sunny)


#4


nota = 7
aprobado = nota >= 6
print("¿El estudiante aprobó?", aprobado)


#5

nota = 9
asistencia = 90

# Para tener beca, necesita nota >= 8 y asistencia >= 85%
tiene_beca = nota >= 8 and asistencia >= 85
print("¿El estudiante tiene beca?", tiene_beca)

#6

entrego_tarea = True

if not entrego_tarea:
    print("El estudiante NO entregó la tarea.")
else:
    print("El estudiante SÍ entregó la tarea.")


#7

nota = 8
asistencia = 90

# ¡Cuidado! Aquí el not se aplica solo a (nota >= 8)
resultado = not (nota >= 8 and asistencia >= 85)

print("Resultado:", resultado)




#8


# Example of an applicant's characteristics
credit_score = 750
annual_income = 60000
has_collateral = True
has_existing_loan = False

# This criterion should be True if the applicant's annual income is at least $50,000 or they have collateral
income_criterion = (annual_income >= 50000 or has_collateral)

# Decision: check if all of the criteria are satisfied
is_approved = (credit_score > 700 and income_criterion and not has_existing_loan)

# Output the decision
print("Loan Approved:", is_approved)


#9

a = True
b = not a


print(not (a and b))

print(not None or 1)
"Si la declaración

Hay situaciones en las que tu programa necesita ejecutar cierto código solo si se cumple una condición específica. Es posible establecer esa condición en Python y, en este tema, ¡vamos a aprender cómo hacerlo!

En Python, un fragmento de código que solo debe ejecutarse bajo ciertas condiciones debe colocarse dentro del cuerpo de una sentencia `if` . El patrón es el mismo que en inglés: primero se usa la palabra clave `if` if, luego la condición y, finalmente, una lista de expresiones a ejecutar. La condición siempre es una expresión booleana , es decir, su valor es verdadero Trueo falso . Aquí hay un ejemplo de cómo debería verse Falseel código con una expresión condicional "":

biscuits = 10
if biscuits >= 5:
    print("It's time for tea!")

"Tenga en cuenta que la condición termina con dos puntos y cada nueva línea comienza con una sangría . Generalmente, se utilizan 4 espacios para indicar cada nivel de sangría. Un fragmento de código en el que todas las líneas tienen el mismo nivel de sangría se denomina bloque de código . En Python, solo se utiliza la sangría para separar diferentes bloques de código; por lo tanto, solo la sangría indica qué líneas de código deben ejecutarse cuando ifse cumple la condición y cuáles deben ejecutarse independientemente de ifella. Vea el siguiente ejemplo:"

biscuits = 10
if biscuits >= 5:
    print("It's time for tea!")
    print("What tea do you prefer?")
print("What about some chocolate?")

Practica
Ejercicio 1:
"Alex escribió un programa que lee "a" numbery "a" wordde la entrada para crear frases como "3 cats""y" "1 dog". Desafortunadamente, la condición para sustantivos plurales no está implementada. Alex no sabe cómo usar sentencias condicionales , pero tú sí. Ayuda a Alex a completar este programa.

La forma plural de una palabra generalmente termina en s . Todos los números, excepto el 1 , esperan la forma plural después de ellos, incluso el cero: "0 birds".

Las palabras cuyo plural no se forma añadiendo una "s" NO aparecerán en las pruebas."



number = 12
word = "dos"

if number == 1:
    print(f"{number} {word}")
else:
    print(f"{number} {word}s")
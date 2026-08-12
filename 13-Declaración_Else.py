# Declaración if-else

Establecer condiciones es una herramienta muy popular y útil en programación. A veces, comprobar si una condición es verdadera o falsa no es suficiente: puede que queramos ejecutar un fragmento de código cuando la condición es verdadera y otro distinto cuando es falsa. Para estas situaciones, Python ofrece la sentencia `if-else`.

## Sintaxis básica

Una sentencia `if-else` es una expresión condicional que contiene la palabra clave adicional `else`. El bloque de código dentro de `else` se ejecuta cuando la condición del `if` no se cumple (evaluación booleana `False`). Dado que `else` es la alternativa al `if`, solo se ejecuta uno de los dos bloques.

```python
if today == "holiday":
	print("¡Tienes suerte!")
else:
	print("Ánimo, que sea un buen día.")
```

Observa que la regla de sangría de 4 espacios también se aplica aquí.

## Operador ternario (if-else en una línea)

Para expresiones condicionales cortas, Python permite escribir un `if-else` en una sola línea, llamado operador ternario:

```python
print("Es de día" if sun else "Es de noche")
```

Forma general:

```
first_alternative if condition else second_alternative
```

Úsalo con moderación: es práctico, pero no sacrifiques legibilidad.

## If-else anidado

Las sentencias `if-else` se pueden anidar igual que las `if` simples. Es posible incluir otra expresión condicional dentro de la rama `if` o dentro de la rama `else`. Recuerda mantener la indentación correcta para que el flujo sea claro:

```python
if x < 100:
	print('x < 100')
else:
	if x == 100:
		print('x = 100')
	else:
		print('x > 100')
	print('Esto se imprimirá porque x >= 100')
```

## Resumen

- **`else`**: se utiliza para dar una alternativa cuando la condición del `if` no se cumple.
- **No requiere condición**: a diferencia del `if`, `else` no lleva expresión booleana.
- **Mutuamente excluyentes**: en una estructura `if-else` sólo se ejecuta un bloque.
- **Anidamiento**: las sentencias `if-else` pueden anidarse para manejar varias condiciones.

## practicando;

## Ejercicio1;


corrector ortográfico sencillo que te indique si una palabra está escrita correctamente. Utiliza el diccionario que aparece en el código a continuación: contiene la lista de todas las palabras escritas correctamente.

word = input().strip()

if word in dictionary:
    print("Correct")
else:
    print("Incorrect")

### Ejercicio2;

# Escribe un programa que compruebe si un año es bisiesto.
# Un año se considera bisiesto si es divisible por 4 pero NO por 100,
# o si es divisible por 400. Por lo tanto, el año 2000 es bisiesto y el 2100 no lo es.
# Genera como salida "Leap" u "Ordinary" dependiendo de la entrada.

year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap")
else:
    print("Ordinary")

### Ejercicio 3

Signo opuesto
Informar de un error tipográfico
Lee un número entero como entrada. Cambia el signo de este número (es decir, conviértelo en negativo si era positivo, o en positivo si era negativo). Ten en cuenta que el cero permanece inalterado al cambiar su signo.

A continuación, imprime dos líneas de salida:

El número entero de entrada con su signo cambiado

Uno de los siguientes mensajes:
- The number is negativesi el número resultante es menor que cero
- The number is positivesi el número resultante es cero o mayor

## Ejercicio 4

##fragmento de un programa que te indica cuál es el mejor momento para visitar una ciudad en particular

city = "..."
summer = "Barcelona, Rome, Istanbul, Lisbon, Paris"
winter = "Oslo, Helsinki, Sydney, Cape Town, Vienna"

if (city in summer) or (city in winter):
    if city in summer:
        print("You should visit it in the summer!")
    else:
        print("You should visit it in the winter!")
else:
    print("I don't know what the best season is :(")


## Ejercicio 5
##Escribas un programa que encuentre el mínimo y el máximo.

Escribe un programa que reciba dos números enteros como entrada, cada uno en una línea nueva. La salida debe mostrar:

El número más grande en la primera línea
El número más pequeño de la segunda línea.

a = int(input())
b = int(input())

# Comparar usando if
if a > b:
    print(a)  # número más grande
    print(b)  # número más pequeño
elif b > a:
    print(b)  # número más grande
    print(a)  # número más pequeño
else:
    # Si son iguales, se muestran ambos
    print(a)
    print(b)

#Ejercicio 6

si la temperatura supera los 30 grados, el programa muestre "Hace mucho calor hoy" y, en caso contrario, "No hace tanto calor". Asegúrate de implementar la estructura de control de flujo correcta para que el programa funcione como se espera.

temperature = 30

response = "It's really hot today."
if temperature > 30:
    response = "It's really hot today."
else:
    reponse = "It's not so hot today."


#Ejercicio 7



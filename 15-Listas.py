# Listas

#Muy a menudo necesitas agrupar varios elementos para procesarlos como un solo objeto. Para ello, necesitarás utilizar diferentes colecciones. Una de las colecciones más importantes y útiles en Python es una lista .

#Creación e impresión de listas

#Observe una lista sencilla que almacena varios nombres de razas de perros:
dog_breeds = ['corgi', 'labrador', 'poodle', 'jack russell']
print(dog_breeds)  # ['corgi', 'labrador', 'poodle', 'jack russell']

#En la primera línea, usamos corchetes para crear una lista que contiene cuatro elementos y luego la asignamos a la dog_breedsvariable. En la segunda línea, la lista se imprime a través del nombre de la variable. Todos los elementos se imprimen en el mismo orden en que se almacenaron en la lista porque las listas están ordenadas .

#Aquí hay otra lista que contiene cinco números enteros:

numbers = [1, 2, 3, 4, 5]
print(numbers)  # [1, 2, 3, 4, 5]

#Otra forma de crear una lista es invocando la listfunción. Esta se utiliza para crear una lista a partir de un objeto iterable : es decir, un tipo de objeto cuyos elementos se pueden obtener uno a uno. El concepto de iterabilidad se explicará con detalle más adelante, pero veamos los ejemplos a continuación:

list_out_of_string = list('danger!')
print(list_out_of_string)  # ['d', 'a', 'n', 'g', 'e', 'r', '!']

list_out_of_integer = list(235)  # TypeError: 'int' object is not iterable

#Así pues, la listfunción crea una lista que contiene cada elemento del objeto iterable dado . Por ahora, recordemos que una cadena es un ejemplo de objeto iterable , y un número entero es un ejemplo de objeto no iterable . Una lista en sí misma también es un objeto iterable .

#También observemos la diferencia entre la listfunción y la creación de una lista utilizando corchetes:

multi_element_list = list('danger!')
print(multi_element_list)  # ['d', 'a', 'n', 'g', 'e', 'r', '!']

single_element_list = ['danger!']
print(single_element_list)  # ['danger!']

#Los corchetes y la listfunción también se pueden usar para crear listas vacías que no tienen ningún elemento.

empty_list_1 = list()
empty_list_2 = []

#En los siguientes temas, analizaremos cómo rellenar listas vacías.


#Características de las listas
#Las listas pueden almacenar valores duplicados tantas veces como sea necesario.

on_off_list = ['on', 'off', 'on', 'off', 'on']
print(on_off_list)  # ['on', 'off', 'on', 'off', 'on']

#Otra cosa importante sobre las listas es que pueden contener diferentes tipos de elementos, incluidas otras listas. Por lo tanto, no hay restricciones ni tipos de lista fijos, y puedes agregar cualquier dato que desees a tu lista, como en el siguiente ejemplo:
different_objects = ['a', 1, 'b', 2, [1, 2, 3]]

#Longitud de una lista

#A veces necesitas saber cuántos elementos hay en una lista. Existe una función integrada len()que se puede aplicar a cualquier objeto iterable y que simplemente devuelve la longitud de ese objeto.
#Así pues, cuando se aplica a una lista, devuelve el número de elementos de esa lista:

numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # 5

empty_list = list()
print(len(empty_list))  # 0

single_element_list = ['danger!']
print(len(single_element_list))  # 1

multi_elements_list = list('danger!')
print(len(multi_elements_list))  # 7

#En el ejemplo anterior, puedes ver cómo len()funciona la función. De nuevo, presta atención a la diferencia entre list()y []aplicada a cadenas: puede que no dé como resultado lo que esperabas.

#Resumen

#A modo de resumen, observamos que las listas son:

#ordenado , es decir, cada elemento tiene una posición fija en una lista;
#iterable , es decir, puedes obtener sus elementos uno por uno;
#capaz de almacenar valores duplicados ;
#capaz de almacenar diferentes tipos de elementos;
#Además de utilizarse para crear una lista vacía, la función también puede utilizarse para crear una lista a partir de un objeto iterable. list()

#Para obtener más información sobre este tema, consulte la función range de Python y sus métodos en el blog de Hyperskill.

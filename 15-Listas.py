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
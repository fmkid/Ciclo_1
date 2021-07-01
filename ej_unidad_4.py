# 1: Utilizar la función incorporada map() para crear una función que retorne 
# una lista con la longitud de cada palabra (separadas por espacios) de una frase. 
# La función recibe una cadena de texto y retornará una lista

def retornar_long_palabras(frase: str):
    return list(map(len, frase.split()))

test = "También muestra los años de los Juegos Olímpicos que han transcurrido mientras la persona ha vivido"
print("\nEjercicio #1:")
print(retornar_long_palabras(test))

# 2: Crear una función que tome una lista de dígitos y devuelva al número al que corresponden. 
# Por ejemplo, [1,2,3] corresponde al número ciento veintitrés (123). Utilizar la función reduce

from functools import reduce

def conv_lista2num(lista):
    return reduce(lambda acum, valor: acum * 10 + valor, lista)

test = [1,2,3]
print("\nEjercicio #2:")
print(conv_lista2num(test))

# 3: Crear una función que retorne las palabras de una lista de palabras que comience 
# con una letra en específico. Utilizar la función filter.

def filtrar_palabras(lista, letra: str):
    return list(filter(lambda palabra: letra.upper() == palabra[0].upper(), lista))

test = ['Perro','Gato','Pelota','Manzana','Libro','Python','Molino','Abaco','Linterna',"Guitarra"]
print("\nEjercicio #3:")
print(filtrar_palabras(test, "g"))

# 4: Realizar una función que tome una lista de comprensión para devolver una lista de
# la misma longitud donde cada valor son las dos cadenas de L1 y L2 concatenadas con un
# conector entre ellas. Ejemplo:
# Listas: ['A', 'a'] ['B','b']  Conector: '-' Salida: ['A-a'] ['B-b']. Utilizar la función zip.

def concatenar_palabras(lista1, lista2, conector: str = " "):
    lista_palabra = list(zip(lista1, lista2))
    lista_palabra = list(zip(lista_palabra[0], lista_palabra[1]))
    return [conector.join(valor) for valor in lista_palabra]

test1, test2 = ['A', 'a'], ['B','b']
print("\nEjercicio #4:")
print(concatenar_palabras(test1, test2, "-"))

# 5: Realizar una función que tome una lista y retorne un diccionario que contenga
# los valores de la lista como clave y el índice como el valor. Utilizar la función enumerate

def list2dict(lista):
    pass

# 6: Realizar una función que retorne el recuento de la cantidad de elementos en 
# la lista cuyo valor es igual a su índice. Utilizar la función enumerate

def iguales_indice(lista):
    pass
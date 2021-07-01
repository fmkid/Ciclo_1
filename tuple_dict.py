def funcion2():
    tupla = tuple("abcdefg")
    return funcion(*tupla)

def funcion(*tupla):
    for elem in tupla:
        print(elem)

def valores_dic(diccionario):
    tupla = ()
    for elem in diccionario.values():
        tupla += (elem,)
    return tupla

tupla = (a, b, c, d) = ("El", "veloz", "murciélago", "vuela")
print(a,c,d,b)
print(*tupla)
diccionario = {"nombre":"Mao", "apellido":"Moreno", "edad":39, "genero":"M"}
tupla = valores_dic(diccionario)
print(*diccionario.keys())
print(*diccionario.values())
print(*tupla, sep = " - ")
print(*range(10))

def funcion3(a: int, b: int, c: int):
    return (a + b * c)

test = (1, 2, 3)
print(funcion3(*test)) # Valores tupla pasan como argumento, equivalente a print(funcion3(1, 2, 3))
test = {"c": 1,"b": 2, "a": 3}
print(funcion3(**test)) # k y v del diccionario pasan como argumento por referencia
                        # equivante a print(funcion3(c = 1, b = 2, a = 3)) o a print(funcion3(3, 2, 1))

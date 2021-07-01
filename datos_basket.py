import numpy
from functools import reduce

def analizar_matriz_alturas(datos_estaturas: numpy.array) -> dict:
    # Crea una lista vacía para guardar las estaturas de ambos equipos
    estaturas = list()
    for fila in datos_estaturas:
        # Guarda en una sola lista los valores de las 2 filas de estaturas de cada equipo (quedan como strings)
        estaturas += list(fila[1:])
    # Convierte las estaturas a float mediante map y lambda
    estaturas = list(map(lambda val: float(val), estaturas))
    # Crea una lista para guardar los resultados de los calculos solicitados:
    vals = []
    # Calcula mayor altura usando reduce y lambda, y la almacena en lista de resultados
    vals.append(reduce(lambda val, mayor = 0: val if val > mayor else mayor, estaturas))
    # Calcula menor altura usando reduce y lambda, y la almacena en lista de resultados
    vals.append(reduce(lambda val, menor = 0: val if val < menor else menor, estaturas))
    # Calcula promedio usando reduce, lambda, len y round, y lo almacena en lista de resultados
    promedio = round(reduce(lambda val, suma: suma + val, estaturas) / len(estaturas), 2)
    vals.append(promedio)
    # Crea una lista con las alturas mayores al promedio usando filter y lambda, y la almacena en lista de resultados
    mayores_prom = list(filter(lambda val: val > promedio, estaturas))
    vals.append(mayores_prom)
    # Calcula la cantidad de alturas mayores al promedio usando len, y la almacena en lista de resultados
    vals.insert(-1, len(mayores_prom))
    # Define una tupla con las claves del diccionario de salida
    claves = ('mayor_altura', 'menor_altura', 'altura_promedio', 'cantidad_mayores_promedio', 'alturas_mayores_promedio')
    # Retorna el diccionario de salida solicitado por el reto, usando zip (para mezclar keys y vals) y dict
    return dict(zip(claves, vals))

datos = numpy.array([['eq1', 1.98, 2.11, 2.02, 2.06, 2.14, 1.97, 1.89, 1.80, 2.00, 1.87],
                     ['eq2', 1.99, 2.02, 2.04, 2.15, 1.97, 1.87, 1.81, 1.80, 2.06, 2.13]])

print(analizar_matriz_alturas(datos))
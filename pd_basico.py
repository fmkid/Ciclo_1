from random import randint, choice
import pandas as pd

lista_edad = [randint(18, 72) for i in range(0,100)]
lista_estatura = [randint(145, 200) for i in range(0,100)]
lista_estrato = [randint(1, 6) for i in range(0,100)]
lista_genero = [choice(["masculino", "femenino"]) for i in range(0,100)]
lista_estadocivil = [choice(("soltero", "casado", "union libre", "n/a")) for i in range(0,100)]

edades = {"Edad": lista_edad, "Estatura (cm)": lista_estatura, "Género": lista_genero, "Estrato": lista_estrato, "Estado civil": lista_estadocivil}

# Crea una tabla de datos a partir del diccionario edades
datafr1 = pd.DataFrame(edades) #Convierte diccionario edades a tabla - edades.keys -> id. de columnas, edades.values -> elementos de columnas
print("=" * 100)
print(datafr1) #Muestra tabla (vista previa)
print("=" * 20)
print(datafr1.count()) #Realiza un conteo de elementos de cada columna
'''
print("=" * 20)
print(datafr1.info()) # Muestra info de cada columna 
print("=" * 20)
print(datafr1.head(30)) #Muestra solo los primeros 30 valores de la tabla
print("=" * 20)
print(datafr1.tail(30)) #Muestra solo los ultimos 30 valores de la tabla
'''

# Calcula frecuencia de cada ocurrencia para cada columna
print("=" * 100)
frec1 = pd.value_counts(datafr1["Edad"])
print(frec1)
print("=" * 20)
frec2 = pd.value_counts(datafr1["Estatura (cm)"])
print(frec2)
print("=" * 20)
frec3 = pd.value_counts(datafr1["Estrato"])
print(frec3)
print("=" * 20)
frec4 = pd.value_counts(datafr1["Género"])
print(frec4)
print("=" * 20)
frec5 = pd.value_counts(datafr1["Estado civil"])
print(frec5)

#Calcula medidas de tendencia central
print("=" * 100)
print(datafr1.mean()) # Promedio de cada una de las columnas (solo numéricas)
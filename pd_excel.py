import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#csv = pd.read_csv("Ciclo_1\\data\\datosEjemplo.csv") #Cargar archivo de datos en .csv
excel = pd.read_excel("Ciclo_1\\data\\notasDigital1.xls") #Cargar archivos datos en excel .xls en un dataframe (o un diccionario)
excel.info() #Ver información resumen del excel
#dfnd = pd.DataFrame(excel) #Crear dataframe a partir de diccionairo excel (no es necesario, ya que excel es un df)
dfnd = excel.replace(np.nan, 0) #Utiliza funcion replace del dataframe y el valor nan de numpy ("NaN") 
                                #para reeemplazar casillas sin info por el valor del 2do argumento de replace
print(dfnd)
print("-" * 100)
print(excel.describe())#Muestra los datos estadísticos de cada una de las columnas del df excel (conteo,promedio,desv estandar,cuartiles...)
print("-" * 100)
print(dfnd.describe())
print("-" * 100)
print(dfnd.iloc[[100,103,150,8]]) #Muestra las filas descritas en la lista
print("-" * 100)
print(dfnd.iloc[[80,81,23,83,85], [2,3]]) #Muestra unicamente las filas y columnas descritas en cada lista (separadas por coma)
print("-" * 100)
print(dfnd.iloc[80:90, 2:6]) #Muestra un rango de filas y columnas (separado por coma)
print("-" * 100)
dfnd.set_index("nota", inplace = True) #Fijar una columna para que sea columna de referencia
print(dfnd.loc[dfnd["Colegio"]=="Privado",["Edad","genero"]]) #Filtrar y mostrar información de acuerdo a una condición
print("-" * 100)
plt.hist(dfnd["Estrato_socioeconómico"], 6, color = "blue", ec = "black")
plt.show()
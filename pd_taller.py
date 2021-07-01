#1. Descargar las librerías pandas, numpy, seaborn, matplotlib e importarlas
import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np
#import seaborn as sb

#2. Cargar archivo de Excel, notasDigital1.xlsx
notas_dict = pd.read_excel("Ciclo_1\\data\\notasDigital1.xlsx")

#3. Crear DataFrame de pandas e imprimir informacióndel archivo y la descripción estadística de los datos
notas_df = pd.DataFrame(notas_dict)
#notas_df.info()
#print("-"*160)
#print(notas_df.describe())

#4. Realizar la limpieza de los datos, eliminar datos que afectan el estudio
#print("-"*160)
#print(notas_df["nota"].isnull()) # Verificar cuales datos son nulos (resultado: True) y cuales no (resultado: False) 
notas_df = notas_df.dropna(subset=['nota']) #drop(): borrar cualquier fila/columna - dropna(): borrar fila/columna con datos vacios
#print(notas_df)

#5. Volver a realizar la descripción posterior a la limpieza de los datos
print("-"*160)
#notas_df.info()
print(notas_df.describe())

# 6. Construir tablas de frecuencia para las columnas de edad, estrato socioeconómico, puntaje de admisión UNAL y promedio académico
'''
# Función que calcula (de forma manual) una tabla de frecuencias y crea un nuevo dataframe con dicha tabla
def calcular_tf(vals: pd.DataFrame, grp: int) -> pd.DataFrame:
    min_val = min(vals)
    max_val = max(vals)
    delta = (max_val - min_val) / grp
    limite = lambda n: round(delta * n + min_val, 2) if n > 0 else round(delta * n + min_val - .01, 2) # función que calcula los limites de cada clase
    interv = [f"({limite(i)} - {limite(i+1)}]" for i in range(grp)] # Creación intervalos
    fabs = [len([val for val in vals if limite(i) < val <= limite(i+1)]) for i in range(grp)] # frec. absolutas
    frel = [round(fa/sum(fabs),3) for fa in fabs] #frec. relativas
    Fabs = [sum(fabs[:i+1]) for i in range(grp)] #frec. absolutas acumuladas
    Frel = [sum(frel[:i+1]) for i in range(grp)] #frec. relativas acumuladas
    return pd.DataFrame({"intervale": interv, "fa": fabs, "fr": frel, "Fa": Fabs, "Fr": Frel}) # Creando y retornando tabla de frecuencia

grupos = 4
valores = notas_df["nota"] #.dropna()
tf = calcular_tf(valores, grupos)
print("-"*160)
print(tf)

# Exportando tabla de frecuencias a xlsx, csv y json
tf.to_excel("Ciclo_1\\data\\frecuencias.xlsx")
tf.to_csv("Ciclo_1\\data\\frecuencias.csv")
tf.to_json("Ciclo_1\\data\\frecuencias.json")

#Importando tabla de frecuencias recien creada desde json
tabla = pd.read_json("Ciclo_1\\data\\frecuencias.json")
print("-"*160)
print(tabla)
tabla.info
'''
# Creando una tabla de frecuencias para la columna "nota" usando pandas
tf = pd.value_counts(notas_df["nota"], bins = 5) #Realiza conteo de repeticiones (frecuencia) de los valores de una columna, con bins los organiza por grupos
print("-"*160)
print(tf)

#7. Realizar un histograma por cada tabla de frecuencias construida
plt.hist(notas_df["nota"], bins = 5, rwidth=0.85) # Crear histograma
plt.show()

#8. Hacer gráficos porcentuales de las columnas, genero, estado laboral, colegio, procedencia y estudios previos
rangos = ["[0.3 - 1.2]", "(1.2 - 2.1]", "(2.1 - 3.0]", "(3.0 - 3.9]", "(3.9 - 4.8]"] 
plt.pie(tf, labels = rangos, autopct = '%1.1f%%') #Crear diagrama porcentual tipo pastel
plt.show()

#9. Realizar gráficos de dispersión para las columnas nota vs promedio académico
plt.scatter(notas_df["Promedio_Académico"], notas_df["nota"])
plt.ylabel("Nota del estudiante")
plt.xlabel("Promedio académico")
plt.grid()
plt.show()
print("-"*160)
print(notas_df.corr()) #Calcula las correlaciones del dataframe entero (columnas vs columnas)

# Extra: Diagramas de cajas y bigotes (graficos de representación de distribución de una sola variable)
plt.boxplot(notas_df["nota"])
plt.show()
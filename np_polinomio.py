import numpy as np
import matplotlib.pyplot as plt
# import pylab as plb # librería mezcla de numpy y matplotlib
from random import randint

def polinomica(x, *coefs):
    polinomio = 0
    grado = len(coefs) - 1
    for exp, coef in enumerate(coefs):
        polinomio += coef * x ** (grado - exp)
    return polinomio

coeficientes = [randint(-9,9) for _ in range(randint(1,10))]
x = np.linspace(-1, 1, 100) # Definir un array de n datos para los valores de x, alternativamente se puede usar la funcion np.arange
#x = np.arange(-10,10,0.01) # La diferencia es que arange necesita definir la tasa de cambio/aumento de la variable, no la cantidad de datos
print(np.poly1d(coeficientes)) # Crea un polinomio de grado len(coeficientes) - 1
y1 = polinomica(x, *coeficientes) # Función propia para la generación de polinomios
plt.plot(x, y1, "-", color = "r") # El tercer argumento (opcional) representa si se va a presentar la grafica de forma continua o solo puntos
plt.grid()
plt.show()
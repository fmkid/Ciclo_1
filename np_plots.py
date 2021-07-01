# librería operaciones matemáticas y de algebra lineal sobre arreglos (equivalente a lo que hace MatLab)
import numpy as np
# librería graficación de funciones matemáticas y estadísticas
import matplotlib.pyplot as plt

def seno(x):
    return np.sin(x)

def lineal(a, b, x):
    return a*x + b

def cuadratica(a, b, c, x):
    return a*x**2 + b*x + c

def cubica(a, b, c, d, x):
    return a*x**3 + b*x**2 + c*x + d

#x = np.linspace(-2*np.pi, 2*np.pi, 100)
#y1 = seno(x)
#y2 = cuadratica(1, 0, 0, x)
#y3 = cubica(1, 0, 0, 0, x)
#plt.plot(x, y1)
#plt.plot(x, y2)
#plt.plot(x, y3)
#coeficientes = [1, 4, 0, 4, 2, -2, -3]
#x = np.linspace(-100, 100, 10)
# y1 = np.poly1d(coeficientes) # Crea un polinomio de grado len(list) - 1, para el caso: grado 6
#coef = [2, 25]
#y2 = np.poly1d(coef)  # Crea un polinomio de grado 1
#plt.plot(x, y1(x))
#plt.plot(x, y2(x))
plt.grid()
plt.show()

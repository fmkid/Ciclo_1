import numpy as np

''' Definir el sistema de ecuaciones:

        x + y + z = 37
        3x - y - z = 3
        x - y + z = 13

    y resolverlo usando np
'''
A = np.array([[1,1,1],[3,-1,-1],[1,-1,1]]) #matriz de coeficientes np.mat('1,1,1;3,-1,-1;1,-1,1')
C = np.array([37,3,13]) #matriz de resultados
# La ecuación en forma matricial sería: A . B = C
B = np.linalg.solve(A,C) #solución: B = [x , y, z]
#B = np.dot(np.linalg.inv(A), C) # Solución usando inversa: B = A^-1 . C
print(B)

'''Solución de ecuaciones polinómicas usando np '''

a = np.roots([4, 48, -81]) # Solucionar la ecuación: 4x^2 + 48x - 81 
print(a)
b= np.roots([1,5,-2,-3])  # Solucionar la ecuación: x^3 + 5x^2 - 2x - 3
print(b)
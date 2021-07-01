#https://programminghistorian.org/es/lecciones/instalar-modulos-python-pip

import matplotlib.pyplot as plt 
from numpy import arange, sin, cos, pi

x = arange(-2*pi,2*pi,0.01)
#y = sin(x)
y = cos(x)
plt.plot(x,y)
plt.grid(True)
plt.xlabel("eje X")
plt.ylabel("eje Y")
plt.show()
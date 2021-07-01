class FocoDeLuz:
    #Constructor
    def __init__(self, tamanoPar, voltajePar, intensidadPar, potenciaPar, tipofocoPar):
        #Propiedades del objeto (públicas: se pueden acceder y cambiar fuera de la clase)
        self.tamano = tamanoPar
        self.voltaje = voltajePar
        self.intensidad = intensidadPar
        self.potencia = potenciaPar
        self.tipoFoco = tipofocoPar
        #Propiedad privada del objeto (no se puede acceder o cambiar fuera de la clase)
        self.__estaEncendido = False 

    #Métodos del objeto:
    def prender(self):
        self.__estaEncendido = True

    def apagar(self):
        self.__estaEncendido = False
    
    def mostrarPropiedades(self):
        print("-" * 50)
        print("El tamaño del foco es: " +  str(self.tamano))
        print("El voltaje del foco es: " +  str(self.voltaje))
        print("La intensidad del foco es: " + self.intensidad)
        print("La potencia del foco es: " +  str(self.potencia))
        print("El tipo del foco es: " +  self.tipoFoco)
        print("El foco está ", end = "")
        print("encendido" if self.__estaEncendido else "apagado")


objeto_foco1 = FocoDeLuz(5, 120,"1900 Lumens", 15, "Ahorrador")
objeto_foco2 = FocoDeLuz(10, 100,"2500 Lumens", 12, "Incandescente")
objeto_foco1.mostrarPropiedades()
objeto_foco1.prender()
objeto_foco1.mostrarPropiedades()
objeto_foco1.apagar()
objeto_foco1.mostrarPropiedades()
objeto_foco2.mostrarPropiedades()
objeto_foco2.prender()
objeto_foco2.mostrarPropiedades()
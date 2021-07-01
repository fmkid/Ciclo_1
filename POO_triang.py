class Triangulo():
    def __init__(self, lado1: float, lado2: float, lado3: float):
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3

    def __str__(self):
        lados = (self.__lado1, self.__lado2, self.__lado3)
        return "El triángulo tiene lados de {}, {} y {} unidades, respectivamente".format(*lados)

    def max_lado(self):
        return max(self.__lado1, self.__lado2, self.__lado3)

    def tipo_triang(self):
        #Llamado a función estática (para ser llamada dentro o fuera de la clase hay que anteponer la clase)
        if not Triangulo.es_valido(self.__lado1, self.__lado2, self.__lado3):
            return "No es un triángulo válido"
        lados = (self.__lado2, self.__lado3)
        conteo = lados.count(self.__lado1)
        if conteo == 2:
            return "Es equilátero"
        elif conteo == 1 or lados[0] == lados[1]:
            return "Es isósceles"
        else:
            return "Es escaleno"

    def es_valido(lado1, lado2, lado3): #Función estática dentro de la clase. No necesita crearse un objeto para ser llamada (no lleva "self")
        #Debe cumplirse que todos los lados sean mayores que cero y que la suma de los lados menores sea mayor que el lado mayor
        lados = (lado1, lado2, lado3)
        mayor = max(lados)
        return all(map(lambda lado: lado > 0, lados)) and sum(lados) - mayor > mayor

tri = Triangulo(3,4,5)
print("-"*100)
print(tri) 
print("El lado mayor mide:", tri.max_lado(), "unidades")
print(tri.tipo_triang())

tri2 = Triangulo(5,0,2)
print("-"*100)
print(tri2) 
print("El lado mayor mide:", tri2.max_lado(), "unidades")
print(tri2.tipo_triang())
#Llamado a función estática fuera de la función
print("-"*100)
print(Triangulo.es_valido(5,5,0.1)) 
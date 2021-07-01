class Estudiante:
    def __init__(self, nombre: str, apellido: str, edad: int, codigo: str):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.codigo = codigo
        self.notas = []

    def imprimir_info(self):
        print("-" * 100)
        print("El nombre completo del estudiante es:", self.nombre, self.apellido)
        print("La edad del estudiante es:", self.edad)
        print("El código del estudiante es:", self.codigo)
        print("Las notas del estudiante son:", self.notas)
        self.calcular_promedio()
        print("El promedio del estudiante es:", self.promedio)
        print("El estudiante fue ", end = "")
        print("APROBADO") if self.es_aprobado() else print("REPROBADO")

    def agregar_nota(self, nota: float):    
        self.notas.append(nota)

    def calcular_promedio(self):
        self.promedio = round(sum(self.notas)/len(self.notas), 1) if self.notas != [] else 0.0

    def es_aprobado(self):
        return self.promedio >= 3.0

est01 = Estudiante("Mao", "Moreno", 35, "01")
est02 = Estudiante("Ingrid", "Cárdenas", 25, "02")
est03 = Estudiante("Javier", "Romero", 34, "03")

est01.agregar_nota(5.0)
est01.agregar_nota(3.2)
est01.agregar_nota(1.0)
est01.imprimir_info()
est02.imprimir_info()
est03.imprimir_info()
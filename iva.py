# Programa que calcula el IVA en distintos paises de Europa
# Autor: Mao Moreno
# Fecha: 07/05/2021

def CalcularIVA(nombre_pais: str, nombre_producto: str, valor_base: int, iva_pais: int):
    valor_mas_iva = round(valor_base * (1 + iva_pais/100),2)
    return f"\nEl valor con IVA del {iva_pais}% de un(a) {nombre_producto} en {nombre_pais} es {valor_mas_iva} euros"

print(CalcularIVA("Alemania", "Cerveza", 5, 19))
print(CalcularIVA("Hungría", "Automovil", 1000, 27))
print(CalcularIVA("Italia", "Pizza", 12, 22))
print()
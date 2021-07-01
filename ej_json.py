from json import load
from datetime import date

# 1)Obtener todas las transferencias realizadas en el último trimestre en los cajeros
# de modelo 101,2017
# 2)Obtener todas las consignaciones realizadas en el último trimestre en los cajeros
# de modelo 101,2017 que se encuentran fuera de servicio
# 3) Todas las transacciones de los cajeros cerrados que pertenecen a la firma integrada
# -> Convencional: Ciclando y con condicionales
# -> Funcional: Map, Filter, Zip o Reduce

def calcular_trim_ant():
    año, mes, dia = list(map(lambda x: int(x), str(date.today()).split("-"))) #Fecha actual
    mes -= 3
    if mes < 1:
        mes += 12
        año -= 1
    if dia == 31 and mes in [4,6,9,11]:
        dia = 30
    elif dia > 28 and mes == 2:
        dia = 28
    return f"{año}-{mes:02}-{dia:02}"

def inv_formato_fecha(fecha:str):
    dia, mes, año = fecha.split("-")
    return f"{año}-{mes}-{dia}"

with open("data\\caso1.json") as filejson:
    caso1 = load(filejson)

# 1)Obtener todas las transferencias realizadas en el último trimestre en los cajeros
# de modelo 101,2017

for k1 in caso1:
    cajero = caso1[k1]
    if cajero["modeloCajero"] in (101, 2017):
        for trans in cajero["transacciones"]:
            if trans["tipoMovimiento"] == "transferencia" and inv_formato_fecha(trans["fechaMovimiento"]) >= calcular_trim_ant():
                print(k1 + " - " + str(cajero["modeloCajero"]) + ":")
                print(trans)
print("-" * 100)

# 2)Obtener todas las consignaciones realizadas en el último trimestre en los cajeros
# de modelo 101,2017 que se encuentran fuera de servicio

for k1 in caso1:
    cajero = caso1[k1]
    if cajero["modeloCajero"] in (101, 2017) and cajero["estado"] == "Fuera de Servicio":
        for trans in cajero["transacciones"]:
            if trans["tipoMovimiento"] == "consignacion" and inv_formato_fecha(trans["fechaMovimiento"]) >= calcular_trim_ant():
                print(k1 + " - " + str(cajero["modeloCajero"]) + " - " + str(cajero["estado"]) + ":")
                print(trans)
print("-" * 100)

# 3) Todas las transacciones de los cajeros cerrados que pertenecen a la firma integrada?

for k1 in caso1:
    cajero = caso1[k1]
    if cajero["estado"] == "Cerrado":
        for trans in cajero["transacciones"]:
            print(k1 + " - " + str(cajero["modeloCajero"]) + " - " + str(cajero["estado"]) + ":")
            print(trans)
print("-" * 100)
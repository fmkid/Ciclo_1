centenas = ("", "ciento ", "doscientos ", "trescientos ", "cuatrocientos ", "quinientos ", "seiscientos ", 
            "setecientos ", "ochocientos ", "novecientos ")
decenas = ("", ("diez ","once ", "doce ", "trece ", "catorce ", "quince ", "dieciséis ", "diecisiete ", "dieciocho ", "diecinueve "), 
           "veinti", "treinta ", "cuarenta ", "cincuenta ", "sesenta ", "setenta ", "ochenta ", "noventa ") 
unidades = ("cero", "uno ", "dos ", "tres ", "cuatro ", "cinco ", "seis ", "siete ", "ocho ", "nueve ")

from random import randrange

def separar_digitos(numero: int) -> list:
    lista = [int(letra) for letra in str(numero)]
    lista.reverse()
    return lista

def numero_en_letras(numero: int) -> str:
    num_str = ""
    lista = separar_digitos(numero)
    long = len(lista)
    for i, digito in enumerate(lista):
        evaluar = i % 3
        if evaluar == 0:
            condicion = long - 1 > i
            if condicion:
                siguiente = lista[i+1]
            else:
                siguiente = -1
            if i in [3,9,15,21]:
                num_str = "mil " + num_str
                if digito == 1 and condicion and i != 3:
                    num_str = "un " + num_str
            elif i == 6:
                if digito == 1:
                    if condicion:
                        num_str = "un millones " + num_str
                    else:
                        num_str = "un millón " + num_str
                else:
                    num_str = "millones " + num_str
            elif i == 12:
                if digito == 1:
                    if condicion:
                        num_str = "un billones " + num_str
                    else:
                        num_str = "un billón " + num_str
                else:
                    num_str = "billones " + num_str
            elif i == 18:
                if digito == 1:
                    if condicion:
                        num_str = "un trillones " + num_str
                    else:
                        num_str = "un trillón " + num_str
                else:
                    num_str = "trillones " + num_str
            if (long > 1 and digito < 1) or (i // 3 > 0 and digito == 1) or siguiente == 1:
                continue
            else:
                num_str = unidades[digito] + num_str
                if siguiente > 2 and digito != 0:
                    num_str = "y " + num_str
        elif evaluar == 1:
            if digito == 1:
                num_str = decenas[digito][lista[i-1]] + num_str
            elif digito == 2 and lista[i-1] == 0:
                num_str = "veinte" + num_str
            else:
                num_str = decenas[digito] + num_str
        else:
            if digito == 1 and lista[i-1] == 0 and lista[i-2] == 0:
                num_str = "cien " + num_str
            else:
                num_str = centenas[digito] + num_str
    return num_str

print(numero_en_letras(10101101000001111))
print(numero_en_letras(101668))

for i in range(100):
    try:
        num = randrange(10000,200000)
        print(num, numero_en_letras(num))
        #print(i, numero_en_letras(i))
    except:
        print(num)
        #print(i)
        #'''
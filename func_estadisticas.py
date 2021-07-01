def media(datos: list):
    return round(sum(datos)/len(datos), 2)

def mediana(datos: list):
    datos.sort()
    print(datos)
    long = len(datos)
    pos_central = (long - 1)//2
    if long % 2 != 0:
        return datos[pos_central]
    else:
        return media([datos[pos_central], datos[pos_central + 1]])

def moda1(datos: list):
    conteo = list()
    for dato in datos:
        conteo.append(datos.count(dato))
    conteo_max = max(conteo)
    conj_moda = set()
    for i in range(len(datos)):
        if conteo[i] == conteo_max:
            conj_moda.add(datos[i])
    return sorted(list(conj_moda))

def moda2(datos: list):
    rep, cont = list(), 0
    anterior = datos[0]
    for dato in sorted(datos):
        if dato == anterior:
            cont += 1
        else:
            rep.append((cont, anterior))
            cont, anterior = 1, dato
    rep.append((cont, anterior))
    mayor = max(rep)[0]
    return [val[1] for val in rep if val[0] == mayor]

def moda3(datos: list):
    sin_rep = list(set(datos))
    rep = {}
    for dato in sin_rep:
        rep[dato] = datos.count(dato)
    mayor = max(rep.values())
    return sorted([key for key, val in rep.items() if val == mayor])

def moda4(datos: list):
    rep = {}
    for dato in datos:
        if dato not in rep:
            rep[dato] = 1
        else:
            rep[dato] += 1
    mayor = max(rep.values())
    return sorted([key for key, val in rep.items() if val == mayor])

def histograma_edad(lista_edad: list):
    encabezado = ["De 18 a 29 años:", "De 30 a 44 años:", "De 45 a 55 años:", "De 56 a 72 años:"]        
    hist = [0 for i in range(4)]
    for edad in lista_edad:
        if 18 <= edad < 30:
            hist[0] += 1
        elif 30<= edad < 45:
            hist[1] += 1
        elif 45 <= edad < 56:
            hist[2] += 1
        elif 56 <= edad < 73:
            hist[3] += 1
    print("\nHistograma:")
    print("===========")
    for i in range(len(hist)):
        print(encabezado[i], "*" * hist[i])

test = [6,0,2,4,4,3,3,5,2,6,0,0]
#test = [2, 3, 5, 5, 7, 9, 9, 9, 10, 12]

print("Datos de entrada =", test)
print()
print("Media =", media(test))
print("Mediana =", mediana(test))
print("Moda =", moda1(test), moda2(test), moda3(test), moda4(test), sep = "\n")
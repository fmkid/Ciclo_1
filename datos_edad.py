###################################
# Autor: Mao Moreno
# Fecha: 13/05/2021
''' DESCRIPCION DEL PROGRAMA:
    
   - Pregunta edad y si este año (2021) ya cumplió años o no
   - Muestra en que año nació, la década en la que nació y la generación a la que pertenece
   - También muestra los años de los Juegos Olímpicos que han transcurrido mientras la persona ha vivido
'''
###################################

def generacion(año:int) -> str:
    # Fuente: https://www.lavanguardia.com/vivo/20180408/442342457884/descubre-que-generacion-perteneces.html
    if 1930 <= año <= 1948:
        return "la Posguerra"
    elif 1949 <= año <= 1968: 
        return "los Baby boomers"
    elif 1969 <= año <= 1980:
        return "la Generación X"
    elif 1981 <= año <= 1993:
        return "los Millenials"
    elif 1994 <= año <= 2010:
        return "la Generación Z"
    else:
        return "** No determinado **"

def años_olimpicos(año_inicial:int) -> list:
    # Calcula el primer año de Olímpicos que vivió la persona
    modulo = año_inicial % 4
    if modulo > 0:
        año_inicial += 4 - modulo
    # Inicializa y retorna la lista de años de Olímpicos, desde cuando nació hasta el 2021
    lista = list(range(año_inicial, 2021, 4))
    return lista

def mostrar_info(año_nac:int): 
    # Calcula la década en la que nació la persona
    decada = (año_nac // 10) * 10
    if decada < 2000:
        decada -= 1900
    # Muestra toda la información requerida   
    print()
    print("- Usted nació en el año:", año_nac)
    print(f"- Pertence a la década de los {decada}")
    print("- Luego pertenece al grupo de", generacion(año_nac))
    print("- Y durante su vida han transcurrido los Juegos Olímpicos de los siguientes años:")
    print(años_olimpicos(año_nac))

#### PROGRAMA PRINCIPAL ####           

edad = int(input("¿Cuál es su edad actual?: "))
cumplir = input("¿Ya cumplió años en lo que va del 2021? (S/N): ")

if cumplir == "s" or cumplir == "S":
    mostrar_info(2021 - edad)
elif cumplir == "n" or cumplir == "N":
    mostrar_info(2021 - edad - 1)
else:
    print()
    print("** No ha digitado una entrada correcta. El programa no se puede ejecutar **")
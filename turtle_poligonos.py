############################################################
# Programa que dibuja poligonos regulares y espirales de 3 
# a n lados
# Autor: Mao Moreno
# Fecha: 21/05/2021
############################################################

import turtle
from math import pi, sin

def casa():
    casa = turtle.Turtle()
    casa.hideturtle()
    lado = 150
    lado_tri = .707107 * lado
    for i in range(4):    
        casa.forward(lado)
        if i < 3:
            casa.right(90)
    for i in [45, 90]:
        casa.right(i)
        casa.forward(lado_tri)
    return

def poligono(lados):
    if lados < 3 or lados > 100:
        print(f"** ERROR: No es posible dibujar un polígono de {lados} lados")
    else:
        poligono = turtle.Turtle()
        poligono.hideturtle()
        radio = 150
        angulo = 360 / lados
        distancia = 2 * radio * sin(pi / lados)
        for i in range(lados):
            poligono.left(angulo)
            poligono.forward(distancia)
    return

def espiral(lados, ciclos = 30):
    if lados < 3 or lados > 50:
        print(f"** ERROR: No es posible dibujar una espiral basada en un polígono de {lados} lados")
    else:
        espiral = turtle.Turtle()
        espiral.hideturtle()
        angulo = 360 / lados
        var = 4.3 / lados
        distancia = 10 * var
        for i in range(ciclos * lados):
            espiral.left(angulo)
            espiral.forward(distancia)
            distancia += 20 * var / lados
    return

def espiral_esp(lados, ciclos = 72):
    if lados < 3 or lados > 50:
        print(f"** ERROR: No es posible dibujar una espiral especial basada en un polígono de {lados} lados")
    else:
        especial = turtle.Turtle()
        especial.hideturtle()
        angulo = 360 / lados
        var = 4.3 / lados
        distancia = 10 * var
        for i in range(ciclos):
            for j in range(lados):
                especial.left(angulo)
                especial.forward(distancia)
            especial.left(10)
            distancia += 3 * var
    return


## PROGRAMA PRINCIPAL ##

menu = \
"""
Menú del programa
=================

1. Dibujar polígono de n lados
2. Dibujar espiral a partir de polígono de n lados
3. Dibujar espiral especial a partir de poligóno de n lados
4. Dibujar una casa
5. Salir
"""
ventana = turtle.Screen()

while True:
    print(menu)
    opcion = input("Digite su opción ===> ")
    if len(opcion) == 1 and (ord("1") <= ord(opcion) <= ord("5")):
        ventana.reset()
        if opcion == "1":
            lados = int(input("Digite la cantidad de lados del polígono (entre 3 y 100): "))
            poligono(lados)
        elif opcion == "2":
            lados = int(input("Digite la cantidad de lados del polígono base (entre 3 y 50): "))
            #ciclos = int(input("Digite la cantidad de ciclos de la espiral: "))
            espiral(lados) #, ciclos)
        elif opcion == "3":
            lados = int(input("Digite la cantidad de lados del polígono base (entre 3 y 50): "))
            #ciclos = int(input("Digite la cantidad de ciclos de la espiral: "))
            espiral_esp(lados)
        elif opcion == "4":
            casa()
        else:
            break
    else:
        print("** ERROR: La opción digitada no es válida")
from tkinter import Tk, Frame, Button, Label, Entry, StringVar # tkinter: Módulo creación GUIs para Python
from random import randint
from functools import partial
#============ Constantes ================
numeros = "".join([str(i) for i in range(1, 7)]) #Cadena que almacena los numeros del 1 al 6
ancho, alto = 300, 170 # Ancho y alto de la ventana
#============ Ventana del GUI ================
dice = Tk() # Creación de una ventana GUI
dice.title("Juego de los dados")
dice.config(cursor = "hand2")
dice.iconbitmap('Ciclo_1\\dados.ico')
x = (dice.winfo_screenwidth() - ancho) // 2 # Calcula posicion central en x con respecto a la pantalla
y = (dice.winfo_screenheight() - alto) // 2 # Calcula posicion central en y con respecto a la pantalla
dice.geometry(f"{ancho}x{alto}+{x}+{y}")
dice.resizable(width=False, height=False)
#============ Frames ================
frame = Frame(dice)
frame.pack()  #(expand = True, fill = "both")
frame2 = Frame(dice)
frame2.pack()
#============ Funcionalidades botones ================
dados = [StringVar() for i in range(3)]
ganador = StringVar()

def lanzar_dado(num_dado):
    return dados[num_dado].set(randint(1,6))

def eval_ganador():
    mayor, conteo, invalidos = "", 1, 0
    for i in range(3):
        valor = dados[i].get()
        if len(valor) == 1 and valor in numeros:
            if valor > mayor:
                mayor = valor
                pos_max = i
                conteo = 1
            elif valor == mayor:
                conteo += 1
        else:
            invalidos += 1
            dados[i].set("")
    if invalidos:
        ganador.set("Aún no hay ganador")
    elif conteo == 1: 
        ganador.set(f"El ganador es el jugador {pos_max + 1}")
    elif conteo == 2:
        ganador.set("Hay un doble empate")
    else:
        ganador.set("Hay un triple empate")
#============ Botones ================
[Button(frame, text = f"Dado {i+1}", cursor = "dotbox", command = partial(lanzar_dado, i)).grid(row = i, column = 0) for i in range(3)] #
#============ Cuadros de texto ================
[Entry(frame, textvariable = dados[i]).grid(row = i, column = 1) for i in range(3)]
#============ Etiquetas ================
[Label(frame, text = f"Jugador {i+1}").grid(row = i, column = 2) for i in range(3)]
#============ Evaluar ================
Label(frame2, textvariable = ganador).grid(row = 0, column = 0)
Button(frame2, text = "Evaluar", command = eval_ganador).grid(row = 1, column = 0)
#============ mainloop ================
dice.mainloop() # Si no se pone, la ventana no aparece
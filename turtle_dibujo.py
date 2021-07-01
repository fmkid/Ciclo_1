import turtle

ventana = turtle.Screen()
flecha = turtle.Turtle()
STEPS = 50

def arriba():
    flecha.setheading(90)
    flecha.forward(STEPS)

def derecha():
    flecha.setheading(0)
    flecha.forward(STEPS)

def abajo():
    flecha.setheading(270)
    flecha.forward(STEPS)

def izquierda():
    flecha.setheading(180)
    flecha.forward(STEPS)


ventana.onkeypress(arriba, "Up")
ventana.onkeypress(derecha, "Right")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(izquierda, "Left")

ventana.listen()
turtle.done()

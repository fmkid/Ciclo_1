import random as rd

palabras = ["paradigma", "constantinopla", "desoxirribonucleico", "palindromo", "murcielago",
            "esternocleidomastoideo", "caleidoscopio", "eucalipto", "ornitorrinco", "electrocardiograma"]
palabra = palabras[rd.randint(0, len(palabras) - 1)]
letrasj = ""
intentos = 5
aciertos = 0

print("\n\t\tListos para jugar al AHORCADO\t\t\n\n*** Adivina una palabra de", len(palabra), "letras ***\n")

while True:
    print()
    for i in palabra:
        if i in letrasj:
            print(" " + str(i) + " ", end="")
        else:
            print(" _ ", end="")
    print("\n")

    while True:
        letra = input("¿Cuál letra crees que va en esa palabra?: ").lower()
        if not letra.isalpha() or len(letra) != 1:
            print("No has digitado una letra. La entrada no es válida\n")
            continue
        if letra in letrasj:
            print("Esa letra ya fue ingresada antes. Prueba con otra\n")
        else:
            letrasj += letra
            break

    if letra in palabra:
        print("Correcto!")
        aciertos += palabra.count(letra)
        if aciertos == len(palabra):
            print("\nHAS GANADO!... Felicidades!")
            break
    else:
        intentos -= 1
        if intentos > 0:
            print(f"Te equivocaste!... Ahora solo te quedan {intentos} intentos")
        else:
            print("\nLo siento!... Has perdido")
            break
print(f'La palabra era: "{palabra}"')
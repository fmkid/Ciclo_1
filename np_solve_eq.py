import numpy as np, os, time, sys

principal = '''
                == MENÚ PRINCIPAL ==

1- Resolver sistema de ecuaciones (de 2 o 3 variables)
2- Resolver polinomio de n grado (encontrar ceros)
3- Salir

Elija su opción ==> '''

menu_seq = '''
        === Sistemas de ecuaciones ===

1- Resolver sistema de ecuaciones de 2 variables (x, y)
2- Resolver sistema de ecuaciones de 3 variables (x, y, z)
3- Volver a menú principal
4- Salir

Elija su opción ==> '''

error = "\n*** ERROR : La opción digitada no es válida ***"

def borrar_pantalla():
    time.sleep(0.5)
    if os.name == "posix": #Equipos no Windows
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos": #Equipos Windows (o basados en Windows)
        os.system("cls")

def menu_principal():
    while True:
        borrar_pantalla()
        print(principal, end = '')
        opcion = input()
        if opcion not in ["1","2","3"]:
            print(error, end = '')
            time.sleep(1.5)
            continue
        elif opcion == "1":
            menu_sisteq()
        elif opcion == "2":
            resolver_poly()
        else:
            borrar_pantalla()
            sys.exit()

def menu_sisteq():
    while True:
        borrar_pantalla()
        print(menu_seq, end = '')
        opcion = input()
        if opcion not in [str(i) for i in range(1,5)]:
            print(error, end = '')
            time.sleep(1)
            continue
        elif opcion == "1":
            resolver_sys_eq(2)
        elif opcion == "2":
            resolver_sys_eq(3)
        elif opcion == "3":
            menu_principal()
        else:
            borrar_pantalla()
            exit()

def resolver_sys_eq(n: int):
    A = list() #matriz de coeficientes de variables
    C = list() #matriz de terminos independientes
    borrar_pantalla()
    print(f"\n==== Resolver un sistema de ecuaciones de {n} variables", end = "") 
    if n == 2:
        terminos = ["x", "y", "término indep."]
        print("(x, y) ====")
    else:
        terminos = ["x", "y", "z", "término indep."]
        print("(x, y, z) ====")
    for i in range(n):
        print()
        var = list()
        for variable in terminos:
            try:
                valor = float(input(f"Digite el valor de {variable} para la ecuación {i + 1}: "))
                if variable != terminos[-1]:
                    var.append(valor)
                else:
                    C.append(valor)
            except:
                print(error, end = '')
                time.sleep(1.5)
                menu_sisteq()
        A.append(var)
    # Conversion de listas A y C a arrays de np
    A = np.array(A)
    C = np.array(C)
    try:
        solucion = np.linalg.solve(A,C)
    except:
        print("\n*** ¡El sistema de ecuaciones no tiene solución definida! ***")
    else:
        print(f"\n*** La solución del sistema de ecuaciones es: ***\n")
        print("(", end = "")
        for i, res in enumerate(solucion):
            print(f"{terminos[i]} = {round(res, 2)}", end = "")
            if i < n - 1:
                print(", ", end = "")
            else:
                print(")")
    input("\nPresione ENTER para continuar...")

def resolver_poly():
    borrar_pantalla()
    print("\n==== Resolver una ecuación polinómica de grado n ====\n") 
    try:
        grado = int(input("Digite el grado de la función polinómica (entero mayor que 0): "))
        assert grado > 0 #Si el grado es menor que 1 salta la excepción (AssertionError)
    except:
        print(error, end = '')
        time.sleep(1.5)
        menu_principal()
    coeficientes = list()
    print()
    for i in range(grado, -1, -1):
        try:
            termino = (f"x^{i}" if i != 0 else "independiente")
            valor = int(input(f"Digite el coeficiente del término {termino}: "))
            coeficientes.append(valor)
        except:
            print(error, end = '')
            time.sleep(1.5)
            menu_principal()
    solucion = np.roots(coeficientes)
    if list(solucion) != []:
        if grado == 1:
            print(f"\n*** La solución de la ecuación polinómica ({escribir_poly(coeficientes)} = 0) es: ***\n")
        else: 
            print(f"\n*** Las soluciones de la ecuación polinómica ({escribir_poly(coeficientes)} = 0) son: ***\n")
        reales, complejos = 0, 0
        for i, raiz in enumerate(solucion):
            if raiz.imag == 0:
                raiz = round(raiz.real, 2)
                reales += 1
            else:
                raiz = round(raiz.real, 2) + complex(0, round(raiz.imag, 2))
                complejos += 1
            resultado = f"x{i + 1} = {raiz}"
            print(resultado, end = " " * (23 - len(resultado)))
            if (i + 1) % 6 == 0 and i != grado - 1:
                print()
        print(f"\n\n<< Reales: {reales} - Complejos: {complejos} >>")
    else:
        print(f"\n*** ¡El polinomio ingresado no tiene soluciones o no fue definido correctamente! ***")
    input("\nPresione ENTER para continuar...")

def escribir_poly(coefs: list) -> str:
    grado = len(coefs) - 1
    primer_signo = False
    polinomio = ""
    for i, valor in enumerate(coefs):
        coef = abs(valor)
        if coef != 0:
            if not primer_signo:
                primer_signo = True
                if valor < 0:
                    polinomio += "-"
            else:
                polinomio += " - " if valor < 0 else " + " 
            polinomio += str(coef) if coef != 1 or i == grado else ""
            if i < grado - 1:
                polinomio += f"x^{grado - i}"
            elif i == grado - 1:
                polinomio += "x"   
    return polinomio

if __name__ == "__main__":
    menu_principal()
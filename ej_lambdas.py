def operacion(funcion, a: float, b: float):
    return funcion(a, b)

a = 10
b = 3
operador = ["+", "-", "*", "/", "**", "^"]
for op in operador:
    if op == "+":
        res = operacion(lambda a,b: a+b, a, b)
    elif op == "*":
        res = operacion(lambda a,b: a*b, a, b)
    elif op == "^":
        res = operacion(lambda a,b: a**b, a, b)
    else:
        res = operacion(lambda a,b: None, 0, 0)
    print(a, op, b, "=", res)

bases = list(range(10))
exp = [i/2 for i in range(10)]

print(list(map(lambda a,b: int(a**b), bases, exp)))
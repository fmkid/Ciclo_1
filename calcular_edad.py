año_act, mes_act, dia_act = 2021, 5, 4

edad = int(input("Digite su edad actual: "))
mes_nac = int(input("Digite su mes de nacimiento (1 a 12): "))
#dia_nac = int(input("Digite su día de nacimiento (1 a 31): "))

fact_mes = (mes_act % mes_nac) // mes_act
#fact_dia = (dia_act % dia_nac) // dia_act

año_nac = año_act - edad - fact_mes# - fact_dia
lst = list(range(año_nac, año_act + 1))

print("\nUsted nació en el año", año_nac, "y por tanto ha vivido en el planeta Tierra durante los siguientes años:\n")
print(lst)
print()
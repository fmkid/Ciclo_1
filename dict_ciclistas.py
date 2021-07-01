def ordenar_datos_ciclistas(Ciclista1: dict, Ciclista2: dict, Ciclista3: dict) -> dict:
    menor = min(Ciclista1["tiempo_cicl_1"], Ciclista2["tiempo_cicl_2"], Ciclista3["tiempo_cicl_3"])
    if menor <= 0:
        return {}
    if Ciclista1["tiempo_cicl_1"] == menor:
        nombre1 = Ciclista1["nom_cicl_1"]
        tiempo1 = Ciclista1["tiempo_cicl_1"]
        if Ciclista2["tiempo_cicl_2"] < Ciclista3["tiempo_cicl_3"]:
            nombre2 = Ciclista2["nom_cicl_2"]
            tiempo2 = Ciclista2["tiempo_cicl_2"]
            nombre3 = Ciclista3["nom_cicl_3"]
            tiempo3 = Ciclista3["tiempo_cicl_3"]
        else:
            nombre2 = Ciclista3["nom_cicl_3"]
            tiempo2 = Ciclista3["tiempo_cicl_3"]
            nombre3 = Ciclista2["nom_cicl_2"]
            tiempo3 = Ciclista2["tiempo_cicl_2"]
    elif Ciclista1["tiempo_cicl_2"] == menor:
        nombre1 = Ciclista2["nom_cicl_2"]
        tiempo1 = Ciclista2["tiempo_cicl_2"]
        if Ciclista1["tiempo_cicl_1"] < Ciclista3["tiempo_cicl_3"]:
            nombre2 = Ciclista1["nom_cicl_1"]
            tiempo2 = Ciclista1["tiempo_cicl_1"]
            nombre3 = Ciclista3["nom_cicl_3"]
            tiempo3 = Ciclista3["tiempo_cicl_3"]
        else:
            nombre2 = Ciclista3["nom_cicl_3"]
            tiempo2 = Ciclista3["tiempo_cicl_3"]
            nombre3 = Ciclista1["nom_cicl_1"]
            tiempo3 = Ciclista1["tiempo_cicl_1"]
    else:
        nombre1 = Ciclista3["nom_cicl_3"]
        tiempo1 = Ciclista3["tiempo_cicl_3"]
        if Ciclista2["nom_cicl_2"] < Ciclista1["nom_cicl_1"]:
            nombre2 = Ciclista2["nom_cicl_2"]
            tiempo2 = Ciclista2["tiempo_cicl_2"]
            nombre3 = Ciclista1["nom_cicl_1"]
            tiempo3 = Ciclista1["tiempo_cicl_1"]
        else:
            nombre2 = Ciclista1["nom_cicl_1"]
            tiempo2 = Ciclista1["tiempo_cicl_1"]
            nombre3 = Ciclista2["nom_cicl_2"]
            tiempo3 = Ciclista2["tiempo_cicl_2"]
    return {"1": nombre1, "T1": tiempo1, "2": nombre2, "T2": tiempo2, "3": nombre3, "T3": tiempo3}

print(ordenar_datos_ciclistas(
    {"num_cicl_1": "23", "nom_cicl_1": "Egan", "tiempo_cicl_1": 2.02},
    {"num_cicl_2": "12", "nom_cicl_2": "Nairo", "tiempo_cicl_2": 2.05},
    {"num_cicl_3": "21", "nom_cicl_3": "Rigoberto", "tiempo_cicl_3": 2.48}
    ))
def formatear_string(palabra: str) -> str:
    letras_cambiar = ("á","é","í","ó","ú","ü","ñ")
    letras_correctas = ("a","e","i","o","u","u","n")
    return "".join([letras_correctas[letras_cambiar.index(letra)] if letra in letras_cambiar else letra for letra in palabra.lower()])

def generar_nombre_usuario(nombre_estudiante={}) -> str:
    if nombre_estudiante['seg_nom'] == "":
        nombres = nombre_estudiante['pri_nom']
    else:
        nombres = nombre_estudiante['pri_nom'][0] + nombre_estudiante['seg_nom']
    apellidos = nombre_estudiante['pri_ape']
    if nombre_estudiante['seg_ape'] != "":
        apellidos += "_" + nombre_estudiante['seg_ape'][0]
    return formatear_string(f"{nombres}.{apellidos}") + "@itb.edu.co"

print(list(map(
 generar_nombre_usuario, (
 { 'pri_nom': 'Manuel', 'seg_nom': 'Andrés', 'pri_ape': 'Ñañez', 'seg_ape': 'Guerra' },
 { 'pri_nom': 'Ana', 'seg_nom': 'María', 'pri_ape': 'Ordoñez', 'seg_ape': '' }, 
 { 'pri_nom': 'Andrea', 'seg_nom': '', 'pri_ape': 'Rodríguez', 'seg_ape': 'Jaramillo' },
 { 'pri_nom': 'Estefanía', 'seg_nom': '', 'pri_ape': 'Arciniegas', 'seg_ape': '' }
))))
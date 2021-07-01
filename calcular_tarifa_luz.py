from functools import reduce

fsuma = lambda val, suma: suma + val    

def determinar_porcentaje(estrato):
    if estrato == 1:
        porcentaje = .45
    elif estrato == 2:
        porcentaje = .3
    elif estrato == 3:
        porcentaje = .15
    else:
        porcentaje = -.55
    return porcentaje

def inforServicio(lectura : dict, tarifa : dict)-> tuple:
    id_predio = list()
    total_predio = list()
    consumos = list()
    subsidios = list()
    for ID in lectura.keys():
        if lectura[ID]['estado'] == 'activo':
            tarifas = list(tarifa.values())
            lecturas = list(lectura[ID]['toma_lectura'][0].values())
            consumo = reduce(lambda val, acum: acum - val, lecturas)
            tarifas[1] *= consumo
            porcentaje = determinar_porcentaje(lectura[ID]["estrato"])
            id_predio.append(ID)
            consumos.append(consumo)           
            total_predio.append(round(reduce(fsuma, tarifas) * (1 - porcentaje), 2))
            subsidios.append(round(reduce(fsuma, tarifas) * porcentaje, 2) if porcentaje > 0 else 0)
    if total_predio != []:
        list_tuplas = list(zip(id_predio, total_predio))
        total_consumo = reduce(fsuma, consumos)
        total_sub = reduce(fsuma, subsidios)
        return (list_tuplas, total_consumo, total_sub)
    else:
        return 'Sin lecturas'

### PRUEBAS - No subir a la plataforma ####

lectura = {
    '201501001': {
        'toma_lectura': [
            {
                'lec_anterior': 12,
                'lec_actual': 60,
            }
        ],
        'estrato': 1,
        'estado': 'activo'
    },
    '201501002': {
        'toma_lectura':
        [
            {
                'lec_anterior': 2,
                'lec_actual': 6,
            }
        ],
        'estrato': 2,
        'estado': 'activo'
    },
    '201501003': {
        'toma_lectura': [
            {
                'lec_anterior': 23,
                'lec_actual': 43,
            }
        ],
        'estrato': 3,
        'estado': 'activo'
    },
    '201501004': {
        'toma_lectura': [
            {
                'lec_anterior': 90,
                'lec_actual': 120,
            }
        ],
        'estrato': 1,
        'estado': 'activo'
    },
    '201501005': {
        'toma_lectura': [
            {
                'lec_anterior': 1,
                'lec_actual': 9,
            }
        ],
        'estrato': 1,
        'estado': 'inactivo'
    },
    '201564006': {
        'toma_lectura': [
            {
                'lec_anterior': 10,
                'lec_actual': 20}
        ],
        'estrato': 6,
        'estado': 'activo'
    }
}

tarifa = {
    'cargo_basico': 9850,
    'consumo': 800.27}

print(inforServicio(lectura, tarifa))

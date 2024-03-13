# Aquí se listan los juzgados y el proceso que le corresponde.

# El valor de la llave, correspondiente al id del juzgago, es una lista con 4 elementos:
# - Una lista cos dos datos:
#   - El id del proceso
#   - Los datos específicos para el proceso
# - Una lista de funciones que reciben un parámetro `datos` las cuales expresan las condiciones que se deben
#   de cumplir para ejecutar el proceso. Si el proceso no tiene condiciones, se debe de dejar una lista vacía.
# - Valor booleano que indica si se debe de usar el seleccionador de mes. Si se desea utilizar el valor
#   predefinido establecer como None
# - Nombre del juzgado

from typing import List, Tuple


def generarMesesDict(
    *valoresMeses: List[Tuple[int, int]]
):
    """
    Esta función se encarga de generar el diccionario de meses relacionando cada mes con
    una tupla de dos números enteros.

    Arguments:
        valoresMeses -- Lista de 12 tuplas con dos números enteros. Representan cada mes.

    Returns:
        Diccionario de meses con valores relacionados a las tuplas enviadas.
    """
    return {
        "enero": valoresMeses[0],
        "febrero": valoresMeses[1],
        "marzo": valoresMeses[2],
        "abril": valoresMeses[3],
        "mayo": valoresMeses[4],
        "junio": valoresMeses[5],
        "julio": valoresMeses[6],
        "agosto": valoresMeses[7],
        "septiembre": valoresMeses[8],
        "octubre": valoresMeses[9],
        "noviembre": valoresMeses[10],
        "diciembre": valoresMeses[11]
    }

procesos = {
    "EE-6-20-387-299": [
        [
            1,
            ["td[2]", "ESTADO-69-3|PROVIDENCIAS-01-4", "td[1]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 035 DE PEQUEÑAS CAUSAS Y COMPETENCIA MÚLTIPLE DE BOGOTÁ"
    ],
    "EE-4-7-78-327": [
        [2, ["td[2]" , True, "td[3]"]],
        [],
        None,
        "JUZGADO 012 CIVIL DEL CIRCUITO DE BOGOTÁ"
    ],
    # TODO: Migrar los juzgados en las condicionales en app-juzg-validado-base.py a partir de la línea 165
    "EE-6-23-478-1791": [
        [25, [True]],
        [],
        None,
        "JUZGADO 001 PROMISCUO MUNICIPAL DE TABIO - CUNDINAMARCA"
    ],
    "EE-4-7-89-123": [
        [
            21,
            [
                True,
                "ESTADO-08",
                generarMesesDict((2,1), (2, 2), (2, 3), (4, 1), (4, 2), (4, 3), (6, 1), (6, 2), (6, 3), (8, 1), (8, 2), (8, 3))
            ]
        ],
        [],
        None,
        "JUZGADO 01 CIVIL CIRCUITO DE ZIPAQUIRÁ - CUNDINAMARCA"
    ],
    "EE-4-7-80-906": [
        [2, ["td[2]" , True, "td[3]"]],
        [],
        None,
        "JUZGADO 01 CIVIL CIRCUITO DE CHIQUINQUIRÁ - BOYACÁ"
    ],
    "EE-4-7-89-977": [
        [2, ["td[2]" , True, "td[1]"]],
        [],
        None,
        "JUZGADO 01 CIVIL CIRCUITO DE CHOCONTÁ - CUNDINAMARCA"
    ],
    "EE-4-7-74-841": [
        [
            21,
            [
                True,
                "ESTADO-23",
                generarMesesDict((2, 1), (2, 2), (2, 3), (4, 1), (4, 2), (4, 3), (6, 1), (6, 2), (6, 3), (8, 1), (8, 2), (8, 3))
            ]    
        ],
        [],
        None,
        "JUZGADO 01 CIVIL CIRCUITO DE ENVIGADO - ANTIOQUIA"
    ],
    "EE-4-7-89-968": [
        [10, ["td[2]","td[3]", 1, True, False, "td[1]"]],
        [],
        None,
        "JUZGADO 01 CIVIL CIRCUITO DE FACATATIVÁ - CUNDINAMARCA"
    ],
    "4-7-89-970": [
        [4, ['td[2]','td[1]-00-01', True, -1 ]],
        [],
        None,
        "JUZGADO 01 CIVIL CIRCUITO DE FUNZA - CUNDINAMARCA"
    ]
}
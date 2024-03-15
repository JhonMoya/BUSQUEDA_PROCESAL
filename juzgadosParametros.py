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
    enero: Tuple[int, int] = (2,1),
    febrero: Tuple[int, int] = (2,2),
    marzo: Tuple[int, int] = (2,3),
    abril: Tuple[int, int] = (4, 1),
    mayo: Tuple[int, int] = (4, 2),
    junio: Tuple[int, int] = (4, 3),
    julio: Tuple[int, int] = (6, 1),
    agosto: Tuple[int, int] = (6, 2),
    septiembre: Tuple[int, int] = (6, 3),
    octubre: Tuple[int, int] = (8, 1),
    noviembre: Tuple[int, int] = (8, 2),
    diciembre: Tuple[int, int] = (8, 3),
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
        "enero": enero,
        "febrero": febrero,
        "marzo": marzo,
        "abril": abril,
        "mayo": mayo,
        "junio": junio,
        "julio": julio,
        "agosto": agosto,
        "septiembre": septiembre,
        "octubre": octubre,
        "noviembre": noviembre,
        "diciembre": diciembre
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
                generarMesesDict()
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
                generarMesesDict((1, 1), (1, 8), (1, 15), (2, 1), (2, 8), (2, 15), (3, 1), (3, 8), (3, 15), (4, 1), (4, 8), (4, 15))
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
    "EE-4-7-89-970": [
        [4, ['td[2]','False|td[1]-00-20', True, -1 ]],
        [],
        None,
        "JUZGADO 01 CIVIL CIRCUITO DE FUNZA - CUNDINAMARCA"
    ],
    "EE-4-7-89-972:2023": [
        [2, ['td[2]' , True, 'td[3]']],
        [],
        None,
        "JUZGADO 01 CIVIL CIRCUITO DE FUSAGASUGÁ - CUNDINAMARCA"         
    ],
    "EE-4-7-89-972:2024": [
        [
            1,
            ["td[2]", "ESTADO-116-2|PROVIDENCIAS-01-03", "td[1]", "/", 1, 0, True, True, 1]
        ]
    ],
    "EE-4-7-89-979": [
        [
            1,
            ["td[2]", "ESTADO-117-1|PROVIDENCIAS-00", "td[1]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 CIVIL CIRCUITO DE LA MESA - CUNDINAMARCA"
    ],
    "EE-4-7-80-912": [
         [
            1,
            ["td[2]", "ESTADO-118-3|PROVIDENCIAS-00", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 CIVIL CIRCUITO DE TUNJA - BOYACÁ"
    ],
    "EE-4-7-89-980": [
        [
            1,
            ["td[2]", "ESTADO-119-1|PROVIDENCIAS-01-04", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 CIVIL CIRCUITO DE VILLA DE SAN DIEGO DE UBATÉ - CUNDINAMARCA"
    ],
    "EE-4-7-82-928": [
        [4, ['td[2]','td[3]|td[1]-01-01', True, False]],
        [],
        None,
        "JUZGADO 01 CIVIL DEL CIRCUITO DE PUERTO BOYACA"
    ],
    "EE-6-19-358-404": [
        [
            1,
            ["td[2]", "ESTADO-121-3|PROVIDENCIAS-01-04", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 CIVIL MUNICIPAL DE TUNJA - BOYACÁ"
    ],
    "EE-6-19-353-381:2023": [
        [2, ['td[2]' , True, 'td[1]']],
        [],
        None,
        "JUZGADO 01 CIVIL MUNICIPAL DE ARAUCA - ARAUCA"
    ],
    "EE-6-19-353-381:2024": [
        [
            1,
            ["td[2]", "ESTADO-122-1|PROVIDENCIAS-01-03", "td[1]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 CIVIL MUNICIPAL DE ARAUCA - ARAUCA"
    ],
    "EE-6-19-352-369": [
        [12, [True, 'ESTADO-23|PROVIDENCIAS-00']],
        [],
        None,
        "JUZGADO 01 CIVIL MUNICIPAL DE BELLO - ANTIOQUIA"
    ],
    "EE-6-19-367-126": [
        [
            1,
            ["td[2]", "ESTADO-92-2|PROVIDENCIAS-01-03", "td[2]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 CIVIL MUNICIPAL DE CHIA"
    ],
    "EE-6-19-367-458": [
        [
            1,
            ["td[1]", "ESTADO-34-3|PROVIDENCIAS-00", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 CIVIL MUNICIPAL DE CHOCONTÁ - CUNDINAMARCA"
    ],
    "EE-6-19-359-413": [
        [12, [True, 'ESTADO-123|PROVIDENCIAS-00']],
        [],
        None,
        "JUZGADO 01 CIVIL MUNICIPAL DE DUITAMA - BOYACÁ"
    ],
    "EE-6-19-352-374": [
        [15, [True, 'ESTADO-23']],
        [],
        None,
        "JUZGADO 01 CIVIL MUNICIPAL DE ENVIGADO - ANTIOQUIA"
    ],
    "EE-6-19-361-427": [
        [
            1,
            ["td[1]", "ESTADO-01-02|PROVIDENCIAS-01-03", "td[2]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 CIVIL MUNICIPAL DE CHOCONTÁ - CUNDINAMARCA"
    ],
    "EE-6-19-367-155": [
        [
            1,
            ["td[2]", "ESTADO-90-01|PROVIDENCIAS-01-03", "td[1]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 CIVIL MUNICIPAL DE FUNZA - CUNDINAMARCA"
    ],
    "EE-6-19-367-243": [
        [
            1,
            ["td[2]", "ESTADO-33-03|PROVIDENCIAS-01-04", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 CIVIL MUNICIPAL DE FUSAGASUGA"
    ],
    "EE-6-19-367-459": [
        [
            1,
            ["td[2]", "ESTADO-124-03|PROVIDENCIAS-01-04", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 CIVIL MUNICIPAL DE GIRARDOT - CUNDINAMARCA"
    ],
    "EE-6-19-367-463": [
        [
            1,
            ["td[1]", "ESTADO-98-02|PROVIDENCIAS-01-02", "td[2]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 CIVIL MUNICIPAL DE GIRARDOT - CUNDINAMARCA"
    ],
    "EE-6-19-367-464": [
        [2, ['td[2]' , True, 'td[3]']],
        [],
        None,
        "JUZGADO 01 CIVIL MUNICIPAL DE LETICIA - AMAZONAS"
    ],
    "EE-6-19-360-415": [
        [2, ['td[1]' , True, 'td[2]']],
        [],
        None,
        "JUZGADO 01 CIVIL MUNICIPAL DE MANIZALES - CALDAS"
    ],
    "EE-6-19-352-209": [
        [
            1,
            ["td[1]", "ESTADO-23-02|PROVIDENCIAS-01-03", "td[2]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 CIVIL MUNICIPAL DE MEDELLÍN - ANTIOQUIA"
    ],
    "EE-6-19-367-241": [
        [
            1,
            ["td[2]", "ESTADO-97-01|PROVIDENCIAS-01-03", "td[1]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 CIVIL MUNICIPAL DE MOSQUERA"
    ],
    "EE-6-19-363-438": [
        [14, [True, 'ESTADO-126']],
        [],
        None,
        "JUZGADO 01 CIVIL MUNICIPAL DE POPAYÁN - CAUCA"
    ],
    "EE-6-19-365-449:2023": [
        [
            1,
            ["td[2]", "ESTADO-03-01|PROVIDENCIAS-01-03", "td[1]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 CIVIL MUNICIPAL DE QUIBDÓ - CHOCÓ"
    ],
    "EE-6-19-365-449:2024": [
        [
            21,
            [
                True,
                'ESTADO-03',
                generarMesesDict((3, 1), (3, 8), (10, 1), (10, 8), (18, 1), (18, 8), (26, 1), (26, 8), (33, 1), (33, 8), (40, 1), (40, 8))
            ]
        ],
        [],
        None,
        "JUZGADO 01 CIVIL MUNICIPAL DE QUIBDÓ - CHOCÓ"
    ],
    "EE-6-19-359-409": [
        [2, ['td[1]', True, 'td[2]']],
        [],
        None,
        "JUZGADO 01 CIVIL MUNICIPAL DE SOGAMOSO - BOYACÁ"
    ],
    "EE-6-19-364-444": [
        [2, ['td[2]', True, 'td[1]']],
        [],
        None,
        "JUZGADO 01 CIVIL MUNICIPAL DE VALLEDUPAR - CESAR"
    ],
    "EE-6-19-367-466:2023": [
        [
            1,
            ["td[1]", "ESTADO-07-02|PROVIDENCIAS-00", "td[2]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 CIVIL MUNICIPAL DE VILLA DE SAN DIEGO DE UBATÉ - CUNDINAMARCA"
    ],
    "EE-6-19-367-466:2024": [
        [
            21,
            [
                True,
                'ESTADO-07',
                generarMesesDict((1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3), (4, 1), (4, 2), (4, 3)),
            ]
        ],
        [],
        None,
        "JUZGADO 01 CIVIL MUNICIPAL DE VILLA DE SAN DIEGO DE UBATÉ - CUNDINAMARCA"
    ],
    "EE-6-19-362-432": [
        [
            1,
            ["td[1]", "ESTADO-127-02|PROVIDENCIAS-00", "td[2]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 CIVIL MUNICIPAL DE YOPAL - CASANARE"
    ],
    "EE-6-19-362-432": [
        [
            1,
            ["td[1]", "ESTADO-127-02|PROVIDENCIAS-00", "td[2]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 CIVIL MUNICIPAL DE YOPAL - CASANARE"
    ],
    "EE-6-19-367-120": [
        [
            1,
            ["td[2]", "ESTADO-06-01|PROVIDENCIAS-00", "td[1]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 CIVIL MUNICIPAL DE ZIPAQUIRA"
    ],
    "EE-6-20-389-712": [
        [12, [True, 'ESTADO-03|PROVIDENCIAS-00']],
        [],
        None,
        "JUZGADO 01 CIVIL MUNICIPAL DE BELLO - ANTIOQUIA"
    ],
    "EE-6-20-388-701": [
        [15, [True, 'ESTADO-03']],
        [],
        None,
        "JUZGADO 01 PEQUEÑAS CAUSAS Y COMPETENCIAS MULTIPLE DE CARTAGENA - BOLÍVAR"
    ],
    "EE-6-23-478-1724:2023": [
        [
            1,
            ["td[4]", "ESTADO-128-02|PROVIDENCIAS-01-03", "td[2]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE ANOLAIMA - CUNDINAMARCA"
    ],
    "EE-6-23-478-1724:2024": [
        [
            1,
            ["td[2]", "ESTADO-06-01|PROVIDENCIAS-01-04", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE ANOLAIMA - CUNDINAMARCA"
    ],
    "EE-6-23-478-1725": [
        [
            21,
            [
                True,
                "ESTADO-129",
                generarMesesDict((4, 1), (4, 9), (4, 17), (12, 1), (12, 9), (12, 17), (21, 1), (21, 9), (21, 17), (30, 1), (30, 9), (30, 17))
            ]
        ],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL APULO - CUNDINAMARCA"
    ],
    "EE-6-23-478-1728": [
        [5, ['td[2]', 'No. ESTADO-136-01|PROVIDENCIAS-00', True ]],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL BOJACA-CUNDINAMARCA"
    ],
    "EE-6-23-478-1730": [
        [
            1,
            ["td[2]", "ESTADO-137-03|PROVIDENCIAS-00", "td[1]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL CACHIPAY - CUNDINAMARCA"
    ],
    "EE-6-23-478-1726:2023": [
        [
            1,
            ["td[2]", "ESTADO-138-03|PROVIDENCIAS-00", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL CACHIPAY - CUNDINAMARCA"
    ],
    "EE-6-23-478-1726:2024": [
        [
            21,
            [
                True,
                "ESTADO-138",
                generarMesesDict((6, 1), (6, 9), (6, 16), (15, 1), (15, 9), (15, 16), (24, 1), (24, 9), (24, 16), (33, 1), (33, 9), (33, 16))
            ]
        ],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE ARBELAEZ - CUNDINAMARCA"   
    ],
    "EE-6-23-478-1702": [
        [22, ['td[1]', True, 1 ]],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE CAJICA"
    ],
    "EE-6-23-469-1380": [
        [
            1,
            ["td[2]", "ESTADO-141-03|PROVIDENCIAS-00", "td[1]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE CHÍQUIZA - BOYACÁ"
    ],
    "EE-6-23-478-1749": [
        [9, ['td[1]', True, 'td[2]']],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE GUACHETA-CUNDINAMARCA"
    ],
    "EE-6-23-478-1749:2023:2": [
        [10, ['td[1]', 'td[2]', 1, True, "ESTADO-142-02|PROVINCIAS-01-03", 'td[2]']],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE GUACHETA-CUNDINAMARCA"
    ],
    "EE-6-23-478-1713": [
        [
            1,
            ["td[2]", "ESTADO-143-01|PROVIDENCIAS-00", "td[1]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE GUADUAS CUNDINAMARCA"
    ],
    "EE-6-23-478-1753:2023": [
        [
            1,
            ["td[2]", "ESTADO-144-01|PROVIDENCIAS-00", "td[1]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE GUAYABAL DE SIQUIMA-CUNDINAMARCA"
    ],
    "EE-6-23-478-1753:2024": [
        [4, ['td[2]','False|td[1]-00-144', True, -1 ]],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE GUAYABAL DE SIQUIMA-CUNDINAMARCA"
    ],
    "EE-6-23-463-1227": [
         [
            1,
            ["td[2]", "ESTADO-00|PROVIDENCIAS-01-01", "td[1]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE LA ESTRELLA - ANTIOQUIA"
    ],
    "EE-6-23-469-1360": [
        [
            1,
            ["td[2]", "ESTADO-155-03|PROVIDENCIAS-01-01", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE MONIQUIRÁ - BOYACÁ"
    ],
    "EE-6-23-477-1687": [
        [2, ['td[2]', True, 'td[3]']],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE MOÑITOS - CÓRDOBA"
    ],
    "EE-6-23-469-1398:2023": [
        [22, ['td[2]', True, 1]],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE NUEVO COLÓN - BOYACÁ"
    ],
    "EE-6-23-469-1398:2024": [
        [
            1,
            ["td[2]", "ESTADO-160-03|PROVIDENCIAS-00", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE NUEVO COLÓN - BOYACÁ"
    ],
    "EE-6-23-470-1437": [
        [
            1,
            ["td[3]", "ESTADO-161-04|PROVIDENCIAS-00", "td[4]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE PAIPA - BOYACÁ"
    ],
    "EE-6-23-477-1692": [
        [2, ["td[2]" , True, "td[3]"]],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE PURISIMA - CORDOBA"
    ],
    "EE-6-23-469-1365": [
        [
            1,
            ["td[2]", "ESTADO-162-03|PROVIDENCIAS-00", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE RAMIRIQUI - BOYACÁ"
    ],
    "EE-6-23-469-1405": [
        [
            1,
            ["td[2]", "ESTADO-163-03|PROVIDENCIAS-00", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE RÁQUIRA - BOYACÁ"
    ],
    "EE-6-23-466-1279": [
        [2, ["td[2]" , True, "td[3]"]],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE SABANALARGA - ATLÁNTICO"
    ],
    "EE-6-23-469-1409": [
        #TODO
        [4, ['td[2]','td[4]|td[3]-01-164', True, False]],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE SAMACÁ - BOYACÁ"
    ],
    "EE-6-23-477-1693": [
        [
            1,
            ["td[2]", "ESTADO-03-03|PROVIDENCIAS-01-04", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE SAN ANDRÉS SOTAVENTO - CÓRDOBA"
    ],
    "EE-6-23-477-1694:2023": [
        [4, ['td[2]','False|td[3]-00-03', True, False]],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE SAMACÁ - BOYACÁ"
    ],
    "EE-6-23-477-1694:2024": [
        [
            1,
            ["td[2]", "ESTADO-03-03|PROVIDENCIAS-00", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE SAN ANTERO - CORDOBA"
    ],
    "EE-6-23-473-1560:2023": [
        [
            6, 
            lambda datos: ['td[5]', datos["NumeroRadicacion"], -1, True]
        ],
        [],
        False,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE SAN LUIS DE PALENQUE - CASANARE"
    ],
    "EE-6-23-473-1560:2024": [
        [
            1,
            ["td[2]", "ESTADO-167-03|PROVIDENCIAS-00", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE SAN LUIS DE PALENQUE - CASANARE"
    ],
    "EE-6-23-469-1418": [
        [
            1,
            ["td[2]", "ESTADO-168-03|PROVIDENCIAS-00", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE SIACHOQUE - BOYACÁ"
    ],
    "EE-6-23-478-1787": [
        [
            1,
            ["td[2]", "ESTADO-169-03|PROVIDENCIAS-00", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE SUESCA - CUNDINAMARCA"
    ],
    "EE-6-23-470-1478:2023": [
        [4, ['td[2]','False|td[3]-00-170', True, False]],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE TIBASOSA - BOYACÁ"
    ],
    "EE-6-23-470-1478:2024": [
        [7, ['td[2]', True, 'td[3]']],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE TIBASOSA - BOYACÁ"
    ],
    "EE-6-23-469-1434": [
        [
            1,
            ["td[2]", "ESTADO-172-03|PROVIDENCIAS-00", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL DE VENTAQUEMADA - BOYACÁ"
    ],
    "EE-6-23-478-1740": [
        [7, ['td[2]', True, 'td[3]']],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL EL ROSAL-CUNDINAMARCA"
    ],
    "EE-6-23-478-1741": [
        [
            1,
            ["td[2]", "ESTADO-174-03|PROVIDENCIAS-00", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL FOMEQUE - CUNDINAMARCA"
    ],
    "EE-6-23-478-1762": [
        [9, ['td[5]', True, 'td[6]']],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL MANTA - CUNDINAMARCA"
    ],
    "EE-6-23-478-1770:2023": [
        [
            1,
            ["td[2]", "ESTADO-175-03|PROVIDENCIAS-00", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL PASCA-CUNDINAMARCA"
    ],
    "EE-6-23-478-1770:2024": [
        [
            1,
            ["td[2]", "ESTADO-176-03|PROVIDENCIAS-00", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL PASCA-CUNDINAMARCA"
    ],
    "EE-6-23-478-1707:2023": [
        [11, ['td[4]', True, 'td[3]']],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL RICAURTE -CUNDINAMARCA"
    ],
    "EE-6-23-478-1707:2024": [
        [7, ['td[2]', True, 'td[3]']],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL RICAURTE -CUNDINAMARCA"
    ],
    "EE-6-23-478-1779": [
        [25, [True]],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL SAN JUAN DE RIOSECO-CUNDINAMARCA"
    ],
    "EE-6-23-478-1783": [
        [
            1,
            ["td[2]", "ESTADO-183-03|PROVIDENCIAS-01-04", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL SILVANIA - CUNDINAMARCA"
    ],
    "EE-6-23-478-1793": [
        [
            1,
            ["td[2]", "ESTADO-181-03|PROVIDENCIAS-01-04", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 PROMISCUO MUNICIPAL TENA-CUNDINAMARCA"
    ],
    "EE-6-23-485-2007:2023": [
        [
            1,
            ["td[2]", "ESTADO-166-03|PROVIDENCIAS-01-04", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 ROMISCUO MUNICIPAL DE COTA- CUNDINAMARCA"
    ],
    "EE-6-23-485-2007:2024": [
        [
            1,
            ["td[2]", "ESTADO-01EXCEL-03|PROVIDENCIAS-01-04", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 01 ROMISCUO MUNICIPAL DE COTA- CUNDINAMARCA"
    ],
    "EE-4-7-89-971:2023": [
        [
            1,
            ["td[1]", "ESTADO-01-02|PROVIDENCIAS-01-03", "td[2]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 02 CIVIL CIRCUITO DE FUNZA - CUNDINAMARCA"
    ],
    "EE-4-7-89-971:2024": [
        [
            1,
            ["td[1]", "ESTADO-03-02|PROVIDENCIAS-01-03", "td[2]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 02 CIVIL CIRCUITO DE FUNZA - CUNDINAMARCA"
    ],
    "EE-7-24-503-2337": [
        [
            1,
            ["td[2]", "ESTADO-180-03|PROVIDENCIAS-01-04", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 02 CIVIL MUNICIPAL DE EJECUCION DE SENTENCIA - CALI"
    ],
    "EE-6-19-361-428": [
        [
            1,
            ["td[2]", "ESTADO-85-01|PROVIDENCIAS-01-03", "td[1]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 02 CIVIL MUNICIPAL DE FLORENCIA - CAQUETÁ"
    ],
    "EE-6-19-367-156:2024": [
        [
            1,
            ["td[2]", "ESTADO-91-03|PROVIDENCIAS-01-04", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 02 CIVIL MUNICIPAL DE FUNZA - CUNDINAMARCA"
    ],
    "EE-6-19-367-460:2023": [
        [
            1,
            ["td[2]", "ESTADO-185-03|PROVIDENCIAS-01-04", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 02 CIVIL MUNICIPAL DE GIRARDOT - CUNDINAMARCA"
    ],
    "EE-6-19-367-460:2024": [
        [
            1,
            ["td[2]", "ESTADO-186-03|PROVIDENCIAS-01-04", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 02 CIVIL MUNICIPAL DE GIRARDOT - CUNDINAMARCA"
    ],
    "EE-6-19-352-210": [
        [14, [True, 'ESTADO-23']],
        [],
        None,
        "JUZGADO 02 CIVIL MUNICIPAL DE MEDELLÍN - ANTIOQUIA"
    ],
    "EE-6-19-364-445": [
        [10, ["td[2]","td[3]", 1, True, False, "td[1]"]],
        [],
        None,
        "JUZGADO 02 CIVIL MUNICIPAL DE VALLEDUPAR - CESAR"
    ],
    "EE-6-19-366-454:2023": [
        [2, ["td[2]" , True, "td[3]"]],
        [],
        None,
        "JUZGADO 02 DE PEQUEÑAS CAUSAS Y COMPETENCIAS MULTIPLES MONTERIA - CORDOBA"
    ],
    "EE-6-19-366-454:2024": [
        [
            1,
            ["td[2]", "ESTADO-03-03|PROVIDENCIAS-00", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 02 DE PEQUEÑAS CAUSAS Y COMPETENCIAS MULTIPLES MONTERIA - CORDOBA"
    ],
    "EE-6-20-383-630:2023": [
        [
            1,
            ["td[2]", "ESTADO-03-01|PROVIDENCIAS-00", "td[1]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 02 PEQUEÑAS CAUSAS COMPETENCIAS MULTIPLE CASA DE JUSTICIA EL BOSQUE - MEDELLIN"
    ],
    "EE-6-20-383-630:2024": [
        [14, [True, 'ESTADO-03']],
        [],
        None,
        "JUZGADO 02 PEQUEÑAS CAUSAS COMPETENCIAS MULTIPLE CASA DE JUSTICIA EL BOSQUE - MEDELLIN"
    ],
    "EE-6-23-478-1703:2024": [
        [
            1,
            ["td[2]", "ESTADO-191-03|PROVIDENCIAS-00", "td[3]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 02 PROMISCUO MUNICIPAL DE CAJICA"
    ],
    "EE-6-19-352-211:2024": [
        [15, [True, 'ESTADO-23']],
        [],
        None,
        "JUZGADO 03 CIVIL MUNICIPAL DE MEDELLÍN - ANTIOQUIA"
    ],
    "EE-6-19-364-446": [
        [
            1,
            ["td[3]", "ESTADO-01-01|PROVIDENCIAS-01-02", "td[1]", "/", 1, 0, True, True, 1]
        ],
        [],
        None,
        "JUZGADO 03 CIVIL MUNICIPAL DE VALLEDUPAR - CESAR"
    ],
    "EE-7-24-502-2332:2023": [
        [
            21,
            [
                True,
                "ESTADO-01",
                generarMesesDict((10, 1), (10, 9), (10, 17), (18, 1), (18, 9), (18, 17), (27, 1), (27, 9), (27, 17), (36, 1), (36, 9), (36, 17))
            ]
        ],
        [],
        None,
        "JUZGADO 04 CIVIL MUNICIPAL DE EJECUCION DE SENTENCIA - BUCARAMANGA - SANTANDER"
    ],
    "EE-7-24-502-2332:2024": [
        [
            21,
            [
                True,
                "ESTADO-01",
                generarMesesDict((8, 1), (8, 9), (8, 17), (17, 1), (17, 9), (17, 17), (26, 1), (26, 9), (26, 17), (34, 1), (34, 9), (34, 17))
            ]
        ],
        [],
        None,
        "JUZGADO 04 CIVIL MUNICIPAL DE EJECUCION DE SENTENCIA - BUCARAMANGA - SANTANDER"
    ],
    "EE-7-24-496-2305": [
        [
            21,
            [
                True,
                "ESTADO-23",
                generarMesesDict((5, 2), (5, 10), (5, 18), (15, 2), (15, 10), (15, 18), (25, 2), (25, 10), (25, 18), (35, 2), (35, 10), (35, 18))
            ]
        ],
        [],
        None,
        "JUZGADO 04 CIVIL MUNICIPAL DE EJECUCION DE SENTENCIAS DE MEDELLÍN - ANTIOQUIA"
    ],
    "EE-6-19-352-372:2023": [
        [2, ["td[2]" , True, "td[3]"]],
        [],
        None,
        "JUZGADO 05 CIVIL MUNICIPAL DE BELLO - ANTIOQUIA"
    ],
    "EE-6-19-352-372:2024": [
        [14, [True, 'ESTADO-23']],
        [],
        None,
        "JUZGADO 05 CIVIL MUNICIPAL DE BELLO - ANTIOQUIA"
    ],
    "EE-7-24-496-2307:2024": [
        [
            21,
            [
                True,
                "ESTADO-23",
                generarMesesDict((5, 2), (5, 10), (5, 18), (15, 2), (15, 10), (15, 18), (25, 2), (25, 10), (25, 18), (35, 2), (35, 10), (35, 18))
            ]
        ],
        [],
        None,
        "JUZGADO 06 CIVIL MUNICIPAL DE EJECUCION DE SENTENCIAS DE MEDELLÍN - ANTIOQUIA"
    ],
    "EE-6-19-377-541:2023": [
        [
            21,
            [
                True,
                "ESTADO-194",
                generarMesesDict((3, 1), (3, 8), (3, 15), (11, 1), (11, 8), (11, 15), (19, 1), (19, 8), (19, 15), (27, 1), (27, 8), (27, 15))
            ]
        ],
        [],
        None,
        "JUZGADO 06 CIVIL MUNICIPAL DE PEREIRA - RISARALDA"
    ],
    "EE-6-19-377-541:2024": [
        [
            21,
            [
                True,
                "ESTADO-194",
                generarMesesDict((3, 1), (3, 8), (3, 15), (11, 1), (11, 8), (11, 15), (19, 1), (19, 8), (19, 15), (27, 1), (27, 8), (27, 15))
            ]
        ],
        [],
        None,
        "JUZGADO 06 CIVIL MUNICIPAL DE PEREIRA - RISARALDA"
    ],
    "EE-6-20-383-634:2023": [
        [14, [True, 'ESTADO-192']],
        [],
        None,
        "JUZGADO 06 CIVIL PEQUEÑAS CAUSAS Y COMPETENCIAS MULTIPLES DE MEDELLÍN - ANTIOQUIA"
    ],
    "EE-7-24-496-2308:2024": [
        [
            21,
            [
                True,
                "ESTADO-23",
                generarMesesDict((5, 2), (5, 10), (5, 18), (15, 2), (15, 10), (15, 18), (25, 2), (25, 10), (25, 18), (35, 2), (35, 10), (35, 18))
            ]
        ],
        [],
        None,
        "JUZGADO 07 CIVIL MUNICIPAL DE EJECUCION DE SENTENCIAS DE MEDELLÍN - ANTIOQUIA"
    ],
    "EE-6-19-357-396:2023": [
        [15, [True, 'ESTADO-01']],
        [],
        None,
        "JUZGADO 12 CIVIL MUNICIPAL DE CARTAGENA - BOLÍVAR"
    ],
    "EE-6-19-357-396:2024": [
        [14, [True, 'ESTADO-03']],
        [],
        None,
        "JUZGADO 12 CIVIL MUNICIPAL DE CARTAGENA - BOLÍVAR"
    ],
    "EE-6-19-352-228": [
        [19, [True, 'ESTADO-23']],
        [],
        None,
        "JUZGADO 20 CIVIL MUNICIPAL DE MEDELLÍN - ANTIOQUIA"
    ],
    "EE-6-20-386-670": [
        [
            21,
            [
                True,
                "ESTADO-03",
                generarMesesDict((1, 1), (1, 8), (1, 15), (2, 1), (2, 8), (2, 15), (3, 1), (3, 8), (3, 15), (4, 1), (4, 8), (4, 15))
            ]
        ],
        [],
        None,
        "JUZGADO 20 PEQUEÑAS CAUSAS Y COMPETENCIAS MULTIPLES DE BARRANQUILLA, ATLÁNTICO ANTES JUZGADO 29 CIVIL MUNICIPAL DE BARRANQUILLA, ATLÁNTICO"
    ],
    "EE-6-23-462-1180:2023": [
        [
            24,
            [
                True,
                'ESTADO-152',
                generarMesesDict((3, 1), (3, 9), (3, 17), (11, 1), (11, 9), (11, 17), (20, 1), (20, 9), (20, 17), (29, 1), (29, 9), (29, 17))
            ]
        ],
        [],
        None,
        "JUZGADO PROMISCUO MUNICIPAL DE GRANADA- CUNDINAMARCA"
    ],
    "EE-6-23-462-1180:2024": [
        [
            24,
            [
                True,
                'ESTADO-152',
                generarMesesDict((1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3), (4, 1), (4, 2), (4, 3))
            ]
        ],
        [],
        None,
        "JUZGADO PROMISCUO MUNICIPAL DE GRANADA- CUNDINAMARCA"
    ],
    "EE-6-23-478-1760:2023": [
        [
            6, 
            lambda datos: ['td[2]', datos["NumeroRadicacion"], -1, True]
        ],
        [],
        False,
        "JUZGADO PROMISCUO MUNICIPAL DE LENGUAZAQUE, CUNDINAMARCA"
    ],
    "EE-6-23-478-1760:2024": [
        [9, ['td[2]', True, 'td[6]']],
        [],
        False,
        "JUZGADO PROMISCUO MUNICIPAL DE LENGUAZAQUE, CUNDINAMARCA"
    ],
    "EE-6-23-478-1738:2024": [
        [25, [True]],
        [],
        None,
        "JUZGADO PROMISCUO MUNICIPAL MESITAS DEL COLEGIO-CUNDINAMARCA"
    ],
}
# Estado-Modelo-Columna|Provdencia-01-col
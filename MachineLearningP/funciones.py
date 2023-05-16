

def codificador(tabla):
    '''
    Esta función utiliza las señales O, H, L y C para
    generar códigos y colores de plantilla resumen.

    Para esta función tabla debe estar formateada según especificación abajo

    Formato columnas tabla: HORA - OPEN - HIGH - LOW - CLOSE (type: str, float...)

    retorno: lista de arreglos [[hora, 'codigo letra', 'color'], ...]
    '''
    respuesta = {}
    for k in range(1, len(tabla)):
        salida = []
        # este comando resta dos tuplas consecutivas tabla[k] - tabla[k-1]
        # La función mapea cada tupla y va restando componente a componente
        res = tuple(map(lambda i, j: i - j, tabla[k][1::], tabla[k-1][1::]))

        # genera LSOI
        if res[1] > 0 and res[2] >= 0: 
            salida = [tabla[k][0], 'L']
        if res[1] <= 0 and res[2] < 0: 
            salida = [tabla[k][0], 'S'] 
        if res[1] > 0 and res[2] < 0 : 
            salida = [tabla[k][0], 'O']
        if res[1] <= 0 and res[2] >= 0:
            salida = [tabla[k][0], 'I']

        # genera colores (green, red, yellow)
        if tabla[k][4] > tabla[k][1]: 
            salida.append('green')
        if tabla[k][4] < tabla[k][1]:
            salida.append('red')
        if tabla[k][4] == tabla[k][1]: 
            salida.append('yelow') 
        
        # respuesta.append(salida)
        respuesta['tiempo'].append(salida[0])
    return respuesta


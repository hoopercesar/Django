from django.db import models
import pickle
import sqlite3
import datetime
import pandas as pd
import numpy as np
import yfinance as yf


con = sqlite3.connect('C:/Users/Cesar Hooper/Desktop/github/proyecto_MARCELO/dbsheets.db', check_same_thread=False)
cur = con.cursor()

cur.execute("SELECT * FROM datos5m")
tabla = cur.fetchall()

# Create your models here.
def codificador(tabla):
    '''
    Esta función utiliza las señales O, H, L y C para
    generar códigos y colores de plantilla resumen.

    Para esta función tabla debe estar formateada según especificación abajo

    Formato columnas tabla: HORA - OPEN - HIGH - LOW - CLOSE (type: str, float...)

    retorno: lista de arreglos [[hora, 'codigo letra', 'color'], ...]
    '''
    respuesta = []

    for k in range(1, len(tabla)):
        salida = []
        parcial = {}
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
        
        parcial['tiempo'] = salida[0]
        parcial['simbolo'] = salida[1]
        parcial['color'] = salida[2]

        respuesta.append(parcial)
    return respuesta

def codificado():
    return codificador(tabla)

def financial(start, end):
    tsla = yf.Ticker('TSLA')
    data = yf.download("TSLA", interval = "1d", start=start, end=end)
    # "2022-01-01"
    # "2023-01-01"
    return data


print(pd.__version__)
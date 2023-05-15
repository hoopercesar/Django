# from django.test import TestCase
import sqlite3
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from collections import Counter
from funciones import codificador

# Create your tests here.
# con = sqlite3.connect("data/portal_mammals.sqlite")
# df = pd.read_sql_query("SELECT * from surveys", con)
path = 'C:/Users/Cesar Hooper/Desktop/github/proyecto_MARCELO/'
dbs = [db for db in os.listdir(path) if db[-2::] == 'db' and db[5].isdigit()==True]

con = sqlite3.connect('C:/Users/Cesar Hooper/Desktop/github/proyecto_MARCELO/dbsheets.db', check_same_thread=False)
cur = con.cursor()

cur.execute("SELECT * FROM datos5m")
rows = cur.fetchall()

# selecciona las tablas dentro de una DB
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tablas = cur.fetchall()

def formated(vector):
    return datetime.date(int(vector[0]), int(vector[1]), int(vector[2]))

# hora = [hora[1] for hora in rows]
# fecha = [fecha[0][0:10].split('-') for fecha in rows]
# fechaformated = list(map(formated, fecha))
# f = fecha[0]
# z = Counter(fechaformated)
# c = 0
# for k in z:
#     c += z[k]
#     print(k, z[k], c)

# cuenta y selecciona los días -diferentes entre sí- en la DB
# cur.execute('SELECT DISTINCT fecha FROM data')
# # crea una lista con las fechas de la DB
# filas = cur.fetchall()
# # define una fecha específica de la lista de fechas
# my_string = filas[10]
# # selecciona todos los datos correspondientes a la fecha definida anteriormente
# cur.execute("SELECT * FROM data WHERE fecha = ?", (my_string))
# resultado = cur.fetchall()
# print(dbs)

respuesta = codificador(rows)

print(respuesta)

    # print(res)
    # print(k, rows[k][1::]-rows[k-1][1::])

con.close()





from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
import sqlite3
import os

import dash
# import dash_core_components as dcc
from dash import dcc, html
import plotly
import pickle as pk
import joblib
# import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
from plotly.offline import plot
from plotly.graph_objs import Scatter
from django_plotly_dash import DjangoDash


# ruta = 'C:/Users/Cesar Hooper/Desktop/github/proyecto_MARCELO/bdml2023.xlsx'

path = 'C:/Users/Cesar Hooper/Desktop/github/proyecto_MARCELO/DOCUMENTO/'
con = sqlite3.connect('C:/Users/Cesar Hooper/Desktop/github/proyecto_MARCELO/data.db')
cur = con.cursor()

cur.execute("SELECT * FROM data")
rows = cur.fetchall()

# selecciona fecha
cur.execute("SELECT DISTINCT fecha FROM data")
fechas = cur.fetchall()

# selecciona hora
cur.execute("SELECT hora FROM data")
hora = cur.fetchall()

# los datos x e y
y0 = [row[10] for row in rows]
y1 = [row[11] for row in rows]
y2 = [row[12] for row in rows]
t = np.arange(len(y1))

r0 = list(rows[0])

# 6+!3pbYw?2YfbkE
# modelo_enero2022.pkl

model_name = [modelo for modelo in os.listdir(path) if modelo[-3::] == 'pkl']

# función para calcular la entropía
def entropy(vector):
    return sum([0 if k == 0 else -k*np.log2(k) for k in vector])


# cargar modelo con joblib
modelo = joblib.load(path + 'modelo_enero2022.pkl')

# data scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# datos = pd.DataFrame(rows)
# fecha = datos['fecha']
# hora = datos['hora']
# datos = datos.drop(['fecha', 'hora'], axis=1)
# datos = datos.apply(pd.to_numeric)


# scaler.fit(datos)
# X = scaler.transform(datos)

# x_pred = modelo.predict(X)
# x_prob = modelo.predict_proba(X)

# x0 = [k[1] for k in x_prob] # 0
# x_1 = [k[0] for k in x_prob] # -1
# x1 = [k[2] for k in x_prob] # 1
# # Create your views here.

# # cálculo de entropia
# entropia = list(map(entropy, x_prob))

# # columnas
# columnas = ['col' + str(k) for k in range(0, 14)]


def home(request):
    print(fechas)
    return render(request, 'home.html', {
        'plot_div': 'mensaje', 
        'hola': 'mensaje', 
        'color': 'red',

    })
   

def base(request):   
    # # cuenta y selecciona los días -diferentes entre sí- en la DB
    # cur.execute('SELECT DISTINCT fecha FROM data')
    # # crea una lista con las fechas de la DB 
    # fechas = cur.fetchall()
    if request.method == 'POST':
        accion = request.POST.get('accion')
        # print(accion)

    print('Aquí va', request.POST.get('fecha'))

    return render(request, 'base.html', {
        'plot_div': 'mensaje',
        'fechas' : fechas,
        })

 
def probs(request):
    return render(request, 'probs.html', {
        'plot_div': 'un mensaje', 
    })


def tablas(request):
    return render(request, 'tablas.html', context={
        'tabla' : rows,     
        'titulo': 'Aquí van las tablas', 
        # 'columnas': columnas,
    })

con.close()
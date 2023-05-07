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

datos = pd.DataFrame()
datos['hola'] = [1, 2, 3, 4]
datos['ok'] = [-4, 3, 0, 8]
# ruta = 'C:/Users/Cesar Hooper/Desktop/github/proyecto_MARCELO/bdml2023.xlsx'
x = [1, 2, 3, 4]
y = [-4, 3, 0, 8]
path = 'C:/Users/Cesar Hooper/Desktop/github/proyecto_MARCELO/DOCUMENTO/'
con = sqlite3.connect('C:/Users/Cesar Hooper/Desktop/github/proyecto_MARCELO/data.db')
cur = con.cursor()
cur.execute("SELECT * FROM data")
rows = cur.fetchall()

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

datos = pd.DataFrame(rows)
fecha = datos['fecha']
hora = datos['hora']
datos = datos.drop(['fecha', 'hora'], axis=1)
datos = datos.apply(pd.to_numeric)


scaler.fit(datos)
X = scaler.transform(datos)

x_pred = modelo.predict(X)
x_prob = modelo.predict_proba(X)

x0 = [k[1] for k in x_prob] # 0
x_1 = [k[0] for k in x_prob] # -1
x1 = [k[2] for k in x_prob] # 1
# Create your views here.

# cálculo de entropia
entropia = list(map(entropy, x_prob))

# columnas
columnas = ['col' + str(k) for k in range(0, 14)]


def home(request):
    print(columnas)
    x_data = t
    y_data = y0
    plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')


    title = 'esto es un título'
    return render(request, 'home.html', 
                  context={
                      'plot_div': plot_div, 
                      'hola': x_pred[0], 
                      'color': 'red',
                      })


def base(request):   

    trace1 = go.Scatter(
        x=t,
        y=y1,
        mode='lines',
        name='CCI 5'
    )
    
    trace2 = go.Scatter(
        x=t,
        y=y2,
        mode='lines',
        name='CCI 30'
    )

    trace3 = go.Scatter(
        x = t,
        y = 200*x_pred,
        mode = 'lines',
        name = 'Classificación'
    )
    
    data = [trace1, trace2, trace3]
    layout = go.Layout(title='CCI', height=500)
    fig = go.Figure(data=data, layout=layout)
    
    plot_div = plotly.offline.plot(fig, auto_open=False, output_type='div')
    
    context = {'plot_div': plot_div}
    
    return render(request, 'base.html', context)

 
def probs(request):

    trace0 = go.Scatter(
        x = t,
        y = x0,
        mode = 'lines',
        name = 'Prob: 0'
    )

    trace_1 = go.Scatter(
        x = t,
        y = x_1,
        mode = 'lines',
        name = 'Prob: -1'
    )

    trace1 = go.Scatter(
        x = t,
        y = entropia,
        mode = 'lines',
        name = 'Prob: 1'
    )

    data = [trace0, trace_1, trace1]
    layout = go.Layout(title='Probabilidades', height=500)
    fig = go.Figure(data=data, layout=layout)
    
    plot_div = plotly.offline.plot(fig, auto_open=False, output_type='div')
    
    context = {'plot_div': plot_div}

    return render(request, 'probs.html', context)

def tablas(request):
    return render(request, 'tablas.html', context={
        'tabla' : rows,     
        'titulo': 'Aquí van las tablas', 
        'columnas': columnas,
    })
    


    

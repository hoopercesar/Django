from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
import sqlite3
import os
from collections import Counter
from .models import codificado, financial, creaRangeBar

import dash
from .graficos import graficoSegunFecha
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

# las funciones para graficar


path = 'C:/Users/Cesar Hooper/Desktop/github/proyecto_MARCELO/DOCUMENTO/'
con = sqlite3.connect('C:/Users/Cesar Hooper/Desktop/github/proyecto_MARCELO/data.db', check_same_thread=False)
cur = con.cursor()
#
cur.execute("SELECT * FROM data")
rows = cur.fetchall()

# selecciona fecha
cur.execute("SELECT DISTINCT fecha FROM data")
fechas = cur.fetchall()

# selecciona hora
cur.execute("SELECT hora FROM data")
hora = cur.fetchall()

# los datos x e y
# y0 = [row[10] for row in rows]
# y1 = [row[11] for row in rows]
# y2 = [row[12] for row in rows]
# t = np.arange(len(y1))

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

# fechas = [fecha[0] for fecha in fechas]

def home(request):

    if request.method == 'POST':
        fecha_string = eval(request.POST.get('accion'))[0]
        datos_selected = [row for row in rows if row[0]==fecha_string]

        t = [col[1] for col in datos_selected] 
        y1 = [float(col[12]) for col in datos_selected]
 
        trace1 = go.Scatter(
            x = t,
            y=y1,
            mode='lines',
            name='Precio'
        )

        layout = go.Layout(title='Precio', height=500)
        fig = go.Figure(data=trace1, layout=layout)

        plot_div = plotly.offline.plot(fig, auto_open=False, output_type='div')
        
        context = {
            'plot_div': plot_div,
            'fechas' : fechas,
            'titulo' : fecha_string,
            }      
        return render(request, 'home.html', context)
   
   
    else: 
        return render(request, 'home.html', {
            'plot_div': 'Selecciona una Fecha', 
            'fechas': fechas,
            })


def base(request): 
        
    if request.method == 'POST':
        fecha_string = eval(request.POST.get('accion'))[0]
        datos_selected = [row for row in rows if row[0]==fecha_string]
        
        y1 = [col[13] for col in datos_selected] 
        t = [col[1] for col in datos_selected]      

        trace1 = go.Scatter(
            x = t,
            y=y1,
            mode='lines',
            name='CCI 5'
        )
    
        y2 = [col[14] for col in datos_selected]
        trace2 = go.Scatter(
            x=t,
            y=y2,
            mode='lines',
            name='CCI 30'
        )
        
        data = [trace1, trace2]
        layout = go.Layout(title='CCI', height=500)
        fig = go.Figure(data=data, layout=layout)
    
        plot_div = plotly.offline.plot(fig, auto_open=False, output_type='div')
        
        context = {
            'plot_div': plot_div,
            'fechas' : fechas,
            'titulo' : fecha_string,
            }       
            

        return render(request, 'base.html', context)
    else:
        return render(request, 'base.html', {
            'fechas': fechas,
            'plot_div': 'Selecciona una Fecha',

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


def resumen(request):
    resultados = codificado()
    
    return render(request, 'resumen.html', {
        'minutos': resultados,
        'test' : {
            'hola': ['chao', 'pronto', 'quizás'], 
            'dia': ['noche', 'tarde', 'mañana'], 
            'frio': [1, 2, 5]
            }, 
    })


def bolsa(request):
    instrumentos = ['AAPL', 'GIGA', 'AMZN', 'TSLA', 'MSFT', 'NKE']
    intervalos = ['1m', '2m', '5m', '15m', '30m', '60m', 
                '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo']
    
    if request.method == 'POST':
        desde = request.POST.get('desde')
        hasta = request.POST.get('hasta')
        intervalo = request.POST.get('intervalo')
        instrumento = request.POST.get('instrumento')
        df = financial(desde, hasta, intervalo, instrumento)

        y1 = list(df.Close)
        t = df.index  #np.arange(0, 115)   

        trace1 = go.Scatter(
            x = t,
            y=y1,
            mode='lines',
            name='CLOSE'
        )

        y2 = list(df.Open)
        trace2 = go.Scatter(
            x = t,
            y = y2,
            mode = 'lines',
            name = 'OPEN'
        )

        data = [trace1, trace2]
        layout = go.Layout(title='Señales Open y Close vs Tiempo', height=500)
        fig = go.Figure(data=data, layout=layout)

        plot_div = plotly.offline.plot(fig, auto_open=False, output_type='div')
        
        context = {
            'plot_div': plot_div,
            'intervalos': intervalos,
            'instrumentos': instrumentos,
        }
     
        return render(request, 'bolsa.html', context)
    else:
        context = {
            'plot_div': 'Seleccione para obtener información',
            'intervalos': intervalos,
            'instrumentos':instrumentos,
        }
        return render(request, 'bolsa.html', context)
 
    # df = financial(desde, hasta)


def rangeBar(request):
    layout = go.Layout(title='Range Bar', height=700)
    df = financial("2023-05-05", "2023-05-10", "5m", "CME")
    rangebar = creaRangeBar(df.Close)


    fig = go.Figure(data=go.Ohlc(x=df.index,
                                    open=df.Open,
                                    high=df.High,
                                    low=df.Low,
                                    close=df.Close),
                                    layout=layout)

    fig.update(layout_xaxis_rangeslider_visible=False)
    plot_div = plotly.offline.plot(fig, auto_open=False, output_type='div')
    context = {
            'plot_div': plot_div,
            'titulo': 'éste es un título',
        }
    

    return render(request, 'rangebar.html', context)


con.close()
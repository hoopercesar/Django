from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
import sqlite3

import dash
# import dash_core_components as dcc
from dash import dcc, html
import plotly
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
con = sqlite3.connect('dataset.db')
cur = con.cursor()
cur.execute("SELECT col10, col11, col12 FROM dataset")
rows = cur.fetchall()

# los datos x e y
y1 = [row[1] for row in rows]
y2 = [row[2] for row in rows]
t = np.arange(len(y1))

# 6+!3pbYw?2YfbkE

# Create your views here.
def home(request):
    x_data = t
    y_data = y1
    plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')


    title = 'esto es un título'
    return render(request, 'home.html', context={'plot_div': plot_div})


def base(request):   

    trace1 = go.Scatter(
        x=t,
        y=y1,
        mode='lines',
        name='CCI 30'
    )
    
    trace2 = go.Scatter(
        x=t,
        y=y2,
        mode='lines',
        name='CCI 5'
    )
    
    data = [trace1, trace2]
    layout = go.Layout(title='CCI')
    fig = go.Figure(data=data, layout=layout)
    
    plot_div = plotly.offline.plot(fig, auto_open=False, output_type='div')
    
    context = {'plot_div': plot_div}


    
    return render(request, 'base.html', context)
  

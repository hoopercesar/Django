import sqlite3
import pandas as pd
import numpy as np
import os

from dash import dcc, html
import plotly
import pickle as pk
# import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
from plotly.offline import plot
from plotly.graph_objs import Scatter
from django_plotly_dash import DjangoDash

# conexion a la DB
con = sqlite3.connect('C:/Users/Cesar Hooper/Desktop/github/proyecto_MARCELO/data.db', check_same_thread=False)
cur = con.cursor()
# table = """"""
# cur.execute(table)

cur.execute("SELECT * FROM data")
rows = cur.fetchall()

def graficoSegunFecha(fecha):
    my_string = fecha
    # cur.execute("SELECT * FROM data WHERE fecha = ?", (my_string))
    # data = cur.fetchall()
    print('HOLA, los datos', my_string)

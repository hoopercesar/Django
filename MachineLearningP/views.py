from django.shortcuts import render
import pandas as pd

datos = pd.DataFrame()
datos['hola'] = [1, 2, 3, 4]
datos['ok'] = [-4, 3, 0, 8]
# ruta = 'C:/Users/Cesar Hooper/Desktop/github/proyecto_MARCELO/bdml2023.xlsx'

# 6+!3pbYw?2YfbkE

# Create your views here.
def home(request):
    title = 'esto es un título'
    return render(request, 'home.html', {
        'titulo': title,
    })

def base(request):
    
    return render(request, 'base.html', {
        'datos': datos
    })
  

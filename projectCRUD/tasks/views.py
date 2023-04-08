from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def holamundo(request):
    titulo = 'éste es un título'
    return render(request, 'signup.html', {
        # 'mytitle' : titulo,
        'form' : UserCreationForm,

    })
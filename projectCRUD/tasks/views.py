from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db import IntegrityError

# Create your views here.
def signup(request):

    if request.method == 'GET': 
        print('enviando formularios')
        return render(request, 'signup.html', {
            'form' : UserCreationForm,
        })
    else:
       if request.POST['password1'] == request.POST['password2']:
           try:
                
                print('password correcto')
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                
                user.save()
                print('user = ', user)
                login(request, user)
                # return HttpResponse('Usuario creado')
                return redirect('tasks')
           except IntegrityError:
                   
               # el integrityError aparece cuando se registra un usuario
               # con un nombre que ya existe en la base de datos
               return render(request, 'signup.html', {
                    'form' : UserCreationForm,
                    'mensaje' : 'Usuario ya existe',
                })
            #    HttpResponse('Usuario ya existe')
          
       else:
           return render(request, 'signup.html', {
                    'form' : UserCreationForm,
                    'mensaje' : 'Contraseñas no son iguales',
                })
    
def tasks(request):
    return render(request, 'tasks.html')



def home(request):
    return render(request, 'home.html')
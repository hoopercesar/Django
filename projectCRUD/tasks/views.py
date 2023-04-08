from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

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
                print(user)
                # return HttpResponse('Usuario creado')
                return render(request, 'login.html', {
                    # 'form' : AuthenticationForm,
                    'mensaje' : 'Usuario Creado Correctamente. Ingresa a tu cuenta',
                })
           except:
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

def login(request):
    return render(request, 'login.html')
    # usuario = request.POST['usuario'],
    # password = request.POST['password'],
    # user = authenticate(request, username=usuario, password=password)
    # if user is not None:
    #     return HttpResponse('Bienvenido')
    # else:
    #     return render(request, 'login.html', {
    #         'mensaje': 'Usuario incorrecto'
    #     })

def home(request):
    return render(request, 'home.html')
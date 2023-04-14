from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from .forms import TaskForm
from .models import Task
from django.shortcuts import get_object_or_404


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
                # login(request, user)
                # return HttpResponse('Usuario creado')
                return redirect('signin')
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
    tasks = Task.objects.filter(user=request.user)
    # print(tasks)
    return render(request, 'tasks.html', {
        'tasks' : tasks,
    })

def task_details(request, task_id):
    # task = Task.objects.get(user=request.user, pk=task_id)
    cantidad = Task.objects.filter(user=request.user)
    # print( 'tarea =', len(cantidad)) , pk=task_id
    task = get_object_or_404(Task, user=request.user, pk=task_id)
    form = TaskForm(instance=task)
    
    return render(request, 'task_details.html',{
        'id': task_id,
        'task' : task,
        'form' : form,  
        'cantidad' : len(cantidad),
    })       

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
                'form': TaskForm
            })
    else: 
        # con el comando TaskForm(request.POST).save() se guardan los datos
        # en formato formulario que vienen de la clase TaskForm en forms
        try:
            new_task = TaskForm(request.POST).save(commit=False)
            new_task.user = request.user
            new_task.save()
            print(new_task)
            return redirect('tasks')
        except ValueError: 
            return render('create_task.html', {
                'form': TaskForm,
                'error': 'Datos no Válidos', 
            })
    

def home(request):
    return render(request, 'home.html')

# para mostrar el usuario en el nav
def usuario(request):
    print(request.user)

# para cerrar la sesión
def signout(request):
    logout(request)
    return redirect('home')

# para entrar en la sesión del usuario
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        # usuario = False
        print(request)
        if user is not None: 
            login(request, user)
            return redirect('tasks')
        else:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario incorrecto',
            })

            
def editar(request):
    if request.method == 'POST':
        return render(request, 'editar.html')





    
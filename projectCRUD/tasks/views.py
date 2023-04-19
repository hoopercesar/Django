from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from .forms import TaskForm
from .models import Task
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required


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

@login_required   
def tasks(request):
    tasks = Task.objects.filter(user=request.user)
    # print(tasks)
    return render(request, 'tasks.html', {
        'tasks' : tasks,
    })

# función muestra detalles de cada tarea
@login_required 
def task_details(request, task_id):
    # task = Task.objects.get(user=request.user, pk=task_id)
    cantidad = Task.objects.filter(user=request.user)
    # print( 'tarea =', len(cantidad)) , pk=task_id
    task = get_object_or_404(Task, user=request.user, pk=task_id)
   
    return render(request, 'task_details.html',{
            'id': task_id,
            'task' : task, 
            'cantidad' : len(cantidad),
        }) 


# tarea completada
@login_required
def complete_task(request, task_id): 
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')

@login_required   
def delete_task(request, task_id): 
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')


# editar tarea:
# esta función se divide en dos etapas.
# el botón editar conduce a formulario y el formulario
# instancia la tarea actual. Una vez hechos los cambios en el formulario
# se guarda la tarea y los cambios quedan actualizados en la base de datos.
# se redirige a tasks
# el botón cancelar cancela la operación de edición y redirige a tasks.
# 
@login_required
def editar(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        return render(request, 'editar.html', {
            'form' : TaskForm(instance=task),
            'id': task.id,
            })
    
@login_required
def guardar_cambios(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(request.POST, instance=task)
        form.save()
        print(task)
        return redirect('tasks')

@login_required       
def cancelar(request, task_id):
    # task = get_object_or_404(Task, user=request.user, pk=task_id)
    if request.method == 'POST':
        # task.save()
        print('canceló')
        return redirect('home')

# función crea nueva tarea tarea
@login_required 
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
@login_required
def usuario(request):
    print(request.user)

# para cerrar la sesión
@login_required 
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

            






    
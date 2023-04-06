from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Projects, Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    title = 'Bienvenido a Django!!'
    return render(request, 'index.html', {'titulo' : title})

def about(request):
    return render(request, 'about.html')

def hello(request, username):
   
    return HttpResponse('<h1>Hola, Mundo %s</h1>' % username)
    



def projects(request):
    projects = list(Projects.objects.values())
    # return JsonResponse(projects, safe=False)
    return render(request, 'projects', {
        'proyectos': projects,
    })

def task(request):
    # task = get_object_or_404(Task, id=id)
    task = Task.objects.all()
    # return HttpResponse('task: %s' % task.title)
    return render(request, 'task.html', {
        'tareas': task,
    })

# crea nueva tarea
def create_task(request):
    if request.method == 'GET':
        # show interface
        return render(request, 'create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(
            title = request.POST['title'], 
            description = request.POST['description'], 
            project_id = 2,
            )
        return redirect('/task/')

# crea nuevo proyecto  
def create_project(request):
    if request.method == 'GET':
        # muentra interface
        return render(request, 'create_project.html', {
         'form': CreateNewProject()   
        })
    else: 
        Projects.objects.create(
            name = request.POST['name']            
        )
        return redirect('projects')


def project_detail(request, id):
    project = get_object_or_404(Projects, id=id)
    print(project)
    return render(request, 'projects/detail.html')
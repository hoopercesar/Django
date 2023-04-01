from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Projects, Task
from django.shortcuts import render, get_object_or_404
from .forms import CreateNewTask

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
    return render(request, 'projects.html', {
        'proyectos': projects,
    })

def task(request):
    # task = get_object_or_404(Task, id=id)
    task = Task.objects.all()
    # return HttpResponse('task: %s' % task.title)
    return render(request, 'task.html', {
        'tareas': task,
    })

def create_task(request):
    return render(request, 'create_task.html')
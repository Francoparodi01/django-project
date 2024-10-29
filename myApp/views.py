from django.http import HttpResponse #JsonResponse 
from .models import Project, Task
from django.shortcuts import get_object_or_404, render
from .forms import CreateNewTask

def index(request):
    #title sería el nombre de la variable que se va a usar en el template
    title = "Hello, Django!"
    return render(request, 'index.html', {
        'title': title   #'title' es la variable que se va a usar en el template y el que está despues de los dos puntos es la variable que se está pasando
    })

def about(request):
    username = 'franco'
    return render(request, 'about.html', {
        'username': username
    })

def idNumber(request, id):
    print(type(id))
    return HttpResponse("<h1>ID number: %s</h1>" %id)

def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello, %s!</h1>" %username)

def projects(request):
    #projects = list(Project.objects.values())
    # return JsonResponse(projects, safe=False)
    projects = Project.objects.all()
    return render(request, "projects.html", {
        "projects": projects
        })
    
    
def task (request):
    tasks = Task.objects.all()
    return render(request, "task.html", {
        "tasks": tasks
        })

def create_task(request):
    return render (request, "create_task.html", {
        'form': CreateNewTask()
    })
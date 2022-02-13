from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Task
# Create your views here.

def taskList(request):
    #Pegando todo os objetos do BD
    tasks = Task.objects.all()
    #Colocando as tarefas no template, os valores que resgatei no BD
    return render(request, 'tasks/list.html', {'tasks': tasks})

def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})

def helloWorld(request):
    return HTTPResponse('Hello World')

def yourName(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})

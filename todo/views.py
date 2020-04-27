from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .form import inputTask
from django.utils import timezone

# Create your views here.
def index(request):
    tasks = Task.objects.all()

    if request.method == 'POST':
        task = inputTask(request.POST)
        if task.is_valid():
            task.save()
        return redirect('index')

    return render(request, 'home.html', {'tasks': tasks})

def addTask(request):
    return render(request, 'addTask.html')

def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'addTask.html', {'task': task})

def deleteTask(request, id):
    item = get_object_or_404(Task, pk=id)
    item.delete()
    return redirect('index')

def toggleTask(request, id):
    item = get_object_or_404(Task, pk=id)
    item.complete = not item.complete

    time = timezone.now()
    hour = int(str(timezone.now())[11:13]) + 1

    theTime = str(time)[0:10] + ' ' + str(hour) + str(time)[13:50]

    item.time = theTime

    item.save()



    return redirect('index')
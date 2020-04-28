from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Food, Messages
from .form import inputTask, inputFood, inputMessages
from django.utils import timezone

# Create your views here.
def index(request):

    tasks = Task.objects.all()
    taskLength = len(tasks)
    food = Food.objects.all()
    foodsLength = len(food)

    if request.method == 'POST':
        task = inputTask(request.POST)
        if task.is_valid():
            time = timezone.now()
            hour = int(str(timezone.now())[11:13]) + 1
            theTime = str(time)[0:10] + ' ' + str(hour) + str(time)[13:50]
            task.time = theTime
            task.save()
        return redirect('index')

    return render(request, 'home.html', {'tasks': tasks, 'tasksLength': taskLength, 'foods': food, 'foodsLength':foodsLength})

# add a task for the house
def addTask(request):
    return render(request, 'addTask.html')

# edit a task for the house
def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'addTask.html', {'task': task})

# delete any task
def deleteTask(request, id):
    item = get_object_or_404(Task, pk=id)
    item.delete()
    return redirect('index')

# delete food
def deleteFood(request, id):
    item = get_object_or_404(Food, pk=id)
    item.delete()
    return redirect('index')

# totgle the completion of a task.
def toggleTask(request, id):
    item = get_object_or_404(Task, pk=id)
    item.complete = not item.complete

    time = timezone.now()
    hour = int(str(timezone.now())[11:13]) + 1
    if hour >= 24:
        hour = '00'
    theTime = str(time)[0:10] + ' ' + str(hour) + str(time)[13:50]
    print('the time tht e timte thte itm thte time the time the time', theTime)
    item.time = theTime
    item.save()
    return redirect('index')

# totgle the completion of a food.
def toggleFood(request, id):
    item = get_object_or_404(Food, pk=id)
    item.complete = not item.complete

    time = timezone.now()
    hour = int(str(timezone.now())[11:13]) + 1
    if hour >= 24:
        hour = '00'
    theTime = str(time)[0:10] + ' ' + str(hour) + str(time)[13:50]
    print('the time tht e timte thte itm thte time the time the time', theTime)
    item.time = theTime
    item.save()
    return redirect('index')

# Create a message to be displayed
def message(request):
    messages = Messages.objects.all() 
    messageLength = len(messages)

    for message in messages:
        hexColour = str(message.colour[1:50])
        h = hexColour.lstrip('#')
        messageColour = 'rgba{}'.format( tuple(int(h[i:i+2], 16) for i in (0, 2, 4)) )
        messageColour = messageColour + ';'
        messageColour = messageColour[0:-2] + ',0.2);'
        message.colour = messageColour

    if request.method == 'POST':
        task = inputMessages(request.POST)
        if task.is_valid():
            task.save()
        return redirect('message')
    return render(request, 'addMessage.html', {'messages': messages, 'messageLength': messageLength})

def deleteMessage(request, id):
    item = get_object_or_404(Messages, pk=id)
    item.delete()
    return redirect('message')

def addFood(request):

    if request.method == 'POST':
        food = inputFood(request.POST)
        if food.is_valid():
            food.save()
        return redirect('index')

    return render(request, 'addFood.html')
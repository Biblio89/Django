from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskFrom

def index(request):
    # tasks =Task.objects.all()
    # tasks = Task.objects.order_by('id')
    # tasks = Task.objects.order_by('-id')  обратная сортировка
    tasks = Task.objects.order_by('id')
    return render(request, 'main/index.html', {'title': 'Главная', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Error'
    form = TaskFrom()
    context = { 'form' : form, 'error': error}
    return render(request, 'main/create.html', context)

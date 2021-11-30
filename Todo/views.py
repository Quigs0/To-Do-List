from django.shortcuts import render, redirect
from .models import Todo
from .forms import TaskForm


def index(request):
    tasks = Todo.objects.all()
    context = {'tasks': tasks}
    return render(request, 'index.html', context)


def add(request):
    form = TaskForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'index.html', {'form': form})


def delete(request, task_id):
    task = Todo.objects.get(id=task_id)

    if request.method == 'POST':
        task.delete()
        return redirect('index')

    return render(request, 'delete.html', {'task': task})


def update(request, task_id):
    task = Todo.objects.get(id=task_id)

    form = TaskForm(request.POST or None, instance=task)

    if form.is_valid():
        form.save()
        return redirect('index')

    context = {'form': form, 'task_id': task_id}
    return render(request, 'update.html', context)


def complete_task(request, task_id):
    task = Todo.objects.get(id=task_id)
    task.completed = True
    task.save()

    return redirect('index')


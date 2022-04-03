from typing import Text
from django.shortcuts import render, redirect
from .models import *

from .forms import *
# Create your views here.


def homePage(request):

    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/')

    context = {
        'tasks': tasks,
        'form': form
    }

    return render(request, 'to_do/index.html', context)


def update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()

        return redirect('/') 

    context = {
        'task': task,
        'form': form
    }

    return render(request, 'to_do/task.html', context)


def articlePage(request, pk):

    post = Post.objects.get(nam)


    context = {
        'post': post
    }

    return render(request, 'posts/post.html', context)




from django import urls
from django.shortcuts import render
from .models import Topic

# Create your views here.


def homepage(request):

    topics = Topic.objects.all()
    context = {
        'topics' : topics,
    }

    return render(request, 'notes/home.html', context)


def topics(request):

    topics = Topic.objects.all()

    context = {
        'topics' : topics,
    }
    return render(request, 'notes/home.html', context)


def topic(request, id):

    item = Topic.objects.get(id = id)
    name = item.title # Set it here or in the template

    topics = Topic.objects.all()

    context = {
        'item' : item,
        'name' : name,
        'topics' : topics,
    }

    return render(request, 'notes/topic.html', context)















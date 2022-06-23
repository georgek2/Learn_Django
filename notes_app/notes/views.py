
from django.shortcuts import redirect, render
from .models import Topic
from .forms import TopicForm, UserForm

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def homepage(request):

    topics = Topic.objects.all()
    context = {
        'topics' : topics,
    }

    return render(request, 'notes/home.html', context)


@login_required(login_url='login')
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


def edit_topic(request, id):

    topic = Topic.objects.get(id=id)
    topics = Topic.objects.all() 
    form = TopicForm(instance=topic)

    if request.method == 'POST':
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():

            form.save()

        return redirect('/')

    context = {
        'topics' : topics,
        'topic' : topic,
        'form' : form
    }


    return render(request, 'notes/edit.html', context)

def add_topic(request):

    topics = Topic.objects.all()
    form = TopicForm()

    context = {
        'topics' : topics,
        'form' : form
    }

    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid:

            form.save()

        redirect('/')

    return render(request, 'notes/update.html', context)


def signup(request):
    form = UserForm()
    context = {'form': form}

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account created for " + user)

            return redirect('login')

    return render(request, 'notes/signup.html', context)


def loginPage(request):
    
    form = UserForm()
    context = {'form': form}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        # If user in database
        if user:
            login(request, user)

            return redirect('homepage')

        else: 
            messages.info(request, 'User details incorrect..!!')

    return render(request, 'notes/login.html', context)








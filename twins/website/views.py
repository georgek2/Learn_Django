from django.shortcuts import redirect, render

from .forms import UserForm

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout 
# Create your views here.

def index(request):

    return render(request, 'website/index.html')


def loginPage(request):

    form = UserForm()
    context = {'form': form}

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username = username, password = password)

        if user is not None:
            
            if user.is_active:
                login(request, user)

                return redirect('home')

    return render(request, 'website/login.html', context)

def register(request):

    form = UserForm()

    context = {'form': form}

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')

    return render(request, 'website/register.html', context)




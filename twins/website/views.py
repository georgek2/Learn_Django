from django.shortcuts import redirect, render

from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):

    return render(request, 'website/index.html')


def login(request):

    return render(request, 'website/login.html')

def register(request):

    form = UserCreationForm()

    context = {'form': form}

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/login')

    return render(request, 'website/register.html', context)




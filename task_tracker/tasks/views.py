from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.


# Homepage

def homePage(request):

    return render(request, 'tasks/index.html')









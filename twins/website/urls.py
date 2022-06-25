from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.loginPage, name = 'login'),
    path('register/', views.register, name = 'register')
]






from django.urls import path
from . import views

urlpatterns = [
    path('<str:title>/', views.articlePage, name = 'articlePage'),
    path('', views.homePage, name = 'homepage'),
    path('task/<str:pk>/', views.update, name = 'edit task')
]














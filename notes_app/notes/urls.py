from django.urls import path
from . import views



urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('topic/<str:id>/', views.topic, name='topic'),
]














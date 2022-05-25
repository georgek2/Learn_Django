from django.urls import path
from . import views



urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('topic/<str:id>/', views.topic, name='topic'),
    path('add_topic/', views.add_topic, name = 'add'),
    path('edit_topic/<str:id>', views.edit_topic, name = 'edit'),
    path('another', views.another)
]














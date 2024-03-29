from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('topic/<str:id>/', views.topic, name='topic'),
    path('add_topic/', views.add_topic, name = 'add'),
    path('edit_topic/<str:id>', views.edit_topic, name = 'edit'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout')
]














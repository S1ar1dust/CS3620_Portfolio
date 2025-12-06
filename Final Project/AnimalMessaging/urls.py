from django.urls import path
from . import views

urlpatterns = {
    path('', views.Home, name='Home'),
    path('Message Board', views.MessageBoard, name='MessageBoard'),
    path('Custom Messages', views.CustomMessages, name='CustomMessages'),
    path('Dont Sue', views.DontSue, name='DontSue'),
    path('Create Account', views.CreateAccount, name='CreateAccount'),
    path('Login', views.Login, name='Login'),
    path('Logout', views.Logout, name='Logout'),
}
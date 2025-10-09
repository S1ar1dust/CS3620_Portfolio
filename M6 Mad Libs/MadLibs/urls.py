from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('Game/', views.Game, name='Game'),
    path('Stories/', views.Stories, name='Stories'),
    path('About/', views.About, name='About'),
    path('GameResults/', views.GameResults, name='GameResults'),
]
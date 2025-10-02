from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('Hobbies/', views.Hobbies, name='Hobbies'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('Contact/', views.Contact, name='Contact'),
]
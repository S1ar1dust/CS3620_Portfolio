from random import random

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.utils.termcolors import background

from . form import NewAccountForm, LoginUserForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, logout, login
from .customMessageForm import MessagesForm
from .models import Villagers, Messages
from django.views.generic import ListView, DetailView
import schedule
import time

# Create your views here.
def Home(request):
    template = loader.get_template('AnimalMessaging/homePage.html')
    return HttpResponse(template.render({}, request))

def MessageBoard(request):
    context = {}

    villagers = Villagers.objects.all()
    #model = Villagers.objects.get(pk=1)
    context['villagers'] = villagers
    #posts = Posts.objects.all()
    #context['posts'] = posts

    return render(request, 'AnimalMessaging/messageBoard.html', context)

    template = loader.get_template('AnimalMessaging/messageBoard.html')
    return HttpResponse(template.render({}, request))

def CustomMessages(request):
    context = {}
    form = MessagesForm()
    context['form'] = form
    if request.method == 'POST':
        form = MessagesForm(request.POST)
        form.save()

    return render(request, 'AnimalMessaging/customMessages.html', context)



    template = loader.get_template('AnimalMessaging/customMessages.html')
    return HttpResponse(template.render({}, request))

def DontSue(request):
    template = loader.get_template('AnimalMessaging/dontSue.html')
    return HttpResponse(template.render({}, request))

def CreateAccount(request):


    form = NewAccountForm()
    if request.method == 'POST':
        form = NewAccountForm(request.POST)


        if form.is_valid():
            form.save()
            template = loader.get_template('AnimalMessaging/login.html')
            return HttpResponse(template.render({}, request))

    context = {'createAccountForm': form}

    #template = loader.get_template('AnimalMessaging/createAccount.html')
    #return HttpResponse(template.render(context, request))
    return render(request, 'AnimalMessaging/createAccount.html', context)

def Login(request):
    form = LoginUserForm()

    if request.method == 'POST':
        form = LoginUserForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                template = loader.get_template('AnimalMessaging/homePage.html')
                return HttpResponse(template.render({}, request))

    context = {'loginUserForm': form}

    return render(request, 'AnimalMessaging/login.html', context)

def Logout(request):
    auth.logout(request)
    template = loader.get_template('AnimalMessaging/homePage.html')
    return HttpResponse(template.render({}, request))

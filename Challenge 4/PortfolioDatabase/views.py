from django.shortcuts import render
from django.http import HttpResponse
from . models import Hobby
from . models import Portfolio
from django.template import loader

def Home(request):
    return HttpResponse("Hello my name is Jared Esquivel. I am currently a student at Weber State University and it is my senior year here and am currently studying to get a CS degree.")

def Hobbies(request):
    data = list(Hobby.objects.all().values())
    template = loader.get_template("PortfolioDatabase/index.html")
    context = {"data": data}
    return HttpResponse(template.render(context, request))



def portfolio(request):
    data2 = list(Portfolio.objects.all().values())
    template = loader.get_template("PortfolioDatabase/portfolio.html")
    context = {"data": data2}
    return HttpResponse(template.render(context, request))

def Contact(request):
    return HttpResponse("jaredesquivel@mail.weber.edu")

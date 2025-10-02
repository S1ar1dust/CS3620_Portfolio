from django.shortcuts import render
from django.http import HttpResponse
from . models import Hobby
from . models import Portfolio
from . models import Contacts
from django.template import loader
from DB.contactForm import ContactForm
from .portfolioForm import PortfolioForm


def Home(request):
    template = loader.get_template('DB/homeTemplate.html')
    return HttpResponse(template.render())

def Hobbies(request):
    data = list(Hobby.objects.all().values())
    template = loader.get_template("DB/hobbiesTemplate.html")
    context = {"data": data}
    return HttpResponse(template.render(context, request))

def portfolio(request):
    context = {}
    form = PortfolioForm()
    portfolio = Portfolio.objects.all()
    context['portfolios'] = portfolio
    context['form'] = form
    if request.method == "POST":
        if 'btnPortfolioSave' in request.POST:
            form = PortfolioForm(request.POST)
            form.save()
        elif 'btnPortfolioDelete' in request.POST:
            primKey = request.POST.get('btnPortfolioDelete')
            portfolio = Portfolio.objects.get(id=primKey)
            portfolio.delete()
    return render(request, 'DB/newPortfolioTemplate.html', context)

def Contact(request):
    context = {}
    form = ContactForm()
    contacts = Contacts.objects.all()
    context['contacts'] = contacts
    context['form'] = form
    if request.method == "POST":
        if 'Save' in request.POST:
            form = ContactForm(request.POST)
            form.save()
    return render(request, 'DB/contactTemplate.html', context)

def Login(request):
    template = loader.get_template('users/')
    return HttpResponse(template.render())
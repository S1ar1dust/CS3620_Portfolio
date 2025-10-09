from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Input
from .models import Story
from MadLibs.inputForm import InputForm
import random

# Create your views here.

def Home(request):
    template = loader.get_template('MadLibs/homePage.html')
    #template = loader.get_template('MadLibs/gameResultsPage.html')
    return HttpResponse(template.render())

def Game(request):
    context = {}
    form = InputForm()
    inputs = Input.objects.all()
    context['inputs'] = inputs
    context['form'] = form
    if request.method == "POST":
        if 'Save' in request.POST:
            form = InputForm(request.POST)
            obj = Input(id=1, name=request.POST['name'], noun1=request.POST['noun1'], noun2=request.POST['noun2'], place=request.POST['place'], verb=request.POST['verb'], adjective=request.POST['adjective'], person=request.POST['person'])
            obj.save()
    return render(request, 'MadLibs/gamePage.html', context)

def GameResults(request):
    context = {}
    inputs = Input.objects.get(id=1)

    #stories = Story.objects.all()
    #randStory = random.choice(stories)
    #context['stories'] = randStory
    randNum = random.randint(1, 9)

    test = Story.objects.get(id=randNum)
    ll = test.tellStory
    stringStory = str(ll)
    stringStory = stringStory.replace('NAME', inputs.name)
    stringStory = stringStory.replace('NOUN1', inputs.noun1)
    stringStory = stringStory.replace('NOUN2', inputs.noun2)
    stringStory = stringStory.replace('PLACE', inputs.place)
    stringStory = stringStory.replace('VERB', inputs.verb)
    stringStory = stringStory.replace('ADJECTIVE', inputs.adjective)
    stringStory = stringStory.replace('PERSON', inputs.person)

    context['test'] = stringStory

    return render(request, 'MadLibs/gameResultsPage.html', context)

def Stories(request):
    context = {}
    stories = Story.objects.all()
    context['stories'] = stories

    return render(request, 'MadLibs/storiesPage.html', context)
    #template = loader.get_template('MadLibs/storiesPage.html')
    #return HttpResponse(template.render())

def About(request):
    template = loader.get_template('MadLibs/aboutPage.html')
    return HttpResponse(template.render())




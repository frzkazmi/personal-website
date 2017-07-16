from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *

me = {}
person = {}
if User.objects.get(username='joun'):
    me = User.objects.get(username='joun')
#print (Person.objects.filter(userName=me))
#print (Person.objects.all())
if Person.objects.filter(userName=me):
    person = Person.objects.filter(userName=me)[0]

def index(request):
    
    return render(request, 'index.html', {'person': person})

def home(request):
    
    return render(request, 'home.html', {'person': person})

def portfolio(request):
    return render(request, 'portfolio.html', {'person': person})


def contact(request):
    return render(request, 'contact.html', {'person': person})


def resume(request):
    return render(request, 'resume.html', {'person': person})

def about(request):
    skills={}
    if Person.objects.all()[0]:
        skills = Skills.objects.filter(user=Person.objects.all()[0])    
            
    return render(request, 'about.html', {'person': person,'skills':skills})

# def projects(request):
#     return render(request, 'projects.html', {'person': person})


def error404(request):
    return render(request, '404.html', {'person': person})


def error500(request):
    return render(request, '500.html', {'person': person})

def blog(request):
    return render(request,'blog.html')

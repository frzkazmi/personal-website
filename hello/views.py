from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *

me = User.objects.get(username='joun')

if Person.objects.filter(userName=me):
    person = Person.objects.filter(userName=me)[0]
else:
    person = {}    
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
    if Person.objects.filter(userName=me):
        skills = Skills.objects.filter(user=me)
    else:
        skills = []
        
    return render(request, 'about.html', {'person': person,'skills':skills})

# def projects(request):
#     return render(request, 'projects.html', {'person': person})


def error404(request):
    return render(request, '404.html', {'person': person})


def error500(request):
    return render(request, '500.html', {'person': person})

def blog(request):
    return render(request,'blog.html')

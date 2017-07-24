from django.core.mail import send_mail, BadHeaderError,EmailMultiAlternatives
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template, render_to_string
import os, requests
from gettingstarted import settings

me = {}
person = {}
if User.objects.get(username='joun'):
    me = User.objects.get(username='joun')
##print (Person.objects.filter(userName=me))
##print (Person.objects.all())
if Person.objects.filter(userName=me):
    person = Person.objects.filter(userName=me)[0]

def index(request):
    
    return render(request, 'index.html', {'person': person})

def home(request):
    
    return render(request, 'index.html', {'person': person})

def portfolio(request):
    return render(request, 'portfolio.html', {'person': person})


def contact(request):
    form_class = ContactForm
    validFlag = ""

    if request.method == 'GET':

        #print ("contact GET")
        form = ContactForm()
    else:
        #print ("contact POST")

        form = ContactForm(request.POST)
        #print (form.errors)
        if not form.is_valid():
            pass
            #print ('invalid form')
        if form.is_valid():
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            print (data)
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            print (result)
            ''' End reCAPTCHA validation '''

            if result['success']:
                #form.save()
                messages.success(request, 'Form submitted with success!')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')

            #print ("valid form")
            subject = form.cleaned_data['subject']
            from_person = form.cleaned_data['senderName']
            from_email = form.cleaned_data['senderEmail']
            message = form.cleaned_data['message']
            subject_for_visitor ="Acknowledgement of response submitted on joun-testapp.herokuapp.com"
            #print (subject, from_person,from_email, message)
            #subject, from_email, to = subject, BASKET_MAIL_FROM, BASKET_MAIL_TO
            ctx = {'senderName': from_person,'senderEmail':from_email,'message':message}
            text_content = render_to_string('mail.txt', ctx)
            html_content_for_User = render_to_string('mailfromvisitor.html', ctx)
            html_content_for_Visitor = render_to_string('mailtovisitor.html', ctx)
            to = "kazmifaraz153@gmail.com"
            msgtoUser = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msgtoVisitor = EmailMultiAlternatives(subject_for_visitor, text_content, from_email, [from_email])
            msgtoUser.attach_alternative(html_content_for_User, "text/html")
            msgtoVisitor.attach_alternative(html_content_for_Visitor, "text/html")
            msgtoUser.send()
            msgtoVisitor.send()
            validFlag = "true"
            # try:
            #     send_mail(subject, message, from_email, ['kazmifaraz153@gmail.com'])
            # except BadHeaderError:
            #     return HttpResponse('Invalid header found.')
            # return redirect('contact')


    return render(request, 'contact.html', {'person': person,'form':form_class,'validFlag':validFlag})


def resume(request):
    techskills = TechnicalSkill.objects.filter(user=person)[0]
    company = Company.objects.filter(user=person)
    education = Education.objects.filter(user=person)
    return render(request, 'resume.html', {'person': person,'techskills':techskills,'companies':company,'education':education})

def about(request):
    skills={}
    if Person.objects.all()[0]:
        skills = Skills.objects.filter(user=person)    
            
    return render(request, 'about.html', {'person': person,'skills':skills})

# def projects(request):
#     return render(request, 'projects.html', {'person': person})


def error404(request):
    return render(request, '404.html', {'person': person})


def error500(request):
    return render(request, '500.html', {'person': person})

def blog(request):
    return render(request,'blog.html')

def blogPage(request,num="1"):
    return render(request,'blogPage.html')

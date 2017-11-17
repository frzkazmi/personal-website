from django.core.mail import send_mail, BadHeaderError,EmailMultiAlternatives
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views import generic
from .models import *
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template, render_to_string
import requests
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from gettingstarted import settings

#from hello.templatetags.globaltags import populartags, recentposts


####seeder = Seed.seeder()
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

        ##print ("contact GET")
        form = ContactForm()
    else:
        ##print ("contact POST")

        form = ContactForm(request.POST)
        ##print (form.errors)
        if not form.is_valid():
            pass
            ##print ('invalid form')
        if form.is_valid():
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            #print (data)
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            #print (result)
            ''' End reCAPTCHA validation '''

            if result['success']:
                #form.save()
                messages.success(request, 'Form submitted with success!')
                ##print ("valid form")
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
            else:
                  messages.error(request, 'Invalid reCAPTCHA. Please try again.')

           
            # try:
            #     send_mail(subject, message, from_email, ['kazmifaraz153@gmail.com'])
            # except BadHeaderError:
            #     return HttpResponse('Invalid header found.')
            return redirect('contact')


    return render(request, 'contact.html', {'person': person,'form':form_class,'validFlag':validFlag})


def resume(request):
    # seeder.add_entity(User,4)
    # seeder.add_entity(Person,4)
    # seeder.add_entity(Education,4)
    techskills = {}
    #insertedPks = seeder.execute()
    if TechnicalSkill.objects.all():
        techskills = TechnicalSkill.objects.filter(user=person)[0]
    company = Company.objects.filter(user=person)
    education = Education.objects.filter(user=person)
    return render(request, 'resume.html', {'person': person,'techskills':techskills,'companies':company,'education':education})

def about(request):
    skills={}
    if Person.objects.all()[0]:
        skills = Skills.objects.filter(user=person)    
            
    return render(request, 'about.html', {'person': person,'skills':skills})

def error404(request):
    return render(request, '404.html', {'person': person})


def error500(request):
    return render(request, '500.html', {'person': person})

def blog(request):
    # seeder.add_entity(TagsforBlog,8)
    # seeder.add_entity(Blog, 6)    
    # insertedPks = seeder.execute()
    blogs_list = Blog.objects.publish()
    ##print (blogs_list)

    paginator = Paginator(blogs_list, 3)
    page = request.GET.get('page', 1)
    mapping = []
    tags_queryset = TagsforBlog.objects.all()
    for tag in tags_queryset:
        
        mapping.append({
            'tag': tag,
            'total': blogs_list.filter(tags=tag).count()
        } )
        
    
    mapping.sort(key=lambda x: int(x['total']), reverse=True)
    

    try:


        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
       
    return render(request,'blog.html', {'blogs':blogs,'populartags':mapping[:5],'recentposts':blogs_list[:5],'person': person})

def blogPage(request,slug):
    blog = get_object_or_404(Blog, slug=slug)
    ##print (blog.id)
    tags_list = blog.tags.all()
    related_posts = (Blog.objects.filter(tags__in=list(tags_list)).exclude(id=blog.id).distinct()[:4])
    
    return render(request,'blogPage.html',{'blog':blog,'relatedPosts':related_posts,'person': person})


def tagPostsPage(request,tag):
    #tags_list = get_object_or_404(TagsforBlog)
    ##print (tag)
    filtered_blog_list =  Blog.objects.filter(tags=tag)
    blogs_list = Blog.objects.publish()
    filtered_blogs_count = Blog.objects.filter(tags=tag).count()
    tag_heading = tag
    paginator = Paginator(filtered_blog_list, 3)
    page = request.GET.get('page', 1)
    mapping = []
    tags_queryset = TagsforBlog.objects.all()
    for tag in tags_queryset:
        
        mapping.append({
            'tag': tag,
            'total': Blog.objects.filter(tags=tag).count()
        } )
        
    
    mapping.sort(key=lambda x: int(x['total']), reverse=True)
    
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    
    return render(request,'blog_posts_tag.html',{'person': person,'blogs':blogs,'tag':tag_heading,'blogs_count':filtered_blogs_count,'populartags':mapping[:5],'recentposts':blogs_list[:5]})


def search(request):
    query = request.GET.get('q')
    
    #print ('requested query is')
    #print (query)
    blogs_list = Blog.objects.publish()
    mapping = []
    tags_queryset = TagsforBlog.objects.all()
    for tag in tags_queryset:
        
        mapping.append({
            'tag': tag,
            'total': blogs_list.filter(tags=tag).count()
        } )
        
    
    mapping.sort(key=lambda x: int(x['total']), reverse=True)
            
        
    if query is not None and query != '':
        
        filtered_blogs = Blog.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(keywords__icontains=query)
        )
        #print (filtered_blogs)
        filtered_blogs_count = filtered_blogs.count()
        paginator = Paginator(filtered_blogs, 3)
        page = request.GET.get('page', 1)
        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)
        # you also can limit the maximum of `posts` here.
        # eg: posts[:50]
        return render(
            request, 'blogSearchPage.html',
            {'person': person,'blogs': blogs,'query':query,'count':filtered_blogs_count,'populartags':mapping[:5],'recentposts':blogs_list[:5]}
        )
        
    return render(
        request, 'blogSearchPage.html',{'person': person,'populartags':mapping[:5],'recentposts':blogs_list[:5]}
    )

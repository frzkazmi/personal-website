from django.db import models
from django import forms
import datetime
from django.utils import timezone
from uuid import uuid4
from ckeditor.fields import RichTextField
# from datetime import date
from django.utils.translation import gettext as _
#from dbarray import IntegerArrayField
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


## FORMS MODELS
class ContactForm(forms.Form):
    senderName = forms.CharField(max_length=100)
    senderEmail = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(required=False, widget=forms.Textarea)
      
      
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['senderName'].label = "Your name:"
        self.fields['senderEmail'].label = "Your email:"
        self.fields['subject'].label = "Subject"
        self.fields['message'].label = "Enter your message here"
   
 

class Person(models.Model):

    userName = models.ForeignKey('auth.User',null=True)
    fullName = models.CharField(max_length=200,default='')
    userbio = models.CharField(max_length=200,default='')
    locality = models.CharField(max_length=200,default='')
    userLocation = models.CharField(max_length=200,default='')
    title = models.CharField(max_length=200,default='')
    linkedinUrl = models.CharField(max_length=200,default='')
    githubUrl = models.CharField(max_length=200,default='')
    emailAddress = models.EmailField(max_length=200,default='')
    personalDescription = models.TextField(default='')
    careerObjective = models.TextField(default='')
    fbUrl = models.CharField(max_length=200,default='')
    mywebsite = models.CharField(max_length=200,null=True)
    skypeId = models.CharField(max_length=200,default='')
    mobileNumber = models.CharField(max_length=200,default='')

    
    def __str__(self):
        return self.fullName


class Company(models.Model):
    user = models.ForeignKey('Person')
    companyName = models.CharField(max_length=200,default='')
    companyRole = models.CharField(max_length=200,default='')
    companyLocation = models.CharField(max_length=200,default='')
    joiningDate = models.DateField(_("Date"), default=datetime.date.today)
    leavingDate = models.DateField(_("Date"))
    workDescription = models.TextField(default='')
    projectRoles = ArrayField(models.CharField(max_length=200,default="{}", null=False, blank=False),default="{}")
    todayDate = datetime.date.today()
    if todayDate == leavingDate:
        leavingDate = "Current"

    def __str__(self):
        return self.companyName


class PersonalProjects(models.Model):

    user = models.ForeignKey('Person')
    projectName = models.CharField(max_length=200,default='')
    TechnologiesUsed = models.TextField(default='')
    ProjectDescription = models.TextField(default='')
    projectLink = models.CharField(max_length=200,null=True,blank=True)
    gitHublink = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.projectName

class OrganisationalProject(models.Model):
    user = models.ForeignKey('Person',default=' ')
    company = models.ForeignKey('Company',default='')
    projectName = models.CharField(max_length=200,default='')
    TechnologiesUsed = models.TextField(default='')
    ProjectDescription = models.TextField(default='')

    def __str__(self):
        return self.projectName        


class Education(models.Model):
    user = models.ForeignKey('Person')
    courseName = models.CharField(max_length=200,default='')
    courseDuration = models.CharField(max_length=200,default='')
    coursePercentage = models.CharField(max_length=200,default='')
    instituteName = models.CharField(max_length=200,default='')
    instituteLocation = models.CharField(max_length=200,default='')
    
    def __str__(self):
        return self.courseName




class TechnicalSkill(models.Model):
    user = models.ForeignKey('Person')
    languages = ArrayField(models.CharField(default="{}",max_length=200, null=False, blank=False),default="{}")
    databases = ArrayField(models.CharField(default="{}",max_length=200, null=False, blank=False),default="{}")
    BackEnds = ArrayField(models.CharField(default="{}",max_length=200, null=False, blank=False),default="{}")
    FrontEnds = ArrayField(models.CharField(default="{}",max_length=200, null=False, blank=False),default="{}")
    Devtools = ArrayField(models.CharField(default="{}",max_length=200, null=False, blank=False),default="{}")
    otherLibraries = ArrayField(models.CharField(default="{}",max_length=200, null=False, blank=False),default="{}")
    Webservices = ArrayField(models.CharField(default="{}",max_length=200, null=False, blank=False),default="{}")

    def __unicode__(self):
        return self.commaSeperatedBackEnds

class Skills(models.Model):
    user = models.ForeignKey('Person')
    skillName = models.CharField(max_length=200,default='')
    skillAwarenessPercent = models.CharField(max_length=200,default='')

    def __str__(self):
        return self.skillName


class Achievement(models.Model):
    user = models.ForeignKey('Person')
    achievement = models.TextField(default='')

    def __str__(self):
        return self.achievement

class Strength(models.Model):
    user = models.ForeignKey('Person')
    strength = models.TextField(default='')

    def __str__(self):
        return self.strength

class PostQuerySet(models.QuerySet):

    def publish(self):
        return self.filter(published=True)

class Blog(models.Model):
    content = RichTextField()
    date = models.DateTimeField(default=datetime.datetime.now)
    date_updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=180)
    slug = models.SlugField(unique=True)
    published = models.BooleanField(default=True)
    keywords = models.CharField(max_length=200,null=True)
    tags = models.ManyToManyField('TagsforBlog')
    objects = PostQuerySet.as_manager()
    
    class Meta:
        ordering=['-date']
    
     
    def __str__(self):
        return self.title


    
    
class TagsforBlog(models.Model):
    

    tagname = models.CharField(primary_key=True, max_length=50)
    tagslug = models.SlugField(max_length=200, unique=True, null=True)

    
    def __str__(self):
        return self.tagname

    @property
    def get_total_posts(self):
        return Blog.objects.filter(tags__pk=self.pk).count()

    class Meta:
        verbose_name = 'Detail Tag'
        verbose_name_plural = 'Tags'        
    
class Comment(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    path = ArrayField(models.IntegerField(default="{}", null=False, blank=False))
   # path = IntegerArrayField(blank=True, editable=False) #Can't be null as using append to path for replies and can't append to a None path
    depth = models.PositiveSmallIntegerField(default=0)
    user = models.ForeignKey(User, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    blog = models.ForeignKey('Blog', blank=True, related_name='comments')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='child')
    spam = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.content
    
class Subscriber(models.Model):
    email = models.EmailField()
    uuid = models.CharField(max_length=50, default=uuid4)
    
    def __unicode__(self):
        return self.email
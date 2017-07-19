from django.db import models
from django import forms
from django.db import models
import datetime
from django.utils import timezone
# from datetime import date
from django.utils.translation import gettext as _


class ContactForm(forms.Form):
    senderName = forms.CharField(max_length=100)
    senderEmail = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(required=False, widget=forms.Textarea)
      
    #cc_myself = forms.BooleanField(required=False)
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['senderName'].label = "Your name:"
        self.fields['senderEmail'].label = "Your email:"
        self.fields['subject'].label = "Subject"
        self.fields['message'].label = "Enter your message here"
        
    

class Person(models.Model):

    userName = models.ForeignKey('auth.User')
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

    def __str__(self):
        return self.companyName


class PersonalProject(models.Model):
    user = models.ForeignKey('Person')
    projectName = models.CharField(max_length=200,default='')
    TechnologiesUsed = models.TextField(default='')
    ProjectDescription = models.TextField(default='')
    projectLink = models.CharField(max_length=200,default='')

    def __str__(self):
        return self.projectName

class CompanyProject(PersonalProject):
    #user = models.ForeignKey('Person')
    company = models.ForeignKey('Company',default='')
    # projectName = models.CharField(max_length=200,default='')
    # TechnologiesUsed = models.TextField(default='')
    # ProjectDescription = models.TextField(default='')

    def __str__(self):
        return self.company        


class Education(models.Model):
    user = models.ForeignKey('Person')
    courseName = models.CharField(max_length=200,default='')
    courseDuration = models.CharField(max_length=200,default='')
    coursePercentage = models.CharField(max_length=200,default='')
    instituteName = models.TextField(default='')
    
    def __str__(self):
        return self.courseName




class TechnicalSkill(models.Model):
    user = models.ForeignKey('Person')
    commaSeperatedlanguages = models.TextField(default='')
    commaSeperateddatabases = models.TextField(default='')
    commaSeperatedBackEnds = models.TextField(default='')
    commaSeperatedFrontEnds = models.TextField(default='')
    commaSeperatedDevtools = models.TextField(default='')
    commaSeperatedotherLibraries = models.TextField(default='')
    commaSeperatedWebservices = models.TextField(default='')

    def __str__(self):
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

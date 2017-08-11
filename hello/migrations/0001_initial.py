# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-08 19:27
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievement', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('title', models.CharField(max_length=180)),
                ('slug', models.SlugField(unique=True)),
                ('published', models.BooleanField(default=False)),
                ('keywords', models.CharField(max_length=200, null=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('path', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default='{}'), size=None)),
                ('depth', models.PositiveSmallIntegerField(default=0)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('spam', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('blog', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='hello.Blog')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='hello.Comment')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(default='', max_length=200)),
                ('companyRole', models.CharField(default='', max_length=200)),
                ('companyLocation', models.CharField(default='', max_length=200)),
                ('joiningDate', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('leavingDate', models.DateField(verbose_name='Date')),
                ('workDescription', models.TextField(default='')),
                ('projectRoles', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='{}', max_length=200), default='{}', size=None)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyProjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(default='', max_length=200)),
                ('TechnologiesUsed', models.TextField(default='')),
                ('Project', models.TextField(default='')),
                ('company', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hello.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(default='', max_length=200)),
                ('courseDuration', models.CharField(default='', max_length=200)),
                ('coursePercentage', models.CharField(default='', max_length=200)),
                ('instituteName', models.CharField(default='', max_length=200)),
                ('instituteLocation', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(default='', max_length=200)),
                ('userbio', models.CharField(default='', max_length=200)),
                ('locality', models.CharField(default='', max_length=200)),
                ('userLocation', models.CharField(default='', max_length=200)),
                ('title', models.CharField(default='', max_length=200)),
                ('linkedinUrl', models.CharField(default='', max_length=200)),
                ('githubUrl', models.CharField(default='', max_length=200)),
                ('emailAddress', models.EmailField(default='', max_length=200)),
                ('personalDescription', models.TextField(default='')),
                ('careerObjective', models.TextField(default='')),
                ('fbUrl', models.CharField(default='', max_length=200)),
                ('mywebsite', models.CharField(max_length=200, null=True)),
                ('skypeId', models.CharField(default='', max_length=200)),
                ('mobileNumber', models.CharField(default='', max_length=200)),
                ('userName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalProjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(default='', max_length=200)),
                ('TechnologiesUsed', models.TextField(default='')),
                ('ProjectDescription', models.TextField(default='')),
                ('projectLink', models.CharField(blank=True, max_length=200, null=True)),
                ('gitHublink', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skillName', models.CharField(default='', max_length=200)),
                ('skillAwarenessPercent', models.CharField(default='', max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Strength',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strength', models.TextField(default='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('uuid', models.CharField(default=uuid.uuid4, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TagsforBlog',
            fields=[
                ('tagname', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('tagslug', models.SlugField(max_length=200, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Detail Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='TechnicalSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languages', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='{}', max_length=200), default='{}', size=None)),
                ('databases', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='{}', max_length=200), default='{}', size=None)),
                ('BackEnds', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='{}', max_length=200), default='{}', size=None)),
                ('FrontEnds', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='{}', max_length=200), default='{}', size=None)),
                ('Devtools', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='{}', max_length=200), default='{}', size=None)),
                ('otherLibraries', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='{}', max_length=200), default='{}', size=None)),
                ('Webservices', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='{}', max_length=200), default='{}', size=None)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.Person')),
            ],
        ),
        migrations.AddField(
            model_name='education',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.Person'),
        ),
        migrations.AddField(
            model_name='companyprojects',
            name='user',
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, to='hello.Person'),
        ),
        migrations.AddField(
            model_name='company',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.Person'),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(to='hello.TagsforBlog'),
        ),
        migrations.AddField(
            model_name='achievement',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.Person'),
        ),
    ]

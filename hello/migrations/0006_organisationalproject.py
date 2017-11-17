# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-12 11:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_auto_20170812_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganisationalProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(default='', max_length=200)),
                ('TechnologiesUsed', models.TextField(default='')),
                ('Project', models.TextField(default='')),
                ('company', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hello.Company')),
                ('user', models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, to='hello.Person')),
            ],
        ),
    ]
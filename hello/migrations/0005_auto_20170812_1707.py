# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-12 11:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_auto_20170812_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organisationproject',
            name='company',
        ),
        migrations.RemoveField(
            model_name='organisationproject',
            name='user',
        ),
        migrations.DeleteModel(
            name='OrganisationProject',
        ),
    ]

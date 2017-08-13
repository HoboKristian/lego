# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 17:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email', '0003_auto_20170427_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emaillist',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='email_lists', to='users.AbakusGroup'),
        ),
        migrations.AlterField(
            model_name='emaillist',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='email_lists', to=settings.AUTH_USER_MODEL),
        ),
    ]
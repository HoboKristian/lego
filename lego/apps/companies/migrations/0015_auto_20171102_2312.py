# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 23:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0014_auto_20171102_2244'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='previousstudentcontact',
            options={'ordering': ['-start']},
        ),
        migrations.AlterField(
            model_name='previousstudentcontact',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 2, 23, 12, 52, 47649, tzinfo=utc)),
        ),
    ]

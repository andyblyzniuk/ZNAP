# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 17:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapi', '0020_auto_20171025_2022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='gender',
        ),
        migrations.AddField(
            model_name='rate',
            name='quality',
            field=models.CharField(choices=[('Good', 'G'), ('Bad', 'B')], default='Good', max_length=1),
        ),
        migrations.AlterField(
            model_name='rate',
            name='timeStamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 25, 20, 27, 48, 346000)),
        ),
    ]

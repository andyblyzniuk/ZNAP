# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 17:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapi', '0014_auto_20171025_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='timeStamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 25, 20, 17, 5, 879000)),
        ),
    ]

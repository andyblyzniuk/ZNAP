# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 11:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapi', '0025_auto_20171102_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dialog',
            name='admin',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='userapi.Admin'),
        ),
        migrations.AlterField(
            model_name='dialog',
            name='timeStamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 2, 13, 0, 29, 511000)),
        ),
    ]
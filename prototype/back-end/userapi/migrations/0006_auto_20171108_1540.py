# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-11-08 13:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapi', '0005_auto_20171108_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dialog',
            name='dialog',
        ),
        migrations.RemoveField(
            model_name='rate',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='rate',
            name='user',
        ),
        migrations.DeleteModel(
            name='Dialog',
        ),
        migrations.DeleteModel(
            name='Rate',
        ),
    ]

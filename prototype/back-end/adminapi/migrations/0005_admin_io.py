# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-12-01 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0004_admin_znap'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='io',
            field=models.IntegerField(default=1),
        ),
    ]

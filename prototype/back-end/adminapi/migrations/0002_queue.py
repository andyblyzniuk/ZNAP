# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-11-08 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameOfDepartment', models.CharField(choices=[('1', 'first')], max_length=1)),
                ('location', models.CharField(choices=[('1', 'NULP')], max_length=1)),
            ],
        ),
    ]
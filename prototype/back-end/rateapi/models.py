from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from model_utils import Choices
import datetime
# Create your models here.

from adminapi.models import Admin

class Rate(models.Model):
    user = models.ForeignKey(User)
    admin = models.ForeignKey(Admin,default=None, null=True)
    quality = models.IntegerField()
    TYPE = Choices(
        ('1', '1')
    )
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=1, choices=TYPE)
    is_closed = models.BooleanField()

class Dialog(models.Model):
    dialog = models.ForeignKey(Rate)
    message = models.CharField(max_length=200)
    timeStamp = models.DateTimeField(default=datetime.datetime.now())
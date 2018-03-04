from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here

class UserProfile(User):
    phone = models.CharField(max_length=15)
    middle_name = models.CharField(max_length=50)

class IMEI(models.Model):
    user = models.ForeignKey(UserProfile)
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=False)




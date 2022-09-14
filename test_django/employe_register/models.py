from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Create user and save to the database
class employeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=30, blank=True)
    employee_profile = models.CharField(max_length=30, blank=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=30, blank=True)

class adminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    apikeys = models.CharField(max_length=30, blank=True)

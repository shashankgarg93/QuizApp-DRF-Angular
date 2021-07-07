from django.db import models
from django.db.models.base import Model
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=25)
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=12)
    phone_number = PhoneNumberField()
    email = models.EmailField()
    profile_pic = models.ImageField(upload_to='uploads/')


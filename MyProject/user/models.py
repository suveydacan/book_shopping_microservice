from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.exceptions import ValidationError

# Create your models here.

class Profile(models.Model):
    name=models.CharField(max_length=30)
    surname=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    birthdate=models.DateField()
    phone=models.CharField(max_length=30)
    password=models.CharField(max_length=8)
    # city=models.CharField(max_length=30)
    # county=models.CharField(max_length=30)
    # postcode=models.IntegerField()
    # addressDetail=models.TextField(max_length=30)


class MyAddress(models.Model):
     user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
     city=models.CharField(max_length=30)
     county=models.CharField(max_length=30)
     neighborhood=models.CharField(max_length=30)
     street=models.CharField(max_length=30)
     binaNo=models.CharField(default='0',max_length=10)
     flights_up=models.CharField(default='0',max_length=10)
     apartmentNo=models.CharField(default='0',max_length=10)
     postcode=models.IntegerField()
     addressDetail=models.TextField(max_length=60)

    

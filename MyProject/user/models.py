from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.exceptions import ValidationError

# Create your models here.

class Profile(models.Model):
    #user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    surname=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    birthdate=models.DateField()
    phone=models.CharField(max_length=30)
    password=models.CharField(max_length=8)
    city=models.CharField(max_length=30)
    county=models.CharField(max_length=30)
    postcode=models.IntegerField()
    addressDetail=models.TextField(max_length=30)


#    def __str__(self):
#        return str(self.user)

#@receiver(post_save,sender=User)
#def create_or_upsate_user_profile(sender,instance,created,**kwargs):
#    if created:
#        Profile.objects.create(user=instance)
#    instance.profile.save()

    

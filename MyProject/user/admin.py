from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display=['user']
    class Meta:
        model=Profile

admin.site.register(Profile)

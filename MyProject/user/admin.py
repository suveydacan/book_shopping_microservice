from django.contrib import admin
from .models import Profile
from .models import MyAddress

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display=['name','surname','phone']
    # class Meta:
    #     model=Profile

class AddressAdmin(admin.ModelAdmin):
    list_display=('user','city','county')

admin.site.register(Profile)
admin.site.register(MyAddress)

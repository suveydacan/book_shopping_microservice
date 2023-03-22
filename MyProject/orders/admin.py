from django.contrib import admin
from orders.models import ShopCart 

# Register your models here.
class ShopCartAdmin(admin.ModelAdmin):
    list_display=['user','book','price','quantity','amount']
    list_filter=['user']

admin.site.register(ShopCart,ShopCartAdmin)

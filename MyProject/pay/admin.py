
from django.contrib import admin
from .models import Payment
# Register your models here.

class PaymentAdmin(admin.ModelAdmin):
    list_display=('payment_method',)
    list_display_links=('payment_method'),
    



admin.site.register(Payment,PaymentAdmin)

# Register your models here.

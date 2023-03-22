from django.db import models

# Create your models here.

class Payment(models.Model):
    payment_method = models.CharField(max_length=30)
   # payment_total =models.CharField(max_length=30)




    def _str_(self):
        return self.payment_method
    

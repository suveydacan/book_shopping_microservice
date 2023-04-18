from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from books.models import Book


class ShopCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    book=models.ForeignKey(Book,on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField()
    
    @property
    def amount(self):
        return(self.quantity*self.book.price)
    
    @property
    def price(self):
        return(self.book.price)
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
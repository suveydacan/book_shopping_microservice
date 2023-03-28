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
    

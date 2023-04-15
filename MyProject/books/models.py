from pyexpat.errors import messages
from django.db import models
from django.shortcuts import redirect

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=200)
    book_name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    publisher=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    page_number=models.IntegerField()
    stocks=models.IntegerField(default=0)
    image=models.CharField(default='image1.jpg',max_length=50)
    
   
    
    def save(self,*args,**kwargs):
        self.title = '{}{}{}{}'.format(self.book_name,self.author,self.publisher,self.category)
        super(Book,self).save(*args,**kwargs)


   

    def __str__(self):
        return self.book_name
    
    def get_image_path(self):
        return '/img/'+ self.image  #img ile resim uzantısını birleştirir.
    
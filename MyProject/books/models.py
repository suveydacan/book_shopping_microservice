from pyexpat.errors import messages
from django.db import models
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=200, default="yazar")
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
    


class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    books=models.ForeignKey(Book,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.CharField(max_length=250,blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status=models.CharField(max_length=10,choices=STATUS, default='New')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.subject

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']
    
    
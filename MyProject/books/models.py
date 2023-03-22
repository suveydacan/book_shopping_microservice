from django.db import models

# Create your models here.

class Book(models.Model):
    book_name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    publisher=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    page_number=models.IntegerField()
    

   

    def __str__(self):
        return self.book_name
    
    
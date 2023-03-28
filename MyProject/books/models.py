from django.db import models

# Create your models here.

class Book(models.Model):
    book_name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    publisher=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    page_number=models.IntegerField()
    stocks=models.IntegerField(default=0)
    image=models.CharField(default='image1.jpg',max_length=50)
    

   

    def __str__(self):
        return self.book_name
    
    def get_image_path(self):
        return '/img/'+ self.image  #img ile resim uzantısını birleştirir.

    
    

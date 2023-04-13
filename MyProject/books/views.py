from django.shortcuts import render
from .models import Book
# Create your views here.

def product_pages(request):
    books=Book.objects.all()  # db'deki objeleri almış oluyoruz.

    context={
        'books': books
    }

    return render(request ,"books/product.html", context)

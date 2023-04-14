from django.shortcuts import render
from .models import Book
# Create your views here.

def product_pages(request):
    books=Book.objects.all()  # db'deki objeleri almış oluyoruz.

    context={
        'books': books
    }

    return render(request ,"books/product.html", context)


def book_detail(request, book_id):
    selectedBook=Book.objects.get(id=book_id)

    # for book in books:
    #     if book.pk==id:
    #         selectedBook=book
    return render(request, "books/detail.html",{
        "book":selectedBook
    })
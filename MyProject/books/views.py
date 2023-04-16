from django.shortcuts import render
from .models import Book
from django.http import HttpResponseRedirect
from .forms import SearchForm

from django.db.models import Q


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

def product_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            #category = Category.objects.all()
            query = form.cleaned_data['query']
            books = Book.objects.filter(title__icontains=query)

            context = {'books': books,
                       
                       }
            return render(request,"books/product.html", context)
    return HttpResponseRedirect('/')

from django.shortcuts import get_object_or_404, redirect, render
from .models import Book
from django.http import HttpResponseRedirect
from .forms import SearchForm
from books.models import CommentForm, Comment
from django.contrib import messages
from django.urls import reverse

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
    comments=Comment.objects.filter(books_id=book_id,status='True')


    # for book in books:
    #     if book.pk==id:
    #         selectedBook=book
    return render(request, "books/detail.html",{
        "book":selectedBook,
        "comments":comments,
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

def add_comment(request,book_id):
    return redirect(reverse('add_to_cart',args=[book_id]))


def addcomment(request,id):
   url = request.META.get('HTTP_REFERER')  # get last url
   #return HttpResponse(url)
   
   if request.method == 'POST':  # check post
      form = CommentForm(request.POST)
      if form.is_valid():
         data = Comment()  # create relation with model
         data.subject = form.cleaned_data['subject']
         data.comment = form.cleaned_data['comment']
         data.rate = form.cleaned_data['rate']
         data.ip = request.META.get('REMOTE_ADDR')
         data.books_id=id
         current_user= request.user
         data.user_id=current_user.id
         data.save()  # save data to table
         messages.success(request, "Mesajınız yayınlanmak için değerlendirmeye alınmıştır")
         return HttpResponseRedirect(url)
      
   messages.warning(request,"Yorumunuz kaydedilemedi,daha sonra tekrar deneyiniz")
   return HttpResponseRedirect(url)







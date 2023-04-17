from pyexpat.errors import messages
from django.contrib.messages import success,warning
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from books.models import Book
from django.contrib.auth.models import User
from .models import Cart, CartItem, Favorite


# Create your views here.

@login_required(login_url='/login/')
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    total_price = sum([item.book.price * item.quantity for item in cart_items])
    return render(request, 'cart/shopping_cart.html', {'cart': cart, 'cart_items': cart_items, 'total_price': total_price})

@login_required(login_url='/login/')
def shopping_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum([item.quantity * item.book.price for item in cart_items])
    context = {'cart_items': cart_items, 'total_price': total_price}
    return render(request, 'cart/shopping_cart.html', context)

@login_required(login_url='/login/')
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        book=book,
    )
    if created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('shopping_cart')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, pk=item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('shopping-cart')

@login_required
def add_to_favorites(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    favorite, created = Favorite.objects.get_or_create(
        user=request.user,
        book=book,
    )
    if created:
        success(request, 'Kitap favorilere eklendi!')
        return redirect('view_favorites')
    else:
     warning(request, 'Kitap zaten favorilerinizde!')
     return redirect('books:detail', id=book_id)

@login_required
def view_favorites(request):
    favorites = Favorite.objects.filter(user=request.user)
    context = {'favorites': favorites}
    return render(request, 'cart/favs.html', context)
from django.shortcuts import render

# Create your views here.


def checkout(request):
    return render(request, "orders/checkout.html")

def detail(request):
    return render(request, "orders/detail.html")

def order_detail(request):
    return render(request, "orders/order-detail.html")

def orders(request):
    return render(request, "orders/orders.html")

def shopping_cart(request):
    return render(request, "orders/shopping-cart.html")
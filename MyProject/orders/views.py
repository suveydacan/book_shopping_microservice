from django.shortcuts import render

# Create your views here.


def checkout(request):
    return render(request, "orders/checkout.html")

def order_details(request):
    return render(request, "orders/order_details.html")

def orders(request):
    return render(request, "orders/orders.html")

def shopping_cart(request):
    return render(request, "orders/shopping-cart.html")
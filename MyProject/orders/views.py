from django.shortcuts import render

# Create your views here.


def checkout(request):
    return render(request, "orders/checkout.html")

def order_detail(request):
    return render(request, "orders/order_details.html")

def orders(request):
    return render(request, "orders/orders.html")


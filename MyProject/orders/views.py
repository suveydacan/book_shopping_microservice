from django.shortcuts import get_object_or_404, render, redirect
#from orders.models import Order
#from MyProject.cart.models import Cart
from .models import Order
from cart.models import Cart


from orders.models import Order

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

def create_order(request):
    cart = Cart.objects.get(user=request.user)
    order = Order.objects.create(user=request.user)
    order_items = []

    for item in cart.items.all():
        order_items.append(item)
        item.cart = None
        item.order = order
        item.save()

    order.items.set(order_items)
    order.save()
    cart.total = 0
    cart.save()

    return redirect('order_confirmation', order_id=order.id)
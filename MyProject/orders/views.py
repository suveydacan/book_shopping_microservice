from django.shortcuts import redirect, render

# Create your views here.


def checkout(request):
    return render(request, "orders/checkout.html")

def order_detail(request):
    return render(request, "orders/order_details.html")

def orders(request):
    return render(request, "orders/orders.html")

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

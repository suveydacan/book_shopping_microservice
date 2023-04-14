from django.urls import path
from . import views

urlpatterns = [
    path('checkout', views.checkout, name='checkout'),
    path('order_details', views.order_details, name='order_details'),
    path('orders', views.orders, name='orders'),
    path('shopping-cart', views.shopping_cart, name='shopping-cart'),
   
]
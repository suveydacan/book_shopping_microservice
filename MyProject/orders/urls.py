from django.urls import path
from . import views

urlpatterns = [
    path('checkout', views.checkout, name='checkout'),
    path('detail', views.detail, name='detail'),
    path('order_detail', views.order_detail, name='order_detail'),
    path('orders', views.orders, name='orders'),
    path('shopping-cart', views.shopping_cart, name='shopping-cart'),
   
]
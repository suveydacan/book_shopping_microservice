from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('checkout', views.checkout, name='checkout'),
    path('order_details', views.order_detail, name='order_details'),
    path('orders', views.orders, name='orders'),
    path('create_order/', views.create_order, name='create_order'),
   
]
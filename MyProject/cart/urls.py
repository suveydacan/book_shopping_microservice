from django.urls import path
from . import views



app_name = 'cart'


urlpatterns = [
    path('cart_detail', views.cart_detail, name='cart_detail'),
    path('view_cart', views.view_cart, name='view_cart'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart', views.remove_from_cart, name='remove_from_cart'),
    
]
#path('add/<int:product_id>/', views.cart_add, name='cart_add'),
#path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
from django.urls import path
from . import views



app_name = 'cart'


urlpatterns = [
      path('shopping-cart', views.view_cart, name='shopping-cart'),
      path('shopping-cart/<int:book_id>/',views.add_to_cart,name='shopping-cart'),
      path('favs/<int:book_id>/', views.view_favorites, name='favs'),
    
]
#path('add/<int:product_id>/', views.cart_add, name='cart_add'),
#path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
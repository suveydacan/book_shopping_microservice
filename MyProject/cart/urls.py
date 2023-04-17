from django.urls import path
from . import views



app_name = 'cart'


urlpatterns = [
      path('shopping_cart', views.shopping_cart, name='shopping_cart'),
      path('add_to_cart/<int:book_id>/',views.add_to_cart,name='add_to_cart'),
      path('favs/<int:book_id>/', views.add_to_favorites, name='favs'),
      path('favs', views.view_favorites, name='favs'),
    
]
#path('add/<int:product_id>/', views.cart_add, name='cart_add'),
#path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
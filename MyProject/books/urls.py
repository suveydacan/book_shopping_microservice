from django.urls import path
from . import views

urlpatterns = [
    path('product', views.product_pages, name='product'),
    path('detail/<int:book_id>/',views.book_detail,name='detail'),
    # path('<int:book_id>',views.detail,name='detail'),
    # path('search',views.search,name='search'),
]
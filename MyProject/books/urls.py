from django.urls import path
from . import views

urlpatterns = [
    path('product', views.product_pages, name='product'),
    # path('<int:book_id>',views.detail,name='detail'),
    # path('search',views.search,name='search'),
]
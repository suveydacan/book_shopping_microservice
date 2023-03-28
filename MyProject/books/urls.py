from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_pages, name='books'),
    # path('<int:book_id>',views.detail,name='detail'),
    # path('search',views.search,name='search'),
]
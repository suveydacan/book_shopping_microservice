from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path("login", views.login_request, name="login"),
    path("register", views.register_request, name="register"),
    path("logout", views.logout_request, name="logout"),
    path("index", views.index, name="index"),
    path("", views.index, name="index"),
]
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from books.models import Book


def index(request):
    books=Book.objects.all()  # db'deki objeleri almış oluyoruz.

    context={
        'books': books
    }

    return render(request ,"account/index.html", context)

@login_required
def profile(request):
    return render(request, "account/profile.html")

def login_request(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user= authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect("account:profile")
        else: 
            return render(request, "account/login.html",{
            "error": "email ya da password yanlış"
        })
    
    return render(request ,"account/login.html") #olusturulan html sayfalarını gosterecek

def register_request(request):
    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        repassword = request.POST.get("repassword")

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request,"account/register.html",
                              {"error": "username kullanılıyor",
                               "username":username,
                               "email":email,
                               "first_name":first_name,
                               "last_name":last_name,    
                               })
            else:
                if User.objects.filter(email=email).exists():
                     return render(request,"account/register.html",
                              {"error": "email kullanılıyor",
                               "username":username,
                               "email":email,
                               "first_name":first_name,
                               "last_name":last_name,    
                               })
                else:
                    user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                    user.save()
                    return redirect("login") #logine dönsün giriş için
        else:
            return render(request,"account/register.html",
                          { "error": "parola eşleşmiyor.",
                            "email":email,
                            "first_name":first_name,
                            "last_name":last_name, 
                           })
    return render(request ,"account/register.html") 

def logout_request(request):
    logout(request)
    return HttpResponseRedirect('/')
    #return redirect("home") #ana sayfaya donuyo bizde yok hata verir logout diyince
# Create your views here.

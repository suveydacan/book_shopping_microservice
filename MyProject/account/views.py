from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User



def login_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user= authenticate(request, username= username, password= password)
        if user is not None:
            login(request, user)
            return redirect("login")
        else: 
            return render(request, "account/login.html",{
            "error": "username ya da password yanlış"
        })
    
    return render(request ,"account/login.html") #olusturulan html sayfalarını gosterecek

def register_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request,"account/register.html",{"error": "username kullanılıyor"})
            else:
                if User.objects.filter(email=email).exists():
                    return render(request,"account/register.html",{"error": "bu mail adresine ait bir hesap zaten var"})
                else:
                    user = User.objects.create_user(username=username, password=password)
                    user.save()
            return redirect("login") #logine dönsün giriş için
        else:
            return render(request,"account/register.html",{"error": "parola eşleşmiyor."})
    return render(request ,"account/register.html") 

def logout_request(request):
    return redirect("home") #ana sayfaya donuyo bizde yok hata verir logout diyince
# Create your views here.

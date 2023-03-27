from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login



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
            pass
        else:
            return render(request,"register",{"error": "parola eşleşmiyor."})
    return render(request ,"login") #logine dönsün giriş için

def logout_request(request):
    return redirect("home") #onceden tanımladıgı bi yere donuyo bizde yok hata verir logout diyince
# Create your views here.

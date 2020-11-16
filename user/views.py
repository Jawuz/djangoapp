from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            newUser = User(username=username)
            newUser.set_password(password)
            newUser.save()
            login(request,newUser)
            messages.info(request,"You are signed up successfully!")
            return redirect("index")
        context = {"form":form}
        return render(request,"register.html", context)
    context = {"form":form}
    return render(request,"register.html", context)
    
def loginUser(request):
    form = LoginForm(request.POST or None)
    context ={
        "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            messages.info(request,"Username or Password is not correct")
            return render(request,"login.html", context)
        messages.success(request,"You are logged in successfully")
        login(request,user)
        return redirect("index")
    return render (request,"login.html", context)

def logoutUser(request):
    logout(request)
    messages.success(request,"You are now logged out")
    return redirect("index")
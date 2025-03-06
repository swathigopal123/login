from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate
# Create your views here.
def home(request):
    return render(request,'home.html')
def loginn(request):
    error_message=None
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            error_message="invalid credentials"
    return render (request,'login.html',{'error_message':error_message})
def logoutt(request):
    logout(request)
    return redirect('login')
def signup(request):
    user=None
    error_message=None
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=User.objects.create_user(username=username,password=password)
        except Exception as e:
            error_message=str(e)
    return render(request,'create.html',{'user':user,'error_message':error_message})
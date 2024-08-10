from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import Group,User

# Create your views here.
def index(request):
    return render(request,'index.html')

def login_view(request):
    return render(request,'accounts/login_c.html')

def register_view(request):
    return render(request,'accounts/register_c.html')

def dashboard_view(request):
    return render(request,'accounts/dashboard_c.html')

def slogin_view(request):
    return render(request,'accounts/login_s.html')

def sregister_view(request):
    return render(request,'accounts/register_s.html')

def sdashboard_view(request):
    return render(request,'accounts/dashboard_s.html')

def logout_view(request):
    return render('index')


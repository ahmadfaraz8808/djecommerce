from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username:
            messages.error(request, 'Username is required')
            return redirect('login')
        if not password:
            messages.error(request, 'Password is required')
            return redirect('login')
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
        if not user.groups.exists():                    # Check if user has a group
            messages.error(request, '!Contact your administrator')
            return redirect('login')
        groups = user.groups.all()       # Get the first group name
        if len(groups)==0 or groups[0].name != 'customer':
            messages.error(request, 'You are not authorized to login!')
            return redirect('login')
        login(request, user)
        return redirect('dashboard')
    return render(request, 'accounts/login_c.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        if not username:
            messages.error(request, 'Username is required')
            return redirect('register')
        if not password:
            messages.error(request, 'Password is required')
            return redirect('register')
        if not cpassword:
            messages.error(request, 'Confirm Password is required')
            return redirect('register')
        if not email:
            messages.error(request, 'Email is required')
            return redirect('register')
        if not first_name:
            messages.error(request, 'First Name is required')
            return redirect('register')
        if not last_name:
            messages.error(request, 'Last Name is required')
            return redirect('register')
        if password != cpassword:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is taken')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is taken')
            return redirect('register')
        user = User(username=username, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        group = Group.objects.get(name='customer')
        user.groups.add(group)
        group.save()
        messages.success(request, 'Account created successfully')
        return redirect('login')
    return render(request, 'accounts/register_c.html')

def dashboard_view(request):
    return render(request, 'accounts/dashboard_c.html')

def slogin_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username:
            messages.error(request, 'Username is required')
            return redirect('seller_login')
        if not password:
            messages.error(request, 'Password is required')
            return redirect('seller_login')
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid credentials')
            return redirect('seller_login')
        if not user.groups.exists():                    # Check if user has a group
            messages.error(request, '!Contact your administrator')
            return redirect('seller_login')
        groups = user.groups.all()       # Get the first group name
        if len(groups)==0 or groups[0].name != 'seller':
            messages.error(request, 'You are not authorized to login!')
            return redirect('seller_login')
        login(request, user)
        return redirect('seller_dashboard')
    return render(request, 'accounts/login_s.html')

def sregister_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        if not username:
            messages.error(request, 'Username is required')
            return redirect('seller_register')
        if not password:
            messages.error(request, 'Password is required')
            return redirect('seller_register')
        if not cpassword:
            messages.error(request, 'Confirm Password is required')
            return redirect('seller_register')
        if not email:
            messages.error(request, 'Email is required')
            return redirect('seller_register')
        if not first_name:
            messages.error(request, 'First Name is required')
            return redirect('seller_register')
        if not last_name:
            messages.error(request, 'Last Name is required')
            return redirect('seller_register')
        if password != cpassword:
            messages.error(request, 'Passwords do not match')
            return redirect('seller_register')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is taken')
            return redirect('seller_register')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is taken')
            return redirect('seller_register')
        user = User(username=username, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        group = Group.objects.get(name='seller')
        user.groups.add(group)
        group.save()
        messages.success(request, 'Seller created successfully')
        return redirect('seller_login')
    return render(request, 'accounts/register_s.html')

def sdashboard_view(request):
    return render(request, 'accounts/dashboard_s.html')

def logout_view(request):
    logout(request)
    return redirect('index')
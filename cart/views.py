from django.shortcuts import render

# Create your views here.

def show_cart(request):
    return render(request, 'cart/show.html')

def sucess(request):
    return render(request, 'cart/success.html')

def failure(request):
    return render(request, 'cart/failure.html')

def add_product(request,product):
    referrer = request.META.get('HTTP_REFERER')
    return render(referrer)

def remove_product(request,product):
    referrer = request.META.get('HTTP_REFERER')
    return render(referrer)

def increase_qty(request,product):
    referrer = request.META.get('HTTP_REFERER')
    return render(referrer)

def decrease_qty(request,product):
    referrer = request.META.get('HTTP_REFERER')
    return render(referrer)

def checkout(request):
    pass


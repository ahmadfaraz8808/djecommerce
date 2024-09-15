from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .models import Cart, CartItem, Order
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def show_cart(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.cartitem_set.all()
    return render(request, 'cart/show.html', {
        'cart_items': cart_items
    })


def success(request):
    return render(request, 'cart/success.html')

def failure(request):
    return render(request, 'cart/failure.html')

def orders(request):
    return render(request, 'cart/orders.html')

@login_required
def add_product(request, product):              #add product in cart
    referrer = request.META.get('HTTP_REFERER')
    product = get_object_or_404(Product, slug=product)
    # if cart exists for user, get it, else create it
    cart, _ = Cart.objects.get_or_create(user=request.user)
    # add the product to CartItem
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not item_created:                                                #what do u mean by item_created???
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, 'Product quantity increased')
    else:
        messages.success(request, 'Product added to cart')
    # count items in cart
    no_of_items = cart.cartitem_set.count()         #???
    request.session['cart'] = no_of_items
    print(request.session['cart'], 'items')
    return redirect(referrer)

def remove_product(request, product):
    referrer = request.META.get('HTTP_REFERER')
    return redirect(referrer)

def increase_qty(request, product):
    referrer = request.META.get('HTTP_REFERER')
    return redirect(referrer)

def decrease_qty(request, product):
    referrer = request.META.get('HTTP_REFERER')
    return redirect(referrer)

def checkout(request):
    pass
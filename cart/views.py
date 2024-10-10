from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .models import Cart, CartItem, Order
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from django.conf import settings
import razorpay

razorpay_client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, 
                                        settings.RAZOR_KEY_SECRET))

@login_required
def show_cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.cartitem_set.all()
        # total price
        total_price = 0
        for item in cart_items:
            total_price += item.product.price * item.quantity

        return render(request, 'cart/show.html', {
            'cart_items': cart_items,
            'total_price': total_price,
        })
    except:
        messages.error(request, 'Cart is empty')
        return redirect('index')


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
    cart = Cart.objects.get(user=request.user)
    product = get_object_or_404(Product, slug=product)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    cart_item.delete()
    no_of_items = cart.cartitem_set.count()
    request.session['cart'] = no_of_items
    messages.success(request, 'Product removed from cart')
    return redirect(referrer)

def increase_qty(request, product):
    referrer = request.META.get('HTTP_REFERER')
    user = request.user
    cart = Cart.objects.get(user=user)
    product = get_object_or_404(Product, slug=product)
    # if it is in cart items
    cart_item = CartItem.objects.get(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect(referrer)

def decrease_qty(request, product):
    referrer = request.META.get('HTTP_REFERER')
    user = request.user
    cart = Cart.objects.get(user=user)
    product = get_object_or_404(Product, slug=product)
    # if it is in cart items
    cart_item = CartItem.objects.get(cart=cart, product=product)
    cart_item.quantity -= 1
    cart_item.save()
    return redirect(referrer)

@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.cartitem_set.all()
    total = 0
    for item in cart_items:
        total += item.product.price * item.quantity
    razorpay_order = razorpay_client.order.create({
        'amount' : int(total * 100),
        'currency': 'INR',
        'payment_capture': 0
    })
    razorpay_order_id = razorpay_order['id']
    callback_url = request.build_absolute_uri('/cart/payment/callback')
    return render(request, 'cart/checkout.html', {
        'cart_items': cart_items,
        'total_price': total,
        'currency': 'INR',
        'callback_url': callback_url,
        'razorpay_order_id': razorpay_order_id,
        'razorpay_merchant_key': settings.RAZOR_KEY_ID,
        'razorpay_amount': int(total * 100),
    })

@csrf_exempt
def payment_callback(request):
    if request.method == 'POST':
        payment_id = request.POST.get('razorpay_payment_id', '')
        razorpay_order_id = request.POST.get('razorpay_order_id', '')
        signature = request.POST.get('razorpay_signature', '')
        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }
        result = razorpay_client.utility.verify_payment_signature(params_dict)
        if not result:
            return redirect('failed')
        else:
            cart = Cart.objects.get(user=request.user)
            cart_items = cart.cartitem_set.all()
            for item in cart_items:
                Order.objects.create(
                    product=item.product,
                    user=request.user,
                    quantity=item.quantity,
                    total_price=item.total_price(),
                    address='Test Address',
                    razorpay_order_id=razorpay_order_id,
                    razorpay_payment_id=payment_id,
                    is_paid=True,
                )
                # clear all cart items
                item.delete()
            cart.delete()
            request.session['cart'] = 0
            return redirect('success')
    return redirect('failed')
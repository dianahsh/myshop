from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

def homePage(r):
    return render(r, "shop/index.html")

def listproduct(request):
    products = Product.objects.all()
    return render(request, 'shop/product/allProductView.html', {'products': products})

def productView(request, id):
    if request.user.is_authenticated:
        user = request.user
    p = Product.objects.get(id=id)
    try:
        cart = ShoppingCart.objects.get(user = user)
        try: 
            listy = ShoppinList.objects.get(cart = cart, product = p)
            l = listy.quantity
        except:
            l = 0
    except:
        l = 0
    return render(request, "shop/product/Oproduct.html", {'product': p, 'quantity': l})

@login_required(login_url="/account/login")
def cartView(req):
    if req.user.is_authenticated:
        user = req.user
    try:
        cart = ShoppingCart.objects.get(user = user)
        shopping = ShoppinList.objects.filter(cart = cart)
    except:
        return HttpResponse("Empty")
    
    return render(req, "shop/Cart/CartView.html", { 'listShops': shopping })

@login_required(login_url="/account/login")
def purchase(req):
    if req.method == "POST":
        if req.user.is_authenticated:
            user = req.user
        ad = req.POST.get("address")
        cart = ShoppingCart.objects.get(user= user)
        lc = ShoppinList.objects.filter(cart = cart)
        if len(lc) == 0:
            return HttpResponse("Empty")
        ord = Order.objects.create(user = user, address = ad)
        try:
            for c in lc:
                OrderList.objects.create(order=ord, product = c.product, 
                                        quantity=c.quantity, price = (c.product.price*c.quantity))
            lc.delete()
        except:
            ord.delete
        return redirect("/profile")
    return render(req, "shop/Order/Purchase.html")

@require_POST
@login_required(login_url="/account/login")
def addToCart(request):
    b = int(request.body)
    user = request.user
    product = Product.objects.get(id = b)

    try:
        cart = ShoppingCart.objects.get(user = user)
    except:
        cart = ShoppingCart.objects.create(user = user)
    
    try: 
        listy = ShoppinList.objects.get(cart = cart, product = product)
        listy.quantity = listy.quantity + 1
        listy.save()
    except:
        listy = ShoppinList.objects.create(cart = cart, product = product)
    
    return HttpResponse(200)

@require_POST
@login_required(login_url="/account/login")
def decrease(request):
    b = int(request.body)
    user = request.user
    product = Product.objects.get(id = b)

    try:
        cart = ShoppingCart.objects.get(user = user)
        listy = ShoppinList.objects.get(cart = cart, product = product)
        listy.quantity = listy.quantity - 1
        if(listy.quantity <= 0):
            listy.delete()
        else:
            listy.save()
    except:
        return HttpResponse("error")
    
    return HttpResponse(200)

@login_required(login_url="/account/login")
def PastPurchases(req):
    usr = req.user

    ord = Order.objects.prefetch_related('orders_list').filter(user = usr)

    return render(req, "shop/Order/pastPur.html", {'orders': ord})

def viewProfile(req):
    usr = req.user
    return render(req, "shop/profile.html")
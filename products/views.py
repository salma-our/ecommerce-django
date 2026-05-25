from django.shortcuts import render
from .models import Product


def home(request):
    products = Product.objects.all()[:6]
    return render(request, 'products/home.html', {
        'products': products
    })


def cart(request):
    return render(request, 'products/cart.html')


def product_list(request):

    products = Product.objects.all()

    return render(request,
                  'products/product_list.html',
                  {'products': products})


def product_detail(request, id):

    product = Product.objects.get(id=id)

    return render(request,
                  'products/product_detail.html',
                  {'product': product})
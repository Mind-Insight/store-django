from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse

from products.models import ProductCategory, Products, Cart
from users.models import User


def index(request):
    return render(request, 'products/index.html', {'title': "Testing template"})


def products(request):
    context = {
        'title': 'Store - каталог',
        'products': Products.objects.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', context)


def cart_add(request, product_id):
    product = Products.objects.get(id=product_id)
    baskets = Cart.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Cart.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, basket_id):
    basket = Cart.objects.get(id=basket_id)
    basket.remove()
    return HttpResponseRedirect(request.META(['HTTP_REFERER']))
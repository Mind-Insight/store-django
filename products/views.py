from django.shortcuts import render, HttpResponse

from products.models import ProductCategory, Products


def index(request):
    return render(request, 'products/index.html', {'title': "Testing template"})


def products(request):
    context = {
        'title': 'Store - каталог',
        'products': Products.objects.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', context)
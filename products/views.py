from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'products/index.html', {'title': "Testing template"})


def products(request):
    return render(request, 'products/products.html')
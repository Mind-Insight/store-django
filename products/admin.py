from django.contrib import admin

from products.models import ProductCategory, Products
admin.site.register(ProductCategory)
admin.site.register(Products)

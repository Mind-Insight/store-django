from django.urls import path, include
from products.views import products


app_name = 'products'
urlpatterns = [
    path('', products, name='index')
]
from django.urls import path, include
from products.views import products, cart_add


app_name = 'products'
urlpatterns = [
    path('', products, name='index'),
    path('baskets/add/<int:product_id>/', cart_add, name='cart_add')
]
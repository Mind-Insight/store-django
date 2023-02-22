from django.urls import path
from users.views import register, login, profile

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', register, name='registration'),
    path('profile/', profile, name='profile')
]
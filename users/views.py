from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistationForm, UserProfileForm
from products.models import Cart


def login(request):
    # Авторизция пользователя
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)

        # проверка заполненной формы на валидность
        if form.is_valid():

            # получаем данные, который ввел пользователь
            username = request.POST['username']
            password = request.POST['password']

            # проверка на то, есть ли пользователь в системе
            user = auth.authenticate(username=username, password=password)
            if user:
                # если пользователь есть, то мы его авторизовываем
                auth.login(request, user)
                messages.success(request, "Congratulations! You've successfully logged in.")

                # перенаправление на главную страницу
                return HttpResponseRedirect('/')

    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! You've successfully registered")
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistationForm()
    context = {'form': form}

    return render(request, 'users/register.html', context)


def profile(request):
    if request.method == "POST":
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))

    baskets = Cart.objects.filter(user=request.user)
    total_sum = 0
    total_quantity = 0
    for basket in baskets:
        total_sum += basket.sum_price()
        total_quantity += basket.quantity

    form = UserProfileForm(instance=request.user)
    context = {
        'title': 'Store - Профиль',
        'form': form,
        'baskets': baskets,
        'total_sum': total_sum,
        'total_quantity': total_quantity
    }

    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistationForm, UserProfileForm

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

    form = UserProfileForm(instance=request.user)
    context = {'title': 'Store - Профиль', 'form': form}

    return render(request, 'users/profile.html', context)

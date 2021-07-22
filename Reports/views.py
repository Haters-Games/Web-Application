from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# import logging


def auth(request):
    """Функция проверки входа в систему"""
    if request != None:
        # Проверка, что пользователь уже вошел в систему
        if request.user.is_authenticated:
            return True

        # Проверка флажка "Запомнить меня"
        if request.POST.get('action') == 'login':
            if request.POST.get('remember-me') == 'on':
                request.session.set_expiry(2628000)
            else:
                request.session.set_expiry(0)

            # Проверка данных входа
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return True
    return False


def _login(request):
    """Функция отображения для страницы входа"""
    # Проверка, что пришла форма на выход из системы
    if request.POST.get('action') == 'exit':
        logout(request)
    elif auth(request):
        return redirect('/home/')

    return render(request, './Login/index.html')


@login_required(redirect_field_name='')
def _home(request):
    return render(request, './Home/index.html')


@login_required(redirect_field_name='')
def _view(request):
    return render(request, './View/index.html')
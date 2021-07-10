from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def auth(request):
    """Функция проверки входа в систему"""
    if request != None:
        if request.user.is_authenticated:
            return True

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return True
    return False


# Create your views here.
def _login(request):
    """Функция отображения для страницы входа"""
    if auth(request):
	    return redirect('/home/')
    else:
        return render(request, './Login/index.html')

@login_required(redirect_field_name='')
def _home(request):
    return render(request, './Home/index.html')
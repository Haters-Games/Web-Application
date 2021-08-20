from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.middleware.csrf import *
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .forms import (FullReport, ReportAnalyzes, ReportLight, ReportMain,
                    ReportMicroclimate, ReportPhenology, ReportProtection,
                    ReportWatering)

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

@csrf_protect
@login_required(redirect_field_name='')
def _create(request):
    if request.POST.get('action') == 'send-report':
        f = FullReport(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/home/')
        else:
            c = {}
            c.update({'form': f})
            c.update({
            'ReportMain': ReportMain(),
            'ReportLight': ReportLight(),
            'ReportMicroclimate': ReportMicroclimate(),
            'ReportWatering': ReportWatering(),
            'ReportPhenology': ReportPhenology(),
            'ReportAnalyzes': ReportAnalyzes(),
            'ReportProtection': ReportProtection()
            })

            return render(request, './Create/index.html', c
            )

    return render(request, './Create/index.html',  
    {
        'ReportMain': ReportMain(),
        'ReportLight': ReportLight(),
        'ReportMicroclimate': ReportMicroclimate(),
        'ReportWatering': ReportWatering(),
        'ReportPhenology': ReportPhenology(),
        'ReportAnalyzes': ReportAnalyzes(),
        'ReportProtection': ReportProtection()
    })
    
@login_required(redirect_field_name='')
def _report(request):
    return render(request, './Report/index.html')

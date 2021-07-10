from django.shortcuts import render
from django.template.context import RequestContext

# Create your views here.
def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(request, './main/index.html')

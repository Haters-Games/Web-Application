from django.shortcuts import render
from django.template.context import RequestContext

# Create your views here.
def login(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    #if authed(request):
	#	return redirect('/home/')
	#else:
	#	return render(request, './Login/index.html')
    
    return render(request, './Login/index.html')
    
def home(request):
    return render(request, './Home/index.html')

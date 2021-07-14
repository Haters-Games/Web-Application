from django import template

register = template.Library()


# Пример шаблона
# @register.tag(name="temp") - если нужно
# @register.simple_tag(takes_context = True)
# def getInfo(context, temp):
# 	Тело функции


@register.simple_tag(takes_context = False)
def head():
    return """
    <title>Сервис отчетов Чурилово</title>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <link rel="stylesheet" type="text/css" href="{% static 'Server/Styles/Base.css' %}">
    <link rel="shortcut icon" type="image/x-icon" href="{% static 'Server/Pictures/favicon.ico' %}">
    """
	
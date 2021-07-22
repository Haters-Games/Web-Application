from django.http import HttpResponse
from django.conf import settings
from django import template
import logging

register = template.Library()


# Пример шаблона
# @register.tag(name="temp") - если нужно
# @register.simple_tag(takes_context = True)
# def getInfo(context, temp):
# 	Тело функции


@register.simple_tag(takes_context = True)
def meta(context):
    static = settings.STATIC_URL
    page = str(context['request']).split('/')[1].capitalize()

    return '''
    <!-- Основная часть -->
    <title>Сервис отчетов Чурилово</title>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <link rel="stylesheet" type="text/css" href="''' + static + '''Server/Styles/Base.css">
    <link rel="stylesheet" type="text/css" href="''' + static + '''Server/Styles/Icons.css">
    <link rel="shortcut icon" type="image/x-icon" href="''' + static + '''Server/Pictures/favicon.ico'">
    
    <!-- Дополнительная часть -->
    <link rel="stylesheet" type="text/css" href="''' + static + page + '''/Styles/''' + page + '''.css">
    '''

# @register.tag(name="arr")
# @register.simple_tag(takes_context = True)
# def menu(context, arr):
#     arr = arr.split(";")

#     for i in (0, len(arr) - 1):
#         arr[i] = arr[i].split(',')
    
#     logging.warning(arr)
    
#     # Кнопка меню
#     output = '''
#     <menu>
#         <ul>
#             <li class="item">
#                 <span></span>
#                 <button class="icon" id="menu-button"></button>
#             </li>
#     '''

#     # Пункты меню
#     for i in arr:
#         output += '''
#         <li class="item">
#             <span>''' + i[0] + '''</span>
#             <button class="icon"></button>
#         </li>
#         '''
#         logging.warning(i)

#     # Панель профиля
#     output += '''
#             <li class="item">
#                 <span>{{ user.get_username }}</span>
#                 <form action="/login/" method="post">
#                     {% csrf_token %}
#                     <button class="icon" type="submit" name="action" value="exit"></button>
#                 </form>
#             </li>
#         </ul>
#     </menu>
#     '''
    
#     return output
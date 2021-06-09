from django.urls import path
from . import views


urlpatterns = [
    # При отключении редиректа позволит получать в корневом каталоге
	# path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
]
from django.shortcuts import redirect, render, reverse
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

menu = ['О сайте', 'Кабинет пользователя', 'Войти']

def home_page(request):
    return render(request, 'AudioApp/home.html', {'menu': menu, 'title': 'Конвертер аудио'})

def user_account(request):
    return render(request, 'AudioApp/user.html')

def about(request):
    return render(request, 'AudioApp/about.html')

def deletion_page(request):
    return render(request, 'AudioApp/deletion.html')


# Create your views here.

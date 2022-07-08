from django.contrib.auth.models import User
from django.shortcuts import redirect, render, reverse
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .forms import UserAut, UserReg, DelData
from .utils.app_utils import saveuserdata, viewuserdata, resultsize, deluserdata
from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Кабинет пользователя', 'url_name': 'user_account'},
        {'title': 'Войти', 'url_name': 'login'},
        ]

def home_page(request):
    """Домашняя страница"""
    return render(request, 'AudioApp/home.html', {'menu': menu})


def user_account(request):
    return render(request, 'AudioApp/user.html')

def about(request):
    return render(request, 'AudioApp/about.html')

def deletion_page(request):
    return render(request, 'AudioApp/deletion.html')

def login(request):
    return render(request, 'AudioApp/login.html')

def wash(request):
    """Удаление данных"""
    return render(request, 'wash.html', context3)
# Create your views here.

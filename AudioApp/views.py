from django.contrib.auth.models import User
from django.shortcuts import redirect, render, reverse
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .forms import UserAut, UserReg, DelData
from utils.app_utils import saveuserdata, viewuserdata, resultsize, deluserdata
from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Кабинет пользователя', 'url_name': 'user_account'},
        {'title': 'Войти',  'url_name': None}]


def home_page(request):
    """Домашняя страница"""

    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        # Проверка логина и пароля  в БД.
        for item in User.objects.all():
            if login == item.login and password == item.password:
                return mypage(request)
        else:
            return HttpResponse('Неверный логин или пороль')
    else:
        useraut = UserAut()
        # context = {"form": useraut}
    return render(request, 'AudioApp/home.html', {'menu': menu, 'title': 'Конвертер аудио'})


def user_account(request):
    return render(request, 'AudioApp/user.html')

def about(request):
    return render(request, 'AudioApp/about.html')

def deletion_page(request):
    return render(request, 'AudioApp/deletion.html')

def reg(request):
    """Страница регистрации"""
    if request.method == 'POST':
        name = request.POST.get('name')
        login = request.POST.get('login')
        password = request.POST.get('password')
        bust = request.POST.get('bust')  # Обхват груди
        waist = request.POST.get('waist')  # Обхват талии
        hips = request.POST.get('hips')  # Обхват бедер
        sleeves = request.POST.get('sleeves') # Длина рукава
        # Сохранение данных регистрации
        try:
            #  Функция сохранения пользовательских  данных
            saveuserdata(name, login, password, bust, waist, hips, sleeves)
        except:
            #  Логины являются уникальными и повторятся не могут
            return HttpResponse('Данный логин уже занят ,попробуйте другой')

        return mypage(request)
    else:
        userreg = UserReg()
        context = {"form": userreg}
    return render(request, 'reg.html', context)

def mypage(request):
    """Страница пользователя"""

    # Создает словарь с пользовательскими данными из БД.
    data = viewuserdata(request)
    # Дополняет словарь размеразми одежды по стандартам  разных стран ,на основе антропометрических характериск.
    context1 = resultsize(data)
    return render(request, 'mypage.html', context1)

def wash(request):
    """Удаление данных"""
    # Проверка логина и пароля
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        repeat_password= request.POST.get('repeat_password')
        if password == repeat_password:
            #print(login, password, repeat_password)
            #  Отправление логина и пароля в функцию удаления и получение ответа.
            flag = deluserdata(login, password)
            #print(flag)
            if flag == 1:
                return HttpResponse('Ваши данные удалены')
            else:
                return HttpResponse('Неверный логин или пороль!')
        else:
            datadel = DelData()
            context3 = {'form3': datadel,
                        'errorpass': "Пороли не совпадают!"}
    else:
        datadel = DelData()
        context3 = {'form3': datadel}


    return render(request, 'wash.html', context3)
# Create your views here.

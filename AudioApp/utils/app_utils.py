from ..models import User, UserAnthropometry, SizeStandard

def saveuserdata(name, login, password, bust, waist, hips, sleeves):
    """Сохряняет пользвательские данные из регистрации на reg.html в БД"""
    us_id = 0
    usaut = User(name=name, login=login, password=password)
    usaut.save()
    for item in User.objects.all():
        if login == item.login:
            us_id = item.id
    usant = UserAnthropometry(bust=bust, waist=waist, hips=hips, sleeves=sleeves, name_id=us_id)
    usant.save()

def viewuserdata(request):
    """Создает славарь с пользовательскими данными"""
    login = request.POST.get('login')
    password = request.POST.get('password')

    datadict = {}
    us_id = 0
    for item in User.objects.all():
        if login == item.login and password == item.password:
            us_id = item.id
            for item1 in UserAnthropometry.objects.all():
                if item1.name_id == us_id:
                    datadict = {'name': item.name,
                                'bust': item1.bust,
                                'waist': item1.waist,
                                'hips': item1.hips,
                                'sleeves': item1.sleeves,
                                }

    return datadict

def resultsize(datadict):
    """Вычисляет размер по данным  пользователя и дововляет  в славарь"""
    bust = datadict['bust']
    hips = datadict['hips']

    for item in SizeStandard.objects.all():
        if bust == item.st_bust and hips == item.st_hips:
            datadict['international'] = item.international
            datadict['russian'] = item.russian
            datadict['england'] = item.england
            datadict['usa'] = item.usa
            datadict['europe'] = item.europe
            datadict['italy'] = item.italy
            datadict['japan'] = item.japan
            break
        elif bust > item.st_bust and hips > item.st_hips:
            datadict['international'] = item.international
            datadict['russian'] = item.russian
            datadict['england'] = item.england
            datadict['usa'] = item.usa
            datadict['europe'] = item.europe
            datadict['italy'] = item.italy
            datadict['japan'] = item.japan

    return datadict

def deluserdata(log, pas):
    """Удаление пользовательских данных"""
    flag = 0
    #  Поиск совпадений логина и пароля в БД и удаление данных,в том числе и данных в связаной БД
    for item in User.objects.all():
        if log == item.login and pas == item.password:
            us = User.objects.get(name=item.name)
            us.delete()
            flag = 1
    return flag

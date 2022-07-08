from django import forms


class UserAut(forms.Form):
    """Форма ввода логина пороля в home.html"""

    login = forms.CharField(max_length=33)
    password = forms.CharField(max_length=33, widget=forms.PasswordInput())



class UserReg(forms.Form):
    """Форма для регистрации и заполнения БД в reg.html"""
    name = forms.CharField(max_length=45)
    login = forms.CharField(max_length=33)
    password = forms.CharField(max_length=33)

    bust = forms.IntegerField()  # Обхват груди
    waist = forms.IntegerField()  # Обхват талии
    hips = forms.IntegerField()  # Обхват бедер
    sleeves = forms.IntegerField()  # Длина рукава


class DelData(forms.Form):
    """Форма для удаления данных"""
    login = forms.CharField(max_length=33)
    password = forms.CharField(max_length=33, widget=forms.PasswordInput())
    repeat_password = forms.CharField(max_length=33, widget=forms.PasswordInput())
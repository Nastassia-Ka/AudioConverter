
from django.db import models

class User(models.Model):
    """БД пользователя"""

    name = models.CharField(max_length=45)
    login = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=45)

    def __str__(self):
        return str(self.name) + ' ' + str(self.login)

class UserAnthropometry(models.Model):
    """Антропометрические характерисики пользователя"""

    name = models.ForeignKey(User, on_delete=models.CASCADE)
    bust = models.IntegerField() # Обхват груди
    waist = models.IntegerField() # Обхват талии
    hips = models.IntegerField() # Обхват бедер
    sleeves = models.IntegerField() # Длина рукава

    def __str__(self):
        return str(self.name)

class SizeStandard(models.Model):
    """Стандарты размеров"""

    st_bust = models.IntegerField()  # Обхват груди
    st_waist = models.IntegerField()  # Обхват талии
    st_hips = models.IntegerField()  # Обхват бедер
    st_sleeves = models.IntegerField()  # Длина рукава

    international = models.CharField(max_length=45) # Международные размеры
    russian = models.IntegerField() # Российские размеры
    england = models.CharField(max_length=45) # Размеры Англии
    usa = models.IntegerField() # Размеры США
    europe = models.IntegerField() # Европейские Размеры
    italy = models.CharField(max_length=45) # Размеры Италии
    japan = models.IntegerField() # Размеры Японии
    footnote = models.CharField(max_length=45, blank=True) # Примечания. Необязательное поле

    def __str__(self):
        return str(self.international)
# Create your models here.

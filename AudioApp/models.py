from django.db import models


class UserSong(models.Model):
    """Модель для загрузки песни"""
    title = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='audio_files/')

    def __str__(self):
        return str(self.audio_file) + str(self.title)


class AudioData(models.Model):
    """База данных для хранения данных о треках"""
    login = models.CharField(max_length=100, verbose_name='Имя пользователя')
    trek_name = models.CharField(max_length=100, verbose_name='Имя трека')
    original_format = models.CharField(max_length=100, verbose_name='Формат оригинала')
    original_track = models.CharField(max_length=100, verbose_name='Оригинальный трек')
    convertable_track = models.CharField(max_length=100, verbose_name='Сконвертированный трек')
    convertable_format = models.CharField(max_length=100, verbose_name='Формат сконвертированного трека')
    date = models.CharField(max_length=100, verbose_name='Дата конвертации')

    def __str__(self):
        return str(self.login)

    class Meta:
        """Настройки модели"""
        verbose_name = 'Трек пользователя'
        verbose_name_plural = 'Треки пользователя'
        ordering = ['date']
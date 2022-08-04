from django.apps import AppConfig


class AudioappConfig(AppConfig):
    """Настройка приложения"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AudioApp'
    verbose_name = 'Audio converter'

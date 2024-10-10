# your_app/apps.py
from django.apps import AppConfig


class YourAppConfig(AppConfig):
    name = 'your_app'

    def ready(self):
        import signals


class Task2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'task2'

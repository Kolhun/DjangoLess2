#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


# python manage.py runserver

# Создаем миграции с нашим приложением
# python manage.py makemigrations task1
# python manage.py migrate
# Создаем супер пользователя для работой с админкой
# python manage.py createsuperuser

# Создаем шелл с нашим проектом
# python manage.py shell (он выполняет код сразу через консоль, как вариант сделать отдельный .py и запустить там)

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'game_store.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

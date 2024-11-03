from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User


class Buyer(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Имя покупателя")
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'), verbose_name="Баланс")
    age = models.PositiveIntegerField(verbose_name="Возраст")

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name="Название игры")
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    size = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Размер файлов (ГБ)")
    description = models.TextField(verbose_name="Описание")
    age_limited = models.BooleanField(default=False, verbose_name="Возрастное ограничение 18+")
    buyers = models.ManyToManyField(Buyer, related_name='games', verbose_name="Покупатели")

    def __str__(self):
        return self.title


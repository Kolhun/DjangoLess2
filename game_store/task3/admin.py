from django.contrib import admin
from .models import Buyer, Game


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')
    search_fields = ('name',)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size', 'age_limited')
    search_fields = ('title',)
    filter_horizontal = ('buyers',)

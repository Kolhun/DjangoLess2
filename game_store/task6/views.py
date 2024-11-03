# task5/views.py

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .forms import UserRegister
from .models import Buyer, Game


def index(request):
    return render(request, 'six_task/index.html')

def profile(request):
    return render(request, 'six_task/post_list.html')

def blog_list(request):

    buyers = Buyer.objects.all().order_by('name')
    games = Game.objects.all().order_by('title')

    buyer_paginator = Paginator(buyers, 5)
    buyer_page_number = request.GET.get('buyer_page')
    buyer_page_obj = buyer_paginator.get_page(buyer_page_number)

    game_paginator = Paginator(games, 5)
    game_page_number = request.GET.get('game_page')
    game_page_obj = game_paginator.get_page(game_page_number)

    return render(request, 'six_task/post_list.html', {
        'buyer_page_obj': buyer_page_obj,
        'game_page_obj': game_page_obj,
    })
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseNotFound



def index(request):
    return HttpResponse("<h2>Мой сайт task4</h2>")


def games_view(request):
    return render(request, 'four_task/games_base.html')


def bucket_view(request):
    return render(request, 'four_task/bucket_base.html')

from django.urls import path
from . import views
from .views import *

#python mysite/manage.py runserver

urlpatterns = [
    path("", index),
    path('games/', views.games_view, name='games_view'),
    path('bucket/', views.bucket_view, name='bucket_view'),
    path('sign_up/', views.sign_up_by_django, name='sign_up_by_django'),
]
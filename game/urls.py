from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'game'

urlpatterns = [
  path('game', views.index, name='index'),
  path('game/games', views.game_list, name='game_list'),
]
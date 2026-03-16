from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'game'

urlpatterns = [
  path('', views.index, name='index'),
  path('game/games', views.student_list, name='student_list'),
]
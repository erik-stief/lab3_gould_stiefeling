from django.shortcuts import render

# Create your views here.
from .models import Game

def index(request):
    return render(request, 'game/index.html')

def game_list(request):
    games = Game.objects.all()
    return render(request, 'game/game_list.html', {'games': games})
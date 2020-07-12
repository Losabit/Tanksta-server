from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PlayerSerializer
from .serializers import GameSerializer
from .models import Player
from .models import Game


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all().order_by('pseudo')
    serializer_class = PlayerSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all().order_by('name')
    serializer_class = GameSerializer

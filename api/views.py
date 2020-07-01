from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PlayerSerializer
from .models import Player


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all().order_by('pseudo')
    serializer_class = PlayerSerializer

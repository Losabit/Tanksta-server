from django.contrib import admin
from .models import Player
from .models import Game

admin.site.register(Player)
admin.site.register(Game)
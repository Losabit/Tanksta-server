from rest_framework import serializers
from .models import Player
from .models import Game

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'pseudo', 'play_on', 'health', 'canon_orientation', 'puissance', 'shoot', 'pos_x', 'pos_y')

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'turn_id')
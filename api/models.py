from django.db import models

# Create your models here.
class Game(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    turn_id = models.IntegerField(null=True)
    players = models.IntegerField(default = 0)
    players_want_play = models.IntegerField(default = 0)

    def __str__(self):
        return self.name

class Player(models.Model):
    id = models.AutoField(primary_key=True)
    pseudo = models.CharField(max_length=20)
    play_on = models.IntegerField(null=True)
    health = models.IntegerField(null=True)
    canon_orientation = models.FloatField(null=True)
    puissance = models.FloatField(null=True)
    shoot = models.BooleanField(default = False, null=True)
    pos_x = models.FloatField(null=True)
    pos_y = models.FloatField(null=True)
    want_to_play = models.BooleanField(default = False)
    order = models.IntegerField(null=True)
    end_of_turn = models.BooleanField(default = False)

    def __str__(self):
        return self.pseudo

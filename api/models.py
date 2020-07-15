from django.db import models

# Create your models here.
class Game(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    turn_id = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Player(models.Model):
    id = models.AutoField(primary_key=True)
    pseudo = models.CharField(max_length=20)
    play_on = models.CharField(max_length=100, null=True)
    health = models.IntegerField(null=True)
    canon_orientation = models.FloatField(null=True)
    puissance = models.FloatField(null=True)
    shoot = models.IntegerField(null=True)
    pos_x = models.FloatField(null=True)
    pos_y = models.FloatField(null=True)


    def __str__(self):
        return self.pseudo

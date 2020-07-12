from django.db import models

# Create your models here.
class Game(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Player(models.Model):
    id = models.AutoField(primary_key=True)
    pseudo = models.CharField(max_length=20)
    play_on = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.pseudo
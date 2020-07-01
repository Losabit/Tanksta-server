from django.db import models

# Create your models here.
class Player(models.Model):
    token = models.CharField(max_length=100)
    pseudo = models.CharField(max_length=20)

    def __str__(self):
        return self.pseudo
# Generated by Django 3.0.8 on 2020-07-21 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='players',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='game',
            name='players_want_play',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='want_to_play',
            field=models.IntegerField(default=0),
        ),
    ]

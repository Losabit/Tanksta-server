# Generated by Django 3.0.8 on 2020-07-12 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200701_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='play_on',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
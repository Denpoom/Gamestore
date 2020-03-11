from distutils.text_file import TextFile
from numbers import Integral

from django.db import models
from django.contrib.auth.models import User


class Game_type(models.Model):
    game_type_id = models.CharField(max_length=255, primary_key=True)
    type_name = models.CharField(max_length=255)


class Game(models.Model):
    game_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    game_type_id = models.ForeignKey(Game_type, on_delete=models.PROTECT)
    developer = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)
    release_date = models.DateField()
    price = models.FloatField()


class User_games(models.Model):
    purchased_date = models.DateField(auto_now=True)
    serial = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.PROTECT)


class Image(models.Model):
    image_id = models.CharField(max_length=255, primary_key=True)
    game_id = models.ForeignKey(Game, on_delete=models.PROTECT)
    image_url = models.ImageField(upload_to='')
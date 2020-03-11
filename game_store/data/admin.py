from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import Game_type, Game, User_games, Image

# Register your models here.


class Game_typeadmin(admin.ModelAdmin):
    list_display = ['game_type_id', 'type_name']


admin.site.register(Game_type, Game_typeadmin)


class Gameadmin(admin.ModelAdmin):
    list_display = [
        'game_id', 'name', 'description', 'game_type_id', 'developer',
        'rating', 'release_date', 'price'
    ]


admin.site.register(Game, Gameadmin)


class User_gameadmin(admin.ModelAdmin):
    list_display = ['user_id', 'game_id', 'purchased_date', 'serial']


admin.site.register(User_games, User_gameadmin)


class Imageadmin(admin.ModelAdmin):
    list_display = ['image_id', 'game_id', 'image_url']


admin.site.register(Image, Imageadmin)
admin.site.register(Permission)
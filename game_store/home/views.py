from builtins import filter
from contextlib import redirect_stderr
from struct import error
from urllib import request

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from data.models import Game, Image


# Create your views here.
def home(request):
    game_action = Game.objects.filter(game_type_id=1)
    image_action = Image.objects.filter(game_id__game_type_id=1)

    game_adven = Game.objects.filter(game_type_id=2)
    image_adven = Image.objects.filter(game_id__game_type_id=2)

    game_sport = Game.objects.filter(game_type_id=3)
    image_sport = Image.objects.filter(game_id__game_type_id=3)

    game_rac = Game.objects.filter(game_type_id=4)
    image_rac = Image.objects.filter(game_id__game_type_id=4)

    return render(request,
                  'index.html',
                  context={
                      'games': game_action,
                      'images': image_action,
                      'games2': game_adven,
                      'images2': image_adven,
                      'games3': game_sport,
                      'images3': image_sport,
                      'games4': game_rac,
                      'images4': image_rac
                  })


def signup(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST.get('username'),
            password=request.POST.get('password'),
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'))
        # group = Group.objects.get(name='public')
        # user.groups.add(group)
        user.save()

        return render(request, 'login.html')

    return render(request, 'signup.html')


def my_login(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:

            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password!'

    return render(request, 'login.html', context=context)


def my_logout(request):
    logout(request)
    return redirect('login')


def allgame(request):
    game_type = request.POST.get('type')
    game = Game.objects.all()
    image = Image.objects.all()
    print(game_type)
    return render(request,
                  'allgame.html',
                  context={
                      'games': game,
                      'images': image,
                      'game_type': game_type
                  })


def details(request, game_id):
    context = {}
    game = Game.objects.filter(id=game_id)
    image = Image.objects.filter(game_id_id=game_id)

    context['game'] = game
    context['image'] = image

    return render(request, 'details.html', context=context)


def home_member(request):
    game = Game.objects.all()
    image = Image.objects.all()
    print(game)
    return render(request,
                  'index.html',
                  context={
                      'games': game,
                      'images': image
                  })


def details_member(request):
    return render(request, 'details.html')


def mygame(request):
    return render(request, 'mygame.html')

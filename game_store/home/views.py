import profile
import random
from builtins import filter, object
from contextlib import redirect_stderr
from os.path import isdir
from struct import error
from urllib import request

from astroid import context
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group, User
from django.shortcuts import redirect, render

from data.models import Game, Image, User_games


# Create your views here.
def home(request):
    # Game Action
    game_action = Game.objects.filter(game_type_id=1)
    image_action = Image.objects.filter(game_id__game_type_id=1)
    # Game Adven
    game_adven = Game.objects.filter(game_type_id=2)
    image_adven = Image.objects.filter(game_id__game_type_id=2)
    # Game Sport
    game_sport = Game.objects.filter(game_type_id=3)
    image_sport = Image.objects.filter(game_id__game_type_id=3)
    # Game Racing
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


    # สมัครสมาชิก
def signup(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST.get('username'),
            password=request.POST.get('password'),
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'))
        group = Group.objects.get(name='user')
        user.groups.add(group)
        user.save()
        return render(request, 'login.html')
    return render(request, 'signup.html')


    # login
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


# Filter
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


# รายละเอีนดเกม
def details(request, game_id):
    context = {}
    game = Game.objects.get(pk=game_id)
    image = Image.objects.get(game_id_id=game_id)

    context['game'] = game
    context['image'] = image
    return render(request, 'details.html', context=context)


#
@login_required
@permission_required('data.view_user_games')
def payment(request, game_id):
    context = {}
    game = Game.objects.get(pk=game_id)
    image = Image.objects.get(game_id_id=game_id)

    if request.method == 'POST':
        check = request.POST.get('cash')
        check2 = request.POST.get('credit')
        check3 = request.POST.get('airpay')

        print(check)
        if check == 'cash':
            context['cash'] = "cash"
        elif check2 == 'credit':
            context['credit'] = "credit"
        elif check3 == 'airpay':
            context['airpay'] = "airpay"

    context['game'] = game
    context['image'] = image
    return render(request, 'payment.html', context=context)


def buy_payment(request, game_id):
    user = request.user.id
    gameuser = User_games.objects.all()
    check = 0
    for i in gameuser:
        if i.game_id_id == game_id and i.user_id_id == user:
            check = 1
    if check == 1:
        return redirect('details', game_id)
    else:
        post = User_games(user_id_id=user,
                          game_id_id=game_id,
                          serial='%32x' % random.getrandbits(16 * 8))
        post.save()

        return redirect('home')


@login_required
@permission_required('data.view_user_games')
def mygame(request):
    user = request.user.id
    mygame = User_games.objects.filter(user_id=user)
    images = Image.objects.all()
    print(mygame)
    return render(request,
                  'mygame.html',
                  context={
                      'games': mygame,
                      'images': images
                  })


@login_required
@permission_required('data.view_user_games')
def profile(request):
    user = request.user
    return render(request, 'myprofile.html', context={'user': user})


@login_required
@permission_required('data.view_user_games')
def password(request):
    context = {}
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            print(request.user.username)
            user = User.objects.get(username=request.user.username)
            user.set_password(password1)
            user.save()

            return redirect('logout')
        else:
            context['password1'] = password1
            context['password2'] = password2
            context['error'] = "Password does't match!"

    return render(request, 'password.html', context=context)


#
@login_required
@permission_required('data.view_user_games')
def edit(request):
    if request.method == 'POST':
        user = request.user
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        update_data = User.objects.filter(id=user.id).update(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email)
        return redirect('profile')


def edit_profile(request):
    return render(request, 'editprofile.html')


@login_required
def game_user(request):
    return render(request, 'game.html')


# ค้นหาเกมหน้าhome
def search(request):
    search = request.POST.get('search', '')
    game_search = Game.objects.filter(name__icontains=search)

    image_search = Image.objects.all()
    context = {'game_search': game_search, 'image_search': image_search}
    return render(request, 'search.html', context=context)


# ค้นหาเกมหน้าคลังเกม
def search_mygame(request):
    search = request.POST.get('search', '')
    game_search = Game.objects.filter(name__icontains=search)

    image_search = Image.objects.all()

    context = {'game_search': game_search, 'image_search': image_search}

    return render(request, 'mysearch.html', context=context)


# Admin
@permission_required('data.change_game')
def admin(request):
    game = Game.objects.all()
    image = Image.objects.all()

    return render(request,
                  'admin.html',
                  context={
                      'games': game,
                      'images': image,
                  })


@login_required
@permission_required('data.change_game')
def edit_game(request, game_id):
    return render(request, 'home')


@login_required
@permission_required('data.change_game')
def edit_image(request, game_id):
    return render(request, 'home')


@permission_required('data.change_game')
def add_game(request):
    return render(request, '')
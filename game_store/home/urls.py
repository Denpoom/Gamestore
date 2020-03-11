"""game_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    # User
    path('', views.home, name='home'),
    path('login/', views.my_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.my_logout, name='logout'),
    path('allgame/', views.allgame, name='allgame'),
    path('search/', views.search, name='search'),
    # Member
    path('<int:game_id>/', views.details, name='details'),
    path('payment/<int:game_id>/', views.payment, name='payment'),
    path('payment1/<int:game_id>/', views.buy_payment, name='buy_payment'),
    path('editprofile/', views.edit_profile, name='edit_profile'),
    path('password/', views.password, name='password'),
    path('profile/', views.profile, name='profile'),
    path('game_user/', views.game_user, name='game_user'),
    path('mygame/', views.mygame, name='mygame'),
    path('edit/', views.edit, name='edit'),
    # Admin
    path('Admin/', views.admin, name='admin'),
    path('admin/data/game/add/', views.add_game, name='add_game'),
    path('admin/data/game/<int:game_id>/change/',
         views.edit_game,
         name='edit_game'),
    path('admin/data/image/<int:game_id>/change/',
         views.edit_game,
         name='edit_image'),
]

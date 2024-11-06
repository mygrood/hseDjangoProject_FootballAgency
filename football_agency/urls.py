from django.urls import path
from . import views

urlpatterns = [
    path('teams/', views.team_list, name='team_list'),
    path('teams/create/', views.create_team, name='create_team'),
    path('players/', views.player_list, name='player_list'),
    path('players/create/', views.create_player, name='create_player'),
]

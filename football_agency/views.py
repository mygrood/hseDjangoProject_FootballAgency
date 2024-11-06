# football_agency/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Team, Player
from .forms import TeamForm, PlayerForm


# Создание команды
def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('team_list')
    else:
        form = TeamForm()
    return render(request, 'football_agency/create_team.html', {'form': form})

# Создание игрока
def create_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerForm()
    return render(request, 'football_agency/create_player.html', {'form': form})

# Отображение списка команд
def team_list(request):
    teams = Team.objects.all()
    return render(request, 'football_agency/team_list.html', {'teams': teams})

# Отображение списка игроков
def player_list(request):
    players = Player.objects.all()
    return render(request, 'football_agency/player_list.html', {'players': players})

# Функция для отображения деталей игрока
def player_detail(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    return render(request, 'football_agency/player_detail.html', {'player': player})
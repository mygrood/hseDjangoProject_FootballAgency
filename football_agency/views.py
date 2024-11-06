# football_agency/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Team, Player
from .forms import TeamForm, PlayerForm

#ДОМАШНЯЯ СТРАНИЦА
def home(request):
    return render(request, 'football_agency/home.html')

# СОЗДАНИЕ КОМАНДЫ
def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('team_list')
    else:
        form = TeamForm()
    return render(request, 'football_agency/create_team.html', {'form': form})

# СОЗДАНИЕ ИГРОКА
def create_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerForm()
    return render(request, 'football_agency/create_player.html', {'form': form})

# СПИСОК КОМАНД
def team_list(request):
    teams = Team.objects.all()
    return render(request, 'football_agency/team_list.html', {'teams': teams})

# СПИСОК ИГРОКОВ
def player_list(request):
    players = Player.objects.all()
    teams = Team.objects.all()

    #параметры
    sort = request.GET.get('sort', 'id')  # по умолчанию сортируем по 'id'
    direction = request.GET.get('direction', 'asc')  # по умолчанию - по возрастанию
    team = request.GET.get('team')
    search = request.GET.get('search', '')

    if team:
        players = players.filter(id_team__id=team)

    if search:
        players = players.filter(surname__icontains=search)

    if direction == 'desc':
        sort = f'-{sort}'


    players = players.order_by(sort)

    return render(request, 'football_agency/player_list.html', {
        'players': players,
        'teams': teams,
    })

# ПОДРОБНОСТИ ОБ ИГРОКЕ
def player_detail(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    return render(request, 'football_agency/player_detail.html', {'player': player})
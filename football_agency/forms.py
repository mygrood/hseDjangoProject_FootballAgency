from django import forms
from .models import Team, Player

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team_name', 'country', 'team_image']

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'surname', 'age', 'nation', 'position', 'rating', 'potential', 'mood', 'id_team', 'player_image']

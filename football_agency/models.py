# football_agency/models.py
from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    team_image = models.ImageField(upload_to='team_images/', null=True, blank=True)

    def __str__(self):
        return self.team_name

class Player(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    nation = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    rating = models.IntegerField()
    potential = models.IntegerField()
    mood = models.IntegerField()
    player_image = models.ImageField(upload_to='player_images/', null=True, blank=True)
    id_team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

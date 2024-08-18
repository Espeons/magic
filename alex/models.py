

from django.contrib.auth.models import User
from django.db import models

from home.models import Player


# Create your models here.



class Deck(models.Model):

    name = models.CharField(max_length=50)
    commander = models.CharField(max_length=50)
    power_level = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile = models.ImageField(upload_to='trainers/', null=True)
    players = models.ForeignKey(Player, on_delete=models.CASCADE, null=True)
    link =models.URLField(max_length=200, null=True)
    

    def __str__(self):
        return f'{self.name}'



class Card(models.Model):

    type_options = (
        ('creature','Creature'),
        ('instant','Instant'),
        ('sorcery', 'Sorcery'),
        ('artifact', 'Artifact'),
        ('enchantment', 'Enchantment'),
        ('battle', 'Battle'),
        ('planeswalker', 'Planeswalker'),

    )

    name = models.CharField(max_length=50)
    power = models.IntegerField(blank=True, null=True)
    toughness = models.IntegerField(blank=True, null=True)
    card_type = models.CharField(max_length=50, choices=type_options)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, null=True)
    profile = models.ImageField(upload_to='cards/', null=True)
    points = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'








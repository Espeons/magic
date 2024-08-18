
import django_filters
from django import forms

from alex.models import Deck, Card


class CardFilter(django_filters.FilterSet):

    name = django_filters.CharFilter(lookup_expr='icontains', label ='Card name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter first name'}))
    power = django_filters.NumberFilter(label='Power', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the card power'}))
    toughness = django_filters.NumberFilter(label='Toughness', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the card toughness'}))

    # deck = django_filters.ChoiceFilter(widget=forms.RadioSelect(), choices=[(deck.id, deck) for deck in Deck.objects.filter(active=True)])

    points = django_filters.NumberFilter(label='Points', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the cards points'}))



    class Meta:
        model = Card
        fields = ['name', 'power', 'toughness', 'deck', 'points']


class DeckFilter(django_filters.FilterSet):

    name = django_filters.CharFilter(lookup_expr='icontains', label ='Deck name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the deck name'}))
    commander = django_filters.CharFilter(lookup_expr='icontains', label ='Commander name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the commander name'}))
    power_level = django_filters.NumberFilter(label='Power', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the deck power'}))

    class Meta:
        model = Deck
        fields = ['name', 'commander', 'power_level', 'players']
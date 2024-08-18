from django import forms
from django.forms import TextInput, EmailInput, NumberInput, DateInput, Select
from alex.models import Deck, Card

class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck

        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Please enter deck name', 'class': 'form-control'}),
            'commander': TextInput(attrs={'placeholder': 'Please the commanders name', 'class': 'form-control'}),
            'power_level': NumberInput(attrs={'placeholder': 'Please enter the power level of the deck', 'class': 'form-control'}),
            'players': Select(attrs={'class': 'form-select'}),

        }




class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        # exclude = ['first_name']  -> il folosim pt a exclude anumite fielduri din formular / TREBUIE CA IN MODELS.PY SA AVETI BLANK= TRUE SI NULL=TRUE
        fields = '__all__'  # specificam fieldurile dorite in formular
        # fields = ['first_name', 'last_name']

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Please enter the card name', 'class': 'form-control'}),
            'power': NumberInput(attrs={'placeholder': 'Please enter the card power', 'class': 'form-control'}),
            'toughness': NumberInput(attrs={'placeholder': 'Please enter the card toughness', 'class': 'form-control'}),
            'card_type': Select(attrs={'class': 'form-select'}),

            'points': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the card points'}),
        }

    # Atunci cand creati sau personalizati un formular in Django puteti sa implementati validari personalizate
    # care se va aplica pe intregul formular

    # Aceasta metoda este folosita pentru a verifica corectitudinea datelor introduse de utilizator
    # inainte de fi procesate sau salve in baza de date

    def clean(self):
        cleaned_data = super().clean()  # se obtine access la informatiile din formular intr-un dictionar
        print(cleaned_data)

        return cleaned_data

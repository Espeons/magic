from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView

from alex.filters import DeckFilter,CardFilter
from alex.forms import DeckForm, CardForm
from alex.models import Deck,  Card
from django.urls import reverse_lazy

class DeckCreateView(CreateView):
    template_name = 'deck/create_deck.html'  # randam un template dorit in care se va regasi formularul
    model = Deck  # modelului asociat formularului
    form_class = DeckForm
    success_url = reverse_lazy('homepage')


class DeckListView(ListView):
    template_name = 'deck/list_of_decks.html'
    model = Deck
    context_object_name = 'all_decks'

    def get_queryset(self):
        return Deck.objects.filter()

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        decks = Deck.objects.filter()
        myFilter = DeckFilter(self.request.GET, queryset=decks)
        decks = myFilter.qs
        data['all_decks'] = decks
        data['filters'] = myFilter.form
        return data



class DeckDetailView(DetailView):
    template_name = 'deck/details_deck.html'
    model = Deck

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cards'] = Card.objects.filter(deck=self.object)
        return context


class CardCreateView(CreateView):
    template_name = 'card/create_card.html' # randam un template dorit in care se va regasi formularul
    model = Card # modelului asociat formularului
    form_class = CardForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        # Customizarea first_name si last_name pentru a le salva sub forma unui title()
        new_card = form.save(commit=False)
        new_card.name = new_card.name.title()
        new_card.save()




        return redirect('homepage')



class CardListView(ListView):
    template_name = 'card/list_of_cards.html'
    model = Card
    context_object_name = 'all_cards'


    def get_queryset(self):
        return Card.objects.filter()

    # Metoda get_context_data() este o metoda folosita in clase de view-uei (ListView, UpdateView, CreateView etc) pentru
    # a obtine si a pregati datele necesare pentru a fi afisate in template-ul ascociat.

    # Metoda este utilizata pentru a furnica contextul necesar pentru template pentru a afisa corect informatiile

    # Cand apelam get_context_data se obtine un dictionar de date pe care il trimitem in template, iar programatori pot
    # suplimenta cu informatii noi acel dictionar.
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        cards = Card.objects.filter()
        myFilter = CardFilter(self.request.GET, queryset=cards)
        cards = myFilter.qs
        data['all_cards'] = cards
        data['filters'] = myFilter.form
        return data


def get_all_cards_per_deck(request, pk):
    card_per_deck = Card.objects.filter(deck_id=pk)

    return render(request, 'card/list_of_cards.html', {'all_cards': card_per_deck})
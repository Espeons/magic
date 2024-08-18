from django.urls import path

from alex import views


urlpatterns = [
    path('create_card/', views.CardCreateView.as_view(), name='create-card'),
    path('list_cards/', views.CardListView.as_view(), name='list-cards'),
    path('create_deck/', views.DeckCreateView.as_view(), name='create-deck'),
    path('list_decks/', views.DeckListView.as_view(), name='list-decks'),
    path('details_deck/<int:pk>/', views.DeckDetailView.as_view(), name='details-deck'),
]
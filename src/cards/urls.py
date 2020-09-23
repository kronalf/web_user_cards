from django.urls import path
from . import views

urlpatterns = [
    path('get_cards/', views.get_cards, name='get_cards'),
    path('add_cards/', views.add_cards, name='add_cards'),
    path('search_cards/', views.search_cards, name='search_cards'),
]
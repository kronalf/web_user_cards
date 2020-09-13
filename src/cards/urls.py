from django.urls import path
from . import views

urlpatterns = [
    path('get_cards', views.get_cards),
    path('add_cards', views.add_cards),
]
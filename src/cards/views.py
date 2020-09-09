from django.shortcuts import render
from .models import Person

def get_cards(request):
    qs = Person.objects.all()
    return render(request, 'cards/get_cards.html', {'object_list' : qs})

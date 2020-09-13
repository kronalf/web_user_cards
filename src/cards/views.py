from django.shortcuts import render
from .models import Person, Department
from .utils import pswd_generate, login_generate

def get_cards(request):
    qs = Person.objects.all()
    return render(request, 'cards/get_cards.html', {'object_list' : qs})

def add_cards(request):
    d = Department.objects.all()

    if request.GET:
        pass
    if request.POST:
        qs = request.POST
        first_name = qs['first_name']
        last_name = qs['last_name']
        other_name = qs['other_name']
        full_name = last_name + ' ' + first_name + ' ' + other_name
        position = qs['position']
        department = qs['department']
        number_room = qs['number_room']
        password = pswd_generate()
        login = login_generate(last_name, first_name, other_name)
        email = login + '@minudo.ru'
        floor = number_room[0]
        print(full_name, login, email, password, floor)

    return render(request, 'cards/add_cards.html', {'object_list' : d})

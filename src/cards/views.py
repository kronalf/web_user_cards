from django.db import DatabaseError
from django.shortcuts import render
from .models import Person, Department, Floor
from .utils import pswd_generate, login_generate

def get_cards(request):
    qs = Person.objects.all()
    return render(request, 'cards/get_cards.html', {'object_list' : qs})

def add_cards(request):
    qs = request.POST
    person = {}
    password = pswd_generate()
    d = Department.objects.all()

    if request.GET:
        pass
    if request.POST:
        department = Department.objects.filter(name=qs['department']).first()
        login = login_generate(qs['last_name'].strip(),
                               qs['first_name'].strip(),
                               qs['other_name'].strip())
        email = login + '@minudo.ru'
        # n = qs['number_room'][0]
        floor = Floor.objects.filter(number=qs['number_room'][0]).first()
        person = {'first_name' : qs['first_name'].strip(),
                  'last_name' : qs['last_name'].strip(),
                  'other_name' : qs['other_name'].strip(),
                  'full_name' : qs['last_name'] + ' ' + qs['first_name'] + ' ' + qs['other_name'],
                  'position' : qs['position'].strip(),
                  'number_room' : qs['number_room'].strip(),
                  'password' : password,
                  'login' : login,
                  'email' : email}
        p = Person(**person, department=department, floor=floor)
        try:
            p.save()
        except DatabaseError:
            pass
        print(person)

    return render(request, 'cards/add_cards.html', {'object_list' : d})
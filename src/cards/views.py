from django.db import DatabaseError
from django.shortcuts import render
from .models import Person, Department, Floor
from .utils import pswd_generate, login_generate

def get_cards(request):
    qs = Person.objects.all()
    return render(request, 'cards/get_cards.html', {'object_list' : qs})

def add_cards(request):
    person = {}
    d = Department.objects.all()
    qs = request.POST
    if qs:
        department = Department.objects.filter(name=qs['department']).first()
        floor = Floor.objects.filter(number=qs['number_room'][0]).first()
        person = {'first_name' : qs['first_name'],
                  'last_name' : qs['last_name'],
                  'other_name' : qs['other_name'],
                  'full_name' : qs['last_name'] + ' ' + qs['first_name'] + ' ' + qs['other_name'],
                  'position' : qs['position'],
                  'number_room' : qs['number_room'],
                  'password' : pswd_generate(),
                  'login' : login_generate(qs['last_name'],
                                           qs['first_name'],
                                           qs['other_name']),
                  'email' : login_generate(qs['last_name'],
                                           qs['first_name'],
                                           qs['other_name']) + '@minudo.ru'}
        p = Person(**person, department=department, floor=floor)
        try:
            p.save()
        except DatabaseError:
            pass


    return render(request, 'cards/add_cards.html', {'object_list' : d})

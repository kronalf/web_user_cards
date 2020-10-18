from django.db import DatabaseError
from django.shortcuts import render
from .models import Person, Department, Floor
from .utils import pswd_generate, login_generate, file_import


def get_cards(request):
    full_name = request.GET.get('full_name')
    qs = Person.objects.all()
    if full_name:
        full_name = full_name.strip()
        full_name = full_name.upper()
        _filter = {'full_name__contains': full_name}
        qs = Person.objects.filter(**_filter)
        return render(request, 'cards/get_cards.html',
                      {'object_list': qs})
    else:
        if qs:
            return render(request, 'cards/get_cards.html', {'object_list': qs})
        else:
            return render(request, 'cards/get_cards.html')

# def search_cards(request):
#     full_name = request.GET.get('full_name')
#     _filter = {'full_name__contains': full_name}
#     qs = Person.objects.filter(**_filter)
#     return render(request, 'cards/search_cards.html',
#                   {'object_list': qs})


def add_cards(request):
    qs = request.POST
    d = Department.objects.all()

    if request.GET:
        pass
    if qs:
        first_name = qs['first_name'].strip()
        last_name = qs['last_name'].strip()
        other_name = qs['other_name'].strip()
        full_name = last_name + ' ' + first_name + ' ' + other_name
        login = login_generate(last_name, first_name, other_name)
        email = login + '@minudo.ru'
        department = Department.objects.filter(name=qs['department']).first()
        floor = Floor.objects.filter(number=qs['number_room'][0]).first()
        password = pswd_generate()
        person = {'first_name': first_name,
                  'last_name': last_name,
                  'other_name': other_name,
                  'full_name': full_name,
                  'position': qs['position'].strip(),
                  'department': department,
                  'number_room': qs['number_room'],
                  'password': password,
                  'login': login,
                  'email': email,
                  'floor': floor}
        p = Person(**person)
        try:
            p.save()
            return render(request, 'cards/get_cards.html',
                          {'object_list': Person.objects.filter(login=login)})
        except DatabaseError:
            pass
    return render(request, 'cards/add_cards.html', {'object_list': d})

def edit_card(request, full_name):
    try:
        card = Person.objects.get(name=full_name).first()
    except Person.DoesNotExist:
        pass
    return render(request, 'cards/get_cards.html',
                  {'object_list': Person.objects.filter(login=login)})

def load_users(request):
    # set_department = set()
    qs = Person.objects.all()
    # list_users = file_import('cards/Persons_final.csv')
#Блок для импорта Подразделений в модель Department
    # for d in list_users:
    #     set_department.add(d['department'])
    #     # if d['department'] not in unique_department:
    #     #     unique_department.append(d['department'])
    # # for item in unique_department:
    # for item in set_department:
    #     d = Department(name=item)
    #     try:
    #         d.save()
    #     except DatabaseError:
    #         pass
#Блок для импорта Пользователей в модель Person
    # user ={}
    # for lu in list_users:
    #     user['department'] = Department.objects.filter(name=lu['department']).first()
    #     user['full_name'] = lu['full_name']
    #     user['position'] = lu['position']
    #     user['password'] = lu['password']
    #     user['login'] = lu['login']
    #     user['email'] = lu['email']
    #     user['floor'] = Floor.objects.filter(number=1).first()
    #     person = Person(**user)
    #     try:
    #         person.save()
    #     except DatabaseError:
    #         print('Error!!!')
    return render(request, 'cards/get_cards.html', {'object_list': qs})
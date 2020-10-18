import random
from .models import Person

cyrillic_letters = {
    'а':'a',
    'б':'b',
    'в':'v',
    'г':'g',
    'д':'d',
    'е':'e',
    'ё':'e',
    'ж':'zh',
    'з':'z',
    'и':'i',
    'й':'i',
    'к':'k',
    'л':'l',
    'м':'m',
    'н':'n',
    'о':'o',
    'п':'p',
    'р':'r',
    'с':'s',
    'т':'t',
    'у':'u',
    'ф':'f',
    'х':'h',
    'ц':'c',
    'ч':'cz',
    'ш':'sh',
    'щ':'sch',
    'ъ':'',
    'ы':'y',
    'ь':'',
    'э':'e',
    'ю':'yu',
    'я':'ya'
    }

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyz' \
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def from_cyrillic_to_eng(text: str):
    text = text.replace(' ', '_').lower()
    tmp =''
    for ch in text:
        tmp += cyrillic_letters.get(ch, ch)
    return tmp

def pswd_generate():
    pswd = ''
    for i in range(8):
        pswd += random.choice(chars)
    return pswd

def login_generate(first_name: str, last_name: str, other_name: str):
    login = from_cyrillic_to_eng(first_name).lower() + '_' + from_cyrillic_to_eng(last_name)[0:1].lower()
    if other_name:
        login += from_cyrillic_to_eng(other_name)[0:1].lower()
    else:
        login += 'x'
    return login

def file_import(name_file):
    list_user = []
    user = []

    with open(name_file, 'r') as file:
        for line in file:
            card = line.split(';;')
            card = list(filter(None, card))
            info_dict = {}
            for user_info in card[1:]:
                user_info = user_info.split(';')
                user.append(user_info)
            for info in user:
                if len(info) < 2:
                    info.append('')
                if 'Подразделение' in info:
                    info_dict['department'] = info[1]
                elif 'Должность' in info:
                    info_dict['position'] = info[1]
                elif 'Ф.И.О.' in info:
                    info_dict['full_name'] = info[1]
                elif 'Пароль' in info:
                    info_dict['password'] = info[1]
                elif 'Имя для входя в сеть' in info:
                    info_dict['login'] = info[1]
                elif 'E-mail' in info:
                    info_dict['email'] = info[1]
            list_user.append(info_dict)
    return list_user

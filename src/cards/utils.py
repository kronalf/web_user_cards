import random

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

chars = '!&$#?@abcdefghijklnopqrstuvwxyz' \
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
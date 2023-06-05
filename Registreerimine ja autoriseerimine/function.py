import random
import re

def username(n: str, l: list):
    """
    Ищет логин в списке, если находит, то возвращает истину (True).
    Если не находит, то возвращает ложное значение (False).
    """
    if n in l:
        t = True
    else:
        t = False
    return t


def auto_pass():
    """
    Функция, которая генерирует пароли автоматически.
    """
    str0 = "$@^=.,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3
    ls = list(str4)
    random.shuffle(ls)
    # Извлекаем из списка 12 произвольных значений
    password = ''.join([random.choice(ls) for x in range(12)])
    # Сгенирированный автоматически пароль, выводится строчкой ниже
    print(f'Ваш пароль: {password}')
    return password


def my_pass():
    """
    Функция дает создать пароль самому.
    Затем проверяет пароль на наличие цифр, малених и больших букв, спецсимволов.
    """
    print("Пароль должен состоять минимум из 8 символов, иметь мин. 1 цифру, 1 большую и маленькую букву и 1 спецсимвол")

    i = 0
    while True:
        password = input('Введите пароль:')
               
        if len(password) < 8:
            print('Пароль должен состоять минимум из 8 символов')
        elif re.search('[0-9]', password) is None:
            print('В пароле нет цифр')
        elif re.search('[a-z]', password) is None:
            print('В пароле нет букв в нижнем регистре')
        elif re.search('[A-Z]', password) is None:
            print('В пароле нет букв в верхнем регистре')
        elif re.search('[$@^=.,:;!_*-+()/#¤%&]', password) is None:
            print('В пароле нет спецсимволов')
        else:
            print('Ваш пароль надежный')
            break

    return password

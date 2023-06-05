from function import*


def reg(login_list:list, pass_list:list):   
    """
    Регистрация новых пользователей,
    Записывает в списки логины и пароли.
    """
    print('\n* Регистрация *'.center(24, ))

    n = input('\nВведите логин: ')
    u = username(n, login_list)
    i = 0
    while u == True:
        n = input('Такой логин уже существует.\nВведите еще раз: ')
        u = username(n, login_list)
        i += 1
        if i > 1:
            print("Хотите завершить регистрацию? Напишите 1")
            if n == '1':
                print('Завершаем..')
                return


    v = input('Создать пароль автоматически или нет? 1/0: ')
    if v == '1':
        p = auto_pass()
    else:
        p = my_pass()

    login_list.append(n)
    pass_list.append(p)
    print('\nРегистрация завершена'.center(33, )) 
    


def author(login_list:list, pass_list:list):
    '''
    Авторизирует пользователей, которые содержатся в списках.
    '''
    n = input('Введите логин: ')
    u = username(n, login_list)
    if u == True:
        login = login_list.index(n)
        n = input('Введите пароль: ')
        if pass_list[login] == n:
            return True
        else:
            print('--- Неправильный пароль ---')
            return False
    else:
        print('--- Неправильный логин ---')
        return False
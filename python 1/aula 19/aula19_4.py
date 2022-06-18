login = input('login: ')
gender = input('genero: ')

if login == 'user':
    if gender == 'masculino':
        print('ola usuario')
    else:
        print('ola usuaria')
elif login == 'adm':
    if gender == 'masculino':
        print('ola administrador')
    else:
        print('ola administradora')
elif login == 'quest':
    print('ola visitante')
else:
    print('ola desconhecido(a)')

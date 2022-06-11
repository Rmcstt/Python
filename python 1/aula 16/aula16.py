id_user = input('digite o numero de usuario: ')


if id_user.isdigit():
    id_user = int(id_user)

    if id_user % 2 == 0:
        print(f'the {id_user} is pair')
    else:
        print(f'the {id_user} is not a pair')
else:
    print(f'the {id_user} is not a number int')
# apesar de ter funcionado ele diz que os numeros negativos nao sao inteiros
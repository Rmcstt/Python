id_user = input('digite o numero de usuario: ')


if id_user.isnumeric():  # isnumeric() verifica se o valor é um numero
    id_user = int(id_user)  # int() converte o valor para inteiro

    if id_user % 2 == 0:  # % é o operador de resto da divisao
        print(f'the {id_user} is pair')  # the 2 is pair
    else:
        print(f'the {id_user} is not a pair')  # the 3 is not a pair
else:
    print(f'the {id_user} is not a number int')  # the 3 is not a number int
# apesar de ter funcionado ele diz que os numeros negativos nao sao inteiros
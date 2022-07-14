def func(*args):
    print(args)  # os argumentos
    print(args[0])  # o primeiro
    print(args[-1])  # o ultimo
    print(len(args))  # quantidade de args


func(1, 2, 3, 4, 5)


def func2(*args):
    args = list(args)  # transforma a tupla em uma lista
    args[0] = 20
    print(args)


func2(3, 4, 5, 6, 7, 8)


def func3(*args):
    for v in args:
        print(v)  # a cada volta do laço mostra um valor de args


func3(1, 2, 3, 4, 5)


def func4(*args, **kwargs):
    print(args)
    print(kwargs['nome'], kwargs['sobrenome'])  # argumentos nomeados

    nome = kwargs.get('nome')  # ideal para fazer checagens

    print(nome)
    idade = kwargs.get('idade')
    print(idade)

    if idade is not None:
        print(f'{nome} tem {idade} anos de idade')
    else:
        print('idade nao existe')


lista = [1, 2, 3, 4, 5]
lista2 = [11, 12, 13, 14, 15]
func4(*lista, '6', 7, 8, 9, 10, *lista2,
      nome='renato', sobrenome='mota', idade=26)

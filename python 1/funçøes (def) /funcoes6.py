"""
Funções (def) em Python - *args  **kwags -
"""


from ast import arg


def func(a1, a2, a3, a4, a5, nome=None, a6=None):
    print(a1, a2, a3, a4, a5, nome, a6)
    return nome, a6


var = func(1, 2, 3, 4, 5, nome='renato', a6='5')
print(var[0], var[1])
#################


def func2(*args):
    print(args)


lista = [1, 2, 3, 4, 5]
n1, n2, *n = lista
print(n1, n2, n)

# "*"pega a lista inteira e o "sep" serve para colocar um separador
print(*lista, sep='-')

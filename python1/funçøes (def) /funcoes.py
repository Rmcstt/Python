"""
funções - def em Python (parte 1)
"""


def funcao(x, y):
    print(x+y)


funcao(2, 3)  # 5


def saudacao(msg='ola', nome='user'):  # vallores padrao
    print(msg, nome)


saudacao()  # ola user
saudacao("oie", "renato")  # oie renato


def troca(nome='coder'):
    nome = nome.replace('e', '3')
    return f'{nome}'


variavel = troca()


print(variavel)  # cod3r

"""
Funcoes (def) em Python - return 
"""


def funcao(var):
    return var  # return é recomendado,  nao deixa nada ser executado abaixo
    print(' isso nao ser executado')


variavel = funcao('valor que eu quero')

if variavel:
    print(variavel)
else:
    print('nenhum valor')

"""
formatando valores em codificadores

: s - texto (strings)
: d - inteiros (int)
: f - numeros de ponto flutuante
: (numero)f - quantidade de casas decimais (float)
:(caractere)(> ou < ou ^) (quantidade)(tipo - s, d ou f)

> - esquerda
< - direita
^ - centro
"""

"""
num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print(f'{divisao:.2f}')
"""

"""num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1250
print(f'{num_2:0>10}')
print(f'{num_2:0>10.2f}')

nome = 'renato mota'

print(50 - len(nome))

print(f'{nome:#^50}')"""


"""nome = 'renato'
sobrenome = 'mota'
nome_formatado = '{0:$^50} {1:#^50}'.format(nome, sobrenome)
print(nome_formatado)"""

"""nome = 'renato mota'
nome = nome.ljust(20, '$')
print(nome)"""


nome = input('digite o nome: ')
print(nome.lower())
print(nome.upper())
print(nome.title())

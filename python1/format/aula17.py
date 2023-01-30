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


num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print(f'{divisao:.2f}')  # 3.33


num_3 = 1
print(f'{num_3:0>10}')  # 0000000001

num_4 = 1250
print(f'{num_4:0>10}')  # 00001250
print(f'{num_4:0>10.2f}')  # 0001250.00

nome1 = 'renato mota'

print(50 - len(nome1))  # 39

print(f'{nome1:#^50}')  ####################renato mota####################


nome2 = 'renato'
sobrenome = 'mota'
nome_formatado = '{0:$^50} {1:#^50}'.format(nome2, sobrenome)  
print(nome_formatado)  # $$$$$$$$$$$$$$$$$$$$$$renato$$$$$$$$$$$$$$$$$$$$$$ #######################mota#######################

nome3 = 'renato mota'
nome3 = nome3.ljust(20, '$')  # ljust() - esquerda
print(nome3)  #renato mota$$$$$$$$$


nome = input('digite o nome: ')
print(nome.lower())  # converte para minusculo
print(nome.upper())  # converte para maiusculo
print(nome.title())  # converte para maiusculo e a primeira letra de cada palavra

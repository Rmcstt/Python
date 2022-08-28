"""
composição é a relação inde a classe faz parte de outra classe

se uma for apagada... a outra automaticamente é apagada
"""

from classes import Cliente, Endereco

cliente1 = Cliente('renato', 26)
cliente1.inserir_endereco('são paulo', 'sp')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()

cliente2 = Cliente('joão', 32)
cliente2.inserir_endereco('rio de janeiro', 'rj')
cliente2.inserir_endereco('salvador', 'ba')
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2
print()

cliente3 = Cliente('maria', 45)
cliente3.inserir_endereco('salvador', 'ba')
print(cliente3.nome)
cliente3.lista_enderecos()
del cliente3
print()

cliente4 = Cliente('jose', 19)
cliente4.inserir_endereco('curitiba', 'pr')
print(cliente4.nome)
cliente4.lista_enderecos()
del cliente4
print()

print('###############################################')


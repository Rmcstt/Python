"""
geradores e itaradores sao consumiveis, ou seja, depois de ter uum gerador oou um itarador eles nao podem ser usados novamente
"""

nome = 'renato mota'
iterador = iter(nome)  # cria um iterador
gerador = (letra for letra in nome)  # cria um gerador

print(next(gerador))  # r
print(next(gerador))  # e
print(next(gerador))  # n
print(next(gerador))  # a

print('*for a partir daqui')

for letra in gerador:  # percorre o gerador(resto)
  print(letra)  

print('outro for')  

for letra in gerador:  # nao percorre pois acabou o gerador
  print(letra)  

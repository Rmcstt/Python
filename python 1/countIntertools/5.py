from itertools import count

contador = count(+1)
lista = ['luiz','joao','maria','jose','pedro','juma','jiripoca','jacu','jesuino']
lista = zip(contador, lista)
print(list(lista))
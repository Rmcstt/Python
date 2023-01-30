import sys
import time

def gera():  # cria um generator com valores de 1 a 1000000
  for n in range(100):  # cria uma lista com valores de 1 a 1000000
    yield n   # yield retorna o valor de n e pausa o generator
    time.sleep(0.1)  # adiciona um valor a cada 0.1 segundos

g = gera()  # cria um generator com valores de 1 a 1000000

for v in g:  # percorre a lista
  print(v)  # imprime o valor da lista

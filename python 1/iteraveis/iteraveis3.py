import sys
import time

def geraLista():  # cria uma lista com valores de 1 a 1000000
  r = []  # cria uma lista vazia
  for n in range(100):  # cria uma lista com valores de 1 a 1000000
    r.append(n)  # adiciona o valor n a lista
    time.sleep(0.1)  # adiciona um valor a cada 0.1 segundos
  return r  # retorna a lista

g = geraLista()  # cria um generator com valores de 1 a 1000000

for v in g:  # percorre a lista
  print(v)  # imprime o valor da lista

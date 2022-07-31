import sys
import time
def gera():
  variavel = 'valor1'  # cria uma variavel com valor1
  yield variavel  # yield retorna o valor de variavel e pausa o generator
  variavel = 'valor2'  # cria uma variavel com valor2
  yield variavel  
  variavel = 'valor3'
  yield variavel

g = gera()  # cria um generator com valores de 1 a 1000000

print(next(g))  # imprime o valor de variavel
print(next(g))  
print(next(g))
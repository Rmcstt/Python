import sys
import time
def gera():
  variavel = 'valor1'
  yield variavel
  variavel = 'valor2'
  yield variavel
  variavel = 'valor3'
  yield variavel

g = gera()

print(next(g))
print(next(g))
print(next(g))
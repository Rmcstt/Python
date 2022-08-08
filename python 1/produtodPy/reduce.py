from produtos import pessoas, produtos, lista  # importação de produtos.py
from functools import reduce  # importação de funções de reduce

acumula = 0

for x in lista:
  acumula +=x

print(acumula)  # imprime a soma de todos os elementos da lista


import sys  # importa o modulo sys
import time  # importa o modulo time

l1 = [x for x in range(1000000)]  # cria uma lista com valores de 1 a 1000000
l2 = (x for x in range(1000000))  # cria um generator com valores de 1 a 1000000 apenas trocando os colchetes por parenteseses!!!

print(sys.getsizeof(l1))  
print(sys.getsizeof(l2))  
for v in l1:
  print(v)
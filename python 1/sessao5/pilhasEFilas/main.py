"""
pilhas e filas 
pilhas (stack) - LIFO (last in, first out)- primeiro que entra, ultimo que sai
    exemplo: pilha de pratos
filas (queue) - FIFO (first in, first out)- primeiro que entra, primeiro que sai
    exemplo: fila de banco

dependendo de como a pilha ou a fila é implementada, altera o desempenho...

"""

from collections import deque
from time import sleep

# fila = deque(maxlen=4)  # cria uma fila com 4 posições
# fila.append('renato')
# fila.append('joao')
# fila.append('maria')
# fila.append('jose')
# fila.append('pedro')
# fila.append('marcos')

# print(f'saiu: {fila.popleft()}')
# print(f'saiu: {fila.popleft()}')
# print(f'saiu: {fila.popleft()}')
# print(f'saiu: {fila.popleft()}')

# for nome in fila:
#   print(nome)

#---------------------------------------------


# fila = deque(maxlen=10)

# for i in range(1000):
#   if i % 2 == 0:
#     fila.append(i)
#     sleep(.5)
#     print(fila)

#---------------------------------------------



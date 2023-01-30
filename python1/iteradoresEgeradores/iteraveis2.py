import sys

lista = list(range(1000001))  # cria uma lista com valores de 1 a 1000000

print(sys.getsizeof(lista))  # retorna o tamanho da lista alocada em memoria
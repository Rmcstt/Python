"""
Zip - uni os elementos de dois iteráveis em um iterável composto
Zip_longest - Faz um loop entre os dois iteráveis e retorna uma tupla de valores.
"""

from itertools import zip_longest, count  # importa o zip_longest
from textwrap import fill  # importa o fill

indice = count()  # cria um contador
cidades = ["sao paulo", "belo horizonte", "salvador", "taboao da serra"]
estados = ['sp', 'mg', 'ba']

cidades_estados = zip_longest(estados, cidades, fillvalue= 'deve ser em sampa')  # gerador de tuplas

for valor in cidades_estados:  # percorre o gerador
    print(valor)  

cidades_estados = zip(estados, cidades)  # gerador de tuplas

print(list(cidades_estados))  # converte o gerador em lista

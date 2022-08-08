from produtos import pessoas, produtos, lista  # importação de produtos.py
from functools import reduce  # importação de funções de reduce

acumula = 0

for x in lista:
    acumula += x

print(acumula)  # imprime a soma de todos os elementos da lista


somaLista = reduce(lambda ac, i: i + ac, lista, 0)  # chamo a função reduce e passo a função lambda e a lista
print(somaLista)  # imprime a soma de todos os elementos da lista com reduce

########################################################################################################################
print()


somaProdutos = reduce(lambda ac, p: p['price'] + ac, produtos, 0)  # chamo a função reduce e passo a função lambda e a lista

print(round(somaProdutos, 2))  # imprime a soma de todos os preços dos produtos com reduce e arredonda para 2 casas decimais
print(round(somaProdutos / len(produtos), 2))  # imprime a media de todos os preços dos produtos com reduce e arredonda para 2 casas decimais


########################################################################################################################
print()

somaIdade = reduce(lambda ac, p: p['idade'] + ac, pessoas, 0)

print(round(somaIdade))
print(round(somaIdade / len(pessoas)))

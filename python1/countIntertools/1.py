"""
count - intertools
"""
from types import GeneratorType  # importa o GeneratorType

variavel = zip('alo','alo')  # gerador de tuplas

print(list(variavel))  #[('a', 'a'), ('l', 'l'), ('o', 'o')]

variavel = zip('alo','alo') # tive que colocar outro para poder udar o next

print(next(variavel))  # ('a', 'a')
print(next(variavel))  # ('l', 'l')
print(next(variavel))  # ('o', 'o')

print(isinstance(variavel, GeneratorType))  # a instancia nao é um generator

variavel2 = ((x,y) for x, y in zip('alo','alo')) # geradorr de tuplas

print(isinstance(variavel2, GeneratorType))  # a instancia é um generator

print(list(variavel2))  #[('a', 'a'), ('l', 'l'), ('o', 'o')]

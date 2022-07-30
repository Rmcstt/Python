lista = [1,2,3,4,5]
print(hasattr(lista, '__iter__'))  # True
print(hasattr(lista, '__next__'))  # False

lista = iter(lista)  # cria um iterador
print(hasattr(lista, '__next__'))  # True

print(next(lista))  # 1
print(next(lista))  # 2
print(next(lista))  # 3
print(next(lista))  # 4

print(next(lista))  # 5

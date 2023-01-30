"""
a diferença entre listas e tuplas é que as tuplas são imutáveis, ou seja, so consigo alterar na origem.
"""

t1 = (1, 2, 3, 'a', 'renato')

print(type((t1)))  # <class 'tuple'>
print(t1[4])  # renato

for v in t1:
    print(v)

print(t1[2:])  # (3, 'a', 'renato')

t2 = 2
print(type(t2))  # <class 'int'>

t3 = 2,
print(type(t3))  # <class 'tuple'>

t4 = t1 + t3

print(t4, type(t4))  # (1, 2, 3, 'a', 'renato', 2) <class 'tuple'>

n1, n2, n3, n4, *_ = t4

print(_)
print(n4)


t5 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) * 2

t5 = list(t5)  # converte a tupla em lista

t5[3]= 'renato'  # altera o valor da lista

t5 = tuple(t5)  # converte a lista em tupla
 
print(t5)  # [1, 2, 3, 'renato', 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 'renato', 4, 5, 6, 7, 8, 9, 10]





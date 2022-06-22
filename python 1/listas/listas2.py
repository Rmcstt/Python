l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2


print(l1)  # [1, 2, 3]
print(l2)  # [4, 5, 6]
print(l3)  # [1, 2, 3, 4, 5, 6]

l4 = l1.extend(l2)  # concatena as listas
print(l1)  # [1, 2, 3, 4, 5, 6]

l2.append('b')
print(l2)  # [4,5,6,'b']
print(l2[3])  # b

l3.insert(0, 'chevrolet')
print(l3)  # ['chevrolet', 1, 2, 3, 4, 5, 6]

l1.pop(-1)
print(l1)  # [1, 2, 3, 4, 5]

l5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

del(l5[3:5])
print(l5)  # [1, 2, 3, 6, 7, 8, 9]

l5.insert(0, 'oi')
print(l5)  # ['oi', 1, 2, 3, 6, 7, 8, 9]

del(l5[0])
l5.insert(3, 4)
l5.insert(4, 5)
print(l5)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(max(l5))  # 9
print(min(l5))  # 1

l6 = list(range(1, 10))  # gera lista
print(l6)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

l7 = list(range(0, 100, 6))  # (começø, fim, quanto em quanto)
print(l7)  # [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]

l8 = list(range(0, 100, 20))

for valor in l8:
    print(valor)
# 0
# 20
# 40
# 60
# 80

soma = 0
for valor in l8:
    soma = soma + valor
print(soma)  # 200

l9 = ['string', True, 10, 10.5]

for elem in l9:
    print(f'o tipo de elem  é {type(elem)} e seu valor é {elem}')
# o tipo de elem  é <class 'str'> e seu valor é string
# o tipo de elem  é <class 'bool'> e seu valor é True
# o tipo de elem  é <class 'int'> e seu valor é 10
# o tipo de elem  é <class 'float'> e seu valor é 10.5
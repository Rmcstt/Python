d1 = {
  1: 2,
  2: 3,
  3: 4
}

print(d1)  # {1: 2, 2: 3, 3: 4}

d1.pop(3)  # remove a chave 3

print(d1)  # {1: 2, 2: 3}
 
d2 = {
  'a': 'b',
  'c': 'd',
  'e': 'f'
}

print(d2)  # {'a': 'b', 'c': 'd', 'e': 'f'}

d1.update(d2)  # d1 recebe o valor de d2

print(d1)  # {1: 2, 2: 3, 'a': 'b', 'c': 'd', 'e': 'f'}

lista = [
  ['nome', 'renato'],
  ['idade', '25'],
  ['cidade', 'sao paulo'],
  ['estado', 'sp'],
]

tuplas = [
  ('nome', 'renato'),
  ('idade', '25'),
  ('cidade', 'sao paulo'),
  ('estado', 'sp'),
]


d1 = dict(lista)  # d1 recebe o valor de lista
d2 = dict(tuplas)  # d2 recebe o valor de tuplas

print(d1)  # {'nome': 'renato', 'idade': '25', 'cidade': 'sao paulo', 'estado': 'sp'}
print(d2)  # {'nome': 'renato', 'idade': '25', 'cidade': 'sao paulo', 'estado': 'sp'}

# tanto listas como tuplas podem ser convertidas em dicionarios, ou ate tuplas dentro de listas e listas dentro de tuplas.
# apenas pelo fato de terem o mesmo formato (chave e valor).
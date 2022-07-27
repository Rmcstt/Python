list = [
  ('chave1', 'valor1'),
  ('chave2', 'valor2'),
]

d1 = {x.upper(): y.upper() for x,y in list}  # cria um dicionario com as chaves e valores em maiusculo
print(d1)

d2 = {x for x in range(10)}  # set comprehension

print(d2, type(d2))


d3 = {f'chave_{x}': x**2 for x in range(10)}  # cria um dicionario com chaves e valores
print(d3)
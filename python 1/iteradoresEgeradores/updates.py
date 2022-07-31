# listas, tuplas, str -> sequences -> iteraveis 


#### itearando cmo o "for".

nome = 'renato mota'

for letra in nome:
  print(letra)  

print('#' * 50)

for letra in nome:
  print(letra)

print()

#### abaixo um exemplo de iteração manual, ou um "for" manual.

nome2 = 'renato'
iterador = iter(nome2)  # cria um iterador

try:  # tenta executar o codigo abaixo
  print(next(iterador))  # r
  print(next(iterador))  # e
  print(next(iterador))  # n
  print(next(iterador))  # a
  print(next(iterador))  # t
  print(next(iterador))  # o
  print(next(iterador))  # ❌ erro (stopiteration)
except:  # se der erro, executa o codigo abaixo
  pass  # nao ira gerar erro
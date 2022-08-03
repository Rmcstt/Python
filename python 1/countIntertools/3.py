from itertools import count

contador = count(start = 10, step = 0.1)  # cria um contador que começa no 10 ee incremanta de 2 em 2!

for valor in contador:
  print(round(valor, 2))  # round arredonda o valor para "x" casas decimais
  if valor > 20:
    break
from itertools import count

contador = count(start = 10, step = -1)  # tambem pode ser criado com step negativo

for valor in contador:
  print(round(valor, 2))
  if valor >= 20 or valor <= -10:
    break
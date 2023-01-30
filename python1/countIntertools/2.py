from itertools import count

contador = count()

print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))


for valor in contador:
  print(valor)
  if valor > 50:
    break
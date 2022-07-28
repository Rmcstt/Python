import sys
import time

def geraLista():
  r = []
  for n in range(100):
    r.append(n)
    time.sleep(0.1)
  return r

g = geraLista()

for v in g:
  print(v)

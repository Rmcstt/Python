# nesse exemplo, o arquivo tambem é fechado automaticamente.

from contextlib import contextmanager

@contextmanager
def abrir(arquivo, modo):
  try:
    print('abriu')
    arquivo = open(arquivo, modo)
    yield arquivo
  finally:
    print('fechou')
    arquivo.close()

with abrir('Poo/contextManager/abc.txt', 'w') as arquivo:
  arquivo.write('opa, mundo!\n')
  arquivo.write('opa, mundo!\n')
  arquivo.write('opa, mundo!\n')
class TaErradoError(Exception):
  pass

def testar():
  raise TaErradoError('errado !')

try:
  testar()
except TaErradoError as error:
  print(f'Erro: {error}')

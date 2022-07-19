def olaMundo():
  return 'ola mundo'

def mestre(funcao):
  return funcao()

executando = mestre(olaMundo)
print(executando)


def func2():
  return 'renato'

def func1(param):
  return param()

printar = func1(func2)  # tem que haver ainda um elo fora das funções para que elas possam ser chamadas.
print(printar)

def motor():
  print('vruuummmm') 

def Chave(inginicao):
  return inginicao()

def giraChave():
  return Chave(motor)


giraChave()


def escapamento_barulhento():
  print('ratatatatatatatatat')

def guidao(acelera):
  return acelera()

def gira_guidao():
  return guidao(escapamento_barulhento)

gira_guidao()



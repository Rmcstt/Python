import math  # importando math

PI = math.pi  # atribuindo valor de pi a variavel PI

def dobraLista(lista):  # função que duplica os valores de uma lista
  return [x*2 for x in lista]  # retorna uma lista com os valores duplicados


def multiplicador(x):  # função que multiplica os valores de uma lista
  r = 1
  for i in x:
    r *= i
  return r


if __name__ == '__main__':  # isso serve para que o codigo nao execute quando for importado
  lista = [1,2,3,4,5]

  print(dobraLista(lista))  
  print(multiplicador(lista))  # 120
  print(PI)  # 3.141592653589793
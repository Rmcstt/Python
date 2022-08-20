import re


REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def valida(cnpj):
    cnpj = apenasNumeros(cnpj)

    if sequenciaOuNao(cnpj):
      return False


    novoCnpj = calculaDigito(cnpj = cnpj, digito = 1)
    novoCnpj = calculaDigito(cnpj = novoCnpj, digito = 2)

    if novoCnpj == cnpj:
      print(f'{cnpj} é um cnpj valido')

    else:
      print(f'{cnpj} nao é um cnpj valido')

def calculaDigito(cnpj, digito):
  if digito == 1:
    regressivos = REGRESSIVOS[1:]
    novoCnpj = cnpj[:-2]
  elif digito == 2:
    regressivos = REGRESSIVOS
    novoCnpj = cnpj 
  else:
    return None 


  total = 0
  for indice, regressivo in enumerate(regressivos):
    total += int(cnpj[indice]) * regressivo

  digito = 11 - (total % 11)
  digito = digito if digito <=9 else 0

  return f'{novoCnpj}{digito}'

def sequenciaOuNao(cnpj):
  sequencia = cnpj[0] * len(cnpj)

  if sequencia == cnpj:
    return True

  else:
    return False


def apenasNumeros(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)

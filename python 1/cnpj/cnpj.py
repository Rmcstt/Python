import re


REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def valida(cnpj):
    cnpj = apenasNumeros(cnpj)

    if sequenciaOuNao(cnpj):
      return False


    novoCnpj = calculaDigito(cnpj = cnpj, digito = 1)

def calculaDigito(cnpj, digito):
  if digito == 1:
    regressivos = REGRESSIVOS[1:]
  elif digito == 2:
    regressivos = REGRESSIVOS
  else:
    return None 


  total = 0
  for indice, regressivo in enumerate(regressivos):
    print(indice, regressivo)

def sequenciaOuNao(cnpj):
  sequencia = cnpj[0] * len(cnpj)

  if sequencia == cnpj:
    return True

  else:
    return False


def apenasNumeros(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)

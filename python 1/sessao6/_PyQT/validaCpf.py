



def valida_cpf(cpf):
  cpf = cpf
  novo_cpf = cpf[:-2]
  reverso = 10
  total = 0

  for index in range(19):  # multiplicando os numeros do cpf por suas posições 
      if index > 8:  
          index -= 9  # subtraindo 9 para nao ultrapassar o tamanho do cpf

      total += int(novo_cpf[index]) * reverso  # somando os numeros multiplicados

      reverso -= 1
      if reverso < 2:
          reverso = 11
          d = 11 - (total % 11)  # calculando o digito verificador

          if d > 9:
              d = 0
          total = 0
          novo_cpf += str(d)

  sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

  if cpf == novo_cpf and not sequencia:
      return True
  else:
      return False
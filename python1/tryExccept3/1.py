def converteNumero(valor):  # converte um valor para inteiro
    try:  # tenta converter o valor para inteiro
        valor = int(valor)  
        return valor  # retorna o valor convertido

    except ValueError as erro:  # captura o erro e o armazena na variavel erro
        try:  # tenta converter o valor para float
          valor = float(valor)  
          return valor  # retorna o valor convertido
        except ValueError as erro:  
          pass  

   
while True:
  numero = converteNumero(input('digite um numero: '))

  if numero is not None:
    print(numero + 5)
  else:
    print('isso nao é um numero')
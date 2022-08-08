
try:
  a = 0
  try:  # pode ainda haver um try dentro de um try
    a = 1/0
  except:
    print('error')
  
except NameError as error:  # captura o erro e o armazena na variavel erro
  print('Erro do dev!!!', error)

except (IndexError, KeyError) as error:  
  print('Erro de indice ou erro de chave', error)

except Exception as error:
  print('ocorreu um erro inesperado!!!', error)

else:
    pass

finally:  # executa o finally sempre
  a=''

print('bola pra frente...')

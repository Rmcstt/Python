
try:
  a = 0
  try:  # pode ainda haver um try dentro de um try
    a = 1/0
  except:
    print('erro')
  
except NameError as erro:  # captura o erro e o armazena na variavel erro
  print('Erro do dev!!!', erro)

except (IndexError, KeyError) as erro:  
  print('Erro de indice ou erro de chave', erro)

except Exception as erro:
  print('ocorreu um erro inesperado!!!', erro)

else:
    pass

finally:  # executa o finally sempre
  a=''

print('bola pra frente...')

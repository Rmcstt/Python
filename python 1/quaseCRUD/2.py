try:  # tentara abrir  o arquivo
  file = open('quaseCRUD/def.text', 'w+')
  file.write('linha')
  file.seek(0)  # somente '0' tambem da
  print(file.read())
finally:  # mesmo dando erro ele executara o bloco finally
  file.close()
  print('final')

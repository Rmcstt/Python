#  metodo pythonico para esse tipo de arquivo

with open('quaseCRUD/ghi.txt', 'w+') as file:
  file.write('linha 4\n')
  file.write('linha 5\n')
  file.write('linha 6\n')
  
  file.seek(0)
  print(file.read())

with open('quaseCRUD/abc.txt', 'r') as file:
  print(file.read())

with open('quaseCRUD/def.txt', 'a+') as file:
  file.write('outra linha\n')
  file.seek(0)
  print(file.read())


  # 'w+' = leitura e escrita, tambem sobreescreve o que ja tinha no arwuivo
  # 'r' = leitura, nao permite escrita
  # 'a+' = leitura e escrita,  adiciona sem sobreescrever




  # 'import os
  # os.remove('quaseCRUD/abc.txt')' = remove o arquivo
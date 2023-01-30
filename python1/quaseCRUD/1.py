  #https://docs.python.org/3/library/functions.html#open

file = open('quaseCRUD/abc.txt', 'w+')  # w+ = write and read
file.write('linha 1\n')  # escreve no arquivo
file.write('linha 2\n')
file.write('linha 3\n')

file.seek(0, 0)  # seek(0, 0) vai para o início do arquivo
print('lendo o arquivo')
print(file.read())  # lê o arquivo
print('############################')

file.seek(0,0)
print(file.readline(), end='')  # lê a primeira linha do arquivo
print(file.readline(), end='')
print(file.readline(), end='')
print('############################')

file.seek(0,0)
for linha in file.readlines():  # lê todas as linhas do arquivo
  print(linha, end= "")  # end= "" para não pular linha

file.close()  # fecha o arquivo
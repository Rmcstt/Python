#estaaula seviu para mostrar como usar (executar) o python pelo terminal

# neste exemplo ' usar na pasta do arquivo "python3 main.py" '

import sys
import os

argumentos = sys.argv
qtd_argumrntos = len(argumentos)

if qtd_argumrntos <= 1 :
  print('nenhum argumento foi passado')
  print('-a', 'para listar todos os arquivos nesta pasta', sep= '\t')
  print('-d', 'para listar todas as pastas desta pasta', sep= '\t')
  sys.exit()



so_arquivos = False
if '-a' in argumentos:
  so_arquivos = True

so_diretorios  = False
if '-d' in argumentos:
  so_diretorios = True

for arquivo in os.listdir():
  if so_arquivos:
    if os.path.isfile(arquivo):
      print(arquivo)
  elif so_diretorios:
    if os.path.isdir(arquivo):
      print(arquivo)
  else:
    print(arquivo)


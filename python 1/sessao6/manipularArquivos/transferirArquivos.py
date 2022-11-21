import os
import shutil

caminho_original = '/Users/Renatomota/desktop/paralixo'

caminho_novo = '/Users/renatomota/desktop/meuLixo'

try:
  os.mkdir(caminho_novo)
except FileExistsError as e:
  print(f'pasta {caminho_novo} ja existe')
for root, dirs, files in os.walk(caminho_original):
  for file in files:
    old_file_path = os.path.join(root, file)
    new_file_path = os.path.join(caminho_novo, file)
    shutil.move(old_file_path, new_file_path)

    print(f'arquivo {file} moovido com sucesso')
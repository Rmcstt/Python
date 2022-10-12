import os

caminho_original = '/Users/Renatomota/desktop/testafoto3'

caminho_novo = '/Users/renatomota/desktop/testafoto3'

try:
  os.mkdir(caminho_novo)
except FileExistsError as e:
  print(f'pasta {caminho_novo} ja existe')
for root, dirs, files in os.walk(caminho_novo):
  for file in files:
    old_file_path = os.path.join(root, file)
    new_file_path = os.path.join(caminho_novo, file)

    if '_new' in file:
      os.remove(new_file_path)

      print(f'arquivo {file} removido com sucesso')
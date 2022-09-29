from zipfile import ZipFile
import os

caminho = '/Users/renatomota/desktop/test/'

with ZipFile('/Users/renatomota/Desktop/Python/python 1/sessao5/zipfile/arquivo.zip', 'w') as zip:
  for arquivo in os.listdir(caminho):
    caminho_completo = os.path.join(caminho, arquivo)
    zip.write(caminho_completo, arquivo)

with ZipFile('/Users/renatomota/Desktop/Python/python 1/sessao5/zipfile/arquivo.zip', 'r') as zip:
  for arquivo in zip.namelist():
    print(arquivo)
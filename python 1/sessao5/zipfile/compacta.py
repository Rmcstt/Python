from zipfile import ZipFile
import os


# caminho do arquivo e nome do futuro arquivo zip
caminho = '/Users/renatomota/desktop/test/'

arquivoZip = '/Users/renatomota/Desktop/test.zip'
# zipador 
with ZipFile(arquivoZip, 'w') as zip:
  for arquivo in os.listdir(caminho):
    caminho_completo = os.path.join(caminho, arquivo)
    zip.write(caminho_completo, arquivo)


# confere se o Zip foi criado
with ZipFile(arquivoZip, 'r') as zip:
  for arquivo in zip.namelist():
    print(arquivo)
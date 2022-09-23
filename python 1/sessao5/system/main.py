import os

caminho_predefinido = '/Users/renatomota/Desktop/EXTRO/'

meu_caminho = input('digite  o nome da pasta: ')

termo_procura = input('algum termo para procurar? :')

caminho_procura = caminho_predefinido + meu_caminho

def formata_tamanho(tamanho):
  base = 1024
  kilo = base
  mega = base ** 2
  giga = base ** 3
  tera = base ** 4
  peta = base ** 5

  if tamanho < kilo:
    tamanho = base
    texto = 'B'
  elif tamanho < mega:
    tamanho /= kilo
    texto = 'K'
  elif tamanho < giga:
    tamanho /= mega
    texto = 'M'
  elif tamanho < tera:
    tamanho /= giga
    texto = 'G'
  elif tamanho < peta:
    tamanho /= tera
    texto = 'T'

  tamanho = round(tamanho, 2)
  return f'{tamanho} {texto}'

conta = 0
for raiz, diretorios, arquivos in os.walk(caminho_procura):
  for arquivo in arquivos:
    if termo_procura in arquivo:
      try:
        conta += 1
        caminho_completo = os.path.join(raiz, arquivo)
        nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
        tamanho = os.path.getsize(caminho_completo)
        

        print()
        print('arquivo encontrado:', arquivo)
        print('path:', caminho_completo)
        print('nome:', nome_arquivo)
        print('extensao:', ext_arquivo)
        print('tamanho:', formata_tamanho(tamanho))
      except PermissionError as e:
        print('sem acesso')
      except FileNotFoundError as e:
        print('arquivo nao encontrado')
      except Exception as e:
        print('errro desconhecido', e)

print()
print(f'{conta} arquivo(s) encontrado(s)')
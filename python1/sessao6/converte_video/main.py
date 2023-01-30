# https://ffmpeg.zeranoe.com/builds/

import os
import sys
import ffmpeg

"""
ffmpeg -i "ENTRADA"-i "LEGENDA" -c:v libx264 -crf 23 -preset ultrafast -c:a aac -b:a 320k -c:s srt -map 1:0 -ss 00:00:00 -to 00:00:00 "SAIDA"
"""
if sys.platform == 'darwin':
    ffmpeg = '/Users/renatomota/Downloads/ffmpeg'
else:
  ffmpeg = 'ffmpeg'



codec_video = '-c:v libx264'
crf = '-crf 23'
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 320k'

debug = '-ss 00:00:00 -to 00:00:50'

caminho_original = '/Users/Renatomota/desktop/paraLixo'
caminho_novo = '/Users/renatomota/desktop/meulixo'

for raiz, pasta, arquivos in os.walk(caminho_original):
  for arquivo in arquivos:
    if not '.MP4'in arquivo:
      continue

    caminho_completo = os.path.join(raiz, arquivo)
    nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
    caminho_legenda = nome_arquivo + '.MP4'

    if os.path.isfile(caminho_legenda):
      input_legenda = f'-i "{caminho_legenda}"'
      map_legenda = '-c:s srt -map v:0 -map a _map1:0'
    else:
      input_legenda = ''
      map_legenda = ''

    
    nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)

    caminho_saida = f'{caminho_novo}/{nome_arquivo}_NOVO{extensao_arquivo}'

    comando = f'{ffmpeg} -i "{caminho_completo}" {input_legenda} {codec_video} {crf} {preset} {codec_audio} {bitrate_audio} {map_legenda} {debug} "{caminho_saida}"'

    print(comando)





      # comando = f'{ffmpeg} -i "{arquivo_original}" -i "{legenda}" {codec_video} {crf} {preset} {codec_audio} {bitrate_audio} -c:s srt -map 1:0 {debug} "{arquivo_novo}"'
      # print(comando)
      # subprocess.call(comando, shell=True)




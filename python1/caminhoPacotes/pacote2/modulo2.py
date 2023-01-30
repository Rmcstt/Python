
####################################### hack #######################################

try:
  import sys
  import os

  sys.path.append(
    os.path.abspath(
      os.path.join(
        os.path.dirname(__file__),
        '..'
      )
    )
  )
except ImportError:
  raise

######################################### hack ############################################

from pacote1.modulo1 import variavel1

print(variavel1)

variavel2 = 'variavel 2'

# esse programa nao funciona pois o main é o arquivo de entrada, sendo nassim ele nao importa para tras nesse caminho que usa o main como ponto de vista.  a nao ser que use o rack acima!!!
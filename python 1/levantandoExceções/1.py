# https://docs.python.org/3/library/exceptions.html

# def divide(n1 , n2):  # Função que divide dois números
#   try:
#     return n1 / n2  
#   except ZeroDivisionError as error:  # captura o erro e o armazena na variavel erro
#     print('log: ',error)  # imprime o erro
#     raise
# try:
#   print(divide(2,0))
# except ZeroDivisionError as error:  
#   print(error)  # imprime o erro




def divide2(n3,n4):
  if n4 == 0:
    raise ValueError("nenhum numero é divisivel por zero.")  # voce pode criar uma excessão personalizada
  return n3/n4


try:
  print(divide2(n3=2,n4=0))
except ValueError as error:
  print('voce esta tentando dividir por zero')
  print('log', error)
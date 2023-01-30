variavel = 'valor'

def func():
  outra_variavel = 'renato'  # variavel local
  return outra_variavel  # retorna o valor de outra_variavel

def func2(arg):
  print(arg)   

var = func()
func2(var)  # imprime 'valor'


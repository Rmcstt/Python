from ast import arg


variavel = 'valor'

def func():
  print(variavel)

def func2():
  # global variavel # para alterar o valor de uma variavel global
  variavel = 'outro valor'  # so altera o valor dentro do escopo da função
  print(variavel)
  

def func3(arg=None):
  arg = arg.replace('v','c')
  return arg


outra_variavel = func3(arg=variavel)


func()  # imprime 'valor'
func2()  # imprime 'outro valor'


print(variavel)  # imprime 'valor'
print(outra_variavel)  # imprime 'coutro calor'


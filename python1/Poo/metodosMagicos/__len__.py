
"""
metodo __len__ = é chamado para saber o tamanho do objeto, ou seja, quando é chamado o metodo len()
"""

class A:
  def __init__(self):
    pass

  def __len__(self):  # metodo __len__ é usado para retornar o tamanho de um objeto, que nao foi o caso aqui rsrs
    return 10

a = A()
print(len(a)) # retorna 10
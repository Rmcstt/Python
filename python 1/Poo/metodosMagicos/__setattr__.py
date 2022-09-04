
"""
metodo __setattr__ = é chamado sempre que um atributo é atribuido a um objeto, pode ser usado para VALIDAR os atributos
"""


class A:
  def __init__(self):
    pass

  def __setattr__(self, key, value):  # metodo especial para setar atributos
    self.__dict__[key] = value


a = A()
a.nome  = ' renato '

print(a.nome)
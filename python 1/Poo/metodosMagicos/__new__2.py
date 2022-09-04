
"""
outtro exemplo de __new__
"""


class A:
  def __new__(cls, *args, **kwargs):  

    if not hasattr(cls, 'instance'):  # se o atributo 'instance' nao existir, ele é criado
      cls.instance = super().__new__(cls)  # cls.instance é o objeto que será retornado

    return cls.instance  # retorna o objeto

  def __init__(self):
    print('eu sou INIT')


a = A()
b = A()
c = A()

print(id(a), id(b), id(c))  #todos os objetos tem o mesmo id
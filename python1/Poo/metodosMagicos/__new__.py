"""
https://rszalski.github.io/magicmethods/
"""

"""
metodo __new__ = memtodo contrutor, que pode ser usado para criar objetos assim como o __init__
"""

class A:

  def __new__(cls, *args, **kwargs):  # __new__ tambem é um metodo construtor, mas é chamado antes do __init__
    print('eu sou o NEW')
    return super().__new__(cls)  # para que o __init__ seja chamado, é nessesario que o __new__ retorne o objeto
  def __init__(self):
    print('eu sou o INIT')

a = A()

"""
metodo __str__ = é chamado quando o objeto é convertido para string, ou seja, quando é chamado o metodo str()
"""

class A:
  def __init__(self):
    pass

  def __str__(self):  # se esse metodo nao fosse usado, o print retornaria : <__main__.A object at 0x7f9b8c0b7a90>
    return ' essa classse é uma string'


a = A()
print(a)  # por conta do metodo __str__, o print retorna: essa classe é uma sstring
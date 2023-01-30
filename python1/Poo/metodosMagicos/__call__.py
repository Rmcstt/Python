
"""
metodo __call__ = chama o objeto como se fosse uma funcao, pode ser usado para criar um objeto que se comporte como função
"""


class A:
  def __init__(self):
    pass

  def __call__(self, *args, **kwargs):  # metodo especial para chamar a classe como se fosse uma função
    print(args)  #ira retornar uma tupla
    print(kwargs)  # ira retornar um dicionario



a = A()

a(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, nome='joao', idade=20)  #quando chamamos o objeto como uma função, o metodo __call__ é chamado
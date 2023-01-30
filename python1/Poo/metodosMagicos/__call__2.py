
"""
outro exemplo de __call__
"""


class A:
  def __init__(self):
    pass

  def __call__(self, *args, **kwargs):  
    resultado = 1

    for i in args:  
      resultado *= i

    return resultado

a = A()
variavel = a(1,2,3,4,5,6,7,8,9,10)  

print(variavel)
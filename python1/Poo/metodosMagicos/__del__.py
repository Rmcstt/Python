"""
🛑esse metodo nao é tao confiavel, pois as vezes o interpretador pode chamar ele sem querer
"""

class A:
  def __init__(self):
    pass

  def __del__(self):
    print('eu sou o del')

a = A()
"""
animal -> respirar
  lobo(animal) -> respirar/uivar
    cachorro(lobo) -> respirar/uivaa/latir
      chihuahua(cachorro) -> respirar/uivar/latir/tremer

"""

"""
até da para classe pai chamar metodo da classe filha, porem fica muito compexo, vide aula 120 do curso python 3
ou o exemplo abaixo
"""

# 🛑 raramente se usa esse tipo de herança, pois o conceito ira deixar o codigo muito confuso!!!

class A:
  def fala(self):
    self.b_fala()

class B(A):
  def b_fala(self):
    print('oi')

b = B()
b.fala()
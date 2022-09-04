"""
No Python, o comportamento dos operadores é definido por metodos especiais.
vamos alterar o comportamento de operadores com classes definidas pelo usuario.
"""

class Retangulo:  # classe definida pelo usuario
  def __init__(self, x, y):  # metodo construtor
    self.x = x
    self.y = y

  def get_area(self):  # metodo para calcular area
    return self.x * self.y

    # metodo especial para  operador soma, sempre tem que haver dois parametros; self e other onde self é o objeto que chamou o metodo e other é #o objeto que foi passado como paramrtro
  def __add__(self, other):  
    return f'novo retangulo: ({self.x +other.x}, {self.y + other.y})' # retorna uma tupla
    

  def __lt__(self, other):  # metodo especial para operador menor que
    return self.get_area() < other.get_area()

  def __gt__(self, other):  # metodo especial para operador maior que
    return self.get_area() > other.get_area()

  def __eq__(self, other):  # metodo especial para operador igualdade
    return self.get_area() == other.get_area()




r1 = Retangulo(22, 20)
r2 = Retangulo(22, 20)
r3 = Retangulo(44, 40)

print(r1 + r2)

print(r1 < r2)

print(r3 > r2)

print(r1 == r2)
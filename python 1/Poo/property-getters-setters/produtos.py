class Produto:
  def __init__(self, nome, preco):
    self.nome = nome
    self.preco = preco

  def desconto(self, percentual):
    self.preco = self.preco - (self.preco * (percentual / 100))

  #getter
  @property
  def nome(self):
    return self._nome

  #setter
  @nome.setter
  def nome(self, valor):
    self._nome = valor.title() 




  # getter
  @property
  def preco(self):
    return self._preco

  # setter
  @preco.setter
  def preco(self, valor):
    if isinstance(valor, str):
      valor = float(valor.replace('R$', '').replace('.', '').replace(',', '.'))
    self._preco = valor

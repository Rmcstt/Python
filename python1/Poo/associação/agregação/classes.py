"""
agregação:  quando uma classe é composta por outras classses
como um carrinho de compras que é composto por varios produtos
"""

class CarrinhoDeCompras:  # classe principal
  def __init__(self):  # contrutor
    self.produtos = []  # lista de produtos

  def inserir_produtos(self, produto):
    self.produtos.append(produto)

  def lista_produtos(self):
    for produto in self.produtos:
      print(f'item = {produto.nome} -> R${produto.valor:.2f}')

  def soma_total(self):
    total = 0
    for produto in self.produtos:
      total += produto.valor
    return f'total da compra = R${total:.2f}'

class Produto:
  def __init__(self, nome, valor):
    self.nome = nome
    self.valor = valor
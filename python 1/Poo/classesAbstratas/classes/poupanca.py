from classes.conta import Conta

class Poupanca(Conta):
  def sacar(self, valor):  # <-- polimorfismo, mesma assinatura porem comportamento diferente
    if self.saldo <valor:
      print('saldo insuficiente')
      return

    self.saldo -= valor
    self.detalhes()
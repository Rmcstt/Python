from abc import ABC, abstractmethod

class Conta(ABC):  # classe abstrata
  def __init__(self, agencia, conta, saldo):
    self._agencia = agencia
    self._numero = conta
    self._saldo = saldo

  @property
  def agencia(self):
    return self._agencia

  @property
  def conta(self):
    return self._numero

  @property
  def saldo(self):
    return self._saldo
  
  @saldo.setter
  def saldo(self, valor):
    if not isinstance(valor, (int, float)):
      raise ValueError('o valor do saldo deve ser numerico')

    self._saldo = valor


  def depositar(self, valor):
    if not isinstance(valor, (int, float)):
      raise ValueError('o valor do deposito precisa ser numerico')

    self.saldo += valor
    self.detalhes()

  def detalhes(self):
    print(f'Agencia: {self.agencia} ' , end=' ')
    print(f'Conta: {self.conta} ' , end=' ')
    print(f'Saldo: {self.saldo} ')


  @abstractmethod  # metodo abstrato
  def sacar(salf, valor):  
    pass
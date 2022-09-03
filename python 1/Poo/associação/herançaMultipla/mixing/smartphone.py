from eletronico import Eletronico
from log import LogMixin

class Smartphone(Eletronico, LogMixin):
  def __init__(self, nome):
    super().__init__(nome)
    self._conectado = False

  def conectar(self):
    if not self._ligado:
      info = f'{self._nome} precisa estar ligado para conectar'
      print(info)
      self.log_error(info)
      return
    
    if self._conectado:
      error = f'{self._nome} ja esta conectado'
      print(error)
      self.log_error(error)
      return

    info = f'{self._nome} conectado'
    print(info)
    self.log_info(info)
    self._conectado = True

  def desconectado(self):
    if not self._conectado:
      error = f'{self._nome} nao esta conectado'
      print(error)
      self.log_error(error)
      return
    
    info = f'{self._nome} desconectado com sucesso'
    print(info)
    self.log_info(info)
    self._conectdo = False
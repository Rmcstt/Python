from eletronico import Eletronico

class Smartphone(Eletronico):
  def __init__(self, nome):
    super().__init__(nome)
    self._conectado = False

  def conectar(self):
    if not self._ligado:
      print(f'{self._nome} precisa estar ligado para conectar')
      return
    
    if self._conectado:
      print(f'{self._nome}a ja esta conectado')
      return

    self._conectado = True

  def desconectado(self):
    if not self._conectado:
      print(f'{self._nome} nao esta conectado')
      return
    self._conectdo = False
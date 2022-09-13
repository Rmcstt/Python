import re

class CalcIpv4:
  def __init__(self, ip, mascara=None, prefixo=None):
    self.ip = ip
    self.mascara = mascara
    self.prefixo = prefixo

  @property
  def ip(self):
    return self._ip
  @property
  def mascara(self):
    return self._mascara
  @property
  def prefixo(self):
    return self._prefixo

  @ip.setter
  def ip(self, valor):
    if not self._valida_ip(valor):
      raise ValueError('ip invalido')

    self._ip = valor

  @mascara.setter
  def mascara(self, valor):
    if not valor:
      return

    if not self._valida_ip(valor):
      raise ValueError('mascara invalda')

    self._mascara = valor
    self._ip_to_bin(valor)

  @prefixo.setter
  def prefixo(self, valor):
    if not valor:
      return

    if not isinstance(valor, int):
      raise TypeError('prefixo deve ser inteiro')

    if valor < 0 or valor > 32:
      raise ValueError('prefixo deve estar entre 0 e 32') 

    self._prefixo = valor

  @staticmethod
  def _valida_ip(ip):
    """valida o ip informado"""
    regexp = re.compile(r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$')

    if regexp.search(ip):
      return True

  
  @staticmethod
  def _ip_to_bin(self, ip):
    """ converte o ip informado para binario """
    print(ip)

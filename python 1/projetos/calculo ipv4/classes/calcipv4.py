import re

class CalcIpv4:
  def __init__(self, ip, mascara=None, prefixo=None):
    self.ip = ip
    self.mascara = mascara
    self.prefixo = prefixo

    self._set_broadcast()
    self._set_rede()

    print(f'numero ip :           {self.ip}')
    print(f'mascara :             {self.mascara}')
    print(f'rede :                {self.rede}')
    print(f'broadcast :           {self.broadcast}')
    print(f'prefixo :             {self.prefixo}')
    print(f'quantidade de hosts : {self.num_ips()}')

  @property
  def ip(self):
    return self._ip
  @property
  def mascara(self):
    return self._mascara
  @property
  def prefixo(self):
    return self._prefixo
  @property
  def rede(self):
    return self._rede
  @property
  def broadcast(self):
    return self._broadcast
  @property
  def num_ips(self):
    return self._num_ips

  @ip.setter
  def ip(self, valor):
    if not self._valida_ip(valor):
      raise ValueError('ip invalido')

    self._ip = valor
    self._ip_bin = self._ip_to_bin(valor) 

  @mascara.setter
  def mascara(self, valor):
    if not valor:
      return

    if not self._valida_ip(valor):
      raise ValueError('mascara invalda')

    self._mascara = valor
    self._mascara_bin = self._ip_to_bin(valor)

    if not hasattr(self, '_prefixo'):
      self._prefixo = self._mascara_bin.count('1')

  @prefixo.setter
  def prefixo(self, valor):
    if not valor:
      return

    if not isinstance(valor, int):
      raise TypeError('prefixo deve ser inteiro')

    if valor < 0 or valor > 32:
      raise ValueError('prefixo deve estar entre 0 e 32') 

    self._prefixo = valor
    self._mascara_bin = (valor * '1').ljust(32, '0')

    if not hasattr(self, 'mascara'):
      self.mascara = self._bin_to_ip(self._mascara_bin)
    

  @staticmethod
  def _valida_ip(ip):
    """valida o ip informado"""
    regexp = re.compile(r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$')

    if regexp.search(ip):
      return True

  
  @staticmethod
  def _ip_to_bin(ip):
    """ converte o ip informado para binario """
    blocos = ip.split('.')
    blocos_bin = [x for x in map(lambda x: bin(int(x))[2:].zfill(8),blocos)]

    return ''.join(blocos_bin)

  @staticmethod
  def _bin_to_ip(ip):
    """ converte o ip informado para binario"""
    n = 8
    blocos = [str(int(ip[i:n+i],2)) for i in range(0, 32, n)]
    return '.'.join(blocos)

  def _set_broadcast(self):
    """ calcula o broadcast """
    host_bits = 32 - self.prefixo
    self._broadcast_bin = self._ip_bin[:self.prefixo] + (host_bits * '1')
    self._broadcast = self._bin_to_ip(self._broadcast_bin)
    return self._broadcast

  def _set_rede(self):
    """ calcula a rede """
    host_bits = 32 - self.prefixo
    self._rede_bin = self._ip_bin[:self.prefixo] + (host_bits * '0')
    self._rede = self._bin_to_ip(self._rede_bin)
    return self._rede

  def _num_ips(self):
    """ calcula o numero de ips da rede"""
    return 2 ** (32 - self.prefixo) - 2
    


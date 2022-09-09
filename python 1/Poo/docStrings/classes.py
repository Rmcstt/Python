"""..."""

from typing import TextIO


class Myclass:
  """Documentação normal
  conforme qualquer outra documentaçnao que voce tenha usado anteriormente 
  
  """
  atributo = 1
  atributo2 = 'valor'

  def __init__(self, texto):
    """inicializa os dados
    
    :param texto: o texto da classe 
    :type texto: str
    """
    self.texto = texto
    self.exibe_texto(texto)

  @staticmethod
  def exibe_texto(texto):
    """ metodo que exibe um texto de 100 caracteres na tela 
    
    :param texto: um texto de 100 caracteres
    :type texto: str

    :return: o texto de 100 caracteres
    :rtype: str
    
    :raises ValueError: se o texto nao tiver 100 caracteres
    :raises TypeError: se o texto nao for uma string
    """
    if not isinstance(texto, str):
      raise TypeError('texto precisa ser uma string')
    if len(texto) > 100:
      raise ValueError('texto precisa ter 100 caracteres')
    return texto
  
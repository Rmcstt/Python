class Pessoa:  # Superclasse
  def __init__(self, nome, idade):
    self._nome = nome
    self._idade = idade
    self._nome_classe = self.__class__.__name__  # __class__ = <class '__main__.Pessoa'> # __name__ = 'Pessoa'  @property

  @property
  def nome(self):
    return self._nome

  
  @property
  def idade(self):
    return self._idade

  @property
  def nome_classe(self):
    return self._nome_classe

  def falar(self):
    print(f'{self.nome_classe} {self.nome} esta falando...')


class Cliente(Pessoa):  # subclasse
  def acao(self):
    print(f'{self.nome_classe} {self.nome} esta comprando...')
  
class Aluno(Pessoa):  # subclasse
  def acao(self):
    print(f'{self.nome_classe} {self.nome} esta estudando...')
    
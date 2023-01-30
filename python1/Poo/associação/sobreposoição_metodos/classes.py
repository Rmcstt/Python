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
    


class ClienteVip(Cliente):  # subclasse para sobreposição do metodo falar
  def __init__(self, nome, sobrenome, idade):  
    super().__init__(nome, idade)  # metodo para o construtor da superclasse
    self._sobrenome = sobrenome  # adicionei esse novo atributo sem sobrescrever os atributos da suoperclasse

  @property
  def sobrenome(self):
    return self._sobrenome

  def falar(self):
    super().falar()  # metodo para chamar o metodo da classe de cima
    print('como VIP...')

  def acao(self):
    Aluno.acao(self)  # metofo para chamar diretamente o metodo da classe escolhida
    print('como VIP...')
    print(f'{self.nome_classe} {self.nome} {self.sobrenome} esta comprando como VIP...')
from datetime import datetime  # importando a classe datetime

class Pessoa:  # moldura da classe pessoa
    anoAtual = int(datetime.strftime(datetime.now(), '%Y'))  # ano atual

    def __init__(self, nome, idade):  # metodo contrutor
      self.nome = nome
      self.idade = idade

    def get_ano_nascimento(self):  # metodo de instancia
      print(f'{self.nome} nasceu em {self.anoAtual - self.idade}')

    @classmethod  # metodo de classe
    def por_ano_nascimento(cls, nome, get_ano_nascimento):
      idade = cls.anoAtual - get_ano_nascimento
      return cls(nome, idade)


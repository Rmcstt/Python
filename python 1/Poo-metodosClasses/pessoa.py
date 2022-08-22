from datetime import datetime

class Pessoa:
    anoAtual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade):
      self.nome = nome
      self.idade = idade

    def get_ano_nascimento(self):
      print(f'{self.nome} nasceu em {self.anoAtual - self.idade}')

    @classmethod
    def por_ano_nascimento(cls, nome, get_ano_nascimento):
      idade = cls.anoAtual - get_ano_nascimento
      return cls(nome, idade)


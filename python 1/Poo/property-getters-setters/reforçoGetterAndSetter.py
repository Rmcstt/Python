"""
getter retorna o valor 
setter atrbui um valor


getter e setter sao usados para mudar um valor de um atributo privado
"""


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        print('setando nome')
        self._nome = nome


p1 = Pessoa('otavio')

print(p1.nome)

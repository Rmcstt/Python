"""
getter retorna o valor 
setter atrbui um valor


getter e setter sao usados para mudar um valor de um atributo privado
"""


class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        print('seter foi executado')
        self._nome = nome

    @property
    def sobrenome(self):
        return 'desconhecido'


p1 = Pessoa('renato')

print(p1.nome)
print(p1.sobrenome)
